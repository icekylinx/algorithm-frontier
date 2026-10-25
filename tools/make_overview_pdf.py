from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(TTFont('DVSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVSans-Oblique', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVSans-BoldOblique', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'overview.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor('#12233F')
BLUE = colors.HexColor('#2563EB')
CYAN = colors.HexColor('#0EA5A4')
GOLD = colors.HexColor('#D97706')
RED = colors.HexColor('#B42318')
INK = colors.HexColor('#1F2937')
MUTED = colors.HexColor('#64748B')
PALE = colors.HexColor('#F1F5F9')
PALE_BLUE = colors.HexColor('#EFF6FF')
PALE_GOLD = colors.HexColor('#FFFBEB')
LINE = colors.HexColor('#CBD5E1')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle', parent=styles['Title'], fontName='DVSans-Bold', fontSize=30, leading=35, textColor=NAVY, alignment=TA_CENTER, spaceAfter=9*mm))
styles.add(ParagraphStyle(name='CoverSub', parent=styles['Normal'], fontName='DVSans', fontSize=12, leading=17, textColor=MUTED, alignment=TA_CENTER, spaceAfter=10*mm))
styles.add(ParagraphStyle(name='H1x', parent=styles['Heading1'], fontName='DVSans-Bold', fontSize=20, leading=24, textColor=NAVY, spaceBefore=2*mm, spaceAfter=5*mm))
styles.add(ParagraphStyle(name='H2x', parent=styles['Heading2'], fontName='DVSans-Bold', fontSize=13, leading=16, textColor=BLUE, spaceBefore=4*mm, spaceAfter=2.5*mm))
styles.add(ParagraphStyle(name='Bodyx', parent=styles['BodyText'], fontName='DVSans', fontSize=9.3, leading=13.3, textColor=INK, spaceAfter=2.5*mm))
styles.add(ParagraphStyle(name='Smallx', parent=styles['BodyText'], fontName='DVSans', fontSize=7.7, leading=10.2, textColor=MUTED))
styles.add(ParagraphStyle(name='CardTitle', parent=styles['BodyText'], fontName='DVSans-Bold', fontSize=10, leading=12, textColor=NAVY))
styles.add(ParagraphStyle(name='CardBody', parent=styles['BodyText'], fontName='DVSans', fontSize=8.1, leading=10.8, textColor=INK))
styles.add(ParagraphStyle(name='TableHead', parent=styles['BodyText'], fontName='DVSans-Bold', fontSize=7.5, leading=9, textColor=colors.white))
styles.add(ParagraphStyle(name='TableBody', parent=styles['BodyText'], fontName='DVSans', fontSize=7.2, leading=9.1, textColor=INK))
styles.add(ParagraphStyle(name='Quote', parent=styles['BodyText'], fontName='DVSans-Oblique', fontSize=10, leading=14, textColor=NAVY, leftIndent=8*mm, rightIndent=8*mm, spaceBefore=2*mm, spaceAfter=4*mm))


def P(text, style='Bodyx'):
    return Paragraph(text, styles[style])

def card(title, body, color=BLUE):
    t = Table([[P(title, 'CardTitle')], [P(body, 'CardBody')]], colWidths=[58*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.white),
        ('BOX', (0,0), (-1,-1), 0.8, LINE),
        ('LINEBEFORE', (0,0), (0,-1), 4, color),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(18*mm, 14*mm, w-18*mm, 14*mm)
    canvas.setFont('DVSans', 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(18*mm, 9*mm, 'Algorithm Frontier - overview')
    canvas.drawRightString(w-18*mm, 9*mm, f'2026-10-25  |  {doc.page}')
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=16*mm, leftMargin=16*mm, topMargin=15*mm, bottomMargin=20*mm, title='Algorithm Frontier Overview', author='Yilin Liu and GPT-6 Astra Pro')
story=[]

# Cover
story.append(Spacer(1, 25*mm))
story.append(P('Algorithm Frontier', 'CoverTitle'))
story.append(P('A source-linked catalogue of deterministic algorithms, exact and approximation schemes, dynamic graph records, and lower-bound boundaries.', 'CoverSub'))
story.append(Spacer(1, 4*mm))
cover_cards = Table([[card('41 curated records', 'Every problem directory has a result card, proof map, source map, and focused verification notes.', BLUE), card('Four priority tiers', 'Headline records, supporting extensions, boundary records, and archive material remain easy to distinguish.', CYAN), card('Four checkpoint families', 'R, S, T, and U are stored as parent-linked increments with byte-level manifests.', GOLD)]], colWidths=[60*mm,60*mm,60*mm], hAlign='CENTER')
cover_cards.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2)]))
story.append(cover_cards)
story.append(Spacer(1, 15*mm))
story.append(P('Reading order', 'H2x'))
story.append(P('Start with the headline records, then follow each proof map to the exact source paths and the verification notes. The complete catalogue is maintained separately from the short reading path. GitHub-facing cards use readable prose and compact parameter labels; detailed formulas and source notation are preserved in this PDF and the source manuscripts.', 'Quote'))
story.append(Spacer(1, 12*mm))
story.append(P('Repository: github.com/icekylinx/algorithm-frontier', 'Smallx'))
story.append(PageBreak())

