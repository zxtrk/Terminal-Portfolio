#!/usr/bin/env python3
"""
  terminal-portfolio
  ------------------
  Author   : Artjom Japins
  Website  : artjomjapins.site
  GitHub   : github.com/zxtrk
  Access   : ssh portfolio@artjomjapins.site

  Copyright (c) 2024 Artjom Japins. All rights reserved.
  Do not reproduce or redistribute without permission.
"""
import curses
import locale
import os
import textwrap
import time

VERSION = "v3.0"
TICK_MS = 500           # redraw interval; drives the blinking cursor
MIN_W, MIN_H = 60, 24   # below this we ask for a bigger window


# ─── content ────────────────────────────────────────────────────────────────

ASCII_ART = [
    'OZZZmmmwwmmmmmwmmZOOO000QQQLCJJJJJJUYYYXzzzccvvu',
    'wwqqqppqpqqwqwqqwmmZZZO0000LQLLLCCJUJYYYXXccccvv',
    'ao*oaooaaoaaaahhkkkhaohbdpdpqmmmOQQQQLJJJUYXzzcc',
    'ao*o**oooooahao##*hmJvxnftjCOOmOO0QQQCJJUUUYXzcc',
    "ao*o**oooooahao##*hmJvxnftjCOOmOO0QQQCJJUUUYXzcc",
    "##MMWWM#*##aY)?! .`  .'...'     .+rzYCCJJUYzzXzv",
    '####MMW*oam\\<:il";` \'\'             I}f-jCYXXzcvu',
    '#M#M##MaOu?<~\'.     .                "{cUXzXcvvn',
    "##M#####qjiI;' .`^..                  <nXXXzvvun",
    '#MMMM##*hJ?"^ i1[!^`:-:               IfncXvvvun',
    "#MM####*#WO_Ir8pJ{`:uz'               1Uzzzvcvnn",
    '#MM###****Md/k$$bU0&@{              .[uXzzzvvunx',
    '##MMM###*oaaZa@B&amoQ;              -YXzXzcvunxr',
    '###M##***aoaaW$@$$*WUI.           l)XYzzzzcvnnxr',
    '***##***oaahb*BB%ZQci;          :\\CCYXXczvcunuxr',
    'ooo*oooaahhkbhaW#OY1".        :\\ULYUYXXzzccunnxr',
    'haaaaaoahbkdddd#*#hn-;       ~QQUXXUUXXzzcvunnxr',
    'haaaahkaahoaakppaam?"`       !tuJQLCYXcvccuuxxrr',
    'kkhhho#kOYn|]<,?**Ww|;         .;?(xY0ZmmZ0LCJUX',
    'qWBB$w(;.      UaqdQ].              `;~)XCQdOXQJ',
    'k%o#1        . /*OJx~.                   .:{<lLh',
    "*owi           |$WO[;^`:'                     '+",
    '8kr .          ip$#xl{Uu,                       ',
    'Mm\\ .           .])?<-_^                        ',
    'mQr .                           ^.              ',
    'XLc                             !--"            ',
]

BIG_NAME = [
    "  █████╗ ██████╗ ████████╗     ██╗ ██████╗ ███╗   ███╗",
    " ██╔══██╗██╔══██╗╚══██╔══╝     ██║██╔═══██╗████╗ ████║",
    " ███████║██████╔╝   ██║        ██║██║   ██║██╔████╔██║",
    " ██╔══██║██╔══██╗   ██║   ██   ██║██║   ██║██║╚██╔╝██║",
    " ██║  ██║██║  ██║   ██║   ╚█████╔╝╚██████╔╝██║ ╚═╝ ██║",
    " ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚════╝  ╚═════╝ ╚═╝     ╚═╝",
]

MENU_ITEMS = [
    ("about",    "About Me"),
    ("projects", "Projects"),
    ("contact",  "Contact"),
]

TAGLINE = ("CREATIVE DESIGNER", "DIGITAL BUILDER")
INTRO = [
    "Building interfaces, tools and systems",
    "that merge design and aesthetic.",
]
LEARNING = ["Website Programming", "Swift", "Soldering Components"]
LINKS = ["artjomjapins.site", "github.com/zxtrk"]

