#!/usr/bin/env python3
"""The 7LM plate sheet: the Seven-Layer Model developed in diagrams.

One source file. Every drawing on the sheet is defined here and nowhere else, so
there is one place to change when the model changes.

Plates 01-12 state what the Harmonized Authoritative Architecture Specification
(12 September 2026) ratifies. Plates 13-14 carry a proposal that is not in the
specification and are marked open.
"""
import pathlib

OUT = pathlib.Path(__file__).with_name('7lm-plate-sheet.html')

MONO = "IBM Plex Mono, ui-monospace, monospace"
SANS = "Archivo, system-ui, sans-serif"
NARR = "Archivo Narrow, Archivo, system-ui, sans-serif"


def arrows(pid):
    """Marker defs for one plate: <pid> in ink, <pid>a in accent, <pid>o in oxide."""
    out = []
    for suffix, fill in (("", "currentColor"), ("a", "var(--accent)"), ("o", "var(--open)")):
        out.append(
            f'<marker id="{pid}{suffix}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
            f'markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{fill}"/></marker>')
    return '<defs>' + ''.join(out) + '</defs>'


def t(x, y, s, size=11, fam=SANS, fill="currentColor", anchor="start", op=None, extra=""):
    o = f' opacity="{op}"' if op is not None else ''
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}"{o}{extra}>{s}</text>')


def box(x, y, w, h, fill="var(--sheet)", stroke="currentColor", sw=1.2, op=None, dash=None, rx=2):
    o = f' opacity="{op}"' if op is not None else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{o}{d}/>')


def line(x1, y1, x2, y2, stroke="currentColor", sw=1.2, op=None, dash=None, marker=None):
    o = f' opacity="{op}"' if op is not None else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    m = f' marker-end="url(#{marker})"' if marker else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{o}{d}{m}/>')


PLATES = []


def plate(n, part, title, claim, svg, vb, alt, status=None):
    PLATES.append(dict(n=n, part=part, title=title, claim=claim, svg=svg, vb=vb,
                       alt=alt, status=status))


# ============================================================ I. THE OBJECT

def p01():
    rows = [
        ("L6", "Library / Memory", "prior states, corrections, retirement"),
        ("L5", "Research / Discourse", "interpretation, review, findings"),
        ("L4", "Conversion / Realization", "what was made, run, measured, failed"),
        ("L3", "Engineering Mathematics", "units, tolerance, uncertainty, feasibility"),
        ("L2", "Formal Mathematics", "exact relations, operators, proofs"),
        ("L1", "State Space", "admissible states, invariants, exclusions"),
        ("L0", "Semantic / Foundational", "the meaning this object authors"),
    ]
    s = [box(40, 16, 640, 54, fill="var(--accent-wash)", stroke="var(--accent)", sw=1.5),
         t(60, 41, "L7", 15, MONO, "var(--accent-ink)"),
         t(96, 41, "the desk &#183; Surface / Forward Face", 13, NARR, "var(--accent-ink)"),
         t(60, 60, "provenance &#183; governance &#183; peering &#183; publications", 10.5,
           SANS, "var(--accent-ink)", op=0.85),
         t(360, 86, "crossing here is a boundary event, not filesystem nesting", 10.5,
           SANS, "currentColor", "middle", 0.8),
         line(24, 94, 696, 94, dash="5 4", op=0.5, sw=1),
         box(40, 106, 640, 344, fill="none", op=0.45, sw=1),
         t(58, 128, "L8", 13, MONO),
         t(86, 128, "the packet on the desk &#8212; the interior, called the USO", 10.5,
           SANS, "currentColor", op=0.8)]
    y = 142
    for code, name, job in rows:
        s.append(box(60, y, 600, 38, op=0.9))
        s.append(t(78, y + 24, code, 13, MONO, "var(--accent)"))
        s.append(t(118, y + 24, name, 12.5, SANS, "var(--ink)"))
        s.append(t(306, y + 24, job, 10.5, SANS, op=0.85))
        y += 42
    plate("01", "I. The object", "The eight positions",
          "L7 and L8 are siblings on disk. The seven layers sit flat inside L8; each owns one kind of claim.",
          ''.join(s), "0 0 720 462",
          "The desk L7 above a dashed boundary, and below it the packet L8 containing the seven layers L6 down to L0, each with the job it owns")


def p02():
    ordinals = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHTH"]
    s, x = [], 44
    for i in range(8):
        cx, desk = x + 36, (i == 7)
        s.append(t(cx, 54, ordinals[i], 9.5, NARR, "currentColor", "middle", 0.75,
                   ' letter-spacing="0.06em"'))
        s.append(box(x, 64, 72, 46, fill="var(--accent-wash)" if desk else "var(--sheet)",
                     stroke="var(--accent)" if desk else "currentColor", sw=1.4,
                     op=1 if desk else 0.55))
        s.append(t(cx, 94, f"L{i}", 16, MONO,
                   "var(--accent-ink)" if desk else "var(--ink)", "middle"))
        x += 80
    s.append('<path d="M 44 124 L 44 131 L 316 131 L 316 137 L 324 131 L 596 131 L 596 124" '
             'fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.6"/>')
    s.append(t(320, 153, "seven layers &#8212; so the seventh layer is L6", 12, SANS, "var(--ink)", "middle"))
    s.append(t(640, 149, "numbered, not a layer", 10, SANS, "var(--accent)", "middle"))
    s.append('<path d="M 44 172 L 44 179 L 356 179 L 356 185 L 364 179 L 676 179 L 676 172" '
             'fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.6"/>')
    s.append(t(360, 201, "eight positions &#8212; L8 is the count of these, and the name of the folder",
               12, SANS, "var(--ink)", "middle"))
    s.append(line(44, 222, 676, 222, op=0.25, sw=1))
    s.append(t(44, 242, "Peers are counted from 1, not 0: they are physical.", 10.5, SANS, op=0.85))
    s.append(t(360, 242, "L7/peering/peer-1/object-1/", 10.5, MONO, "var(--accent)"))
    plate("02", "I. The object", "The count rule",
          "First is always 0. Ordinals are semantics; numbers are magnitudes; the relation between them is <em>is</em>.",
          ''.join(s), "0 0 720 258",
          "Eight numbered positions L0 to L7 with ordinal names above, a brace under L0 to L6 marking the seven layers and a brace under all eight marking what L8 counts")