# Headline records
story.append(P('Headline records', 'H1x'))
story.append(P('The headline set is ordered by frontier value and maintenance attention. A higher tier does not mean that lower tiers are less correct; it means that the result has a different role in the catalogue.', 'Bodyx'))
headline_data = [
    [P('Record', 'TableHead'), P('Guarantee and role', 'TableHead'), P('Time / resource summary', 'TableHead'), P('Parameters made explicit', 'TableHead'), P('Status', 'TableHead')],
    [P('Numeric-target frontier', 'TableBody'), P('Exact target decisions, scalar optimization, and support-sensitive bounds.', 'TableBody'), P('R: 2 to the power of O((T + 1) log(T + 2)), times polynomial work. S: 2 to the power of O(T log(2 + Q/T)), times polynomial work.', 'TableBody'), P('T = numeric target sum; Q = distinct nonempty support patterns; d = fixed row dimension; H = encoded input and paid primitive work.', 'TableBody'), P('Tier A; internal mathematical review; no formal verification.', 'TableBody')],
    [P('Weighted-prefix and sparse-quota frontier', 'TableBody'), P('Ordered prefix quotas, laminar completion, sparse overlap, and deterministic ground kernels.', 'TableBody'), P('T: one order is exponential in B; two orders are exponential in B log(B + 2); U: sparse time is exponential in Delta B0 log(Delta B0 B + 2).', 'TableBody'), P('B = target/root cap; B0 = distinguished root cap; Delta = positive nonroot incidence bound; p = weight-family count.', 'TableBody'), P('Tier A; T/U parent-linked review; no formal verification.', 'TableBody')],
    [P('Faster Subset Sum', 'TableBody'), P('Exact indexed witness for signed binary integers.', 'TableBody'), P('C + polynomial(n, L) times 2 to the power of E n, with E less than 0.4964618056.', 'TableBody'), P('n = item count; L = total binary encoding length; C = fixed overhead term.', 'TableBody'), P('Tier A; no space exponent claimed.', 'TableBody')],
    [P('Low-space Subset Sum', 'TableBody'), P('Exact indexed witness with an explicit writable-space bound.', 'TableBody'), P('Time: polynomial(n, L) times 2 to the power of n/2. Writable space: polynomial(n, L) times 2 to the power of E_S n, with E_S less than 0.1826163578.', 'TableBody'), P('n = item count; L = binary encoding length; E_S = space exponent; indexed witness output is included.', 'TableBody'), P('Tier A; separate time/space record.', 'TableBody')],
    [P('General-graph matching', 'TableBody'), P('Exact maximum-cardinality matching under a conditional backend contract.', 'TableBody'), P('Linear input work plus an exponential backend factor in the sampled-edge parameter m_s.', 'TableBody'), P('n,m = vertices and edge records; m_s = sampled-edge parameter; backend assumptions remain material.', 'TableBody'), P('Tier A; conditional; internally reviewed.', 'TableBody')],
    [P('Dynamic APSP and spanners', 'TableBody'), P('Incomparable update, stretch, and recourse tradeoffs.', 'TableBody'), P('Several parameterized points; no single point is advertised as globally best.', 'TableBody'), P('U,h and graph size parameters remain tied to each source model.', 'TableBody'), P('Tier A; tradeoff frontier.', 'TableBody')],
]
t=Table(headline_data, colWidths=[31*mm,38*mm,55*mm,48*mm,25*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),NAVY),('GRID',(0,0),(-1,-1),0.35,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE_BLUE]),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)
]))
story.append(t)
story.append(Spacer(1, 5*mm))
story.append(P('The complete record cards preserve exact model, representation, comparator, additive terms, lower-bound type, and review status. The table above is a navigation surface, not a replacement for those source-linked records.', 'Smallx'))
story.append(PageBreak())

# Families
story.append(P('Catalogue families', 'H1x'))
story.append(P('The repository is organized by the mathematical role of a result. This prevents a lower bound, a transfer lemma, and a headline algorithm from competing for the same display slot.', 'Bodyx'))
family_data = [
    [card('Graph algorithms', 'Matching, dynamic APSP, dynamic spanners, incremental SSSP/SCC, dynamic MSF, strong forests, Haxell matching, and independent transversals.', BLUE), card('Allocation and flow', 'Selected flow, robust scenarios, shared setup, min-cost flow, polymatroids, matroid configurations, and factor-two boundaries.', CYAN), card('Scheduling', 'Activated machines, commitments, processing buckets, two-size and two-time models, and profile endpoints.', GOLD)],
    [card('Numeric targets', 'R/S records separate target magnitude, support geometry, fixed dimension, exact optimization, and encoded lower-bound representations.', BLUE), card('Prefix and sparse quotas', 'T/U records separate ordered prefix geometry, laminar caps, positive root charge, sparse overlap, and deterministic ground kernels.', CYAN), card('Robustness and barriers', 'Oracle barriers, bounded certificates, unrelated values, width-two gates, and two-scenario hardness remain boundary records.', RED)],
]
for row in family_data:
    tbl=Table([row], colWidths=[60*mm,60*mm,60*mm], hAlign='CENTER')
    tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    story.append(tbl)