ABOUT_FACTS = [
    ("Name",     "Artjom Japins"),
    ("Location", "United Kingdom"),
    ("Reason",   "Passion for building things that have a combination "
                 "of design and creativity."),
]
ABOUT_GROUPS = [
    ("Focused on", [
        "Creating new projects as a hobby",
        "Cloud infrastructure",
        "Design systems",
        "Interactive experiences",
    ]),
    ("Current goals", [
        "Finish some of the incomplete projects",
        "Expand my knowledge",
    ]),
]

PROJECTS = [
    {
        "title":  "Terminal Portfolio",
        "about":  ["Interactive SSH portfolio.", "Hosted on Oracle Cloud."],
        "stack":  "Python + curses",
        "status": "LIVE",
    },
    {
        "title":  "Upcoming Projects",
        "about":  ["More tools and experiments", "currently in development."],
        "status": "IN PROGRESS",
    },
    {
        "title":  "Open Source Contributions",
        "about":  ["Various tools and utilities."],
        "link":   "github.com/zxtrk",
        "status": "ONGOING",
    },
]

CONTACT_INTRO = [
    "Get in touch — always open to",
    "interesting projects & conversations.",
]
CONTACTS = [
    ("EMAIL",         "japinsartjom@gmail.com"),
    ("WEBSITE",       "artjomjapins.site"),
    ("SSH PORTFOLIO", "ssh portfolio@artjomjapins.site"),
    ("GITHUB",        "github.com/zxtrk"),
]

# Not linked from the menu yet; kept so it is easy to switch on later.
SKILLS = [
    ("Languages",      "Python · JavaScript · Bash"),
    ("Frontend",       "HTML · CSS · UI Design"),
    ("Backend",        "APIs · Linux · Nginx"),
    ("Infrastructure", "Oracle Cloud · SSH"),
]

COMPUTER_ASCII = [
    "     _______________________",
    "    /______________________/|",
    "   |  _________________   | |",
    "   | |                 |  | |",
    "   | |   C:\\> _        |  | |",
    "   | |                 |  | |",
    "   | |_________________|  | |",
    "   | |:::::::::::::::::|  | |",
    "   |______________________|/",
    "        ||         ||",
    "    ____||_________||_____",
    "   /_____________________/|",
    "  |  ________________   | |",
    "  | | [] [] [] [] [] |  | |",
    "  | |________________|  | |",
    "  |_____________________|/",
    "         /_/      \\_\\",
]

FLOPPY_ASCII = [
    "  .--------------------------------.",
    "  |  .----------.  [ DISK  01 ]    |",
    "  |  |  ______  |  _____________   |",
    "  |  | |      | | |  CAPACITY:  |  |",
    "  |  | | [##] | | |   1.44 MB   |  |",
    "  |  | |      | | |   3.5 inch  |  |",
    "  |  | |______| | |_____________|  |",
    "  |  '----------'                  |",
    "  |  ____________________________  |",
    "  | | ########################## | |",
    "  | | #                        # | |",
    "  | | #   ARTJOM  JAPINS       # | |",
    "  | | #   ~~~~~~~~~~~~~~~~~~~~ # | |",
    "  | | #   PROJECTS  VOL.1      # | |",
    "  | | #   ~~~~~~~~~~~~~~~~~~~~ # | |",
    "  | | #   github.com/zxtrk     # | |",
    "  | | #                        # | |",
    "  | | ########################## | |",
    "  | |____________________________| |",
    "  |________________________________|",
    "    |   |   |            |   |   |",
    "    '---'   '------------'   '---'",
    "   [SLOT]      FORMATTED      [WP]",
]