def p03():
    s = [t(24, 28, "L7", 13, MONO, "var(--ink)"),
         t(54, 28, "the two characters draw the desk", 11, SANS, op=0.85),
         '<g transform="translate(118,46) scale(0.82)" fill="var(--accent)">'
         '<g transform="translate(0 132) scale(1 -1) translate(64 0) rotate(90)">'
         '<rect x="4" y="4" width="12" height="56"/><rect x="4" y="48" width="106" height="12"/>'
         '<rect x="22" y="4" width="106" height="12"/><rect x="116" y="4" width="12" height="56"/>'
         '</g></g>',
         t(182, 60, "7", 11, MONO, "var(--accent-ink)"),
         t(194, 60, "top edge + right side", 10, SANS, op=0.85),
         t(118, 176, "L", 11, MONO, "var(--accent-ink)"),
         t(130, 176, "left side + bottom edge", 10, SANS, op=0.85),
         line(330, 20, 330, 190, op=0.3, sw=1),
         t(356, 28, "L8", 13, MONO, "var(--ink)"),
         t(386, 28, "zero over zero closes into an 8", 11, SANS, op=0.85),
         '<circle cx="420" cy="90" r="30" fill="none" stroke="var(--accent)" stroke-width="9"/>',
         '<circle cx="420" cy="150" r="30" fill="none" stroke="var(--accent)" stroke-width="9"/>',
         line(456, 90, 482, 90, op=0.5, sw=1),
         t(490, 86, "L8/0.md", 10.5, MONO, "var(--ink)"),
         t(490, 100, "the interior&#8217;s own zero", 10, SANS, op=0.8),
         line(456, 150, 482, 150, op=0.5, sw=1),
         t(490, 146, "L0/0.md &#8230; L6/0.md", 10.5, MONO, "var(--ink)"),
         t(490, 160, "the seven layer zeros", 10, SANS, op=0.8),
         t(420, 196, "a closed figure: L8 encloses the seven", 10.5, SANS, "currentColor", "middle", 0.85)]
    plate("03", "I. The object", "The names are drawings",
          "L7 draws the desk from its two characters. L8 stacks the interior&#8217;s zero over the layers&#8217; zeros.",
          ''.join(s), "0 0 660 210",
          "Left, the letters L and 7 forming a rectangle. Right, two circles stacked into an eight, the upper labelled the interior zero and the lower the seven layer zeros")


# ============================================================ II. MOVEMENT

def p04():
    s = [arrows("p4")]
    y = 26
    for i, code in enumerate(["L7", "L6", "L5", "L4", "L3", "L2", "L1", "L0"]):
        desk = (i == 0)
        s.append(box(238, y, 184, 32, fill="var(--accent-wash)" if desk else "var(--sheet)",
                     stroke="var(--accent)" if desk else "currentColor", op=1 if desk else 0.85))
        s.append(t(330, y + 21, code, 13, MONO,
                   "var(--accent-ink)" if desk else "var(--ink)", "middle"))
        y += 38
    s.append(line(206, 316, 206, 34, stroke="var(--accent)", sw=1.6, marker="p4a"))
    s.append(t(188, 140, "construction", 12, NARR, "var(--ink)", "end"))
    for i, txt in enumerate(["outward, L0 first", "one layer at a time,",
                             "and only as far as", "dependencies justify"]):
        s.append(t(188, 158 + i * 15, txt, 10, SANS, "currentColor", "end", 0.85))
    s.append(line(454, 34, 454, 316, sw=1.6, marker="p4"))
    s.append(t(472, 140, "inspection", 12, NARR, "var(--ink)"))
    for i, txt in enumerate(["inward, L7 first", "the desk, then the",
                             "memory, then down", "to the meaning"]):
        s.append(t(472, 158 + i * 15, txt, 10, SANS, op=0.85))
    s.append(t(330, 344, "&#8220;Description does not become prescription merely because the structure can be traversed.&#8221;",
               10, SANS, "currentColor", "middle", 0.75))
    plate("04", "II. Movement", "The two directions",
          "Construction climbs from L0 and stops where a dependency is not established. Inspection descends from L7.",
          ''.join(s), "0 0 660 360",
          "A column of the eight positions with an upward arrow labelled construction on the left and a downward arrow labelled inspection on the right")


