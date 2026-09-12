#!/usr/bin/env python3
"""The 7LM plate sheet: the Seven-Layer Model drawn.

One source file. Every drawing on the sheet is defined here and nowhere else, so
there is one place to change when the model changes.

One plate for now, on the owner's word of 12 September 2026: the eight positions,
with L8 as the envelope around all of them. L0 is the origin. L1 is the floor and
L6 the end of the payload. L7 is the glue. L8's trailing edge is the connector to
the next object's L0.
"""
import pathlib

OUT = pathlib.Path(__file__).with_name('7lm-plate-sheet.html')

MONO = "IBM Plex Mono, ui-monospace, monospace"
SANS = "Archivo, system-ui, sans-serif"
NARR = "Archivo Narrow, Archivo, system-ui, sans-serif"


def arrows(pid):
    """Marker defs for one plate: <pid> in ink, <pid>a in accent."""
    out = []
    for suffix, fill in (("", "currentColor"), ("a", "var(--accent)")):
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


SMALLCAPS = ' letter-spacing="0.1em"'

PLATES = []


def plate(n, title, claim, svg, vb, alt):
    PLATES.append(dict(n=n, title=title, claim=claim, svg=svg, vb=vb, alt=alt))


# ------------------------------------------------------- 01. the eight positions

def p01():
    payload = [
        ("L6", "Library / Memory", "prior states, corrections, retirement", "END"),
        ("L5", "Research / Discourse", "interpretation, review, findings", ""),
        ("L4", "Conversion / Realization", "what was made, run, measured, failed", ""),
        ("L3", "Engineering Mathematics", "units, tolerance, uncertainty, feasibility", ""),
        ("L2", "Formal Mathematics", "exact relations, operators, proofs", ""),
        ("L1", "State Space", "admissible states, invariants, exclusions", "FLOOR"),
    ]
    s = [arrows("p1")]

    # the connector: L8's trailing edge, and where it goes
    s.append(line(360, 64, 360, 24, stroke="var(--accent)", sw=1.8, marker="p1a"))
    s.append(t(372, 32, "CONNECTOR", 9.5, NARR, "var(--accent)", "start", 1, SMALLCAPS))
    s.append(t(372, 46, "to the next object&#8217;s L0", 10, SANS, op=0.85))
    s.append(t(348, 46, "L8&#8217;s trailing edge", 10, SANS, "currentColor", "end", 0.85))

    # the envelope: L8 around every position
    s.append(box(30, 70, 660, 532, fill="none", stroke="currentColor", sw=1.4, rx=4))
    s.append('<rect x="30" y="66" width="660" height="8" rx="2" fill="var(--accent)"/>')
    s.append(t(50, 100, "L8", 15, MONO, "var(--ink)"))
    s.append(t(84, 100, "the envelope &#8212; it encloses every position, and hands off to the next object",
               11, SANS, op=0.85))

    # L7: the glue
    s.append(box(50, 114, 620, 54, fill="var(--accent-wash)", stroke="var(--accent)", sw=1.5))
    s.append(t(70, 139, "L7", 15, MONO, "var(--accent-ink)"))
    s.append(t(106, 139, "the desk &#183; Surface / Forward Face", 13, NARR, "var(--accent-ink)"))
    s.append(t(70, 158, "provenance &#183; governance &#183; peering &#183; publications", 10.5,
               SANS, "var(--accent-ink)", op=0.85))
    s.append(t(650, 139, "GLUE", 9.5, NARR, "var(--accent)", "end", 1, SMALLCAPS))
    s.append(t(650, 158, "binds outward", 9.5, SANS, "var(--accent-ink)", "end", 0.85))

    # the payload: floor L1, end L6
    s.append(t(650, 190, "PAYLOAD", 9.5, NARR, "currentColor", "end", 0.75, SMALLCAPS))
    y = 198
    for code, name, job, mark in payload:
        s.append(box(50, y, 620, 40, op=0.9))
        s.append(t(70, y + 25, code, 13, MONO, "var(--accent)"))
        s.append(t(110, y + 25, name, 12.5, SANS, "var(--ink)"))
        s.append(t(300, y + 25, job, 10.5, SANS, op=0.85))
        if mark:
            s.append(t(650, y + 25, mark, 9.5, NARR, "currentColor", "end", 0.75, SMALLCAPS))
        y += 46
    # bracket down the right of the payload
    s.append('<path d="M 680 198 L 686 198 L 686 474 L 680 474" fill="none" stroke="currentColor" '
             'stroke-width="1.1" opacity="0.5"/>')

    # L0: the origin
    s.append(line(50, 486, 670, 486, dash="4 4", op=0.45, sw=1))
    s.append(box(50, 498, 620, 54, fill="var(--ground)"))
    s.append(t(70, 523, "L0", 15, MONO, "var(--ink)"))
    s.append(t(106, 523, "Semantic / Foundational", 13, NARR, "var(--ink)"))
    s.append(t(70, 542, "the meaning &#8212; in the head first, written down second &#183; not payload",
               10.5, SANS, op=0.85))
    s.append(t(650, 523, "ORIGIN", 9.5, NARR, "currentColor", "end", 0.75, SMALLCAPS))

    # the count, unchanged
    s.append(t(360, 576, "Eight positions, L0 through L7. First is always 0.",
               10, SANS, "currentColor", "middle", 0.8))
    s.append(t(360, 591, "L8 is not a ninth position: it is the envelope around the eight, and the connector to the next.",
               10, SANS, "currentColor", "middle", 0.8))

    plate("01", "The eight positions",
          "L8 envelopes them all. L0 is the origin. L1 is the floor and L6 the end of the payload. "
          "L7 is the glue. L8&#8217;s trailing edge is the connector to the next object&#8217;s L0.",
          ''.join(s), "0 0 720 616",
          "An envelope labelled L8 enclosing, from top to bottom, the desk L7 marked glue, the six "
          "payload layers L6 down to L1 with L6 marked end and L1 marked floor, and L0 at the base "
          "marked origin. The envelope's top edge is thickened and an arrow leaves it upward, "
          "labelled connector to the next object's L0.")