story.append(P('Review status vocabulary', 'H2x'))
review_data = [
    [P('Label', 'TableHead'), P('Meaning', 'TableHead'), P('What it does not claim', 'TableHead')],
    [P('Internal mathematical review', 'TableBody'), P('The repository records a complete internal review of the stated proof gates and model boundaries.', 'TableBody'), P('It is not formal verification or external peer review.', 'TableBody')],
    [P('Formal verification', 'TableBody'), P('A machine-checked proof or executable checker is actually present.', 'TableBody'), P('A source audit alone does not qualify.', 'TableBody')],
    [P('Conditional', 'TableBody'), P('The claim depends on an oracle, backend, representation, or complexity assumption.', 'TableBody'), P('It is not an unconditional implementation result.', 'TableBody')],
    [P('Historical', 'TableBody'), P('The record remains for provenance but is no longer the strongest same-scope display.', 'TableBody'), P('It is not deleted or silently rewritten.', 'TableBody')],
]
t=Table(review_data, colWidths=[38*mm,74*mm,68*mm], repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('GRID',(0,0),(-1,-1),0.35,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
story.append(t)
story.append(PageBreak())

# Provenance and workflow
story.append(P('Checkpoint and review workflow', 'H1x'))
story.append(P('Each checkpoint is an increment-only source boundary. The archive is not treated as a single undifferentiated manuscript: parent hashes, byte manifests, review scope, and exclusions remain visible.', 'Bodyx'))
prov = [
    [P('Increment', 'TableHead'), P('Parent', 'TableHead'), P('Archive size', 'TableHead'), P('Manifest payload', 'TableHead'), P('Role', 'TableHead')],
    [P('R', 'TableBody'), P('Q', 'TableBody'), P('110,748 bytes', 'TableBody'), P('17 files', 'TableBody'), P('Numeric-target extensions and exact profile baselines.', 'TableBody')],
    [P('S', 'TableBody'), P('R', 'TableBody'), P('83,739 bytes', 'TableBody'), P('14 files', 'TableBody'), P('Support-pattern geometry and encoded lower-bound boundaries.', 'TableBody')],
    [P('T', 'TableBody'), P('S', 'TableBody'), P('79,861 bytes', 'TableBody'), P('12 files', 'TableBody'), P('Ordered prefix quotas, multi-family weights, and laminar completion.', 'TableBody')],
    [P('U', 'TableBody'), P('T', 'TableBody'), P('76,875 bytes', 'TableBody'), P('11 files', 'TableBody'), P('Sparse overlap, sharp lower bounds, and deterministic ground kernels.', 'TableBody')],
]
t=Table(prov, colWidths=[20*mm,28*mm,35*mm,35*mm,62*mm], repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('GRID',(0,0),(-1,-1),0.35,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE_BLUE]),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
story.append(t)
story.append(Spacer(1, 6*mm))
story.append(P('Review loop', 'H2x'))
steps = [
    ('01', 'Discover', 'Inspect newly uploaded instructions and checkpoint archives at a moderate interval.'),
    ('02', 'Identify', 'Verify parent archive, SHA-256, payload count, exclusions, and internal links.'),
    ('03', 'Review', 'Run independent proof and algorithm reviews, record open gates, and separate model boundaries.'),
    ('04', 'Promote', 'Create or update the smallest source-linked result card, proof map, source map, and focused audits.'),
    ('05', 'Publish', 'Run structural, display, provenance, and review-registry checks before a small commit and push.'),
    ('06', 'Re-audit', 'Read the workflow result and reopen affected records when a new checkpoint or correction arrives.'),
]
step_rows=[]
for num,title,body in steps:
    step_rows.append([P(f'<b>{num}</b>', 'CardTitle'), P(f'<b>{title}</b><br/>{body}', 'CardBody')])
t=Table(step_rows, colWidths=[18*mm,162*mm])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,-1),PALE_BLUE),('GRID',(0,0),(-1,-1),0.35,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
story.append(t)
story.append(Spacer(1, 7*mm))
story.append(P('Current review queue', 'H2x'))
story.append(P('1. Recheck the newest T/U claims against the next checkpoint.  2. Complete the remaining proof/algorithm review cards for Tier B records.  3. Expand the machine-readable complexity index after the display schema stabilizes.  4. Keep source notation and GitHub presentation synchronized without rewriting imported manuscripts.', 'Bodyx'))
story.append(P('This PDF is a presentation and navigation layer. The repository files remain the authoritative source-linked records.', 'Smallx'))

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f'created {OUT} ({OUT.stat().st_size} bytes)')