def p05():
    s = [arrows("p5")]
    rows = [("L4", "realized work", 62), ("L3", "engineering", 140), ("L2", "exact math", 218)]

    def col(x0, title, sub, bridged):
        g, cx = [], x0 + 100
        g.append(t(cx, 26, title, 12, NARR, "var(--ink)", "middle"))
        g.append(t(cx, 44, sub, 10, SANS, "currentColor", "middle", 0.8))
        for code, name, y in rows:
            faint = (not bridged) and code in ("L3", "L4")
            g.append(box(x0, y, 200, 42, op=0.3 if faint else 0.9,
                         dash="4 4" if faint else None))
            g.append(t(x0 + 16, y + 27, code, 13, MONO,
                       "currentColor" if faint else "var(--accent)", op=0.45 if faint else 1))
            g.append(t(x0 + 52, y + 27, name, 11.5, SANS, op=0.45 if faint else 1))
        if bridged:
            for y_from, y_to, ly in ((218, 186, 206), (140, 108, 128)):
                g.append(line(cx, y_from, cx, y_to, stroke="var(--accent)", sw=1.5, marker="p5a"))
                g.append(t(cx + 12, ly, "bridge established", 9.5, SANS, op=0.85))
        else:
            g.append(line(cx, 218, cx, 186, sw=1.4, dash="4 4", op=0.45))
            g.append(line(cx - 13, 194, cx + 13, 210, stroke="var(--accent)", sw=1.8))
            g.append(line(cx + 13, 194, cx - 13, 210, stroke="var(--accent)", sw=1.8))
            g.append(t(cx + 24, 206, "no bridge", 9.5, SANS, "var(--accent)"))
            g.append(t(x0, 288, "the claim stops here &#8212; honest placement", 10.5, SANS, "var(--accent)"))
        return ''.join(g)

    s.append(col(60, "A dependency is established", "the claim may move up", True))
    s.append(line(330, 16, 330, 296, op=0.25, sw=1))
    s.append(col(400, "No dependency is established", "the claim stays where it is", False))
    plate("05", "II. Movement", "The bridge, and honest placement",
          "Build whatever the mathematics permits. Claim only what the layer has earned; stopping is placement, not rejection.",
          ''.join(s), "0 0 660 306",
          "Two columns comparing a claim that moves from L2 through L3 to L4 with one that stops at L2 because no bridge exists")


def p06():
    s = [arrows("p6")]
    order = ["L7", "L6", "L5", "L4", "L3", "L2", "L1", "L0"]

    def stack(x0, w, faint_others):
        g, y, coords = [], 74, {}
        for code in order:
            h = 54 if code == "L4" else 26
            active = (code == "L4") or (not faint_others)
            g.append(box(x0, y, w, h, fill="var(--accent-wash)" if code == "L4" else "var(--sheet)",
                         stroke="var(--accent)" if code == "L4" else "currentColor",
                         op=1 if active else 0.4))
            g.append(t(x0 + 12, y + 17, code, 11.5, MONO,
                       "var(--accent-ink)" if code == "L4" else "var(--ink)",
                       op=1 if active else 0.55))
            coords[code] = (y, h)
            y += h + 4
        return ''.join(g), coords

    s.append(t(176, 30, "How does it operate?", 12, NARR, "var(--ink)", "middle"))
    s.append(t(176, 48, "the whole stack is one L4 object", 10, SANS, "currentColor", "middle", 0.85))
    a, ca = stack(52, 248, True)
    s.append(a)
    ay, _ = ca["L4"]
    s.append(box(64, ay + 20, 224, 28, fill="none", stroke="var(--accent)", sw=1, dash="4 3"))
    s.append(t(176, ay + 38, "OSI L1 &#8230; L7 &#8212; one object", 10.5, MONO, "var(--accent-ink)", "middle"))
    s.append(line(350, 20, 350, 400, op=0.25, sw=1))
    s.append(t(550, 30, "Where did it come from?", 12, NARR, "var(--ink)", "middle"))
    s.append(t(550, 48, "the inquiry expands; the stack does not move", 10, SANS, "currentColor", "middle", 0.85))
    b, cb = stack(396, 150, False)
    s.append(b)
    by, _ = cb["L4"]
    s.append(box(404, by + 20, 134, 26, fill="none", stroke="var(--accent)", sw=1, dash="4 3"))
    s.append(t(471, by + 37, "OSI &#8212; unmoved", 9.5, MONO, "var(--accent-ink)", "middle"))
    answers = {"L7": "the standards bodies", "L6": "its development history",
               "L5": "why it took this form", "L4": "the stack as operated",
               "L3": "the trade-offs that shaped it", "L2": "exact relations, where warranted",
               "L1": "admissible states, if asked", "L0": "terms this object coins"}
    for code in order:
        y, h = cb[code]
        mid = y + h / 2
        s.append(line(548, mid, 566, mid, op=0.45, sw=1))
        s.append(t(572, mid + 3.5, answers[code], 9.5, SANS, op=0.9))
    plate("06", "II. Movement", "Containment and expansion",
          "A contained system stays whole at L4. When the question turns to its origin, each answer goes to the layer that owns it.",
          ''.join(s), "0 0 760 410",
          "Two panels. On the left a 7LM stack with an OSI stack contained inside L4. On the right the same stack with an answer beside every layer and the OSI object still at L4")


# ============================================================ III. PLACEMENT

def p07():
    s = [arrows("p7"),
         '<path d="M 40 76 L 112 76 L 140 104 L 140 172 L 40 172 Z" fill="var(--sheet)" '
         'stroke="currentColor" stroke-width="1.3"/>',
         '<path d="M 112 76 L 112 104 L 140 104" fill="none" stroke="currentColor" stroke-width="1.3"/>']
    for i in range(4):
        s.append(line(54, 122 + i * 12, 126, 122 + i * 12, sw=1, op=0.4))
    s.append(t(90, 196, "one written document", 11, SANS, "var(--ink)", "middle"))
    for i, (code, txt) in enumerate([("L4", "the file as produced"), ("L5", "the argument it makes"),
                                     ("L6", "its versions and corrections"),
                                     ("L7", "the released publication")]):
        y = 40 + i * 48
        s.append(line(148, 124, 292, y + 20, sw=1.1, op=0.65, marker="p7"))
        s.append(box(300, y, 340, 40, op=0.9))
        s.append(t(318, y + 25, code, 13, MONO, "var(--accent)"))
        s.append(t(354, y + 25, txt, 11.5, SANS, "var(--ink)"))
    plate("07", "III. Placement", "One object, four owners",
          "A single document is filed four times over. No layer holds more than its own aspect of it.",
          ''.join(s), "0 0 680 240",
          "A document at left with four arrows to four boxes: L4 the file as produced, L5 the argument, L6 the versions, L7 the released publication")


