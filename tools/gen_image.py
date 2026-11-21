#!/usr/bin/env python3
"""Draw the front page for Saturday 21 November 2026, v2.

A denser front page: 36 stories across 7 regions, in the style of a
vertical newspaper front page. Every story was checked against reporting
published on 21 November 2026 (see NEWS.md for the source of each line).
All drawing uses PIL primitives only -- no photos, no downloaded art, no
network. Deterministic: fixed geometry, fixed text, no randomness, so
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
YELLOW = (240, 200, 40)
SKY = (168, 196, 214)
RULE = (28, 28, 24)
HAIR = (160, 153, 134)
TEAL = (40, 120, 90)
ORANGE = (220, 120, 40)
PURPLE = (120, 80, 140)
SLATE = (60, 60, 70)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def split_lines(draw, text, font, width):
    """Greedy word wrap; returns the lines that fit `width` pixels."""
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def block(draw, x, y, text, font, width, fill=INK, lead=None, limit=None):
    """Draw wrapped text; returns the y just below the last line."""
    lines = split_lines(draw, text, font, width)
    if limit:
        lines = lines[:limit]
    lh = lead if lead is not None else int(font.size * 1.28)
    for ln in lines:
        draw.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y


def tagline(draw, x, y, text, size=12, fill=RED):
    f = fnt(SANS_B, size)
    draw.text((x, y), text, font=f, fill=fill)
    return y + size + 5


def title_lines(draw, x, y, text, size, width, fill=INK, lead=None):
    f = fnt(SERIF_B, size)
    lines = split_lines(draw, text, f, width)
    lh = lead if lead is not None else int(size * 1.08)
    for ln in lines:
        draw.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


def rule(draw, x0, x1, y, w=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=w)


def vline(draw, x, y0, y1, w=1, fill=HAIR):
    draw.line([(x, y0), (x, y1)], fill=fill, width=w)


def four_star(draw, cx, cy, r, fill=RED):
    pts = [(cx, cy - r), (cx + r * 0.28, cy - r * 0.28), (cx + r, cy),
           (cx + r * 0.28, cy + r * 0.28), (cx, cy + r),
           (cx - r * 0.28, cy + r * 0.28), (cx - r, cy),
           (cx - r * 0.28, cy - r * 0.28)]
    draw.polygon(pts, fill=fill)


def burst(draw, cx, cy, r_out, r_in, n, fill, rot=0.0):
    """Jagged starburst with n spikes."""
    pts = []
    for i in range(n * 2):
        ang = rot + i * math.pi / n
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
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


# ---------------------------------------------------------------- big art

def art_riyadh(draw, x0, y0, w, h):
    """Night over Riyadh: skyline, two interceptor bursts, missile trail."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(16, 24, 48))
    # stars
    for (sx, sy, sr) in [(18, 12, 2), (52, 26, 1), (96, 8, 2), (150, 20, 1),
                         (196, 12, 2), (240, 28, 1), (282, 10, 2),
                         (30, 44, 1), (120, 40, 1), (210, 44, 2)]:
        draw.ellipse([x0 + sx - sr, y0 + sy - sr, x0 + sx + sr, y0 + sy + sr],
                     fill=(255, 255, 255))
    # skyline silhouettes
    base = y0 + h
    for (bx, bw, bh) in [(0, 34, 34), (38, 26, 52), (68, 30, 40),
                         (102, 22, 62), (128, 36, 46), (168, 26, 58),
                         (198, 30, 38), (232, 28, 54), (264, 24, 42),
                         (292, 20, 30)]:
        draw.rectangle([x0 + bx, base - bh, x0 + bx + bw, base],
                       fill=(8, 12, 26))
        for wy in range(base - bh + 8, base - 4, 12):
            for wx in range(bx + 5, bx + bw - 3, 9):
                if (wx * 7 + wy * 3) % 5 < 2:
                    draw.rectangle([x0 + wx, wy, x0 + wx + 3, wy + 4],
                                   fill=(240, 200, 40))
    # Kingdom Centre-like tower with arch top
    tx = x0 + w - 52
    draw.rectangle([tx, base - 78, tx + 30, base], fill=(8, 12, 26))
    draw.polygon([(tx, base - 78), (tx + 30, base - 78), (tx + 15, base - 66)],
                 fill=(16, 24, 48))
    draw.rectangle([tx + 4, base - 74, tx + 26, base - 70], fill=(240, 200, 40))
    # missile trail rising from the lower left
    draw.line([(x0 + 30, base - 6), (x0 + 128, y0 + 34)], fill=(255, 180, 60),
              width=3)
    draw.line([(x0 + 30, base - 6), (x0 + 128, y0 + 34)], fill=(255, 240, 200),
              width=1)
    # interceptor burst where the missile is hit
    burst(draw, x0 + 132, y0 + 30, 16, 7, 8, YELLOW)
    burst(draw, x0 + 132, y0 + 30, 9, 4, 8, (255, 255, 255))
    draw.ellipse([x0 + 128, y0 + 26, x0 + 136, y0 + 34], fill=(255, 255, 255))
    # second burst, higher right
    burst(draw, x0 + 232, y0 + 52, 12, 5, 8, YELLOW)
    burst(draw, x0 + 232, y0 + 52, 6, 3, 8, (255, 255, 255))
    # ground glow
    draw.rectangle([x0, base - 3, x0 + w, base], fill=(240, 200, 40))


