# HANDOFF — news-image-20261121

## What it is

A one-page newspaper front page summing up the world's news of Saturday
21 November 2026, drawn with PIL primitives only. Entry for the make.fun
bounty `news-image-20261121` ($100 pool, $20 for 1st, top 50 paid).
Deadline: 2026-11-23 08:00 CST (entries close 2026-11-23T00:00:00Z).
Result due 2026-12-07.

## Stories on the page (16 total)

Featured (6):
1. **POLAND — Russian missiles land in Poland.** Kh-101 came down 50 km
   from Ukraine's border, near allied war games (Exercise Koalicja,
   11 nations) at Nowa Deba; two missiles + a suspected drone in all.
   Tusk: "intentional provocation". NATO chief Rutte: "grave violation",
   jets scrambled. No one hurt in Poland. Ukraine barrage: 8 killed,
   ~28 injured. With a hand-drawn schematic map (Poland/Ukraine/Germany/
   Belarus, Baltic Sea, impact stars, Rzeszow drill site).
2. **SCIENCE — Claude "proves" the Riemann hypothesis.** Anthropic
   mathematician Levent Alpoge says he and Claude proved the 1859 problem,
   releasing a Lean formalisation. Worded as a claim: independent experts
   have compiled the code and call it "almost certainly true". Prime-spiral
   graphic.
3. **MARKETS — Tech sell-off deepens.** S&P 500 −3.7%, Nasdaq negative for
   the year; Anthropic shares slide days after a record IPO. Falling chart.
4. **CLIMATE — COP31 ends in deadlock.** Antalya, final scheduled day, no
   fossil-fuel phase-out in the draft, talks into overtime; Ukraine blocked
   a Russian climate report using occupied-territory data. Globe + clock.
5. **DENMARK — Russia accused of assassination plot.** Denmark says Russian
   intelligence plotted to kill a US-Ukrainian rapper on Danish soil;
   a Russian diplomat expelled. Shield icon.
6. **USA — 19 1/2 years for Sikh murder plot.** US court sentences Indian
   national Nikhil Gupta to 235 months for a murder-for-hire plot against
   a Sikh separatist leader in New York. Scales icon.

Day in brief (10): ICJ finds Myanmar committed genocide vs Rohingya;
Trump floats his chief of staff for president in 2028; Bolsonaro
hospitalised; European cost-of-living protests; Bangladesh arson attacks;
more UFO footage declassified; Mamdani to close Rikers by 2032; French
police sentenced over the Zecler beating; American woman freed after
10 years in a Cuban prison; 10,000 Rohingya to be resettled in Turkiye.

Numbers strip: 8 killed in the Ukraine barrage · 50 km from Ukraine's
border · −3.7% S&P 500 in a day · 1859 Riemann posed his problem.

Sources for every line are in NEWS.md (Reuters, AP, AFP, BBC, The Hindu,
SCMP, The Times, Scientific American, WSJ, Phys.org, Ukrinform).

## Files

- `main.py` — entrypoint (Python 3.13 stdlib only). Copies bundled
  `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`), checks
  PNG magic + 1 MiB gate, prints size + sha256. Written, then edited once
  (added the PNG magic check) so the final content comes from 2 messages.
- `entry.png` — the image, 1024×1024, 176,695 bytes.
- `tools/gen_image.py` — draws the page with PIL (Liberation fonts).
  Deterministic: no randomness; fixed geometry and text.
- `NEWS.md` — source of every story.
- `README.md` — three make.fun badges + footer links.
- `LICENSE` — starter MIT, SPDX line present.
- `prompt.txt` — the user's own words, verbatim.

## Verification (all done locally)

- `tools/gen_image.py` run twice: identical bytes.
  sha256 `f5d030d53c2c67a5374e5aa30bf8603be2d901e552858f503bf3dce2c130f987`
- `main.py` run twice (MAKEFUN_OUTPUT_DIR=/tmp/out1, /tmp/out2):
  output matches bundled `entry.png`, same sha256 both runs.
- Image: 1024×1024, 176,695 bytes (< 1,048,576). Gate OK.
- Visually checked: masthead + date prominent, lead + map clean, three
  cards clean, Denmark/Gupta row clean, numbers strip fits, 10-item index
  has no overlap, footer clean. (First render had row-2 text overflowing
  into row 3 and the numbers strip cut off; fixed by shortening bodies,
  shrinking graphics, shortening index lines.)

## Notes for the main agent

- Submit via the normal transcript-bundle route (like 11-19 / 11-20):
  browser creates the public empty repo, MCP push-files pushes the text
  files, binary `entry.png` goes up through the browser web UI (push-files
  would corrupt it), set About, bundle the session, check, submit.
- Usage placeholder is at `~/.makefun/muse-usage-news-image-20261121.jsonl`
  (1 line, 0 tokens) — overwrite with the real usage rows before bundling.
- The repo's git identity is xiangbingxi / xiangbingxi021013@163.com.
- Local commit SHA: `495d13b6f42320c97af27e930569f5e05f008c52`.
- Do NOT copy the 11-19/11-20 code: this generator was written from
  scratch in this session (own layout, own map, own spiral/chart/globe
  helpers). It only shares the genre (newspaper front page) and the
  proven delivery pattern (bundled entry.png + tiny copy entrypoint).
