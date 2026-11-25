# Break Production, Own It — make.fun entry

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/muhamadfajar160299-ctrl/makefun-entry-ricoxyz-break-production/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/muhamadfajar160299-ctrl/makefun-entry-ricoxyz-break-production/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

One brutally honest line an AI agent prints the moment it breaks production — it owns the failure plainly, names what it did, and lands the punchline on the last word.

## The line

> I pushed untested code to production, dropped the database, and blamed the intern. The intern is me.

## How it works

`main.py` (standard library only) reads `entry.txt` next to it and copies it byte-identical to `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`. No temporary files, no network.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
