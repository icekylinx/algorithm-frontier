"""Run representative workflows in a disposable copy of the curated tree."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
STATUS = json.loads((ROOT / 'STATUS.json').read_text())
CURRENT = (
    STATUS['historical_verification']['certificate']
    if 'historical_verification' in STATUS
    else STATUS['strongest_accepted_rate']['certificate']
)
CHECKS = [
    ('current_schedule', ['tools/verify_schedule.py', CURRENT]),
    ('retuned_density', ['baseline/agents/derandomization/certify_retuned_density_menu.py']),
    ('phase_25_upper', ['baseline/agents/baseline_audit/certify_phase_twenty_five.py']),
    ('phase_25_optimality', ['baseline/agents/baseline_audit/certify_phase_25_optimal.py']),
    ('phase_retuned_entropy', ['baseline/agents/baseline_audit/certify_phase_retuned_entropy.py']),
    ('shared_seed_sampler', ['baseline/agents/derandomization/verify_exact_pairwise_sampler.py']),
    ('weighted_hash', ['baseline/agents/derandomization/verify_weighted_mulshift.py']),
    ('translated_hash', ['baseline/agents/derandomization/verify_mulshift_translates.py']),
    ('sharp_quartic', ['baseline/agents/structural_algorithms/verify_sharp_quartic.py']),
    ('common_gap_witnesses', ['baseline/agents/structural_algorithms/verify_common_gap.py']),
    ('collision_exchange_witnesses', ['baseline/agents/structural_algorithms/verify_collision_exchange.py']),
    ('weighted_transversal', ['baseline/agents/structural_algorithms/verify_weighted_transversal.py']),
    ('uniform_modulus_rank', ['baseline/agents/structural_algorithms/verify_uniform_modulus_rank.py']),
]


def run(copy, name, arguments):
    started = time.monotonic()
    result = subprocess.run([sys.executable, '-B', *arguments], cwd=copy,
                            env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, timeout=300)
    return dict(name=name, command=['python3', '-B', *arguments], returncode=result.returncode,
                status='PASS' if result.returncode == 0 else 'FAIL',
                elapsed_seconds=round(time.monotonic()-started, 3),
                output_sha256=hashlib.sha256(result.stdout.encode()).hexdigest(),
                output_tail=result.stdout[-400:])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    results = []
    with tempfile.TemporaryDirectory(prefix='subset-curated-') as tmp:
        copy = Path(tmp) / 'subset-sum'
        copy.mkdir()
        for name in ('baseline', 'tools', 'rounds'):
            shutil.copytree(ROOT/name, copy/name, ignore=shutil.ignore_patterns('__pycache__'))
        with ThreadPoolExecutor(max_workers=3) as pool:
            futures = [pool.submit(run, copy, name, arguments) for name, arguments in CHECKS]
            for future in as_completed(futures):
                item = future.result()
                results.append(item)
                print(item['name'], item['status'], item['elapsed_seconds'], flush=True)
        # Exercise the retained upstream transcript-based test without the archived Lean suite.
        upstream = copy / 'baseline/agents/derandomization/subsetsum-derand-main'
        results.append(run(upstream, 'upstream_headline_tests', ['-m', 'unittest', 'discover', '-s', 'tests']))
    output = dict(status='PASS' if all(r['status']=='PASS' for r in results) else 'FAIL',
                  checks=sorted(results, key=lambda r:r['name']),
                  disposable_copy=True, active_source_receipts_rewritten=False,
                  scope='Representative retained workflows and finite checks, not a new proof of imported theorems or an exhaustive rerun.')
    args.output.write_text(json.dumps(output, indent=2)+'\n')
    print('Overall:', output['status'], len(results), 'checks', flush=True)
    if output['status'] != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
