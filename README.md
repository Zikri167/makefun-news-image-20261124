# makefun-news-image-20261124

Entry for the [make.fun](https://make.fun) bounty **news-image-20261124** — "Sum up 24 November's world news in one image."

A deterministic 1024x1024 broadsheet news poster rendered entirely in pure Python stdlib (custom PNG encoder, framebuffer primitives and a hand-made 5x7 bitmap font — no randomness, no clock, no network). It produces a byte-identical `entry.png` on every run.

![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)
![bounty](https://img.shields.io/badge/bounty-news--image--20261124-orange)
![license](https://img.shields.io/badge/license-MIT-green)

Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py` and the poster lands in `out/entry.png`.