def p08():
    s = [box(40, 20, 640, 52, fill="var(--accent-wash)", stroke="var(--accent)", sw=1.5),
         t(60, 44, "L7", 14, MONO, "var(--accent-ink)"),
         t(94, 44, "the desk &#8212; where the object meets everything outside it", 12, NARR, "var(--accent-ink)"),
         t(60, 62, "the position most often filed incorrectly", 10, SANS, "var(--accent-ink)", op=0.85)]
    cols = [
        ("L7/provenance/", "where it came from", ["sources, custody, lineage", "cited, never endorsed"]),
        ("L7/governance/", "the conditions on use", ["rights, licence, terms", "legal, not scientific"]),
        ("L7/peering/", "who you exchange with", ["peer-N / object-M", "the path names the source"]),
        ("L7/publications/", "what was released", ["each with a release id", "egress is not publication"]),
    ]
    for i, (path, role, lines) in enumerate(cols):
        x = 40 + i * 165
        s.append(line(x + 72, 76, x + 72, 104, sw=1, op=0.5))
        s.append(box(x, 106, 145, 110))
        s.append(t(x + 14, 128, path, 10, MONO, "var(--accent)"))
        s.append(t(x + 14, 148, role, 11, SANS, "var(--ink)"))
        for j, ln in enumerate(lines):
            s.append(t(x + 14, 172 + j * 24, ln, 9, SANS, op=0.85))
    s.append(line(40, 238, 680, 238, op=0.25, sw=1))
    s.append(t(360, 258, "Being on the desk proves nothing by itself. Each branch answers a different question; none of them makes a claim true.",
               10.5, SANS, "currentColor", "middle", 0.85))
    plate("08", "III. Placement", "The desk, in four branches",
          "Provenance, governance, peering and publications each answer a different question about the outside world.",
          ''.join(s), "0 0 720 276",
          "The L7 desk bar above four branch boxes: provenance, governance, peering and publications, each with the question it answers")


def p09():
    s = [t(330, 26, "DIRECTION", 10, NARR, "currentColor", "middle", 0.8, ' letter-spacing="0.1em"'),
         t(230, 48, "ingress", 12, MONO, "var(--ink)", "middle"),
         t(430, 48, "egress", 12, MONO, "var(--ink)", "middle"),
         t(36, 160, "EXPOSURE", 10, NARR, "currentColor", "middle", 0.8,
           ' letter-spacing="0.1em" transform="rotate(-90 36 160)"'),
         t(120, 112, "public", 12, MONO, "var(--ink)", "end"),
         t(120, 212, "private", 12, MONO, "var(--ink)", "end")]
    cells = [(0, 0, "a standards clause arriving", "public/ingress/peer-N/object-M/"),
             (1, 0, "your definition, exposed", "public/egress/peer-N/object-M/"),
             (0, 1, "an archive, read-only", "private/ingress/peer-N/object-M/"),
             (1, 1, "a controlled transfer out", "private/egress/peer-N/object-M/")]
    for cx, cy, what, path in cells:
        x, y = 134 + cx * 200, 64 + cy * 100
        s.append(box(x, y, 188, 88, op=0.9, rx=3))
        s.append(t(x + 16, y + 34, what, 11, SANS, "var(--ink)"))
        s.append(t(x + 16, y + 62, path, 8.5, MONO, "var(--accent)"))
    plate("09", "III. Placement", "Exposure by direction",
          "The two distinctions are independent. A peer may occupy more than one cell.",
          ''.join(s), "0 0 560 270",
          "A two by two grid of public and private against ingress and egress, each cell showing an example and its path pattern")


def p10():
    s = [arrows("p10"),
         box(20, 56, 320, 244, fill="none", dash="5 4", op=0.5, rx=4),
         t(180, 46, "the owner&#8217;s object", 11.5, NARR, "var(--ink)", "middle"),
         box(40, 108, 280, 44),
         t(56, 130, "L7 public egress", 11, MONO, "var(--ink)"),
         t(56, 145, "the definition, exposed at an exact version", 10, SANS, op=0.85),
         box(40, 228, 280, 44),
         t(56, 250, "L0", 11, MONO, "var(--ink)"),
         t(56, 265, "the definition lives here, once, at its owner", 10, SANS, op=0.85),
         line(180, 224, 180, 160, sw=1.4, marker="p10"),
         line(380, 40, 380, 110, dash="4 4", op=0.45, sw=1),
         line(380, 154, 380, 310, dash="4 4", op=0.45, sw=1),
         t(380, 30, "object boundary", 10, SANS, "currentColor", "middle", 0.8),
         box(420, 56, 320, 244, fill="none", dash="5 4", op=0.5, rx=4),
         t(580, 46, "the receiving object", 11.5, NARR, "var(--ink)", "middle"),
         box(440, 108, 280, 44, fill="var(--accent-wash)", stroke="var(--accent)", sw=1.4),
         t(456, 130, "L7 public ingress", 11, MONO, "var(--accent-ink)"),
         t(456, 145, "bound, reference-only &#183; NO EDIT &#183; NO DELETE", 10, SANS, "var(--accent-ink)", op=0.9),
         box(440, 228, 280, 44),
         t(456, 250, "L0", 11, MONO, "var(--ink)"),
         t(456, 265, "arrives as external input, never as local authorship", 10, SANS, op=0.85),
         line(580, 156, 580, 224, sw=1.4, marker="p10"),
         line(324, 130, 436, 130, stroke="var(--accent)", sw=1.6, marker="p10a"),
         t(380, 122, "exact version", 9.5, SANS, "var(--accent)", "middle"),
         t(380, 332, "an upstream change makes a new binding; it does not mutate the pinned one",
           9.5, SANS, "currentColor", "middle", 0.8)]
    plate("10", "III. Placement", "The route a borrowed definition travels",
          "Source L0, source L7 egress, receiving L7 ingress, receiving L0. Authorship never crosses the boundary.",
          ''.join(s), "0 0 760 346",
          "A definition moving from the owner object L0 up to its L7 egress, across the object boundary into the receiver L7 ingress, and down to the receiver L0")


