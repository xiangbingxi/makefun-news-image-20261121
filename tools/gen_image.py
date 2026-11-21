#!/usr/bin/env python3
"""Draw the front page for Saturday 21 November 2026 as one 1024x1024 PNG.

Own work: every story was checked against reporting published on
21 November 2026 (see NEWS.md for the source of each line). The drawing
uses PIL primitives only -- no photos, no downloaded art, no network.
Deterministic: no randomness anywhere, fixed geometry and fixed text, so
repeated runs write identical bytes.

Run:  python3 tools/gen_image.py   (writes entry.png next to main.py)
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / "entry.png"

W, H = 1024, 1024
PAPER = (247, 242, 230)
INK = (28, 28, 24)
FAINT = (112, 106, 90)
RED = (176, 32, 22)
BLUE = (30, 76, 120)
SKY = (168, 196, 214)
RULE = (28, 28, 24)
HAIR = (160, 153, 134)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns lines that fit `width` pixels."""
    lines, cur = [], ""
    for w in text.split():
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=None, max_lines=None):
    """Draw wrapped text; returns the y just below the last line."""
    lines = wrap(draw, text, fnt, width)
    if max_lines:
        lines = lines[:max_lines]
    lh = leading if leading is not None else int(fnt.size * 1.28)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def kicker(draw, x, y, text, fill=RED):
    f = font(SANS_B, 15)
    draw.text((x, y), text, font=f, fill=fill)
    return y + 20


def headline(draw, x, y, text, size, width, fill=INK, leading=None):
    f = font(SERIF_B, size)
    lines = wrap(draw, text, f, width)
    lh = leading if leading is not None else int(size * 1.08)
    for ln in lines:
        draw.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