def art_poland(draw, x0, y0, w, h):
    """Night field in south-east Poland: explosion bloom over the horizon."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(24, 28, 44))
    for (sx, sy, sr) in [(14, 10, 2), (60, 22, 1), (110, 8, 2), (170, 18, 1),
                         (230, 10, 2), (280, 24, 1), (40, 32, 1), (150, 30, 1)]:
        draw.ellipse([x0 + sx - sr, y0 + sy - sr, x0 + sx + sr, y0 + sy + sr],
                     fill=(255, 255, 255))
    # distant treeline
    base = y0 + h
    draw.rectangle([x0, base - 22, x0 + w, base], fill=(18, 26, 18))
    for (tx, th) in [(6, 12), (26, 18), (52, 10), (80, 16), (250, 14),
                     (276, 18), (296, 11)]:
        draw.polygon([(x0 + tx, base - 22), (x0 + tx + 5, base - 22 - th),
                      (x0 + tx + 10, base - 22)], fill=(12, 18, 12))
    # explosion bloom
    ex, ey = x0 + int(w * 0.62), y0 + 52
    burst(draw, ex, ey, 34, 16, 12, (220, 90, 30))
    burst(draw, ex, ey, 24, 11, 12, (240, 160, 40))
    burst(draw, ex, ey, 13, 6, 12, (255, 230, 150))
    draw.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill=(255, 255, 255))
    # smoke puffs
    for (sx, sy, sr) in [(ex - 34, ey - 18, 9), (ex + 30, ey - 26, 11),
                         (ex + 42, ey - 8, 8), (ex - 40, ey + 2, 7)]:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(90, 90, 96))
    # red impact star on the ground line
    four_star(draw, x0 + 52, base - 26, 8)
    draw.text((x0 + 64, base - 32), "IMPACT", font=fnt(SANS_B, 10), fill=RED)
    # small jet silhouette crossing the sky
    jx, jy = x0 + 30, y0 + 26
    draw.polygon([(jx, jy), (jx + 26, jy - 4), (jx + 30, jy), (jx + 26, jy + 4)],
                 fill=(200, 200, 210))
    draw.polygon([(jx + 8, jy), (jx + 14, jy - 8), (jx + 18, jy)],
                 fill=(200, 200, 210))


def art_mercury(draw, x0, y0, w, h):
    """Mercury fills the frame; the two-orbiters stack sails past the Sun."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(10, 10, 18))
    for (sx, sy, sr) in [(12, 14, 2), (44, 30, 1), (90, 10, 2), (140, 26, 1),
                         (200, 12, 2), (260, 28, 1), (296, 16, 2),
                         (70, 44, 1), (180, 42, 1), (240, 48, 1)]:
        draw.ellipse([x0 + sx - sr, y0 + sy - sr, x0 + sx + sr, y0 + sy + sr],
                     fill=(255, 255, 255))
    # the Sun, low left, with rays
    sx, sy = x0 + 26, y0 + h - 22
    for k in range(12):
        ang = k * math.pi / 6
        draw.line([(sx + 16 * math.cos(ang), sy + 16 * math.sin(ang)),
                   (sx + 24 * math.cos(ang), sy + 24 * math.sin(ang))],
                  fill=YELLOW, width=2)
    draw.ellipse([sx - 14, sy - 14, sx + 14, sy + 14], fill=YELLOW,
                 outline=(255, 240, 160), width=2)
    # Mercury: big cratered disc, right of centre
    cx, cy, r = x0 + int(w * 0.66), y0 + int(h * 0.52), 40
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(168, 160, 148),
                 outline=(120, 112, 100), width=2)
    for (kx, ky, kr) in [(-16, -12, 9), (10, -18, 7), (18, 6, 10), (-6, 12, 8),
                         (2, -4, 5), (-22, 8, 6), (14, 20, 5)]:
        draw.ellipse([cx + kx - kr, cy + ky - kr, cx + kx + kr, cy + ky + kr],
                     outline=(120, 112, 100), width=1, fill=(150, 142, 130))
    draw.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(220, 214, 200),
             width=3)
    # the spacecraft stack: gold bus, blue panels, dish
    bx, by = x0 + 52, y0 + 26
    draw.rectangle([bx - 34, by - 5, bx - 8, by + 5], fill=BLUE,
                   outline=(255, 255, 255), width=1)
    draw.rectangle([bx + 8, by - 5, bx + 34, by + 5], fill=BLUE,
                   outline=(255, 255, 255), width=1)
    draw.rectangle([bx - 8, by - 7, bx + 8, by + 7], fill=(220, 180, 60),
                   outline=(120, 90, 20), width=1)
    draw.line([(bx - 8, by), (bx - 34, by)], fill=(255, 255, 255), width=1)
    draw.line([(bx + 8, by), (bx + 34, by)], fill=(255, 255, 255), width=1)
    draw.arc([bx + 2, by + 7, bx + 18, by + 19], 0, 180, fill=(255, 255, 255),
             width=2)
    draw.text((x0 + 8, y0 + 4), "8 YEARS OUT  ·  2 ORBITERS",
              font=fnt(SANS_B, 10), fill=(255, 255, 255))