# ============================================================ IV. OPERATION

def p11():
    s = [arrows("p11"), '<g transform="translate(0,-34)">',
         box(48, 64, 228, 72, fill="var(--accent-wash)", stroke="var(--accent)", sw=1.4, rx=3),
         t(162, 92, "L8/L5/research/review/", 10.5, MONO, "var(--accent-ink)", "middle"),
         t(162, 110, "the catch-all", 11, SANS, "var(--accent-ink)", "middle"),
         t(162, 126, "everything awaiting the owner", 9.5, SANS, "var(--accent-ink)", "middle", 0.85),
         box(384, 64, 228, 72, sw=1.3, rx=3),
         t(498, 92, "L8/L5/research/lanes/", 10.5, MONO, "var(--ink)", "middle"),
         t(498, 110, "the working position", 11, SANS, "var(--ink)", "middle"),
         t(498, 126, "one lane per question", 9.5, SANS, "currentColor", "middle", 0.85),
         line(282, 86, 378, 86, stroke="var(--accent)", sw=1.5, marker="p11a"),
         t(330, 78, "taken up", 9.5, SANS, "var(--accent)", "middle"),
         line(378, 116, 282, 116, sw=1.4, marker="p11"),
         t(330, 134, "set down again", 9.5, SANS, "currentColor", "middle", 0.85),
         '<path d="M 60 140 C 30 160, 30 186, 68 186" fill="none" stroke="currentColor" '
         'stroke-width="1.3" marker-end="url(#p11)" opacity="0.8"/>',
         t(80, 190, "set aside &#8212; stays here, labelled PARKED", 9.5, SANS, op=0.9),
         line(498, 142, 498, 186, sw=1.4, marker="p11"),
         t(512, 190, "finished &#8212; filed at its own layer", 9.5, SANS, op=0.9),
         '</g>']
    plate("11", "IV. Operation", "The catch-all and the lanes",
          "Two moves and two exits. Position is state: the moves are the record, and nothing is deleted along the way.",
          ''.join(s), "0 0 724 172",
          "The catch-all at review and the working position at lanes, with arrows for taken up, set down again, parked, and filed at its own layer")


def p12():
    s = [arrows("p12"),
         box(20, 96, 176, 52, sw=1.3, rx=3),
         t(108, 120, "a superseded file", 11.5, SANS, "var(--ink)", "middle"),
         t(108, 136, "something replaced", 9.5, SANS, "currentColor", "middle", 0.8),
         line(200, 122, 252, 122, sw=1.4, marker="p12"),
         '<path d="M 340 74 L 424 122 L 340 170 L 256 122 Z" fill="var(--accent-wash)" '
         'stroke="var(--accent)" stroke-width="1.4"/>',
         t(340, 117, "does integrity need it", 9.5, SANS, "var(--accent-ink)", "middle"),
         t(340, 131, "reconstructable?", 9.5, SANS, "var(--accent-ink)", "middle"),
         '<path d="M 340 70 L 340 46 L 470 46" fill="none" stroke="currentColor" '
         'stroke-width="1.4" marker-end="url(#p12)"/>',
         t(352, 40, "yes", 10, MONO, "var(--ink)"),
         box(476, 22, 204, 52, sw=1.3, rx=3),
         t(492, 44, "L8/L6/retired/", 10, MONO, "var(--accent)"),
         t(492, 60, "retired unchanged, headings and all", 10, SANS, op=0.9),
         '<path d="M 340 174 L 340 200 L 470 200" fill="none" stroke="currentColor" '
         'stroke-width="1.4" marker-end="url(#p12)"/>',
         t(352, 194, "no", 10, MONO, "var(--ink)"),
         box(476, 176, 204, 52, sw=1.3, rx=3),
         t(492, 198, "L8/L6/history/", 10, MONO, "var(--accent)"),
         t(492, 214, "enumerate every part, then delete", 10, SANS, op=0.9),
         t(350, 254, "git keeps the change event; the record keeps the enumeration",
           9.5, SANS, "currentColor", "middle", 0.85)]
    plate("12", "IV. Operation", "Retire, or enumerate and delete",
          "The rule enforced is integrity, not the absence of deletion. Deletion after enumeration is the ordinary act.",
          ''.join(s), "0 0 700 264",
          "A decision diagram: a superseded file reaches the question of whether integrity needs it reconstructable, with yes leading to retirement unchanged and no leading to enumeration then deletion")


# ============================================ V. OPEN - NOT IN THE SPECIFICATION

def unit(x0, name, role, sub):
    """One bounded object drawn as a framed packet: start bar, body, stop bar."""
    g = [f'<rect x="{x0}" y="60" width="10" height="120" fill="var(--open)"/>',
         f'<rect x="{x0 + 180}" y="60" width="10" height="120" fill="var(--open)"/>',
         box(x0 + 14, 60, 162, 120)]
    g.append(t(x0 + 95, 84, name, 10, MONO, "var(--ink)", "middle"))
    g.append(t(x0 + 95, 102, role, 10.5, SANS, "currentColor", "middle", 0.9))
    g.append(t(x0 + 95, 116, sub, 9, SANS, "currentColor", "middle", 0.7))
    for i in range(7):
        g.append(line(x0 + 26, 132 + i * 6, x0 + 86, 132 + i * 6, sw=2, op=0.45))
    g.append(t(x0 + 94, 156, "L1 &#8230; L7", 9.5, MONO, op=0.8))
    g.append(t(x0 + 94, 168, "carried", 9, SANS, op=0.7))
    g.append(t(x0 + 95, 196, "L8 &#8212; the frame", 9.5, NARR, "var(--open)", "middle"))
    g.append(line(x0 + 95, 202, x0 + 95, 218, dash="3 3", op=0.5, sw=1))
    g.append(box(x0 + 20, 218, 150, 36, dash="4 3", op=0.75))
    g.append(t(x0 + 95, 234, "L0", 10, MONO, "var(--ink)", "middle"))
    g.append(t(x0 + 95, 247, "in the head, then written down", 8.5, SANS, "currentColor", "middle", 0.8))
    return ''.join(g)


