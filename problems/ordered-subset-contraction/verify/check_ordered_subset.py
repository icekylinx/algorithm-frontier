# Copyright 2026 Yilin Liu and GPT-6 Astra Pro
# SPDX-License-Identifier: Apache-2.0
"""Run the exact ordered subset prototype checks."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from ordered_subset_contraction import main

if __name__ == "__main__":
    main()
