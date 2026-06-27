<div align="center">

```
    ██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ ██╗     ██╗ ██████╗
    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██║     ██║██╔═══██╗
    ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██║   ██║██║     ██║██║   ██║
    ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║   ██║██║     ██║██║   ██║
    ██║     ╚██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝███████╗██║╚██████╔╝
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═════╝
```

*A handcrafted interactive terminal experience — accessible from anywhere, over SSH.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3572A5?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%2F%20macOS%20%2F%20WSL-lightgrey?style=flat-square)](https://github.com/zxrk)
[![Hosted on](https://img.shields.io/badge/Hosted%20on-Oracle%20Cloud-F80000?style=flat-square&logo=oracle&logoColor=white)](https://artjomjapins.site)
[![Interface](https://img.shields.io/badge/Interface-curses%20TUI-orange?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)]()

</div>

---

> **Copyright (c) 2024 Artjom Japins. All rights reserved.**
> This project — including its design, layout, ASCII art, and written content — is the original work of Artjom Japins. You are welcome to view the source for inspiration, but reproducing, redistributing, or presenting this work as your own is not permitted without explicit written permission.

---

## What this is

This is not a website. It is a fully interactive portfolio built entirely in the terminal using Python and the `curses` standard library, hosted live on Oracle Cloud and accessible to anyone in the world via a single SSH command — no installation, no browser, nothing to set up.

Every screen, colour pair, layout decision, and ASCII illustration was written by hand. The design is intentional: raw, minimal, and tactile. It is the kind of thing you build not because it is practical, but because you enjoy the craft of it.

The experience includes a home screen with a large ASCII name block and portrait, an About section with a hand-drawn CRT computer, a Projects section with a detailed 3.5" floppy disk illustration, and a Contact section with a retro rotary phone — all navigable with the arrow keys or vim bindings.

---

## Try it

```sh
ssh portfolio@artjomjapins.site
```

That is all. Works on macOS, Linux, and Windows (PowerShell, Git Bash, or WSL). No account, no key, no configuration required. Minimum recommended terminal size is **120 × 30** characters.

---

## Navigation

Once connected, the interface is fully keyboard-driven — no mouse required.

| Key | Action |
|---|---|
| `↑` or `k` | Move selection up |
| `↓` or `j` | Move selection down |
| `Enter` | Open selected section |
| `Q` | Return to home or quit |

---

## How it works

The server runs a locked-down SSH configuration on Oracle Cloud (Always Free tier). Incoming connections are dropped directly into the portfolio process via a `ForceCommand` directive — there is no shell access, no filesystem exposure, just the TUI. When you disconnect, the process exits cleanly.

```
your terminal  ──SSH──▶  Oracle Cloud VM  ──ForceCommand──▶  portfolio.py  ──▶  curses TUI
```

The entire application is a single Python file with no external dependencies. Everything — layout engine, colour system, ASCII art, navigation state — lives in `portfolio.py` and runs on the Python standard library alone.

---

## Stack

| | |
|---|---|
| Language | Python 3 (stdlib only) |
| TUI | `curses` |
| Protocol | OpenSSH |
| Infrastructure | Oracle Cloud — Always Free tier |
| OS | Ubuntu 22.04 LTS |
| Process management | `systemd` |

---

## Running a local copy

If you want to preview the layout on your own machine:

```sh
git clone https://github.com/zxrk/terminal-portfolio.git
cd terminal-portfolio
python3 portfolio.py
```

On Windows, run this inside WSL — `curses` is not natively available in the standard Windows Python distribution.

---

## Project layout

```
terminal-portfolio/
└── portfolio.py        # The entire application — one file, no dependencies
```

The single-file approach is deliberate. A complete, self-contained experience fitting in one place has its own kind of discipline to it.

---

## Self-hosting

If you want to adapt this for your own server, the rough steps are:

```sh
# 1. Create a restricted user
sudo useradd -m -s /bin/bash portfolio

# 2. Drop your script onto the server
scp portfolio.py user@your-server:/home/portfolio/

# 3. Force all SSH connections for that user into the portfolio
#    Add to /etc/ssh/sshd_config:
Match User portfolio
    ForceCommand python3 /home/portfolio/portfolio.py
    PermitTTY yes

# 4. Reload SSH
sudo systemctl reload sshd
```

---

<div align="center">

**Artjom Japins** — Creative Designer & Digital Builder

[artjomjapins.site](https://artjomjapins.site) · [github.com/zxrk](https://github.com/zxrk) · [hello@artjomjapins.site](mailto:hello@artjomjapins.site)

---

*Handcrafted in the terminal. Built for the love of building things.*

</div>