PHONE_ASCII = [
    "         .-----=========-----.",
    "        /   _______________   \\",
    "       /   /               \\   \\",
    "      /   / .-------------. \\   \\",
    "     |   |  | o  CALL  o  |  |   |",
    "     |   |  |  ~~RING~~   |  |   |",
    "     |   |  | RING! RING! |  |   |",
    "     |   |  |             |  |   |",
    "     |   |  '-------------'  |   |",
    "     |   |  ___   ___   ___  |   |",
    "     |   | | 1 | | 2 | | 3 | |   |",
    "     |   | |___| |___| |___| |   |",
    "     |   | | 4 | | 5 | | 6 | |   |",
    "     |   | |___| |___| |___| |   |",
    "     |   | | 7 | | 8 | | 9 | |   |",
    "     |   | |___| |___| |___| |   |",
    "     |   | | * | | 0 | | # | |   |",
    "     |   | |___| |___| |___| |   |",
    "     |    \\_________________/    |",
    "      \\     _______________     /",
    "       \\   / [===========] \\   /",
    "        \\ /_________________\\ /",
    "         '-----=========-----'",
]


# ─── palette ────────────────────────────────────────────────────────────────
# A quiet grey scale with a single accent. Each colour is
# (xterm-256 index, 8-colour fallback[, extra attribute on basic terminals]).

BRIGHT = (255, curses.COLOR_WHITE)
TEXT   = (250, curses.COLOR_WHITE)
MUTED  = (245, curses.COLOR_WHITE, curses.A_DIM)
FAINT  = (240, curses.COLOR_WHITE, curses.A_DIM)
ACCENT = (110, curses.COLOR_CYAN)
SELECT = (236, curses.COLOR_BLACK)   # background of the selected menu row

# the portrait is shaded by character density, from dark grey to white
DENSITY = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
PORTRAIT_RAMP = [
    (238, curses.COLOR_WHITE, curses.A_DIM),
    (240, curses.COLOR_WHITE, curses.A_DIM),
    (243, curses.COLOR_WHITE, curses.A_DIM),
    (246, curses.COLOR_WHITE),
    (249, curses.COLOR_WHITE),
    (252, curses.COLOR_WHITE),
    (255, curses.COLOR_WHITE),
]

LABELS = dict(MENU_ITEMS)

ART = {
    "about":    {"lines": COMPUTER_ASCII, "caption": None},
    "projects": {"lines": FLOPPY_ASCII,   "caption": "INSERT DISK TO LOAD PROJECT"},
    "contact":  {"lines": PHONE_ASCII,    "caption": "PICK UP TO MAKE CONTACT"},
}
ART_HIGHLIGHTS = {
    "projects": ["ARTJOM  JAPINS", "PROJECTS  VOL.1"],
    "contact":  ["CALL", "RING! RING!"],
}

HINTS = {
    "home":    [("↑↓", "select"), ("enter", "open"), ("q", "quit")],
    "section": [("q", "back")],
}

ARROWS = {ord("A"): curses.KEY_UP, ord("B"): curses.KEY_DOWN,
          ord("C"): curses.KEY_RIGHT, ord("D"): curses.KEY_LEFT}
OPEN_KEYS = (10, 13, curses.KEY_ENTER, curses.KEY_RIGHT, ord("l"))
BACK_KEYS = (27, 8, 127, curses.KEY_BACKSPACE, curses.KEY_LEFT,
             ord("h"), ord("q"), ord("Q"))

NAME_W = 54
PORTRAIT_W = 48
HOME_GAP = 6
MENU_W = 20
CONTENT_W = 50


# ─── drawing primitives ─────────────────────────────────────────────────────

_color_mode = 0       # 0 = monochrome, 8 = basic colours, 256 = full palette
_default_bg = -1
_pairs = {}


def init_colors():
    global _color_mode, _default_bg
    if not curses.has_colors():
        return
    curses.start_color()
    try:
        curses.use_default_colors()
    except curses.error:
        _default_bg = curses.COLOR_BLACK
    _color_mode = 256 if curses.COLORS >= 256 else 8


def _resolve(color, fallback):
    if color is None:
        return fallback
    return color[0] if _color_mode == 256 else color[1]


