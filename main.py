"""main.py — draws "The World in One Day", 24 November 2026.

Pure stdlib. Writes one 1024x1024 PNG to $MAKEFUN_OUTPUT_DIR (else
/output) as entry.png. Deterministic: same bytes every run.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import draw
from draw import Canvas, png_bytes, draw_text, draw_text_centered, wrap_words

# ---------------------------------------------------------------- colors --
PAPER = bytes([248, 244, 232])
BEIGE = bytes([239, 231, 211])
INK = bytes([26, 26, 26])
RED = bytes([192, 57, 43])
BLUE = bytes([44, 95, 138])
GREEN = bytes([46, 125, 50])
ORANGE = bytes([230, 126, 34])
YELLOW = bytes([241, 196, 15])
DARK = bytes([58, 58, 58])
GREY = bytes([107, 107, 107])
LBLUE = bytes([127, 179, 213])
DBLUE = bytes([31, 97, 141])
SMOKE = bytes([80, 80, 80])

W = 1024
H = 1024


# ------------------------------------------------------------ masthead ----
def draw_masthead(cv):
    draw_text_centered(cv, W // 2, 14, "THE WORLD IN ONE DAY", INK, 6)
    cv.hline(20, 96, W - 40, INK, 2)
    draw_text(cv, 20, 106, "TUESDAY 24 NOVEMBER 2026", INK, 2)
    tag = "ONE DAY - ONE IMAGE"
    draw_text(cv, W - 20 - draw.text_width(tag, 2), 106, tag, INK, 2)
    cv.hline(20, 132, W - 40, INK, 1)


# -------------------------------------------------------------- lead 1 ----
def draw_lead1(cv):
    """Factory fire in Banten. Panel x 20..504, art y 248..500."""
    x0, x1 = 28, 496
    # kicker + headline
    draw_text(cv, 28, 152, "INDONESIA", RED, 2)
    draw_text(cv, 28, 178, "INDONESIA FACTORY", INK, 4)
    draw_text(cv, 28, 210, "BLAZE KILLS 24", INK, 4)
    # ground
    cv.fill_rect(x0, 462, x1 - x0, 38, DARK)
    # chimney + smoke
    cv.fill_rect(392, 268, 22, 66, DARK)
    for cx, cy, r in ((403, 254, 12), (397, 236, 14), (405, 218, 10)):
        cv.disc(cx, cy, r, SMOKE)
    # factory block + gable roof
    cv.fill_rect(96, 332, 330, 130, GREY)
    cv.poly([(84, 332), (261, 292), (438, 332)], DARK)
    # lit windows
    for wx in (120, 180, 300, 360):
        cv.fill_rect(wx, 360, 34, 30, YELLOW)
        cv.rect(wx, 360, 34, 30, INK, 2)
    # door + workers
    cv.fill_rect(236, 402, 44, 60, INK)
    for wx, wy in ((206, 436), (292, 436)):
        cv.disc(wx, wy - 8, 7, INK)
        cv.fill_rect(wx - 6, wy, 12, 26, INK)
    # hose from the left edge to the workers
    cv.line(28, 486, 200, 452, BLUE, 4)
    cv.line(200, 452, 236, 446, BLUE, 4)
    for dx, dy in ((12, -8), (22, -14), (32, -6), (18, -20)):
        cv.line(236, 446, 236 + dx, 446 + dy, LBLUE, 2)
    # flames rising from the roof: red, orange, yellow tongues
    cv.poly([(150, 330), (190, 238), (215, 300), (240, 226), (268, 302),
             (292, 244), (330, 330)], RED)
    cv.poly([(180, 330), (205, 262), (228, 308), (252, 254), (278, 306),
             (300, 268), (316, 330)], ORANGE)
    cv.poly([(215, 330), (232, 282), (250, 316), (266, 276), (282, 330)],
            YELLOW)
    # embers
    for ex, ey, r in ((170, 222, 3), (300, 230, 3), (258, 208, 4),
                      (330, 258, 3)):
        cv.disc(ex, ey, r, ORANGE)
    # caption
    draw_text(cv, 28, 516, "BANTEN: 24 DEAD, 30 MISSING", INK, 2)
    cv.rect(20, 144, 484, 436, INK, 2)


# -------------------------------------------------------------- lead 2 ----
def draw_lead2(cv):
    """Ukraine war spreads: air, sea, fire. Panel x 520..1004."""
    draw_text(cv, 528, 152, "UKRAINE WAR", RED, 2)
    draw_text(cv, 528, 178, "UKRAINE WAR SPREADS", INK, 4)
    draw_text(cv, 528, 210, "AIR, SEA, FIRE", INK, 4)
    # sub-panel separators
    cv.vline(682, 248, 252, INK, 1)
    cv.vline(840, 248, 252, INK, 1)
    # --- A: house in Dymer, Kyiv region (x 528..682)
    cv.fill_rect(528, 462, 154, 38, DARK)
    cv.fill_rect(556, 392, 96, 70, GREY)
    cv.poly([(546, 392), (604, 352), (662, 392)], RED)
    cv.fill_rect(592, 420, 22, 42, INK)
    for cx, cy, r in ((604, 336, 13), (598, 312, 16), (606, 286, 12),
                      (600, 264, 8)):
        cv.disc(cx, cy, r, SMOKE)
    # missile lightning bolt
    cv.poly([(646, 262), (628, 300), (640, 300), (624, 338), (656, 292),
             (644, 292), (662, 262)], RED)
    # --- B: cargo ship Sparta II afire (x 682..840)
    cv.fill_rect(682, 430, 158, 70, LBLUE)
    cv.line(682, 446, 840, 446, DBLUE, 2)
    cv.line(682, 470, 840, 470, DBLUE, 2)
    cv.poly([(700, 404), (824, 404), (812, 432), (712, 432)], DARK)
    for bx, bc in ((706, RED), (738, YELLOW), (770, BLUE)):
        cv.fill_rect(bx, 376, 28, 28, bc)
    cv.poly([(742, 376), (756, 336), (766, 362), (780, 330), (792, 376)],
            ORANGE)
    cv.disc(770, 322, 5, YELLOW)
    # drone above
    cv.line(748, 296, 772, 312, INK, 3)
    cv.line(772, 296, 748, 312, INK, 3)
    cv.hline(742, 292, 36, INK, 2)
    # --- C: corvette Merkury lost in Benghazi (x 840..1004)
    cv.fill_rect(840, 462, 164, 38, DARK)
    # explosion burst behind the ship
    cv.poly([(922, 280), (936, 318), (962, 306), (946, 336), (972, 344),
             (944, 358), (956, 386), (928, 372), (918, 400), (906, 372),
             (880, 384), (892, 356), (866, 348), (892, 336), (876, 308),
             (904, 320)], RED)
    cv.disc(920, 344, 22, ORANGE)
    cv.disc(920, 344, 11, YELLOW)
    cv.poly([(872, 420), (972, 420), (960, 448), (884, 448)], DARK)
    cv.fill_rect(916, 384, 8, 38, DARK)
    cv.poly([(924, 384), (924, 366), (946, 374)], RED)
    # caption
    draw_text(cv, 528, 516, "KYIV HIT - SHIP AFIRE - CORVETTE LOST",
              INK, 2)
    cv.rect(520, 144, 484, 436, INK, 2)


# ------------------------------------------------------------ grid icons --
def icon_leaf(cv, cx, cy, s):
    """COP31 climate leaf, size ~s."""
    pts = [(cx - s // 2, cy), (cx - s // 4, cy - s // 2),
           (cx + s // 4, cy - s // 2), (cx + s // 2, cy),
           (cx + s // 4, cy + s // 2), (cx - s // 4, cy + s // 2)]
    cv.poly(pts, GREEN)
    cv.line(cx - s // 2, cy + s // 2, cx + s // 2, cy - s // 2, PAPER, 3)
    cv.line(cx, cy + s // 2, cx, cy + s // 2 + 12, GREEN, 3)


def icon_megaphone(cv, cx, cy, s):
    """Lisbon protest megaphone."""
    cv.poly([(cx - s // 2, cy - s // 4), (cx + s // 4, cy - s // 2),
             (cx + s // 4, cy + s // 2), (cx - s // 2, cy + s // 4)], RED)
    cv.fill_rect(cx + s // 4, cy - s // 2, 8, s, RED)
    cv.fill_rect(cx - s // 2 - 4, cy - s // 6, 12, s // 3, INK)


def icon_flag(cv, cx, cy, s):
    """Checkered racing flag."""
    cv.vline(cx - s // 2, cy - s // 2 - 8, s + 16, INK, 4)
    fw, fh = s - 8, s // 2
    fx, fy = cx - s // 2 + 4, cy - fh // 2
    cell = fw // 4
    for r in range(2):
        for c in range(4):
            col = INK if (r + c) % 2 == 0 else PAPER
            cv.fill_rect(fx + c * cell, fy + r * (fh // 2), cell, fh // 2,
                         col)
    cv.rect(fx, fy, fw, fh, INK, 2)


def icon_racket(cv, cx, cy, s):
    """Tennis racket."""
    import math
    r = s // 2 - 6
    cv.ring(cx, cy - 8, r, INK, 4)
    for d in (-r // 2, 0, r // 2):
        half = int(math.sqrt(max(0, r * r - d * d)))
        cv.hline(cx - half, cy - 8 + d, half * 2, INK, 1)
        cv.vline(cx + d, cy - 8 - half, half * 2, INK, 1)
    cv.fill_rect(cx - 5, cy - 8 + r, 10, s // 2, ORANGE)
    cv.disc(cx + r - 4, cy - 8 - r + 6, 6, YELLOW)


# ------------------------------------------------------------ grid cells --
CELLS = [
    ("COP31 ANTALYA STALEMATE ON FOSSILS",
     "NO STRONGER FOSSIL PHASE-OUT", icon_leaf, GREEN, "CLIMATE"),
    ("LISBON MASS PROTEST OVER LIVING COSTS",
     "THOUSANDS MARCH IN LISBON", icon_megaphone, RED, "PROTEST"),
    ("VERSTAPPEN WINS LAS VEGAS GRAND PRIX",
     "RED BULL TAKES VEGAS", icon_flag, ORANGE, "SPORT"),
    ("ALCARAZ CLAIMS FIRST ATP FINALS TITLE",
     "BEATS ZVEREV FOR FIRST TITLE", icon_racket, ORANGE, "SPORT"),
]


def draw_cell(cv, x, y, w, h, headline, caption, icon, color, kicker):
    cv.rect(x, y, w, h, INK, 2)
    icon(cv, x + 62, y + h // 2, 84)
    tx = x + 122
    tw = w - 122 - 14
    draw_text(cv, tx, y + 12, kicker, color, 2)
    lines = wrap_words(headline, 3, tw)
    ly = y + 34
    for ln in lines:
        draw_text(cv, tx, ly, ln, INK, 3)
        ly += 24
    draw_text(cv, tx, ly + 6, caption, INK, 2)


def draw_grid(cv):
    xs = (20, 520)
    ys = (596, 764)
    for i, cell in enumerate(CELLS):
        draw_cell(cv, xs[i % 2], ys[i // 2], 484, 156, *cell)


# ------------------------------------------------------------ in brief ----
def draw_inbrief(cv):
    cv.fill_rect(20, 936, 984, 76, BEIGE)
    cv.rect(20, 936, 984, 76, INK, 2)
    draw_text(cv, 34, 946, "IN BRIEF", RED, 2)
    items = ("INDIA SENSEX SLIDES 1,484 POINTS | NVIDIA GAINS $1 TRILLION, "
             "HUANG RETURNS | GUKESH OPENS WORLD CHESS DEFENCE | OXFAM: "
             "GAZA AIR, SOIL, WATER TOXIC")
    lines = wrap_words(items, 2, 956)
    ly = 968
    for ln in lines[:2]:
        draw_text(cv, 34, ly, ln, INK, 2)
        ly += 16


# ---------------------------------------------------------------- main ----
def main():
    cv = Canvas(W, H, PAPER)
    draw_masthead(cv)
    draw_lead1(cv)
    draw_lead2(cv)
    draw_grid(cv)
    draw_inbrief(cv)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.png")
    with open(path, "wb") as f:
        f.write(png_bytes(cv))
    print("wrote", path)


if __name__ == "__main__":
    main()
