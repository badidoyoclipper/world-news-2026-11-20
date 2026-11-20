# world-news-2026-11-20

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/badidoyoclipper/world-news-2026-11-20/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/badidoyoclipper/world-news-2026-11-20/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world news of **Friday 20 November 2026**: the front page of *The Daily Record*, drawn programmatically with Python and PIL. Under a huge date line, the hero panel covers the night's defining story — hours after the Shenzhen peace declaration, Russia fires more than 110 missiles at Ukraine and damages three of Kyiv's Dnipro bridges. Around it: COP31's draft deal erasing every mention of fossil fuels on the talks' final scheduled day, the deepening global AI stock selloff, the US Senate's 62–33 vote to speed up energy permitting, and the departure of the US national cyber director after a week of technology outages — plus a four-item ticker along the bottom. Each story was reported on 20 November 2026 and cross-checked against at least two independent outlets; several widely recycled items from earlier days were checked and deliberately left out.

The entry for the make.fun competition [news-image-20261120](https://make.fun/bounty/news-image-20261120) ("Sum up 20 November's world news in one image", $250 across 50 places).

## How it was made

A single Python script typesets the whole page with PIL: the masthead and black date band first, then the hero panel — with its small drawn scene of a three-span river bridge, the middle span sagging where the missiles hit — then four story cards and the bottom ticker. Nothing is photographed or AI-generated; every headline is real type set in the Liberation faces, which is why the page survives being shrunk to a 300-pixel thumbnail with its text intact.

## Run it

```sh
python3 main.py
```

`main.py` needs nothing beyond Python 3's standard library. It verifies that the shipped `entry.png` is a real PNG within the 1024×1024 limit, then writes it to `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set, else to `/output/entry.png` (or `./output/entry.png` where `/output` is unavailable). No network access, no dependencies, identical bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