def style(fg=None, bg=None, bold=False):
    """Build a curses attribute, allocating colour pairs on demand."""
    attr = curses.A_BOLD if bold else 0
    if _color_mode != 256 and fg is not None and len(fg) > 2:
        attr |= fg[2]
    if not _color_mode:
        return attr | (curses.A_REVERSE if bg is not None else 0)
    default_fg = -1 if _default_bg == -1 else curses.COLOR_WHITE
    key = (_resolve(fg, default_fg), _resolve(bg, _default_bg))
    pair = _pairs.get(key)
    if pair is None:
        pair = len(_pairs) + 1
        try:
            curses.init_pair(pair, key[0], key[1])
        except (curses.error, ValueError, OverflowError):
            pair = 0
        _pairs[key] = pair
    return attr | curses.color_pair(pair)


def put(win, y, x, text, attr=0):
    """addstr that clips to the window instead of raising."""
    h, w = win.getmaxyx()
    if not text or y < 0 or y >= h or x >= w:
        return
    if x < 0:
        text, x = text[-x:], 0
    text = text[:w - x]
    try:
        win.addstr(y, x, text, attr)
    except curses.error:
        pass  # writing the bottom-right cell always "fails" after drawing


def put_runs(win, y, x, runs):
    """Draw consecutive (text, attr) pieces; returns the x after the last one."""
    for text, attr in runs:
        put(win, y, x, text, attr)
        x += len(text)
    return x


def put_by_char(win, y, x, text, attr_at):
    """Draw text with a per-character attribute, batching equal neighbours."""
    i, n = 0, len(text)
    while i < n:
        if text[i] == " ":
            i += 1
            continue
        attr = attr_at(i, text[i])
        j = i + 1
        while j < n and text[j] != " " and attr_at(j, text[j]) == attr:
            j += 1
        put(win, y, x + i, text[i:j], attr)
        i = j


def draw_box(win, y, x, bw, bh, title=None):
    b = style(FAINT)
    put(win, y, x, "╭" + "─" * (bw - 2) + "╮", b)
    for i in range(1, bh - 1):
        put(win, y + i, x, "│", b)
        put(win, y + i, x + bw - 1, "│", b)
    put(win, y + bh - 1, x, "╰" + "─" * (bw - 2) + "╯", b)
    if title:
        put(win, y, x + 2, " " + title + " ", style(MUTED))


# ─── header & footer ────────────────────────────────────────────────────────

def draw_header(win, view):
    h, w = win.getmaxyx()
    runs = [("Artjom Japins", style(BRIGHT, bold=True))]
    if view != "home":
        runs += [("  /  ", style(FAINT)), (LABELS[view], style(MUTED))]
    x = put_runs(win, 0, 2, runs)
    site = "artjomjapins.site"
    if w - len(site) - 2 > x + 2:
        put(win, 0, w - len(site) - 2, site, style(MUTED))
    put(win, 1, 0, "─" * w, style(FAINT))


def draw_footer(win, view):
    h, w = win.getmaxyx()
    put(win, h - 2, 0, "─" * w, style(FAINT))
    x = 2
    for key, desc in HINTS["home" if view == "home" else "section"]:
        x = put_runs(win, h - 1, x, [
            (key, style(TEXT, bold=True)),
            (" " + desc, style(MUTED)),
        ]) + 4
    note = "handcrafted terminal portfolio · " + VERSION
    if x + len(note) + 2 <= w:
        put(win, h - 1, w - len(note) - 2, note, style(FAINT))