def hrule(draw, x0, x1, y, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def vrule(draw, x, y0, y1, width=1, fill=HAIR):
    draw.line([(x, y0), (x, y1)], fill=fill, width=width)


def star(draw, cx, cy, r, fill=RED):
    """Four-point star marker."""
    pts = [(cx, cy - r), (cx + r * 0.28, cy - r * 0.28), (cx + r, cy),
           (cx + r * 0.28, cy + r * 0.28), (cx, cy + r),
           (cx - r * 0.28, cy + r * 0.28), (cx - r, cy),
           (cx - r * 0.28, cy - r * 0.28)]
    draw.polygon(pts, fill=fill)


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def draw_map(draw, x0, y0, w, h):
    """Schematic map of Poland and its neighbours. Not to scale."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    draw.rectangle([x0, y0, x0 + w, y0 + 42], fill=SKY)
    de = [(x0, y0 + 78), (x0 + 52, y0 + 66), (x0 + 52, y0 + 118),
          (x0 + 88, y0 + 168), (x0 + 58, y0 + 198), (x0, y0 + 208)]
    draw.polygon(de, fill=(214, 210, 196), outline=HAIR)
    pl = [(x0 + 55, y0 + 68), (x0 + 118, y0 + 50), (x0 + 198, y0 + 46),
          (x0 + 263, y0 + 58), (x0 + 298, y0 + 93), (x0 + 293, y0 + 138),
          (x0 + 268, y0 + 183), (x0 + 208, y0 + 198), (x0 + 148, y0 + 193),
          (x0 + 88, y0 + 168), (x0 + 52, y0 + 118)]
    draw.polygon(pl, fill=(250, 246, 236), outline=INK)
    ua = [(x0 + 148, y0 + 203), (x0 + 228, y0 + 196), (x0 + 298, y0 + 188),
          (x0 + 343, y0 + 208), (x0 + 343, y0 + h - 4), (x0 + 178, y0 + h - 4),
          (x0 + 138, y0 + 233)]
    draw.polygon(ua, fill=(226, 222, 206), outline=HAIR)
    by = [(x0 + 298, y0 + 93), (x0 + 343, y0 + 98), (x0 + 343, y0 + 203),
          (x0 + 298, y0 + 188), (x0 + 293, y0 + 138)]
    draw.polygon(by, fill=(214, 210, 196), outline=HAIR)
    sf = font(SANS_B, 13)
    sf2 = font(SANS, 12)
    draw.text((x0 + 10, y0 + 12), "BALTIC SEA", font=sf2, fill=(70, 100, 125))
    draw.text((x0 + 128, y0 + 108), "POLAND", font=sf, fill=INK)
    draw.text((x0 + 208, y0 + 232), "UKRAINE", font=sf, fill=(90, 86, 74))
    draw.text((x0 + 8, y0 + 138), "GERMANY", font=sf2, fill=(90, 86, 74))
    draw.text((x0 + 300, y0 + 128), "BELARUS", font=sf2, fill=(90, 86, 74))
    draw.line([(x0 + w - 4, y0 + 118), (x0 + 300, y0 + 158)], fill=RED, width=3)
    draw.polygon([(x0 + 300, y0 + 158), (x0 + 314, y0 + 152), (x0 + 310, y0 + 166)],
                 fill=RED)
    draw.text((x0 + w - 78, y0 + 92), "Kh-101", font=font(SANS_B, 13), fill=RED)
    for (sx, sy) in [(286, 172), (304, 190), (268, 158)]:
        star(draw, x0 + sx, y0 + sy, 9)
    ex, ey = x0 + 238, y0 + 178
    draw.ellipse([ex - 6, ey - 6, ex + 6, ey + 6], fill=BLUE,
                 outline=(255, 255, 255), width=2)
    draw.text((x0 + 176, y0 + 192), "Rzeszow drills", font=font(SANS_B, 12),
              fill=BLUE)
    draw.text((x0 + 8, y0 + h - 20), "Map: schematic, not to scale",
              font=font(SANS_I, 11), fill=FAINT)


def draw_spiral(draw, x0, y0, size):
    """Ulam spiral of the numbers 1..225; primes in red."""
    n = 15
    cell = size // n
    pos = {}
    x, y = 0, 0
    dx, dy = 1, 0
    steps = 1
    num = 1
    pos[(0, 0)] = 1
    while num < n * n:
        for _ in range(2):
            for _ in range(steps):
                if num >= n * n:
                    break
                x += dx
                y += dy
                num += 1
                pos[(x, y)] = num
            dx, dy = -dy, dx
        steps += 1
    cx, cy = x0 + size // 2, y0 + size // 2
    for (gx, gy), v in pos.items():
        px = cx + gx * cell
        py = cy + gy * cell
        r = 3 if is_prime(v) else 2
        fill = RED if is_prime(v) else (196, 190, 172)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=fill)


def draw_chart(draw, x0, y0, w, h):
    """Falling market line, fixed points, deterministic."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(255, 255, 255),
                   outline=HAIR)
    for i in range(1, 4):
        gy = y0 + h * i // 4
        draw.line([(x0, gy), (x0 + w, gy)], fill=(228, 224, 212), width=1)
    pts = [(0, 0.12), (0.14, 0.18), (0.26, 0.10), (0.38, 0.30), (0.50, 0.26),
           (0.62, 0.48), (0.74, 0.44), (0.86, 0.72), (1.0, 0.88)]
    xy = [(x0 + int(px * w), y0 + int(py * h)) for px, py in pts]
    draw.line(xy, fill=RED, width=3)
    for (px, py) in xy[1:-1]:
        draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED)
    draw.text((x0 + w - 78, y0 + 4), "S&P 500", font=font(SANS_B, 12), fill=INK)
    draw.text((x0 + w - 62, y0 + h - 22), "-3.7%", font=font(SANS_B, 16),
              fill=RED)