# ---------------------------------------------------------------- small art

def icon_globe_clock(draw, x0, y0, w, h):
    """Earth with a clock running over: climate talks in overtime."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    cx, cy, r = x0 + 22, y0 + h // 2, 16
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SKY, outline=BLUE,
                 width=2)
    for k in (-2, -1, 0, 1, 2):
        rx = abs(r * math.cos(k * math.pi / 6))
        draw.ellipse([cx - rx, cy - r, cx + rx, cy + r], outline=BLUE, width=1)
    for k in (-1, 0, 1):
        ry = r * math.sin(k * math.pi / 6)
        yy = cy + ry
        half = math.sqrt(max(r * r - ry * ry, 0))
        draw.arc([cx - half, yy - 5, cx + half, yy + 5], 0, 360, fill=BLUE,
                 width=1)
    draw.ellipse([cx - 6, cy - 4, cx + 8, cy + 10], fill=(90, 160, 90))
    ccx, ccy, cr = x0 + w - 16, y0 + h - 14, 11
    draw.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=(255, 255, 255),
                 outline=RED, width=2)
    draw.line([(ccx, ccy), (ccx, ccy - 7)], fill=RED, width=2)
    draw.line([(ccx, ccy), (ccx + 5, ccy + 2)], fill=RED, width=2)
    # thermometer at right
    tx = x0 + w - 8
    draw.rectangle([tx - 3, y0 + 4, tx + 3, y0 + h - 12], fill=(255, 255, 255),
                   outline=RED, width=1)
    draw.ellipse([tx - 6, y0 + h - 16, tx + 6, y0 + h - 4], fill=RED)
    draw.rectangle([tx - 1, y0 + 8, tx + 1, y0 + h - 12], fill=RED)


def icon_spiral(draw, x0, y0, w, h):
    """Ulam spiral, primes in red, 13x13."""
    n = 13
    cell = min(w, h) // n
    pos, x, y = {}, 0, 0
    dx, dy = 1, 0
    steps, num = 1, 1
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
    cx, cy = x0 + w // 2, y0 + h // 2
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(255, 255, 255),
                   outline=HAIR)
    for (gx, gy), v in pos.items():
        px, py = cx + gx * cell, cy + gy * cell
        r = 3 if is_prime(v) else 2
        fill = RED if is_prime(v) else (196, 190, 172)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=fill)


def icon_chart(draw, x0, y0, w, h):
    """Falling market line on a white card."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(255, 255, 255),
                   outline=HAIR)
    for i in range(1, 4):
        gy = y0 + h * i // 4
        draw.line([(x0, gy), (x0 + w, gy)], fill=(228, 224, 212), width=1)
    pts = [(0, 0.10), (0.14, 0.16), (0.26, 0.08), (0.38, 0.28),
           (0.50, 0.24), (0.62, 0.46), (0.74, 0.42), (0.86, 0.70),
           (1.0, 0.86)]
    xy = [(x0 + int(px * w), y0 + int(py * h)) for px, py in pts]
    draw.line(xy, fill=RED, width=2)
    for (px, py) in xy[1:-1]:
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)
    draw.text((x0 + 4, y0 + 2), "S&P", font=fnt(SANS_B, 10), fill=INK)
    draw.text((x0 + w - 34, y0 + h - 14), "-3.7%", font=fnt(SANS_B, 11),
              fill=RED)


