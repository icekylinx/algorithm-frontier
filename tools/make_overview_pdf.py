from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "overview.pdf"
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Serif", f"{FONT_DIR}/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Bold", f"{FONT_DIR}/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans", f"{FONT_DIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", f"{FONT_DIR}/DejaVuSans-Bold.ttf"))

NAVY = colors.HexColor("#14213D")
INK = colors.HexColor("#202938")
MUTED = colors.HexColor("#5E6B7E")
RULE = colors.HexColor("#B8C2D1")
PALE = colors.HexColor("#F5F7FA")
ACCENT = colors.HexColor("#2F5D8C")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleAcademic", fontName="Serif-Bold", fontSize=26, leading=31, textColor=NAVY, alignment=TA_CENTER, spaceAfter=5*mm))
styles.add(ParagraphStyle(name="Subtitle", fontName="Serif", fontSize=10.5, leading=15, textColor=MUTED, alignment=TA_CENTER, spaceAfter=7*mm))
styles.add(ParagraphStyle(name="Section", fontName="Serif-Bold", fontSize=16, leading=20, textColor=NAVY, spaceBefore=2*mm, spaceAfter=3*mm))
styles.add(ParagraphStyle(name="Family", fontName="Serif-Bold", fontSize=12, leading=15, textColor=ACCENT, spaceBefore=3*mm, spaceAfter=2*mm))
styles.add(ParagraphStyle(name="Body", fontName="Serif", fontSize=8.8, leading=12.5, textColor=INK, spaceAfter=2.5*mm))
styles.add(ParagraphStyle(name="Small", fontName="Sans", fontSize=7.1, leading=9.5, textColor=MUTED))
styles.add(ParagraphStyle(name="TableHead", fontName="Sans-Bold", fontSize=7.2, leading=8.7, textColor=colors.white))
styles.add(ParagraphStyle(name="TableCell", fontName="Sans", fontSize=7.2, leading=9.1, textColor=INK))
styles.add(ParagraphStyle(name="TableCellBold", fontName="Sans-Bold", fontSize=7.2, leading=9.1, textColor=NAVY))
styles.add(ParagraphStyle(name="Formula", fontName="Serif", fontSize=8.2, leading=11, textColor=INK, leftIndent=4*mm, rightIndent=4*mm, spaceBefore=1*mm, spaceAfter=2*mm))


def P(text, style="Body"):
    return Paragraph(text, styles[style])


def cell(text, bold=False):
    return P(text, "TableCellBold" if bold else "TableCell")


def family_table(rows):
    data = [[P("Problem", "TableHead"), P("Problem statement", "TableHead"), P("Complexity", "TableHead"), P("Record", "TableHead")]]
    for problem, statement, complexity, record in rows:
        data.append([cell(problem, True), cell(statement), cell(complexity), cell(record)])
    t = Table(data, colWidths=[34*mm, 62*mm, 65*mm, 19*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("GRID", (0,0), (-1,-1), 0.3, RULE),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, PALE]),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    w, _ = A4
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.35)
    canvas.line(18*mm, 13*mm, w-18*mm, 13*mm)
    canvas.setFont("Sans", 6.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18*mm, 8.5*mm, "Algorithm Frontier  ·  curated overview")
    canvas.drawRightString(w-18*mm, 8.5*mm, f"2026.10.25  ·  {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=16*mm, leftMargin=16*mm, topMargin=15*mm, bottomMargin=19*mm, title="Algorithm Frontier: curated overview", author="Algorithm Frontier")
story = []

# Cover: academic title and compact catalogue metadata.
story += [Spacer(1, 26*mm), P("Algorithm Frontier", "TitleAcademic"), P("A curated catalogue of exact algorithms, approximation schemes, dynamic graph data structures, and lower-bound results", "Subtitle")]
cover = Table([
    [P("Scope", "TableCellBold"), P("Deterministic, source-linked records with explicit model and parameter boundaries.", "TableCell")],
    [P("Organization", "TableCellBold"), P("Problem families first; each family is a mathematical object rather than a maintenance queue.", "TableCell")],
    [P("Complexity", "TableCellBold"), P("Time, writable space, output cost, and the named parameters are reported separately.", "TableCell")],
    [P("Evidence", "TableCellBold"), P("Each record links a result card, proof map, source map, and focused checks. Review status is stated explicitly.", "TableCell")],
], colWidths=[28*mm, 142*mm])
cover.setStyle(TableStyle([
    ("BOX", (0,0), (-1,-1), 0.55, RULE), ("INNERGRID", (0,0), (-1,-1), 0.3, RULE),
    ("BACKGROUND", (0,0), (0,-1), PALE), ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story += [cover, Spacer(1, 10*mm), P("Reading convention", "Family"), P("Read a row from left to right: the problem being solved, the guarantee and output, then the asymptotic bound with its parameters. A tier or review label is a maintenance signal; it is not a mathematical ranking.", "Body"), Spacer(1, 6*mm), P("Repository: github.com/icekylinx/algorithm-frontier", "Small"), PageBreak()]

# Subset-sum and target families: central page.
story += [P("I. Numeric target families", "Section"), P("These records study exact subset-sum-style feasibility and optimization under binary input. The target budget, support geometry, and quota structure are independent parameters; they are never silently folded into one symbol.", "Body")]
story.append(P("Subset Sum", "Family"))
story.append(family_table([
    ("Faster deterministic Subset Sum", "Given signed binary weights and a target, decide exact reachability and return the selected indices.", "Time: a polynomial term plus polynomial(n,L) · 2<sup>E n</sup>, with E = 149809813343531 / 301754962128739 ≈ 0.4964618056. No space exponent is claimed.", "Tier A"),
    ("Low-space deterministic Subset Sum", "The same exact decision and indexed-witness task under an explicit writable-space budget.", "Time: polynomial(n,L) · 2<sup>n/2</sup>. Writable space: polynomial(n,L) · 2<sup>E<sub>S</sub> n</sup>, E<sub>S</sub> = 0.18261635770550353.", "Tier A"),
]))
story.append(P("Numeric target and support", "Family"))
story.append(family_table([
    ("R/S numeric-target frontier", "Exact target decisions and scalar optimization, with support-sensitive and fixed-dimension variants.", "R: exponential in (T + 1) log(T + 2), times polynomial(H). S: exponential in T log(2 + Q/T), times polynomial(H).", "Tier A"),
    ("T/U weighted-prefix quotas", "Ordered prefixes, shared weight families, laminar caps, sparse mixed quotas, and deterministic ground kernels.", "Representative rows: exponential in B; exponential in B log(B + 2); sparse rows exponential in ΔB₀ log(ΔB₀B + 2). Kernel outputs are reported separately.", "Tier A"),
]))
story.append(P("Parameters", "Family"))
story.append(P("n: item count. L: full binary encoding length. T: numeric target budget. Q: distinct nonempty support patterns. d: fixed row dimension. B: maximum cap. B₀: root cap. Δ: positive nonroot incidence bound. p: number of shared weight families. H: complete encoded input and paid polynomial primitive work. E and E<sub>S</sub> are exact exponents, not empirical constants.", "Body"))
story.append(PageBreak())

# Graphs.
story += [P("II. Graph algorithms", "Section"), P("The graph family keeps update time, query time, stretch, recourse, path output, and backend assumptions separate. A tradeoff curve is presented as a curve, not collapsed into a single headline number.", "Body")]
story.append(family_table([
    ("General-graph matching", "Compute a maximum-cardinality matching and return original edge identifiers after loop and parallel-edge normalization.", "Linear input normalization plus a backend-dependent exponential-in-polylog term in the retained edge count m<sub>s</sub>; a uniform m<sup>1+o(1)</sup> point is retained as a comparison.", "Tier A"),
    ("Fully dynamic APSP", "Maintain approximate all-pairs distances under edge updates and answer distance queries.", "Equalized point: update work and stretch exponential in U<sup>4/5</sup>h<sup>1/5</sup>. Fixed C: update exponential in U<sup>3/4</sup>h<sup>(C+1)/4</sup>; stretch exponential in U/h<sup>C</sup>. Queries polynomial in U.", "Tier A"),
    ("Dynamic spanners", "Maintain a spanner with bounded stretch, size, amortized work, and output recourse.", "Rows retain insertion/deletion counts I,D, history scale N, U = log N + O(1), and h = log U + O(1); each row has its own stretch and recourse expression.", "Tier A"),
    ("Incremental SSSP", "Maintain approximate one-source distances under insertions and report a simple directed path with original identifiers.", "Update envelope depends on N, U = log N, h = log U + O(1), and ε; path output costs linear in the returned path length k up to polylog factors.", "Tier B"),
    ("Incremental SCC / dynamic MSF", "Maintain exact strongly connected components or an exact minimum spanning forest under settled updates.", "Both are composed bounds: the backend hierarchy and graph inventory are charged separately. No unstated worst-case or independent space exponent is promoted.", "Tier B"),
]))
story.append(P("Graph parameters", "Family"))
story.append(P("n: vertices. m: current edge records. m₀: initial edge records. N: declared lifetime or history cap. U: log N plus a fixed constant. h: log U plus a fixed constant. C: fixed stretch-tuning constant. ε: approximation accuracy. k: output path length.", "Body"))
story.append(PageBreak())

# Allocation/scheduling/limits, concise.
story += [P("III. Allocation, flow, and scheduling", "Section"), P("These records share a certificate-oriented style: the objective, the selected basis or scenario set, and the exact budget contract are stated before the approximation or exponential factor.", "Body")]
story.append(P("Allocation and flow", "Family"))
story.append(family_table([
    ("Selected and robust flow", "Select a common commodity set and route it at a common rate, either in one instance or across explicit scenarios.", "Selector base Γ(1/ε)<sup>c</sup> times polynomial(H), where c = q − r is the rejected count; scenario count and routing rows are included in H.", "Tier B"),
    ("Recipient polymatroid and matroid models", "Maximize common intrinsic value subject to recipient polymatroids, player bases, and exact availability.", "Exponential in selected rank r times polynomial(H); the recipient-polymatroid guarantee is 4 − 3/r, with its rank-quasipolynomial alternative stated separately.", "Tier B"),
    ("Robust certificate boundaries", "Return a common basis and scenario allocations, or a certificate when the width promise fails.", "Exponential in omission count c with width-dependent base A, times polynomial scenario input; whole-ground conversion uses a separate (2 − 1/A) base.", "Tier C"),
]))
story.append(P("Scheduling", "Family"))
story.append(family_table([
    ("Activated and arbitrary-processing machines", "Assign mandatory job totals while minimizing makespan under machine and setup constraints.", "Exponential in the physical-machine/profile parameter divided by ε, times polynomial complete binary input; job counts are not expanded into unit slots.", "Tier B"),
    ("Many-size, two-size, and two-time profiles", "Return an integral schedule while preserving the source's additive workload and machine-profile terms.", "Profile-specific compressed-rank or endpoint bounds; each card names D, OPT, u, a, λ<sub>k</sub>, k, or the two-time parameters that actually enter the theorem.", "Tier B"),
]))
story.append(P("Boundary and evidence", "Family"))
story.append(P("Lower-bound cards, proof maps, and finite checks remain attached to the individual problem directory. A finite rational certificate or enumeration check validates only the checked component; it is not a formal proof of an arbitrary-input theorem.", "Body"))
story.append(Spacer(1, 4*mm))
story.append(P("Source and review index", "Family"))
story.append(P("The GitHub-facing result cards are the authoritative display layer. Follow each card's proof.md and sources.md for the exact source paths, model assumptions, lower-bound scope, and review status. The machine-readable registry is in reviews/registry.json.", "Body"))
story.append(Spacer(1, 5*mm))
story.append(P("This PDF is deliberately compact: it is a scholarly reading map, not a replacement for the source manuscripts.", "Small"))

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"created {OUT} ({OUT.stat().st_size} bytes)")
