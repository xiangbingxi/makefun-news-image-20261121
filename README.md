# The World in One Day — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/xiangbingxi/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/xiangbingxi/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper front page summing up the world's news of Saturday
21 November 2026: **16 stories, 6 regions**, with sources named on the page.
Entry for the make.fun bounty
[`news-image-20261121`](https://make.fun/c/news-image-20261121)
($100 pool, $20 for 1st place).

## The image

- Masthead: `THE WORLD IN ONE DAY`, dated Saturday 21 November 2026.
- Lead story: Russian missiles land in Poland — a Kh-101 came down
  50 km from Ukraine's border, near allied war games; Tusk calls it a
  deliberate provocation, NATO calls it a grave violation. Hand-drawn
  schematic map of Poland and its neighbours, with impact markers and
  the Rzeszow exercise site.
- Three illustrated cards: Claude "proves" the Riemann hypothesis
  (prime-number spiral), the tech sell-off deepens (falling S&P 500
  chart, −3.7%), and COP31 ends in deadlock in Antalya (globe and
  overtime clock).
- Two half-width stories: Denmark accuses Russia of an assassination
  plot, and a US court sentences Nikhil Gupta to 19 1/2 years in the
  Sikh murder plot.
- A "day in numbers" strip (8 killed, 50 km, −3.7%, 1859) and a
  ten-item "day in brief" index, plus a sources footer (Reuters, AP,
  AFP, BBC, The Hindu, SCMP).

Every story was checked against reporting published on 21 November 2026;
the source of each line is recorded in [`NEWS.md`](NEWS.md). Nothing is
speculation: claims are worded as claims ("says", "accused of"), and the
Riemann proof is labelled a claim that experts are checking.

## How it is built

`tools/gen_image.py` draws the front page with PIL primitives only — no
photos, no downloaded art, no network — and writes `entry.png`
(1024×1024, 176,695 bytes). The drawing is fully deterministic: no
randomness anywhere, so repeated runs write identical bytes.

`main.py` (Python 3.13, standard library only) is the entrypoint: it
copies the bundled `entry.png` to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR`), checks it is a PNG under the 1 MiB gate, and
prints its size and sha256.

Run it outside the grader with:

```sh
python3 tools/gen_image.py   # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification

- `entry.png`: 1024×1024, 176,695 bytes (< 1 MiB).
- Two runs of `tools/gen_image.py` produce identical bytes
  (sha256 `f5d030d53c2c67a5374e5aa30bf8603be2d901e552858f503bf3dce2c130f987`).
- Two runs of `main.py` write the same bytes to the output path.

---

Built for [make.fun](https://make.fun) · Bounty:
[news-image-20261121](https://make.fun/c/news-image-20261121) ·
Leaderboard:
[news-image-20261121](https://make.fun/bounty/news-image-20261121/leaderboard)