def draw_globe(draw, cx, cy, r):
    """Wireframe globe with a small clock: talks running over time."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SKY, outline=BLUE,
                 width=2)
    for k in (-2, -1, 0, 1, 2):
        rx = abs(r * math.cos(k * math.pi / 6))
        draw.ellipse([cx - rx, cy - r, cx + rx, cy + r], outline=BLUE, width=1)
    for k in (-1, 0, 1):
        ry = r * math.sin(k * math.pi / 6)
        y = cy + ry
        half = math.sqrt(max(r * r - ry * ry, 0))
        draw.arc([cx - half, y - 6, cx + half, y + 6], 0, 360, fill=BLUE,
                 width=1)
    ccx, ccy, cr = cx + r - 6, cy + r - 6, 14
    draw.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=(255, 255, 255),
                 outline=RED, width=2)
    draw.line([(ccx, ccy), (ccx, ccy - 9)], fill=RED, width=2)
    draw.line([(ccx, ccy), (ccx + 7, ccy + 3)], fill=RED, width=2)


def draw_scales(draw, cx, cy):
    """Simple scales of justice."""
    draw.line([(cx, cy - 26), (cx, cy + 26)], fill=INK, width=3)
    draw.line([(cx - 26, cy - 20), (cx + 26, cy - 20)], fill=INK, width=3)
    for sx in (-26, 26):
        draw.line([(cx + sx, cy - 20), (cx + sx, cy - 4)], fill=INK, width=2)
        draw.polygon([(cx + sx - 10, cy - 4), (cx + sx + 10, cy - 4),
                      (cx + sx, cy + 8)], outline=INK, fill=(220, 214, 198))
    draw.line([(cx - 14, cy + 26), (cx + 14, cy + 26)], fill=INK, width=3)


def draw_shield(draw, cx, cy):
    """Shield with an exclamation mark."""
    pts = [(cx - 22, cy - 26), (cx + 22, cy - 26), (cx + 22, cy + 2),
           (cx, cy + 28), (cx - 22, cy + 2)]
    draw.polygon(pts, outline=RED, fill=(255, 255, 255), width=3)
    draw.text((cx - 4, cy - 22), "!", font=font(SERIF_B, 34), fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, W - 11, H - 11], outline=RULE, width=2)
    d.rectangle([16, 16, W - 17, H - 17], outline=HAIR, width=1)

    # ---- masthead (24-136) ----
    d.text((512, 26), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
           fill=INK, anchor="mt")
    hrule(d, 24, 1000, 100, width=2)
    d.text((24, 110), "SATURDAY, 21 NOVEMBER 2026", font=font(SANS_B, 20),
           fill=RED)
    d.text((1000, 110), "ONE DAY'S NEWS, IN ONE PICTURE",
           font=font(SANS_B, 16), fill=FAINT, anchor="rt")
    hrule(d, 24, 1000, 136, width=3)

    # ---- lead: Poland (148-452) ----
    x, y = 24, 148
    y = kicker(d, x, y, "POLAND  ·  NATO ON ALERT")
    y = headline(d, x, y, "Russian missiles land in Poland", 40, 600)
    y = para(d, x, y + 2,
             "Tusk calls it a deliberate provocation as NATO jets "
             "scramble. A Kh-101 cruise missile came down 50 km from "
             "Ukraine's border, near allied war games in the south-east.",
             font(SERIF, 19), 600, leading=24, max_lines=4)
    y = para(d, x, y + 4,
             "Two missiles and a suspected drone crashed in fields "
             "during Russia's overnight barrage on Ukraine, which killed "
             "8 and injured about 28. NATO chief Mark Rutte called the "
             "incursion a \"grave violation\" of Polish airspace.",
             font(SANS, 15), 600, leading=19, max_lines=4)
    draw_map(d, 648, 148, 352, 268)
    d.text((648, 420), "The Kh-101 fell near Nowy Lipowiec; the other objects",
           font=font(SANS_I, 12), fill=FAINT)
    d.text((648, 436), "near Rudnik nad Sanem and Molodycz. No one was hurt.",
           font=font(SANS_I, 12), fill=FAINT)
    hrule(d, 24, 1000, 452, width=2)

    # ---- row 2: three columns (464-700) ----
    col_w = 312
    xs = [24, 356, 688]
    # Riemann
    y = 464
    y = kicker(d, xs[0], y, "SCIENCE  ·  MATHS")
    y = headline(d, xs[0], y, "Claude 'proves' the Riemann hypothesis", 23,
                 col_w, leading=26)
    draw_spiral(d, xs[0], y + 2, 72)
    d.text((xs[0] + 84, y + 4), "The primes,\nspiralled.\nFirst posed\nin 1859.",
           font=font(SANS, 13), fill=FAINT)
    para(d, xs[0], y + 80,
         "Anthropic mathematician Levent Alpoge says he and Claude "
         "proved the most famous open problem in mathematics. "
         "Independent experts have compiled the Lean code and call it "
         "\"almost certainly true\".",
         font(SANS, 13), col_w, leading=17, max_lines=4)
    # Markets
    y = 464
    y = kicker(d, xs[1], y, "MARKETS  ·  WALL STREET")
    y = headline(d, xs[1], y, "Tech sell-off deepens", 23, col_w, leading=26)
    draw_chart(d, xs[1], y + 2, col_w, 72)
    para(d, xs[1], y + 80,
         "The S&P 500 fell 3.7% and the Nasdaq turned negative for the "
         "year as the AI sell-off deepened. Anthropic shares slid days "
         "after a record stock market debut.",
         font(SANS, 13), col_w, leading=17, max_lines=4)
    # COP31
    y = 464
    y = kicker(d, xs[2], y, "CLIMATE  ·  COP31, ANTALYA")
    y = headline(d, xs[2], y, "Climate talks end in deadlock", 23, col_w,
                 leading=26)
    draw_globe(d, xs[2] + 40, y + 40, 34)
    d.text((xs[2] + 92, y + 4), "No fossil-fuel\nphase-out in\nthe draft deal.\nTalks run over\ninto overtime.",
           font=font(SANS, 13), fill=FAINT)
    para(d, xs[2], y + 80,
         "The UN climate summit reached its final scheduled day with no "
         "agreement in sight. Ukraine blocked a Russian climate report "
         "that used data from occupied Ukrainian territory.",
         font(SANS, 13), col_w, leading=17, max_lines=4)
    vrule(d, 340, 464, 692)
    vrule(d, 672, 464, 692)
    hrule(d, 24, 1000, 700, width=2)

    # ---- row 3: two half-width stories (712-806) ----
    y = 712
    y = kicker(d, 24, y, "DENMARK  ·  ESPIONAGE")
    y = headline(d, 24, y, "Russia accused of assassination plot", 21, 440,
                 leading=24)
    draw_shield(d, 62, y + 28)
    para(d, 104, y, "Denmark says Russian intelligence plotted to kill a "
                   "US-Ukrainian rapper on Danish soil. Copenhagen expelled "
                   "a Russian diplomat.",
         font(SANS, 13), 380, leading=17, max_lines=3)
    y = 712
    y = kicker(d, 540, y, "USA  ·  COURTS")
    y = headline(d, 540, y, "19 1/2 years for Sikh murder plot", 21, 440,
                 leading=24)
    draw_scales(d, 578, y + 28)
    para(d, 620, y, "A US court sentenced Indian national Nikhil Gupta to "
                   "235 months for a murder-for-hire plot against a Sikh "
                   "separatist leader in New York.",
         font(SANS, 13), 360, leading=17, max_lines=3)
    vrule(d, 512, 712, 798)
    hrule(d, 24, 1000, 806, width=2)

    # ---- numbers strip (816-860) ----
    d.rectangle([24, 816, 1000, 860], fill=INK)
    nums = [("8", "killed in the Ukraine barrage"),
            ("50 km", "from Ukraine's border"),
            ("-3.7%", "the S&P 500 in a day"),
            ("1859", "Riemann posed his problem")]
    nx = 40
    for big, small in nums:
        bf = font(SERIF_B, 24)
        sf = font(SANS, 12)
        d.text((nx, 824), big, font=bf, fill=(247, 242, 230))
        wbig = d.textlength(big, font=bf)
        d.text((nx + wbig + 10, 830), small, font=sf, fill=(200, 194, 178))
        wsmall = d.textlength(small, font=sf)
        nx += wbig + wsmall + 40
        if nx < 960:
            d.line([(nx - 20, 824), (nx - 20, 852)], fill=(90, 86, 74), width=1)

    # ---- the day in brief (872-982) ----
    d.text((24, 872), "THE DAY IN BRIEF", font=font(SANS_B, 15), fill=RED)
    hrule(d, 24, 1000, 894, width=1, fill=HAIR)
    brief = [
        ("THE HAGUE", "ICJ: Myanmar committed genocide vs Rohingya."),
        ("USA", "Trump floats his chief of staff for president in 2028."),
        ("BRAZIL", "Bolsonaro hospitalised with abdominal pain."),
        ("EUROPE", "Cost-of-living protests sweep European cities."),
        ("BANGLADESH", "Fresh arson attacks amid political unrest."),
        ("USA", "More UFO footage declassified, filmed in Middle East."),
        ("NEW YORK", "Mamdani plans to close Rikers Island by 2032."),
        ("FRANCE", "Police sentenced over beating of Michel Zecler."),
        ("CUBA", "American woman freed after 10 years in prison."),
        ("MALAYSIA", "10,000 Rohingya to be resettled in Turkiye."),
    ]
    for i, (tag, txt) in enumerate(brief):
        bx = 24 if i < 5 else 512
        byy = 902 + (i % 5) * 17
        d.text((bx, byy), tag + " — ", font=font(SANS_B, 13), fill=INK)
        tw = d.textlength(tag + " — ", font=font(SANS_B, 13))
        d.text((bx + tw, byy), txt, font=font(SANS, 13), fill=INK)

    # ---- footer ----
    hrule(d, 24, 1000, 990, width=1, fill=HAIR)
    d.text((24, 996), "Drawn from reporting published 21 November 2026.",
           font=font(SANS_I, 12), fill=FAINT)
    d.text((1000, 996), "Sources: Reuters, AP, AFP, BBC, The Hindu, SCMP.",
           font=font(SANS_I, 12), fill=FAINT, anchor="rt")

    img.save(OUT, format="PNG")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