def p13():
    s = [arrows("p13"),
         box(16, 78, 118, 84, fill="none", dash="4 3", op=0.6),
         t(75, 100, "nine standards", 10, SANS, "currentColor", "middle", 0.9),
         t(75, 114, "bodies", 10, SANS, "currentColor", "middle", 0.9),
         t(75, 134, "ISO &#183; IEEE &#183; NIST", 8.5, MONO, "currentColor", "middle", 0.75),
         t(75, 147, "EU &#183; DoD &#183; EASA &#183; ETSI", 8.5, MONO, "currentColor", "middle", 0.75),
         line(138, 120, 164, 120, sw=1.4, marker="p13"),
         unit(170, "aybllc/autonomous", "consensus baseline", "the narrowest agreement"),
         line(364, 120, 404, 120, stroke="var(--open)", sw=1.6, marker="p13o"),
         t(384, 112, "bound", 9, SANS, "var(--open)", "middle"),
         unit(410, "aybllc/auditonomous", "local delta", "its own difference only"),
         line(604, 120, 640, 120, stroke="var(--open)", sw=1.6, marker="p13o"),
         t(692, 116, "&#8230; the stream continues", 10, SANS, "currentColor", "middle", 0.7),
         t(692, 132, "each frame joins to the next", 9, SANS, "currentColor", "middle", 0.6),
         line(16, 286, 744, 286, op=0.25, sw=1),
         t(16, 306, "The frame is the glue: it marks where one object ends and the next begins, so a run of them reads as a stream rather than a blur.",
           10, SANS, op=0.9),
         t(16, 322, "L0 sits outside the frame. The packet carries a reference to the meaning, not the meaning itself.",
           10, SANS, op=0.9)]
    plate("13", "V. Open &#8212; not in the specification", "Objects in a stream",
          "L8 read as the frame that makes one object a single unit, so objects can be set end to end and the run of them is lineage.",
          ''.join(s), "0 0 760 336",
          "Nine standards bodies feeding the autonomous object, which binds to the auditonomous object, each object drawn as a packet between two frame bars with L0 outside the frame",
          status="PROPOSED")


def p14():
    s = [arrows("p14")]
    # Reading A - what the specification says today
    s.append(box(16, 44, 348, 168, fill="none", op=0.5))
    s.append(t(32, 34, "READING A &#183; specification, 12 September 2026", 9.5, NARR,
               "currentColor", "start", 0.8, ' letter-spacing="0.08em"'))
    s.append(box(36, 64, 96, 40, fill="var(--accent-wash)", stroke="var(--accent)", sw=1.3))
    s.append(t(84, 89, "L7", 13, MONO, "var(--accent-ink)", "middle"))
    s.append(box(146, 64, 198, 40))
    s.append(t(245, 89, "L8 &#8835; L0 &#8230; L6", 12, MONO, "var(--ink)", "middle"))
    s.append(t(190, 122, "siblings on disk", 10, SANS, "currentColor", "middle", 0.85))
    for i in range(8):
        s.append(box(36 + i * 32, 140, 28, 28, op=0.8))
        s.append(t(50 + i * 32, 158, f"{i}", 10, MONO, "var(--ink)", "middle"))
    s.append(box(298, 140, 46, 28, fill="var(--accent-wash)", stroke="var(--accent)", sw=1.3))
    s.append(t(321, 158, "L8", 10, MONO, "var(--accent-ink)", "middle"))
    s.append(t(36, 186, "L0 &#8230; L7 are the eight bits; L8 is the extra bit, a check bit.", 9.5, SANS, op=0.85))
    s.append(t(36, 200, "It carries the semantic and catches an error.", 9.5, SANS, op=0.85))
    # Reading B - the proposal
    s.append(box(396, 44, 348, 168, fill="none", stroke="var(--open)", op=0.6))
    s.append(t(412, 34, "READING B &#183; proposed", 9.5, NARR, "var(--open)", "start", 1,
               ' letter-spacing="0.08em"'))
    s.append('<rect x="416" y="64" width="8" height="40" fill="var(--open)"/>')
    s.append('<rect x="700" y="64" width="8" height="40" fill="var(--open)"/>')
    s.append(box(428, 64, 268, 40))
    s.append(t(500, 89, "L7", 12, MONO, "var(--ink)", "middle"))
    s.append(line(540, 68, 540, 100, op=0.35, sw=1))
    s.append(t(620, 89, "L1 &#8230; L6", 12, MONO, "var(--ink)", "middle"))
    s.append(t(562, 122, "L8 frames the whole object", 10, SANS, "var(--open)", "middle"))
    s.append(box(416, 140, 84, 30, dash="4 3", op=0.75))
    s.append(t(458, 159, "L0", 11, MONO, "var(--ink)", "middle"))
    s.append(line(504, 155, 524, 155, dash="3 3", op=0.5, sw=1))
    s.append(t(530, 152, "outside the frame &#8212; referenced,", 9.5, SANS, op=0.85))
    s.append(t(530, 165, "not carried", 9.5, SANS, op=0.85))
    s.append(t(416, 190, "The extra bit changes job: framing marks the boundary,", 9.5, SANS, op=0.85))
    s.append(t(416, 204, "where parity only detects a corruption after the fact.", 9.5, SANS, op=0.85))
    # the two unresolved questions
    s.append(line(16, 238, 744, 238, op=0.25, sw=1))
    qs = [(16, "Does the tree move?",
           "L7/ and L8/ stay siblings", "L7/ moves inside L8/",
           "semantic enclosure only, paths unchanged",
           "every path in three repositories, plus check G-002"),
          (396, "What does eight count?",
           "L0 &#8230; L7 are the bits", "L1 &#8230; L7, and L0 outside",
           "the byte reading stands as written",
           "the byte reading is retired for the frame reading")]
    for x0, q, optA, optB, noteA, noteB in qs:
        s.append(t(x0, 262, q, 12, NARR, "var(--open)"))
        for i, (opt, note) in enumerate(((optA, noteA), (optB, noteB))):
            y = 276 + i * 44
            s.append(box(x0, y, 348, 38, stroke="var(--open)", op=0.55, dash="4 3"))
            s.append(t(x0 + 14, y + 17, opt, 10.5, MONO, "var(--ink)"))
            s.append(t(x0 + 14, y + 31, note, 9, SANS, op=0.8))
    plate("14", "V. Open &#8212; not in the specification", "What does L8 enclose?",
          "Two readings, and the two questions that have to be ruled before either can be written into the specification.",
          ''.join(s), "0 0 760 372",
          "Reading A shows L7 and L8 as siblings with L0 to L7 as eight bits and L8 as a check bit. Reading B shows L8 as a frame around the whole object with L0 outside it. Below, two open questions: whether the directory tree moves, and what the count of eight refers to",
          status="OPEN CALL")