p01()

# ---------------------------------------------------------------- the page

CSS = """
:root {
  --ground:#E9ECE8; --sheet:#FAFBF9; --ink:#14201C; --ink-2:#45524C; --ink-3:#74817A;
  --rule:#C6CEC8; --rule-2:#DCE2DD; --accent:#14554A; --accent-ink:#0E3F37;
  --accent-wash:#DCE9E5;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ground:#101614; --sheet:#18201D; --ink:#E4EAE6; --ink-2:#AFBCB6; --ink-3:#7C8A84;
    --rule:#2C3733; --rule-2:#222B28; --accent:#6FC2B0; --accent-ink:#9BD8C9;
    --accent-wash:#16302B;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --ground:#101614; --sheet:#18201D; --ink:#E4EAE6; --ink-2:#AFBCB6; --ink-3:#7C8A84;
  --rule:#2C3733; --rule-2:#222B28; --accent:#6FC2B0; --accent-ink:#9BD8C9;
  --accent-wash:#16302B;
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
.mono { font-family: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace; }

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

/* plates */
.plate { display: grid; grid-template-columns: 62px minmax(0, 1fr); }
.rail { border-right: 1px solid var(--rule-2); padding: 1.15rem 0 1.5rem;
        display: flex; flex-direction: column; align-items: center; gap: 0.5rem; }
.rail .no { font-family: "IBM Plex Mono", monospace; font-size: 1.05rem; color: var(--ink-3);
            font-variant-numeric: tabular-nums; }
.rail .tick { width: 1px; flex: 1; background: var(--rule-2); }
.body { padding: 1.15rem clamp(16px, 2.6vw, 32px) 1.6rem 1.3rem; min-width: 0; }
h2 { font-family: "Archivo Narrow", Archivo, sans-serif; font-weight: 600; font-size: 1.32rem;
     line-height: 1.15; margin: 0 0 0.35rem; text-wrap: balance; }
.claim { margin: 0 0 1rem; color: var(--ink-2); font-size: 0.94rem; max-width: 74ch; }
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
  <p class="lede">One plate, for now: the eight positions, with L8 as the envelope around all of
  them. Every rule of the model that can be drawn will be drawn here, and here only &#8212; one
  sheet to change when the model changes.</p>
  <dl class="specs">
    <div><dt>Source</dt><dd>The owner&#8217;s words of 12 September 2026, on the Harmonized Authoritative Architecture Specification of the same date</dd></div>
    <div><dt>Repository</dt><dd class="mono">aybllc/7lm</dd></div>
    <div><dt>Plates</dt><dd>1 &#183; the eight positions</dd></div>
    <div><dt>Standing</dt><dd>The specification&#8217;s text still places L7 beside L8 and names L8 the interior. This plate draws L8 as the owner has since described it; the specification&#8217;s revision awaits the owner&#8217;s word on the tree.</dd></div>
  </dl>
</header>
"""

FOOT = """
<footer class="foot">
  <div>
    <h3>Reading the drawing</h3>
    <p><span class="swatch a"></span>Pine marks the two faces of the packet: the glue at L7, and the connector at L8&#8217;s trailing edge.</p>
    <p>Monospace is a real path in the repository. Every position named here carries its own <span class="mono">0.md</span> sheet.</p>
  </div>
  <div>
    <h3>What the drawing does not decide</h3>
    <p>Whether <span class="mono">L7/</span> moves inside <span class="mono">L8/</span> on disk, or the envelope is semantic and the paths stay as they are. That is the owner&#8217;s call, and it is what stands between this drawing and the specification.</p>
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
    out = []
    for p in PLATES:
        out.append(
            '<section class="plate">'
            f'<div class="rail"><span class="no">{p["n"]}</span><span class="tick"></span></div>'
            '<div class="body">'
            f'<h2>{p["title"]}</h2>'
            f'<p class="claim">{p["claim"]}</p>'
            f'<div class="frame"><svg viewBox="{p["vb"]}" role="img" aria-label="{p["alt"]}">'
            f'{p["svg"]}</svg></div>'
            '</div></section>')
    page = (HEAD + '\n<div class="sheet">' + TITLEBLOCK + ''.join(out) + FOOT + '</div>\n'
            '<p class="colophon">Drawn from the owner&#8217;s words and the '
            '<span class="mono">0.md</span> sheets of <span class="mono">aybllc/7lm</span>. '
            'The plain-language companion is the 7LM Field Guide, filed at '
            '<span class="mono">L8/L0/pedagogy/7lm-field-guide.md</span>.</p>\n')
    OUT.write_text(page, encoding='utf-8')
    print(f"wrote {OUT} ({len(page):,} bytes); plates: {len(PLATES)}")


if __name__ == '__main__':
    render()
