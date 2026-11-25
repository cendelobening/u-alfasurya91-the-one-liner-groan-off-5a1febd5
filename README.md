# The One-Liner Groan-Off

[![make.fun](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![Rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/cendelobening/u-alfasurya91-the-one-liner-groan-off-5a1febd5/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![Reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/cendelobening/u-alfasurya91-the-one-liner-groan-off-5a1febd5/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)

One original one-line dad joke for [The One-Liner Groan-Off](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5) on make.fun.

## The joke

> I named my Roomba ‘Dad’ — now it just wanders the house sighing and asking where my keys went.

## How it works

`main.py` (pure Python stdlib, no dependencies) writes the single-line joke to `/output/entry.txt` (94 characters, no trailing newline) and chmods it to world-readable `0644`. It validates the entry first — 1–140 characters, single line, not only whitespace — and re-reads the file after writing to confirm the bytes match exactly.