def icon_target(draw, x0, y0, w, h):
    """Concentric target with a dagger across it."""
    cx, cy = x0 + w // 2, y0 + h // 2
    for r, fill in [(17, (255, 255, 255)), (13, RED), (9, (255, 255, 255)),
                    (5, RED)]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill,
                     outline=INK, width=1)
    draw.line([(cx - 20, cy + 18), (cx + 20, cy - 18)], fill=INK, width=3)
    draw.polygon([(cx + 14, cy - 22), (cx + 22, cy - 14), (cx + 16, cy - 10),
                  (cx + 8, cy - 18)], fill=INK)


def icon_scales(draw, x0, y0, w, h):
    """Scales of justice on a pale card."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    cx, cy = x0 + w // 2, y0 + h // 2 + 2
    draw.line([(cx, cy - 14), (cx, cy + 12)], fill=INK, width=2)
    draw.line([(cx - 14, cy - 10), (cx + 14, cy - 10)], fill=INK, width=2)
    for sx in (-14, 14):
        draw.line([(cx + sx, cy - 10), (cx + sx, cy - 2)], fill=INK, width=1)
        draw.polygon([(cx + sx - 6, cy - 2), (cx + sx + 6, cy - 2),
                      (cx + sx, cy + 5)], outline=INK, fill=(220, 214, 198))
    draw.line([(cx - 8, cy + 12), (cx + 8, cy + 12)], fill=INK, width=2)
    draw.ellipse([cx - 2, cy - 18, cx + 2, cy - 14], fill=INK)


def icon_court(draw, x0, y0, w, h):
    """Courthouse: pediment, columns, steps."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    draw.polygon([(x0 + 6, y0 + 12), (x0 + w // 2, y0 + 2),
                  (x0 + w - 6, y0 + 12)], fill=BLUE)
    draw.rectangle([x0 + 6, y0 + 12, x0 + w - 6, y0 + 16], fill=BLUE)
    for i in range(4):
        cx = x0 + 12 + i * ((w - 24) // 3)
        draw.rectangle([cx - 2, y0 + 16, cx + 2, y0 + h - 10], fill=INK)
    draw.rectangle([x0 + 4, y0 + h - 10, x0 + w - 4, y0 + h - 6], fill=INK)
    draw.rectangle([x0 + 2, y0 + h - 6, x0 + w - 2, y0 + h - 2], fill=INK)


def icon_podium(draw, x0, y0, w, h):
    """Campaign podium with microphone and bunting."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    for i, c in enumerate([RED, BLUE, YELLOW, RED, BLUE]):
        bx = x0 + 2 + i * ((w - 4) // 5)
        draw.polygon([(bx, y0 + 2), (bx + (w - 4) // 5, y0 + 2),
                      (bx + (w - 4) // 10, y0 + 10)], fill=c)
    cx = x0 + w // 2
    draw.rectangle([cx - 16, y0 + 16, cx + 16, y0 + h - 2], fill=(90, 60, 40))
    draw.rectangle([cx - 20, y0 + 14, cx + 20, y0 + 18], fill=(60, 40, 26))
    draw.line([(cx + 10, y0 + 14), (cx + 16, y0 + 6)], fill=INK, width=2)
    draw.ellipse([cx + 14, y0 + 2, cx + 20, y0 + 8], fill=INK)
    draw.text((cx - 8, y0 + 22), "2028", font=fnt(SANS_B, 10),
              fill=(255, 255, 255))


def icon_bridge(draw, x0, y0, w, h):
    """Suspension bridge over water, one span broken."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    wy = y0 + h - 10
    draw.rectangle([x0, wy, x0 + w, y0 + h], fill=SKY)
    for wx in range(x0, x0 + w, 8):
        draw.line([(wx, wy), (wx + 4, wy + 3)], fill=BLUE, width=1)
    # towers
    for tx in (x0 + 14, x0 + w - 18):
        draw.rectangle([tx, y0 + 8, tx + 4, wy], fill=INK)
    # deck, left span intact, right span dropped
    draw.line([(x0, y0 + 18), (x0 + w // 2 - 4, y0 + 18)], fill=INK, width=3)
    draw.line([(x0 + w // 2 + 4, y0 + 26), (x0 + w - 4, y0 + 30)], fill=RED,
              width=3)
    # cables
    draw.line([(x0 + 16, y0 + 8), (x0 + w // 2, y0 + 18)], fill=INK, width=1)
    draw.line([(x0 + w - 16, y0 + 8), (x0 + w // 2, y0 + 18)], fill=INK, width=1)
    # blast puff at the break
    burst(draw, x0 + w // 2, y0 + 20, 8, 4, 8, (220, 90, 30))


def icon_eu_coin(draw, x0, y0, w, h):
    """EU flag disc beside a gold coin."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    cx, cy, r = x0 + 18, y0 + h // 2, 15
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE)
    for k in range(12):
        ang = -math.pi / 2 + k * math.pi / 6
        sx, sy = cx + 10 * math.cos(ang), cy + 10 * math.sin(ang)
        four_star(draw, sx, sy, 2, fill=YELLOW)
    ccx, ccy, cr = x0 + w - 16, y0 + h // 2, 12
    draw.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=YELLOW,
                 outline=(160, 120, 20), width=2)
    draw.text((ccx - 4, ccy - 8), "€", font=fnt(SANS_B, 14), fill=INK)


def icon_harbour(draw, x0, y0, w, h):
    """Harbour: crane, container ship, water."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(233, 238, 240))
    wy = y0 + h - 10
    draw.rectangle([x0, wy, x0 + w, y0 + h], fill=SKY)
    # crane
    draw.rectangle([x0 + 6, y0 + 6, x0 + 10, wy], fill=INK)
    draw.line([(x0 + 8, y0 + 6), (x0 + w - 8, y0 + 14)], fill=INK, width=2)
    draw.line([(x0 + w - 12, y0 + 14), (x0 + w - 12, y0 + 22)], fill=INK,
              width=1)
    draw.rectangle([x0 + w - 16, y0 + 22, x0 + w - 8, y0 + 28], fill=RED)
    # container ship
    draw.polygon([(x0 + 14, wy - 4), (x0 + w - 6, wy - 4), (x0 + w - 12, wy),
                  (x0 + 20, wy)], fill=(60, 60, 70))
    for i, c in enumerate([RED, BLUE, YELLOW]):
        bx = x0 + 18 + i * 12
        draw.rectangle([bx, wy - 12, bx + 10, wy - 4], fill=c,
                       outline=INK, width=1)
    draw.rectangle([x0 + w - 22, wy - 18, x0 + w - 14, wy - 4], fill=(255, 255, 255),
                   outline=INK, width=1)


def draw_world(draw, x0, y0, w, h, pins):
    """Schematic world map, pale ocean, grey continents, red numbered pins."""
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(222, 232, 238))
    # continents, very rough, not to scale
    na = [(x0 + 8, y0 + 34), (x0 + 44, y0 + 18), (x0 + 92, y0 + 22),
          (x0 + 118, y0 + 44), (x0 + 104, y0 + 66), (x0 + 78, y0 + 62),
          (x0 + 66, y0 + 84), (x0 + 40, y0 + 78), (x0 + 14, y0 + 58)]
    draw.polygon(na, fill=(214, 210, 196), outline=HAIR)
    sa = [(x0 + 84, y0 + 96), (x0 + 116, y0 + 92), (x0 + 136, y0 + 116),
          (x0 + 128, y0 + 156), (x0 + 108, y0 + 178), (x0 + 92, y0 + 150),
          (x0 + 82, y0 + 122)]
    draw.polygon(sa, fill=(214, 210, 196), outline=HAIR)
    eu = [(x0 + 178, y0 + 26), (x0 + 206, y0 + 18), (x0 + 228, y0 + 28),
          (x0 + 224, y0 + 46), (x0 + 200, y0 + 52), (x0 + 182, y0 + 44)]
    draw.polygon(eu, fill=(214, 210, 196), outline=HAIR)
    af = [(x0 + 182, y0 + 62), (x0 + 214, y0 + 56), (x0 + 242, y0 + 68),
          (x0 + 250, y0 + 96), (x0 + 238, y0 + 128), (x0 + 218, y0 + 148),
          (x0 + 200, y0 + 124), (x0 + 186, y0 + 94)]
    draw.polygon(af, fill=(214, 210, 196), outline=HAIR)
    as_ = [(x0 + 232, y0 + 22), (x0 + 280, y0 + 12), (x0 + 330, y0 + 18),
           (x0 + 366, y0 + 36), (x0 + 360, y0 + 66), (x0 + 330, y0 + 82),
           (x0 + 300, y0 + 74), (x0 + 284, y0 + 96), (x0 + 262, y0 + 78),
           (x0 + 240, y0 + 58), (x0 + 228, y0 + 40)]
    draw.polygon(as_, fill=(214, 210, 196), outline=HAIR)
    au = [(x0 + 308, y0 + 138), (x0 + 344, y0 + 132), (x0 + 362, y0 + 148),
          (x0 + 344, y0 + 164), (x0 + 314, y0 + 160)]
    draw.polygon(au, fill=(214, 210, 196), outline=HAIR)
    lab = fnt(SANS_I, 10)
    draw.text((x0 + 10, y0 + 108), "PACIFIC", font=lab, fill=(90, 110, 130))
    draw.text((x0 + 130, y0 + 96), "ATLANTIC", font=lab, fill=(90, 110, 130))
    draw.text((x0 + 268, y0 + 128), "INDIAN OCEAN", font=lab,
              fill=(90, 110, 130))
    # numbered pins: (story_no, fx, fy) as fractions of the map box
    for num, fx, fy in pins:
        px, py = x0 + int(fx * w), y0 + int(fy * h)
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                     outline=(255, 255, 255), width=2)
        tf = fnt(SANS_B, 10)
        tw = draw.textlength(str(num), font=tf)
        draw.text((px - tw / 2, py - 6), str(num), font=tf,
                  fill=(255, 255, 255))
    draw.text((x0 + 4, y0 + h - 14), "Map: schematic, not to scale",
              font=fnt(SANS_I, 10), fill=FAINT)


# ---------------------------------------------------------------- the page

BIG3 = [
    ("RIYADH · MISSILES", "Three missiles down over Riyadh",
     "Saudi defences intercepted three Houthi missiles aimed at the "
     "capital early on Saturday — the second attack on Riyadh in days. "
     "Eight emergency alerts in 24 hours.", art_riyadh),
    ("POLAND · NATO ON ALERT", "Russian missiles land in Poland",
     "Tusk calls it a deliberate provocation as NATO jets scramble. A "
     "Kh-101 came down 50 km from Ukraine's border in a barrage that "
     "killed 8 and injured about 28.", art_poland),
    ("MERCURY · SPACE", "BepiColombo reaches Mercury",
     "After eight years in space, the ESA/JAXA probe is captured by "
     "Mercury's gravity today. Its two orbiters separate in December; "
     "science begins in April 2027.", art_mercury),
]

NUMBERS = [
    ("3", "missiles over Riyadh"),
    ("8", "killed in Ukraine barrage"),
    ("1.6M", "Russian troops lost"),
    ("-3.7%", "S&P 500 in a day"),
    ("€7.9B", "EU aid to Ukraine"),
    ("10,000", "Rohingya resettled"),
]

SMALL = [
    ("COP31 · ANTALYA", "Climate talks end in deadlock",
     "No fossil-fuel phase-out in the draft as the Antalya summit runs over.",
     icon_globe_clock),
    ("SCIENCE · MATHS", "Claude 'proves' Riemann",
     "Anthropic says its AI proved the 1859 problem; experts are verifying it.",
     icon_spiral),
    ("MARKETS · WALL STREET", "Tech sell-off deepens",
     "The S&P 500 fell 3.7% and the Nasdaq turned negative for the year.",
     icon_chart),
    ("DENMARK · ESPIONAGE", "Russia accused of plot to kill",
     "Denmark says Russia plotted to kill a rapper; a diplomat was expelled.",
     icon_target),
    ("USA · COURTS", "19½ years for Sikh murder plot",
     "Nikhil Gupta gets 235 months for a murder-for-hire plot in New York.",
     icon_scales),
    ("THE HAGUE · JUSTICE", "ICJ: Myanmar committed genocide",
     "The court finds genocide against the Rohingya; Myanmar calls it unfair.",
     icon_court),
    ("USA · 2028", "Trump floats chief of staff",
     "Asked 'Do you wanna run?', Trump floated his chief of staff for 2028.",
     icon_podium),
    ("UKRAINE · KYIV", "Three Kyiv bridges struck",
     "Russia hits Kyiv crossings days after Ukraine struck the Crimean Bridge.",
     icon_bridge),
    ("EU · AID", "€1B more arms for Ukraine",
     "The EU Council approves €1B in arms; a €7.9B lump sum follows.",
     icon_eu_coin),
    ("YEMEN · HARBOUR", "Coalition hits Hodeidah port",
     "Coalition forces strike the harbour as Houthis warn shipping.",
     icon_harbour),
]

BRIEFS = [
    (14, "BRAZIL", "Bolsonaro hospitalised with abdominal pain."),
    (15, "EUROPE", "Cost-of-living protests sweep European cities."),
    (16, "BANGLADESH", "Fresh arson attacks amid political unrest."),
    (17, "USA", "More UFO footage declassified, filmed in the Middle East."),
    (18, "NEW YORK", "Mamdani plans to close Rikers Island by 2032."),
    (19, "FRANCE", "Police sentenced over beating of Michel Zecler."),
    (20, "CUBA", "American woman freed after 10 years in prison."),
    (21, "MALAYSIA", "10,000 Rohingya to be resettled in Turkiye."),
    (22, "SUDAN", "Army retakes RSF strongholds in West Kordofan."),
    (23, "MEXICO", "Migrant caravan of ~300 crosses into the south."),
    (24, "CHINA", "Trump, Xi and Putin hold trilateral summit in Shenzhen."),
    (25, "CHINA", "US approved ~900,000 AI chips for China in six months."),
    (26, "USA", "California subpoenas Nvidia over ex-CEO and China ties."),
    (27, "SOUTH AFRICA", "Homicides still reach 60 a day."),
    (28, "IRAQ", "Forces retake Jurf al-Sakhar after 12 years."),
    (29, "VENEZUELA", "Rejects ICJ jurisdiction over Essequibo."),
    (30, "NEPAL", "Balendra Shah faces his India test."),
    (31, "FRANCE", "Depardieu investigated over sexual allegations."),
    (32, "USA", "Trump threatens ban on AI data centres abroad."),
    (33, "YEMEN", "'It's just fireworks': life in a besieged city."),
    (34, "EGYPT", "Egypt eyes an AI lead, built on data."),
    (35, "CHINA", "Tech firms fear AI curbs after Nvidia fallout."),
    (36, "GERMANY", "Defence chief open to talks with the Kremlin."),
]

PINS = [
    (1, 0.73, 0.44), (2, 0.51, 0.18), (4, 0.56, 0.34), (7, 0.49, 0.12),
    (11, 0.59, 0.26), (14, 0.29, 0.64), (16, 0.81, 0.40), (22, 0.55, 0.62),
    (23, 0.13, 0.44), (27, 0.56, 0.76), (28, 0.69, 0.34), (34, 0.58, 0.50),
]

REGIONS = [
    ("Europe", 10, BLUE), ("North America", 10, RED), ("Asia", 6, YELLOW),
    ("Middle East", 4, TEAL), ("Africa", 3, PURPLE), ("South America", 2, ORANGE),
    ("Space", 1, SLATE),
]

LEFT_OUT = [
    "19 NOV — First Houthi strike hits Riyadh's PIF tower (Thursday). "
    "Today's Riyadh story is Saturday's interception.",
    "20 NOV — Riemann proof announced by Anthropic (Friday).",
    "20 NOV — UK and EU agree a post-Brexit deal (Friday).",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, W - 11, H - 11], outline=RULE, width=2)
    d.rectangle([16, 16, W - 17, H - 17], outline=HAIR, width=1)

    # ---- masthead (20-116) ----
    d.text((512, 24), "THE WORLD IN ONE DAY", font=fnt(SANS_B, 15),
           fill=RED, anchor="mt")
    d.text((512, 44), "SATURDAY, 21 NOVEMBER 2026", font=fnt(SERIF_B, 46),
           fill=INK, anchor="mt")
    d.text((512, 96),
           "Three missiles over Riyadh, a Russian strike on Poland, and a "
           "spacecraft reaches Mercury.",
           font=fnt(SERIF_I, 16), fill=FAINT, anchor="mt")
    rule(d, 20, 1004, 114, w=2)

    # ---- six big numbers (118-172) ----
    cell = 984 // 6
    for i, (big, label) in enumerate(NUMBERS):
        cx = 20 + i * cell
        bf = fnt(SERIF_B, 30)
        bw = d.textlength(big, font=bf)
        d.text((cx + (cell - bw) / 2, 120), big, font=bf, fill=BLUE)
        lf = fnt(SANS, 10)
        lw = d.textlength(label, font=lf)
        d.text((cx + (cell - lw) / 2, 154), label, font=lf, fill=FAINT)
        if i:
            vline(d, cx, 122, 168)
    rule(d, 20, 1004, 172, w=2)

    # ---- three big headlines (176-380) ----
    cols = [20, 356, 692]
    for ci, (kick, head, body, art) in enumerate(BIG3):
        x = cols[ci]
        tagline(d, x, 176, kick, size=12)
        title_lines(d, x, 192, head, 20, 312, lead=22)
        art(d, x, 240, 312, 88)
        block(d, x, 334, body, fnt(SANS, 12), 312, lead=15, limit=3)
        if ci:
            vline(d, x - 12, 176, 380)
    rule(d, 20, 1004, 382, w=2)

    # ---- ten small items, two rows of five (386-588) ----
    xs = [20, 218, 416, 614, 812]
    for row in range(2):
        y = 386 + row * 100
        for col in range(5):
            it = SMALL[row * 5 + col]
            x = xs[col]
            it[3](d, x, y, 190, 32)
            tagline(d, x, y + 36, it[0], size=10)
            title_lines(d, x, y + 48, it[1], 12, 190, lead=13)
            block(d, x, y + 76, it[2], fnt(SANS, 10), 190, lead=12,
                  limit=2)
            if col:
                vline(d, x - 4, y, y + 96)
        if row == 0:
            rule(d, 20, 1004, y + 98, w=1, fill=HAIR)
    rule(d, 20, 1004, 590, w=2)

    # ---- where it happened: map + numbered list (594-834) ----
    d.text((20, 594), "WHERE IT HAPPENED", font=fnt(SANS_B, 14), fill=RED)
    d.text((1004, 594), "STORIES 14–36, IN BRIEF", font=fnt(SANS_B, 12),
           fill=FAINT, anchor="rt")
    draw_world(d, 20, 616, 380, 216, PINS)
    bx, byy = 420, 616
    for num, place, txt in BRIEFS:
        head = f"{num} {place} — "
        hf = fnt(SANS_B, 10)
        tf = fnt(SANS, 10)
        d.text((bx, byy), head, font=hf, fill=INK)
        hw = d.textlength(head, font=hf)
        d.text((bx + hw, byy), txt, font=tf, fill=INK)
        byy += 9.4
    rule(d, 20, 1004, 836, w=2)

    # ---- region bar (840-866) ----
    total = sum(n for _, n, _ in REGIONS)
    rx = 20
    for name, n, col in REGIONS:
        seg = int(984 * n / total)
        d.rectangle([rx, 840, rx + seg, 850], fill=col)
        rx += seg
    lx = 20
    for name, n, col in REGIONS:
        d.rectangle([lx, 854, lx + 10, 864], fill=col)
        lab = f"{name} {n}"
        d.text((lx + 14, 854), lab, font=fnt(SANS_B, 10), fill=INK)
        lx += 14 + d.textlength(lab, font=fnt(SANS_B, 10)) + 16

    # ---- how it was made + date check (870-956) ----
    d.text((20, 870), "HOW THIS PAGE WAS MADE", font=fnt(SANS_B, 11),
           fill=INK)
    block(d, 20, 886,
          "Every story was checked against reporting published on Saturday "
          "21 November 2026. Figures are as the cited outlets reported "
          "them. The map is schematic, not to scale; pin numbers match the "
          "numbered stories. 36 stories, 7 regions.",
          fnt(SANS, 11), 580, lead=14, limit=4)
    d.rectangle([620, 870, 1004, 956], outline=RED, width=2)
    d.text((630, 876), "DATE CHECK — WHAT WE LEFT OUT",
           font=fnt(SANS_B, 12), fill=RED)
    yy = 892
    for item in LEFT_OUT:
        yy = block(d, 630, yy, item, fnt(SANS, 10), 364, lead=11, limit=2)
        yy += 2

    # ---- footer (960-1000) ----
    rule(d, 20, 1004, 960, w=1, fill=HAIR)
    d.text((20, 966), "Drawn from reporting published Saturday 21 November 2026.",
           font=fnt(SANS_I, 11), fill=FAINT)
    d.text((1004, 966),
           "Sources: Reuters, AP, AFP, BBC, The Hindu, Arab News, ESA, SCMP.",
           font=fnt(SANS_I, 11), fill=FAINT, anchor="rt")
    d.text((512, 984), "THE WORLD IN ONE DAY  ·  36 STORIES  ·  7 REGIONS",
           font=fnt(SANS_B, 10), fill=FAINT, anchor="mt")

    img.save(OUT, format="PNG")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