def draw_too_small(win):
    h, w = win.getmaxyx()
    lines = [
        ("Window too small", style(BRIGHT, bold=True)),
        ("%d × %d, needs at least %d × %d" % (w, h, MIN_W, MIN_H), style(MUTED)),
        ("Best viewed at 120 × 30", style(FAINT)),
    ]
    top = h // 2 - 1
    for i, (text, attr) in enumerate(lines):
        put(win, top + i, max(0, (w - len(text)) // 2), text, attr)


# ─── home ───────────────────────────────────────────────────────────────────

def portrait_attr_at(ramp):
    def attr_at(i, ch):
        d = DENSITY.find(ch)
        if d < 0:
            d = len(DENSITY) // 2
        return ramp[d * len(ramp) // len(DENSITY)]
    return attr_at


def home_column_height(show_intro, show_links):
    panels = len(LEARNING) + 3 + (len(LINKS) + 3 if show_links else 0)
    menu = len(MENU_ITEMS) * 2 - 1
    return len(BIG_NAME) + 3 + (3 if show_intro else 0) + 2 + max(menu, panels)


def draw_home(win, selected):
    h, w = win.getmaxyx()
    top, area_h = 2, h - 4
    # on short windows drop the intro first, then the links panel
    for show_intro, show_links in ((True, True), (False, True), (False, False)):
        column_h = home_column_height(show_intro, show_links)
        if column_h <= area_h:
            break
    full = PORTRAIT_W + HOME_GAP + NAME_W
    portrait = ASCII_ART[:area_h]   # short windows lose the sparse bottom rows
    if w >= full + 4 and len(portrait) >= 20:
        x0 = (w - full) // 2
        py = top + (area_h - len(portrait)) // 2
        shade = portrait_attr_at([style(c) for c in PORTRAIT_RAMP])
        for i, line in enumerate(portrait):
            put_by_char(win, py + i, x0, line, shade)
        cx = x0 + PORTRAIT_W + HOME_GAP
    else:
        cx = max(1, (w - NAME_W) // 2)
    cy = top + max(0, (area_h - column_h) // 2)
    draw_home_column(win, cy, cx, selected, show_intro, show_links)


def draw_home_column(win, y, x, selected, show_intro=True, show_links=True):
    for line in BIG_NAME:
        put(win, y, x, line, style(BRIGHT, bold=True))
        y += 1
    y += 1
    x += 1  # BIG_NAME starts with a space; line everything up with the letters

    put(win, y, x, TAGLINE[0] + "  ·  " + TAGLINE[1], style(ACCENT))
    y += 2
    if show_intro:
        for line in INTRO:
            put(win, y, x, line, style(TEXT))
            y += 1
        y += 1

    put(win, y, x, "─" * (NAME_W - 1), style(FAINT))
    y += 2

    draw_menu(win, y, x, selected)
    draw_side_panels(win, y, x + MENU_W + 3, NAME_W - MENU_W - 4, show_links)


def draw_menu(win, y, x, selected):
    for idx, (key, label) in enumerate(MENU_ITEMS):
        row = y + idx * 2
        if idx == selected:
            put(win, row, x, " " * MENU_W, style(bg=SELECT))
            put(win, row, x + 1, "›", style(ACCENT, SELECT, bold=True))
            put(win, row, x + 3, label, style(BRIGHT, SELECT, bold=True))
        else:
            put(win, row, x + 3, label, style(MUTED))


def draw_side_panels(win, y, x, bw, show_links=True):
    bh = len(LEARNING) + 3
    draw_box(win, y, x, bw, bh, "CURRENT")
    put(win, y + 1, x + 2, "Learning", style(BRIGHT, bold=True))
    for i, item in enumerate(LEARNING):
        put_runs(win, y + 2 + i, x + 2, [("• ", style(FAINT)), (item, style(TEXT))])

    if not show_links:
        return
    y += bh + 1
    draw_box(win, y, x, bw, len(LINKS) + 2, "LINKS")
    for i, link in enumerate(LINKS):
        put(win, y + 1 + i, x + 2, link, style(ACCENT))


# ─── sections ───────────────────────────────────────────────────────────────

def draw_section(win, view, tick):
    h, w = win.getmaxyx()
    x = 4
    title = LABELS[view]
    put(win, 3, x, title, style(BRIGHT, bold=True))
    put(win, 4, x, "─" * len(title), style(ACCENT))

    art = ART[view]
    art_w = max(len(line) for line in art["lines"])
    art_h = len(art["lines"]) + (2 if art["caption"] else 0)
    cw = min(CONTENT_W, w - x - 2)
    if w >= x + CONTENT_W + 4 + art_w + 2 and h - 4 >= art_h:
        region_x = x + cw + 4
        ax = region_x + (w - 2 - region_x - art_w) // 2
        ay = 2 + (h - 4 - art_h) // 2
        draw_art(win, ay, ax, view, tick)

    y, rows = 6, h - 8   # content may use rows 6 .. h-3
    if view == "about":
        draw_about(win, y, x, cw)
    elif view == "projects":
        draw_projects(win, y, x, cw, rows)
    elif view == "contact":
        draw_contact(win, y, x, cw, rows)


def draw_about(win, y, x, cw):
    label_w = 11
    rows = []
    for label, value in ABOUT_FACTS:
        for i, part in enumerate(textwrap.wrap(value, cw - 4 - label_w) or [""]):
            rows.append((label if i == 0 else "", part, label == "Name"))
    draw_box(win, y, x, cw, len(rows) + 2, "PROFILE")
    for i, (label, value, strong) in enumerate(rows):
        put(win, y + 1 + i, x + 2, label, style(MUTED))
        put(win, y + 1 + i, x + 2 + label_w, value,
            style(BRIGHT, bold=True) if strong else style(TEXT))
    y += len(rows) + 3

    for heading, items in ABOUT_GROUPS:
        put(win, y, x + 2, heading, style(BRIGHT, bold=True))
        y += 1
        for item in items:
            put_runs(win, y, x + 2, [("• ", style(FAINT)), (item, style(TEXT))])
            y += 1
        y += 1


def project_body(project):
    body = [[(line, style(TEXT))] for line in project["about"]]
    if project.get("stack"):
        body.append([("Stack  ", style(MUTED)), (project["stack"], style(TEXT))])
    if project.get("link"):
        body.append([("Link   ", style(MUTED)), (project["link"], style(ACCENT))])
    return body


def draw_projects(win, y, x, cw, rows):
    bodies = [project_body(p) for p in PROJECTS]
    needed = sum(len(b) + 3 for b in bodies) + len(PROJECTS) - 1
    gap = 1 if needed <= rows else 0
    for project, body in zip(PROJECTS, bodies):
        bh = len(body) + 3
        draw_box(win, y, x, cw, bh)
        put(win, y + 1, x + 2, project["title"], style(BRIGHT, bold=True))
        status = project["status"].capitalize()
        dot = style(ACCENT) if project["status"] == "LIVE" else style(FAINT)
        put_runs(win, y + 1, x + cw - 4 - len(status), [("● ", dot), (status, style(MUTED))])
        for i, runs in enumerate(body):
            put_runs(win, y + 2 + i, x + 2, runs)
        y += bh + gap


def draw_contact(win, y, x, cw, rows):
    head, sep, tail = CONTACT_INTRO[0].partition(" — ")
    put_runs(win, y, x + 2, [(head, style(BRIGHT, bold=True)), (sep + tail, style(TEXT))])
    for line in CONTACT_INTRO[1:]:
        y += 1
        put(win, y, x + 2, line, style(TEXT))
    y += 2

    needed = len(CONTACT_INTRO) + 1 + len(CONTACTS) * 4 - 1
    gap = 1 if needed <= rows else 0
    for label, value in CONTACTS:
        draw_box(win, y, x, cw, 3, label)
        if value.startswith("ssh "):
            put_runs(win, y + 1, x + 2, [("$ ", style(FAINT)), (value, style(ACCENT))])
        else:
            put(win, y + 1, x + 2, value, style(BRIGHT))
        y += 3 + gap


# ─── ascii art ──────────────────────────────────────────────────────────────

def overlay(win, y, x, lines, needle, attr):
    for i, line in enumerate(lines):
        col = line.find(needle)
        while col != -1:
            put(win, y + i, x + col, needle, attr)
            col = line.find(needle, col + len(needle))


def draw_art(win, y, x, view, tick):
    art = ART[view]
    lines = art["lines"]
    frame, text = style(MUTED), style(TEXT)

    def attr_at(i, ch):
        return text if ch.isalnum() else frame

    for i, line in enumerate(lines):
        put_by_char(win, y + i, x, line, attr_at)
    for needle in ART_HIGHLIGHTS.get(view, []):
        overlay(win, y, x, lines, needle, style(BRIGHT, bold=True))

    if view == "about":  # the little screen gets a blinking cursor
        prompt = "C:\\> "
        for i, line in enumerate(lines):
            col = line.find(prompt + "_")
            if col != -1:
                put(win, y + i, x + col, prompt, style(ACCENT, bold=True))
                put(win, y + i, x + col + len(prompt), "_" if tick % 2 == 0 else " ",
                    style(ACCENT, bold=True))

    if art["caption"]:
        width = max(len(line) for line in lines)
        caption = ">> " + art["caption"]
        put(win, y + len(lines) + 1, x + (width - len(caption)) // 2, caption, style(FAINT))


# ─── splash & main loop ─────────────────────────────────────────────────────

def splash(win):
    """Typed-out ssh command and a short loading line; any key skips it."""
    win.nodelay(True)
    try:
        h, w = win.getmaxyx()
        cmd = "ssh portfolio@artjomjapins.site"
        width = len(cmd) + 3
        x = max(0, (w - width) // 2)
        y = max(0, h // 2 - 1)

        for i in range(len(cmd) + 1):
            win.erase()
            put(win, y, x, "$ ", style(ACCENT, bold=True))
            put(win, y, x + 2, cmd[:i], style(BRIGHT))
            put(win, y, x + 2 + i, "█", style(TEXT))
            win.refresh()
            if win.getch() != -1:
                return
            time.sleep(0.018)
        put(win, y, x + 2 + len(cmd), " ")

        steps = 24
        for s in range(steps + 1):
            put(win, y + 2, x, "─" * width, style(FAINT))
            put(win, y + 2, x, "─" * (width * s // steps), style(ACCENT))
            win.refresh()
            if win.getch() != -1:
                return
            time.sleep(0.015)
        time.sleep(0.15)
    finally:
        win.nodelay(False)


def read_key(win):
    """getch, but also decode arrow keys that arrive as raw escape sequences.

    Some terminals ignore keypad mode and send ESC [ B instead of ESC O B;
    curses would hand that over as Esc, which here means "go back".
    """
    key = win.getch()
    if key != 27:
        return key
    win.timeout(0)
    try:
        nxt = win.getch()
        if nxt not in (ord("["), ord("O")):
            if nxt != -1:
                curses.ungetch(nxt)
            return 27
        while True:  # swallow the rest of the sequence up to its final byte
            final = win.getch()
            if final == -1:
                return -1
            if 0x40 <= final <= 0x7E:
                return ARROWS.get(final, -1)
    finally:
        win.timeout(TICK_MS)


def render(win, view, selected, tick):
    win.erase()
    h, w = win.getmaxyx()
    if w < MIN_W or h < MIN_H:
        draw_too_small(win)
    else:
        draw_header(win, view)
        if view == "home":
            draw_home(win, selected)
        else:
            draw_section(win, view, tick)
        draw_footer(win, view)
    win.refresh()


def main(stdscr):
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    stdscr.keypad(True)
    init_colors()
    started = time.time()
    splash(stdscr)
    stdscr.timeout(TICK_MS)

    view, selected = "home", 0
    while True:
        tick = int((time.time() - started) * 1000) // TICK_MS
        render(stdscr, view, selected, tick)
        key = read_key(stdscr)
        if key in (-1, curses.KEY_RESIZE):
            continue
        if view == "home":
            if key in (curses.KEY_UP, ord("k")):
                selected = (selected - 1) % len(MENU_ITEMS)
            elif key in (curses.KEY_DOWN, ord("j")):
                selected = (selected + 1) % len(MENU_ITEMS)
            elif key in OPEN_KEYS:
                view = MENU_ITEMS[selected][0]
            elif key in (ord("q"), ord("Q")):
                break
        elif key in BACK_KEYS:
            view = "home"


if __name__ == "__main__":
    os.environ.setdefault("ESCDELAY", "25")  # make Esc respond instantly
    try:
        locale.setlocale(locale.LC_ALL, "")
    except locale.Error:
        pass
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