for fn in (p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p11, p12, p13, p14):
    fn()

# ---------------------------------------------------------------- the page

CSS = """
:root {
  --ground:#E9ECE8; --sheet:#FAFBF9; --ink:#14201C; --ink-2:#45524C; --ink-3:#74817A;
  --rule:#C6CEC8; --rule-2:#DCE2DD; --accent:#14554A; --accent-ink:#0E3F37;
  --accent-wash:#DCE9E5; --open:#A8431C; --open-wash:#F4E4DC;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ground:#101614; --sheet:#18201D; --ink:#E4EAE6; --ink-2:#AFBCB6; --ink-3:#7C8A84;
    --rule:#2C3733; --rule-2:#222B28; --accent:#6FC2B0; --accent-ink:#9BD8C9;
    --accent-wash:#16302B; --open:#E08A5E; --open-wash:#33211A;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --ground:#101614; --sheet:#18201D; --ink:#E4EAE6; --ink-2:#AFBCB6; --ink-3:#7C8A84;
  --rule:#2C3733; --rule-2:#222B28; --accent:#6FC2B0; --accent-ink:#9BD8C9;
  --accent-wash:#16302B; --open:#E08A5E; --open-wash:#33211A;
  color-scheme: dark;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0; background: var(--ground); color: var(--ink);
  font-family: Archivo, "Helvetica Neue", Arial, sans-serif; font-size: 16px; line-height: 1.55;
  padding-block: 1.5rem 3rem; padding-inline: clamp(16px, 3vw, 36px);
}
.sheet { max-width: 1180px; margin: 0 auto; border: 1px solid var(--rule); background: var(--sheet); }
code, .mono { font-family: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace; }

/* title block */
.titleblock { border-bottom: 2px solid var(--ink); padding: 1.6rem clamp(16px, 2.6vw, 32px) 1.2rem; }
.titleblock .kicker {
  font-family: "Archivo Narrow", Archivo, sans-serif; font-size: 0.74rem; font-weight: 600;
  letter-spacing: 0.18em; text-transform: uppercase; color: var(--accent); margin: 0 0 0.5rem;
}
h1 {
  font-family: "Archivo Narrow", Archivo, sans-serif; font-weight: 600;
  font-size: clamp(1.75rem, 4.2vw, 2.6rem); line-height: 1.05; letter-spacing: -0.01em;
  margin: 0 0 0.6rem; text-wrap: balance;
}
.titleblock .lede { margin: 0 0 1.3rem; max-width: 62ch; color: var(--ink-2); font-size: 1rem; }
.specs { display: grid; grid-template-columns: repeat(auto-fit, minmax(168px, 1fr));
         gap: 0.9rem 1.6rem; border-top: 1px solid var(--rule); padding-top: 0.9rem; }
.specs dt { font-family: "Archivo Narrow", Archivo, sans-serif; font-size: 0.68rem; font-weight: 600;
            letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-3); margin: 0 0 0.2rem; }
.specs dd { margin: 0; font-size: 0.86rem; line-height: 1.4; color: var(--ink); }
.specs dd.mono { font-size: 0.8rem; }

/* parts and plates */
.part {
  display: flex; align-items: baseline; gap: 1rem;
  padding: 1.5rem clamp(16px, 2.6vw, 32px) 0.5rem;
  font-family: "Archivo Narrow", Archivo, sans-serif; font-weight: 600;
  font-size: 0.82rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent);
}
.part::after { content: ""; flex: 1; height: 1px; background: var(--rule); }
.part.open { color: var(--open); }

.plate { display: grid; grid-template-columns: 62px minmax(0, 1fr);
         border-top: 1px solid var(--rule-2); }
.plate:first-of-type { border-top: 0; }
.rail { border-right: 1px solid var(--rule-2); padding: 1.15rem 0 1.5rem;
        display: flex; flex-direction: column; align-items: center; gap: 0.5rem; }
.rail .no { font-family: "IBM Plex Mono", monospace; font-size: 1.05rem; color: var(--ink-3);
            font-variant-numeric: tabular-nums; }
.rail .tick { width: 1px; flex: 1; background: var(--rule-2); }
.body { padding: 1.15rem clamp(16px, 2.6vw, 32px) 1.6rem 1.3rem; min-width: 0; }
h2 { font-family: "Archivo Narrow", Archivo, sans-serif; font-weight: 600; font-size: 1.32rem;
     line-height: 1.15; margin: 0 0 0.35rem; text-wrap: balance; }
.claim { margin: 0 0 1rem; color: var(--ink-2); font-size: 0.94rem; max-width: 74ch; }
.claim em { font-style: italic; }
.chip { display: inline-block; vertical-align: 0.22em; margin-left: 0.6rem;
        font-family: "Archivo Narrow", Archivo, sans-serif; font-size: 0.62rem; font-weight: 600;
        letter-spacing: 0.12em; text-transform: uppercase; color: var(--open);
        background: var(--open-wash); border: 1px solid var(--open); padding: 0.12em 0.5em; }
.frame { overflow-x: auto; border: 1px solid var(--rule); background: var(--sheet); }
.frame svg { display: block; width: 100%; height: auto; color: var(--ink-2); padding: 0.6rem 0.4rem; }
@media (max-width: 680px) { .frame svg { min-width: 560px; } }

/* foot */
.foot { border-top: 2px solid var(--ink); padding: 1.4rem clamp(16px, 2.6vw, 32px) 1.6rem;
        display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1.4rem 2rem; }
.foot h3 { font-family: "Archivo Narrow", Archivo, sans-serif; font-size: 0.68rem; font-weight: 600;
           letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-3); margin: 0 0 0.5rem; }
.foot p, .foot li { font-size: 0.84rem; color: var(--ink-2); margin: 0 0 0.4rem; line-height: 1.45; }
.foot ul { margin: 0; padding-left: 1.05rem; }
.foot li::marker { color: var(--ink-3); }
.swatch { display: inline-block; width: 0.72em; height: 0.72em; margin-right: 0.35em;
          vertical-align: -0.02em; border: 1px solid var(--rule); }
.swatch.a { background: var(--accent); border-color: var(--accent); }
.swatch.o { background: var(--open); border-color: var(--open); }
.colophon { max-width: 1180px; margin: 0.9rem auto 0; color: var(--ink-3); font-size: 0.78rem;
            line-height: 1.5; }
a { color: var(--accent); text-underline-offset: 3px; }
a:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
"""

