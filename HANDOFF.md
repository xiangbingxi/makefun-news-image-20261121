# HANDOFF — news-image-20261121

## v2 (this round — ready to re-submit before 2026-11-23 08:00 CST)

User said v1 (01a1fc3e) was too thin vs the top 3 (~99%, 11–12 wins,
0 losses). v2 rebuilds the page in the top-3 front-page format — same
genre, own layout, own illustrations, own text (nothing copied from the
leaders). 36 stories, 7 regions.

### What's on the page (36 stories, 7 regions)

- Masthead: "THE WORLD IN ONE DAY" kicker, huge serif date
  "SATURDAY, 21 NOVEMBER 2026", italic one-line summary.
- 6 big numbers (blue, serif): **3** missiles over Riyadh ·
  **8** killed in Ukraine barrage · **1.6M** Russian troops lost ·
  **-3.7%** S&P 500 in a day · **€7.9B** EU aid to Ukraine ·
  **10,000** Rohingya resettled.
- 3 big illustrated headlines (each with a detailed flat vector scene):
  1. **RIYADH — Three missiles down over Riyadh** (night skyline,
     missile trail, airburst stars).
  2. **POLAND — Russian missiles land in Poland** (explosion burst,
     smoke, IMPACT star, jet silhouette).
  3. **MERCURY — BepiColombo reaches Mercury** (spacecraft with solar
     panels, cratered Mercury, sun, "8 YEARS OUT · 2 ORBITERS").
- 10 small illustrated stories (2 rows of 5, each with its own icon):
  COP31 deadlock (globe+clock+thermometer) · Claude "proves" Riemann
  (prime spiral) · Tech sell-off (falling chart) · Denmark assassination
  plot (target) · Gupta 19½ years (scales) · ICJ Myanmar genocide
  (courthouse) · Trump floats chief of staff (podium) · Three Kyiv
  bridges struck (bridge) · €1B more arms for Ukraine (EU coin) ·
  Coalition hits Hodeidah port (harbour + ship).
- "WHERE IT HAPPENED" world map (schematic continents, 12 red numbered
  pins: 1, 2, 4, 7, 11, 14, 16, 22, 23, 27, 28, 34) + numbered briefs
  14–36 on the right (Brazil, Europe protests, Bangladesh arson, UFO
  footage, Rikers, Zecler, Cuba, Rohingya, Sudan, Mexico caravan,
  Shenzhen summit, AI chips, Nvidia subpoena, South Africa homicides,
  Iraq, Venezuela, Nepal, Depardieu, AI data centres, Yemen, Egypt AI,
  China AI curbs, Germany–Kremlin talks).
- Colour region bar + legend: Europe 10, North America 10, Asia 6,
  Middle East 4, Africa 3, South America 2, Space 1.
- Red-bordered "DATE CHECK — WHAT WE LEFT OUT" box (3 excluded items:
  19 Nov PIF tower strike, 20 Nov Riemann announcement, 20 Nov UK–EU
  post-Brexit deal) + "HOW THIS PAGE WAS MADE" note + sources footer.

### Verification (all done locally)

- `tools/gen_image.py` run twice: identical bytes.
  sha256 `693bac02fb06abe195ff5eb61bc5b9dc905298a185841cbd171230363ebf4622`
- `main.py` run twice (MAKEFUN_OUTPUT_DIR=/tmp/news-v2-check/out1,
  /tmp/news-v2-check/out2): output matches bundled `entry.png`, same
  sha256 both runs.
- Image: 1024×1024, RGB, 193,493 bytes (< 1,048,576). Gate OK.
- Visually checked (full page + top and bottom crops): masthead and
  numbers strip clean (single-line labels), 3 illustrations complete,
  10 small icons/titles/leads fit, numbered list 14–36 readable with no
  overlap, map pins visible, region bar + legend fit, DATE CHECK box
  fully inside its red border, footer clean. (First v2 render had the
  numbers-strip labels clipping to 2 lines, the 14–36 list overlapping,
  and the DATE CHECK third item overflowing the box; all three fixed by
  shortening labels, giving the list 9.4 px leading in a taller section,
  and shortening the two Friday exclusions to one line each.)
- `main.py` untouched from v1 (still just copies entry.png); it already
  comes from 2 write/edit messages in v1, so no change needed.

### Files changed (v2)

- `tools/gen_image.py` — rewritten from scratch (own illustration
  functions and layout; v1 read only as a format reference).
- `entry.png` — regenerated v2 image (193,493 bytes).
- `NEWS.md` — rewritten for the 36 stories with sources.
- `main.py`, `README.md`, `LICENSE`, `prompt.txt` — unchanged from v1.

### Local commit

- v2 commit SHA: `b33d00d1ab05156624e9b07b0ef5016aa661c655`
  (message: "v2: 36-story front page — 6 numbers, 3 illustrated
  headlines, 10 small stories, map + numbered briefs 14-36, DATE CHECK
  box, region bar"). Local only, NOT pushed. v1 commit was `d9e642a`.

### Usage placeholder

- `~/.makefun/muse-usage-news-image-20261121.jsonl` — now 2 lines:
  line 1 is v1's (agent ed06f4f2…, real tokens), line 2 is this
  session's placeholder (agent_id
  `71fdd9a8-8390-42ac-92db-35598094fa6f`, 0 tokens, model
  ipnext/avocado-5.17-v2). Main agent: overwrite with real usage rows
  before bundling, as usual.

### Notes for the main agent

- Re-submit via the normal transcript-bundle route: push the changed
  text files (tools/gen_image.py, NEWS.md, HANDOFF.md) via MCP
  push-files, binary `entry.png` through the browser web UI, set About,
  bundle the session, check, submit as a new submission for
  `news-image-20261121` (replaces v1 final 01a1fc3e).
- The `.makefun/owner.json` is already in the repo (from v1); it is
  untracked in the local clone — leave it, it is already on GitHub.
- Do NOT copy the top-3 leaders' images, text, or code: this generator
  was written from scratch in this session. It only shares the genre
  (newspaper front page) and the proven delivery pattern.

---

## v1 (already submitted — record kept below)

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
