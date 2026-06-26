#!/usr/bin/env python3
import curses
import time

ASCII_ART = [
    'OZZZmmmwwmmmmmwmmZOOO000QQQLCJJJJJJUYYYXzzzccvvu',
    'wwqqqppqpqqwqwqqwmmZZZO0000LQLLLCCJUJYYYXXccccvv',
    'ao*oaooaaoaaaahhkkkhaohbdpdpqmmmOQQQQLJJJUYXzzcc',
    'ao*o**oooooahao##*hmJvxnftjCOOmOO0QQQCJJUUUYXzcc',
    "a##M####**oa#*pQx[!' : .   .:~[{n0OQQCJJJUYXzXzv",
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

SECTIONS = {
    "about": {
        "title": "ABOUT ME",
        "lines": [
            "  My name:   Artjom Japins",
            "  Location:   United Kingdom",
            "  Reason   Passion for building things that have a combination of design and creativity."
            "",
            "",
            "",
            "Focused on:",
            "• Creating new projects as a hobby",
            "• Cloud infrastructure",
            "• Design systems",
            "• Interactive experiences",
            "",
            "",
            "Current goals:",
            "Finish some of the incomplete projects i have been working on."
            "Expand my knowledge"
        ]
    },
    "projects": {
        "title": "PROJECTS",
        "lines": [
            "01  Terminal Portfolio",
            "",
            "Interactive SSH portfolio.",
            "Hosted on Oracle Cloud.",
            "Python + curses.",
            "",
            "02  Upcoming Projects",
            "",
            "More tools and experiments",
            "currently in development."
        ]
    },
    "skills": {
        "title": "SKILLS",
        "lines": [
            "Languages",
            "Python · JavaScript · Bash",
            "",
            "Frontend",
            "HTML · CSS · UI Design",
            "",
            "Backend",
            "APIs · Linux · Nginx",
            "",
            "Infrastructure",
            "Oracle Cloud · SSH"
        ]
    },
    "contact": {
        "title": "CONTACT",
        "lines": [
            "Email",
            "hello@artjomjapins.site",
            "",
            "Website",
            "artjomjapins.site",
            "",
            "SSH",
            "ssh portfolio@artjomjapins.site"
        ]
    }
}

C_TEXT      = 1
C_TITLE     = 2
C_ACCENT    = 3
C_DIM       = 4
C_SELECTED  = 5
C_ASCII     = 6
C_PANEL     = 7
C_HIGHLIGHT = 8

def init_colors():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(C_TEXT,      15,  -1)
    curses.init_pair(C_TITLE,      7,  -1)
    curses.init_pair(C_ACCENT,   215,  -1)
    curses.init_pair(C_DIM,      245,  -1)
    curses.init_pair(C_SELECTED,   0, 215)
    curses.init_pair(C_ASCII,    252,  -1)
    curses.init_pair(C_PANEL,    244,  -1)
    curses.init_pair(C_HIGHLIGHT,223,  -1)

def safe_add(win, y, x, text, attr=0):
    h, w = win.getmaxyx()
    if y < 0 or y >= h:
        return
    if x < 0 or x >= w:
        return
    text = text[:max(0, w - x)]
    try:
        win.addstr(y, x, text, attr)
    except:
        pass

def draw_box(stdscr, y, x, width, height, title=None):
    safe_add(stdscr, y, x, "┌" + "─"*(width-2) + "┐", curses.color_pair(C_PANEL))
    for i in range(1, height - 1):
        safe_add(stdscr, y+i, x,          "│", curses.color_pair(C_PANEL))
        safe_add(stdscr, y+i, x+width-1,  "│", curses.color_pair(C_PANEL))
    safe_add(stdscr, y+height-1, x, "└" + "─"*(width-2) + "┘", curses.color_pair(C_PANEL))
    if title:
        safe_add(stdscr, y, x + 2, f" {title} ", curses.color_pair(C_ACCENT) | curses.A_BOLD)

def draw_home(stdscr, selected):
    stdscr.erase()
    h, w = stdscr.getmaxyx()

    start_x_left  = 2
    start_x_right = 60
    start_y = max(1, (h - len(ASCII_ART)) // 2)

    # ── ASCII art ────────────────────────────────────────────────────────
    for i, line in enumerate(ASCII_ART):
        safe_add(stdscr, start_y + i, start_x_left, line, curses.color_pair(C_ASCII))

    y = start_y

    # ── Big block name ───────────────────────────────────────────────────
    for line in BIG_NAME:
        safe_add(stdscr, y, start_x_right, line, curses.color_pair(C_TITLE) | curses.A_BOLD)
        y += 1

    y += 1

    safe_add(stdscr, y, start_x_right,
             "CREATIVE DESIGNER • DIGITAL BUILDER",
             curses.color_pair(C_ACCENT) | curses.A_BOLD)
    y += 2

    safe_add(stdscr, y, start_x_right,
             "Building interfaces, tools and systems",
             curses.color_pair(C_TEXT))
    y += 1
    safe_add(stdscr, y, start_x_right,
             "that merge design and aesthetic.",
             curses.color_pair(C_TEXT))
    y += 2

    # thin divider
    divider_len = 54
    safe_add(stdscr, y, start_x_right,
             "·" * divider_len,
             curses.color_pair(C_DIM))
    y += 2

    # ── Menu items ───────────────────────────────────────────────────────
    # Fixed menu width: longest label is "Projects" = 8 chars
    # Box inner content: "> Projects" = 10 chars, pad 1 each side = 12 inner
    # Total box width = 12 + 2 (borders) = 14, plus 2 leading spaces = 16 total render width
    MENU_BOX_INNER_W = 14   # fixed inner width for all items ("> About Me  " padded to 12 + 2 spaces)
    menu_col      = start_x_right
    start_menu_y  = y

    for idx, (_, label) in enumerate(MENU_ITEMS):
        row = start_menu_y + idx * 3

        if idx == selected:
            arrow_label = f"> {label}"
            # pad to fixed width so box is always the same size
            padded = arrow_label.ljust(MENU_BOX_INNER_W)
            top    = "┌" + "─" * (MENU_BOX_INNER_W + 2) + "┐"
            mid    = "│ " + padded + " │"
            bot    = "└" + "─" * (MENU_BOX_INNER_W + 2) + "┘"
            safe_add(stdscr, row,     menu_col, top, curses.color_pair(C_ACCENT))
            safe_add(stdscr, row + 1, menu_col, mid, curses.color_pair(C_SELECTED) | curses.A_BOLD)
            safe_add(stdscr, row + 2, menu_col, bot, curses.color_pair(C_ACCENT))
        else:
            # indent to visually align with the box content (border + space = 2 chars offset)
            safe_add(stdscr, row + 1, menu_col + 2,
                     label.ljust(MENU_BOX_INNER_W),
                     curses.color_pair(C_ACCENT))

    # ── Info boxes (right of menu) ───────────────────────────────────────
    # Place them right after the menu block (fixed box width = MENU_BOX_INNER_W + 4)
    menu_block_w = MENU_BOX_INNER_W + 4   # borders + spaces
    box_col   = menu_col + menu_block_w + 2
    box_width = 28

    current_inner = ["Learning:", "• Cloud Infrastructure", "• Backend Systems", "• UI Engineering"]
    current_box_h = len(current_inner) + 2
    draw_box(stdscr, start_menu_y, box_col, box_width, current_box_h, "CURRENT")
    safe_add(stdscr, start_menu_y + 1, box_col + 2, "Learning:",              curses.color_pair(C_HIGHLIGHT))
    safe_add(stdscr, start_menu_y + 2, box_col + 2, "• Website Programming", curses.color_pair(C_TEXT))
    safe_add(stdscr, start_menu_y + 3, box_col + 2, "• Swift",      curses.color_pair(C_TEXT))
    safe_add(stdscr, start_menu_y + 4, box_col + 2, "• Soldering Components",       curses.color_pair(C_TEXT))

    links_top   = start_menu_y + current_box_h + 1
    links_box_h = 4
    draw_box(stdscr, links_top, box_col, box_width, links_box_h, "LINKS")
    safe_add(stdscr, links_top + 1, box_col + 2, "artjomjapins.site",      curses.color_pair(C_ACCENT))
    safe_add(stdscr, links_top + 2, box_col + 2, "github.com/zxrk", curses.color_pair(C_TEXT))

    # ── Footer ───────────────────────────────────────────────────────────
    footer_left  = "[ ↑ ↓ navigate ]  [ enter open ]  [ q quit ]"
    footer_right = "v2.0 • handcrafted terminal portfolio"
    safe_add(stdscr, h - 2, 2,              footer_left,  curses.color_pair(C_DIM))
    safe_add(stdscr, h - 2, w - len(footer_right) - 2,
             footer_right, curses.color_pair(C_DIM))

    stdscr.refresh()


def draw_section(stdscr, key):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    data = SECTIONS[key]
    safe_add(stdscr, 2, 4, data["title"], curses.color_pair(C_ACCENT) | curses.A_BOLD)
    safe_add(stdscr, 3, 4, "─" * (w - 8), curses.color_pair(C_PANEL))
    y = 5
    for line in data["lines"]:
        safe_add(stdscr, y, 4, line, curses.color_pair(C_TEXT))
        y += 1
    safe_add(stdscr, h - 2, 4, "[ backspace ] return", curses.color_pair(C_DIM))
    stdscr.refresh()


def splash(stdscr):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    msg = "ssh portfolio@artjomjapins.site"
    x = (w - len(msg)) // 2
    y = h // 2
    for i, ch in enumerate(msg):
        safe_add(stdscr, y, x + i, ch, curses.color_pair(C_ACCENT) | curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.02)
    time.sleep(0.4)


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    init_colors()
    splash(stdscr)
    selected = 0
    view = "home"
    while True:
        if view == "home":
            draw_home(stdscr, selected)
        else:
            draw_section(stdscr, view)
        key = stdscr.getch()
        if view == "home":
            if key in (curses.KEY_UP, ord("k")):
                selected = (selected - 1) % len(MENU_ITEMS)
            elif key in (curses.KEY_DOWN, ord("j")):
                selected = (selected + 1) % len(MENU_ITEMS)
            elif key in (10, 13, curses.KEY_ENTER):
                view = MENU_ITEMS[selected][0]
            elif key in (ord("q"), ord("Q")):
                break
        else:
            if key in (curses.KEY_BACKSPACE, 127, 8, ord("q"), ord("Q")):
                view = "home"


if __name__ == "__main__":
    curses.wrapper(main)
