<div align="center">

```
  ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗
  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║
     ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║
     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║
     ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

             P  O  R  T  F  O  L  I  O
```

**A handcrafted interactive terminal portfolio, accessible over SSH from anywhere in the world.**

---

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?style=flat-square&logo=linux&logoColor=white)
![Shell](https://img.shields.io/badge/Interface-curses-orange?style=flat-square)
![Hosted](https://img.shields.io/badge/Hosted-Oracle%20Cloud-red?style=flat-square&logo=oracle&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## Overview

This is not a website. It is a fully interactive portfolio built in the terminal using Python and the `curses` library, hosted on a live server and accessible to anyone via SSH — no installation, no browser, no dependencies on your end.

The design philosophy is intentional: raw, minimal, and tactile. Every screen, layout, and ASCII illustration is hand-authored. It is the kind of thing you build because you enjoy the craft of building it.

---

## Access

Connect directly from your terminal. No setup required on your machine.

```sh
ssh portfolio@artjomjapins.site
```

> Works on macOS, Linux, and Windows (via PowerShell, Git Bash, or WSL). No account or key needed.

---

## Navigation

Once connected, the interface is fully keyboard-driven.

| Key | Action |
|-----|--------|
| `↑` / `k` | Move selection up |
| `↓` / `j` | Move selection down |
| `Enter` | Open selected section |
| `Q` | Return to home / Quit |

---

## What's Inside

```
HOME
├── ASCII portrait
├── Name & title block
├── Navigation menu
├── Currently learning panel
└── Links panel

ABOUT ME
├── Bio & location
├── Focus areas
├── Current goals
└── Vintage CRT ASCII art

PROJECTS
├── Terminal Portfolio  [ LIVE ]
├── Upcoming Projects   [ IN PROGRESS ]
├── Open Source         [ ONGOING ]
└── Floppy disk ASCII art

CONTACT
├── Email
├── Website
├── SSH command
├── GitHub
└── Rotary phone ASCII art
```

---

## Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3 |
| TUI Library | `curses` (stdlib) |
| Protocol | OpenSSH |
| Server | Oracle Cloud (Always Free tier) |
| OS | Ubuntu 22.04 LTS |
| Process Manager | `systemd` |

No frameworks. No dependencies beyond the Python standard library.

---

## Architecture

```
client terminal (any OS)
        |
        |  SSH (port 22)
        v
 Oracle Cloud VM
        |
        |  systemd service
        v
  restricted shell
        |
        |  executes
        v
  portfolio.py  ──>  curses TUI
```

The server runs a restricted SSH configuration that drops incoming connections directly into the portfolio process. Users are sandboxed — they cannot access the shell or filesystem.

---

## Running Locally

If you want to run a local copy:

**Clone the repository**

```sh
git clone https://github.com/zxrk/terminal-portfolio.git
cd terminal-portfolio
```

**Run directly**

```sh
python3 portfolio.py
```

> Requires Python 3.8 or higher. No pip installs needed — `curses` ships with Python on macOS and Linux. On Windows, use WSL.

**Minimum terminal size:** 120 × 30 characters for the layout to render correctly.

---

## Self-Hosting

To host your own version on a VPS:

**1. Copy the script to your server**

```sh
scp portfolio.py user@your-server:/home/portfolio/
```

**2. Create a restricted user**

```sh
sudo useradd -m -s /bin/bash portfolio
```

**3. Set up a systemd service**

```ini
# /etc/systemd/system/portfolio.service
[Unit]
Description=SSH Terminal Portfolio

[Service]
ExecStart=/usr/bin/python3 /home/portfolio/portfolio.py
User=portfolio
Restart=always

[Install]
WantedBy=multi-user.target
```

**4. Configure SSH to auto-run the portfolio**

```sh
# In /home/portfolio/.ssh/authorized_keys or via sshd_config ForceCommand
ForceCommand python3 /home/portfolio/portfolio.py
```

**5. Enable and start**

```sh
sudo systemctl enable portfolio
sudo systemctl start portfolio
```

---

## Design Notes

The terminal is treated as a creative constraint, not a limitation. Choices made throughout:

- **Fixed-width ASCII illustrations** drawn by hand to complement each section
- **Colour palette** built on 256-colour terminal support with a warm accent (`#ffaf5f`) against a dark background
- **No external libraries** — the entire experience runs on stdlib `curses`, keeping the server footprint minimal
- **Keyboard-first navigation** with both arrow keys and vim-style `j`/`k` bindings

---

## Project Structure

```
terminal-portfolio/
└── portfolio.py        # Single-file application — all layout, colour, and logic
```

The entire portfolio is intentionally a single file. There is something satisfying about a complete experience fitting in one place.

---

## License

MIT — use it, fork it, make it yours.

---

<div align="center">

**Built by Artjom Japins**

[artjomjapins.site](https://artjomjapins.site) · [github.com/zxrk](https://github.com/zxrk)

```
ssh portfolio@artjomjapins.site
```

</div>