HEAD = ('<title>The 7LM Plate Sheet</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Archivo:wght@400;500;600&family=Archivo+Narrow:wght@500;600'
        '&family=IBM+Plex+Mono:wght@400;500&display=swap">\n'
        '<style>' + CSS + '</style>')

TITLEBLOCK = """
<header class="titleblock">
  <p class="kicker">Seven-Layer Model &#183; drawn, not described</p>
  <h1>The 7LM Plate Sheet</h1>
  <p class="lede">Fourteen plates. Every rule of the model that can be drawn is drawn here, and
  drawn here only &#8212; one sheet to change when the model changes. Plates 01&#8211;12 state what the
  specification ratifies. Plates 13&#8211;14 carry a proposal it does not yet contain.</p>
  <dl class="specs">
    <div><dt>Source</dt><dd>Harmonized Authoritative Architecture Specification, 12 September 2026</dd></div>
    <div><dt>Repository</dt><dd class="mono">aybllc/7lm</dd></div>
    <div><dt>Plates</dt><dd>14 &#183; twelve ratified, two open</dd></div>
    <div><dt>Controls</dt><dd>Where this sheet and the specification differ, the specification controls.</dd></div>
  </dl>
</header>
"""

FOOT = """
<footer class="foot">
  <div>
    <h3>Reading the drawings</h3>
    <p><span class="swatch a"></span>Pine marks the element carrying the claim in each plate.</p>
    <p><span class="swatch o"></span>Oxide marks what is proposed and not yet ruled &#8212; plates 13 and 14 only.</p>
    <p>Monospace is a real path in the repository. Every file and folder named here exists.</p>
  </div>
  <div>
    <h3>Open calls on this sheet</h3>
    <ul>
      <li>Does the tree move, or is the enclosure semantic only?</li>
      <li>What does the count of eight refer to once L0 sits outside the frame?</li>
    </ul>
    <p>Both are the owner&#8217;s to rule. Until then the specification stands as written.</p>
  </div>
  <div>
    <h3>Standing rules</h3>
    <ul>
      <li>Nothing is deleted before it is enumerated at <span class="mono">L8/L6/history/</span>.</li>
      <li>Retired sets stay verbatim, headings and all.</li>
      <li>Higher layers never silently repair lower ones.</li>
    </ul>
  </div>
</footer>
"""


def render():
    out, last_part = [], None
    for p in PLATES:
        if p["part"] != last_part:
            cls = "part open" if p["part"].startswith("V.") else "part"
            out.append(f'<div class="{cls}"><span>{p["part"]}</span></div>')
            last_part = p["part"]
        chip = f'<span class="chip">{p["status"]}</span>' if p["status"] else ''
        out.append(
            '<section class="plate">'
            f'<div class="rail"><span class="no">{p["n"]}</span><span class="tick"></span></div>'
            '<div class="body">'
            f'<h2>{p["title"]}{chip}</h2>'
            f'<p class="claim">{p["claim"]}</p>'
            f'<div class="frame"><svg viewBox="{p["vb"]}" role="img" aria-label="{p["alt"]}">'
            f'{p["svg"]}</svg></div>'
            '</div></section>')
    page = (HEAD + '\n<div class="sheet">' + TITLEBLOCK + ''.join(out) + FOOT + '</div>\n'
            '<p class="colophon">Drawn from the Harmonized Authoritative Architecture Specification '
            'and the <span class="mono">0.md</span> sheets of <span class="mono">aybllc/7lm</span>. '
            'The plain-language companion is the 7LM Field Guide, filed at '
            '<span class="mono">L8/L0/pedagogy/7lm-field-guide.md</span>.</p>\n')
    OUT.write_text(page, encoding='utf-8')
    print(f"wrote {OUT} ({len(page):,} bytes); plates: {len(PLATES)}")


if __name__ == '__main__':
    render()
