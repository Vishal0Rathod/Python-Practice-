
import tkinter as tk
import math
import random
from datetime import datetime

WIDTH, HEIGHT = 460, 520
CX, CY = 230, 235
RADIUS = 155

BG = "#08050d"
ORANGE = "#ff7518"
GLOW = "#ff3900"
PURPLE = "#6826a0"
RED = "#e00025"
WHITE = "#fff0d5"

root = tk.Tk()
root.title("🎃 The Haunted Clock")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.configure(bg=BG)

canvas = tk.Canvas(
    root, width=WIDTH, height=HEIGHT,
    bg=BG, highlightthickness=0
)
canvas.pack()

random.seed(42)

# Fixed floating sparks
sparks = [
    (random.randint(10, WIDTH - 10),
     random.randint(10, HEIGHT - 10),
     random.choice([2, 3, 4]))
    for _ in range(65)
]


def glow_circle(x, y, radius, colors):
    """Layered circles create a soft neon-like glow."""
    for i, color in enumerate(colors):
        r = radius * (1 - i / len(colors))
        canvas.create_oval(
            x-r, y-r, x+r, y+r,
            fill=color, outline=""
        )


def draw_pumpkin(x, y, size):
    # Warm glow behind the lantern
    glow_circle(
        x, y, size * 1.65,
        ["#29100d", "#3b170b", "#54200a", "#6a2808"]
    )

    # Pumpkin body
    canvas.create_oval(
        x-size*0.75, y-size*0.48,
        x+size*0.75, y+size*0.48,
        fill="#d94b08", outline="#ff8c16", width=2
    )

    # Pumpkin ridges
    for offset in [-0.4, -0.2, 0.2, 0.4]:
        canvas.create_arc(
            x-size*0.72, y-size*0.46,
            x+size*0.72, y+size*0.46,
            start=70 if offset > 0 else 110,
            extent=180,
            style=tk.ARC,
            outline="#923006",
            width=2
        )
        break

    # Stem
    canvas.create_polygon(
        x-size*0.12, y-size*0.42,
        x-size*0.08, y-size*0.68,
        x+size*0.10, y-size*0.72,
        x+size*0.16, y-size*0.40,
        fill="#46601b", outline="#758a2e"
    )

    # Glowing triangular eyes
    eye_y = y - size*0.12
    eye_size = size*0.19

    for direction in [-1, 1]:
        ex = x + direction * size*0.32
        canvas.create_polygon(
            ex-eye_size, eye_y-eye_size*0.55,
            ex+eye_size, eye_y-eye_size*0.35,
            ex, eye_y+eye_size,
            fill="#fff39a", outline="#ffdd45", width=1
        )

    # Nose
    canvas.create_polygon(
        x, y-size*0.02,
        x-size*0.10, y+size*0.14,
        x+size*0.10, y+size*0.14,
        fill="#ffed86", outline=""
    )

    # Jagged glowing grin
    canvas.create_polygon(
        x-size*0.43, y+size*0.18,
        x-size*0.28, y+size*0.24,
        x-size*0.18, y+size*0.19,
        x-size*0.06, y+size*0.29,
        x+size*0.08, y+size*0.20,
        x+size*0.20, y+size*0.27,
        x+size*0.42, y+size*0.16,
        x+size*0.34, y+size*0.39,
        x-size*0.32, y+size*0.39,
        fill="#fff19a", outline="#ffca37", width=1
    )

    # Dark mouth gaps
    for dx in [-0.2, 0, 0.2]:
        canvas.create_polygon(
            x+size*dx, y+size*0.25,
            x+size*(dx+0.06), y+size*0.34,
            x+size*(dx+0.12), y+size*0.25,
            fill="#32100a", outline=""
        )


def draw_web(x, y, size):
    for i in range(7):
        angle = math.radians(i * 30)
        canvas.create_line(
            x, y,
            x + size*math.cos(angle),
            y + size*math.sin(angle),
            fill="#432454", width=1
        )

    for ring in range(1, 5):
        points = []
        distance = size * ring / 4

        for i in range(13):
            angle = math.radians(i * 30)
            points.extend([
                x + distance*math.cos(angle),
                y + distance*math.sin(angle)
            ])

        canvas.create_line(
            *points, fill="#432454", width=1
        )


def draw_bat(x, y, scale):
    points = [
        x, y,
        x-8*scale, y-7*scale,
        x-7*scale, y+2*scale,
        x-17*scale, y-4*scale,
        x-13*scale, y+8*scale,
        x, y+5*scale,
        x+13*scale, y+8*scale,
        x+17*scale, y-4*scale,
        x+7*scale, y+2*scale,
        x+8*scale, y-7*scale
    ]
    canvas.create_polygon(
        points, fill="#030207", outline="#50275f"
    )


def draw_clock():
    canvas.delete("all")

    # Background haze
    glow_circle(
        230, 235, 225,
        ["#100718", "#130817", "#170b17", "#1b0c16"]
    )

    # Pumpkin lanterns behind the clock
    draw_pumpkin(75, 385, 43)
    draw_pumpkin(385, 390, 40)

    # Floating embers
    for x, y, size in sparks:
        canvas.create_oval(
            x-size, y-size, x+size, y+size,
            fill=random.choice([ORANGE, "#8b2c14", "#ffbd45"]),
            outline=""
        )

    draw_bat(70, 75, 1.0)
    draw_bat(370, 90, 0.8)
    draw_bat(390, 290, 0.6)

    # Clock's outer glow
    glow_circle(
        CX, CY, RADIUS+24,
        ["#24102d", "#321323", "#481713", "#58200e"]
    )

    # Dark metal frame
    canvas.create_oval(
        CX-RADIUS-9, CY-RADIUS-9,
        CX+RADIUS+9, CY+RADIUS+9,
        fill="#09070d", outline=RED, width=3
    )

    canvas.create_oval(
        CX-RADIUS, CY-RADIUS,
        CX+RADIUS, CY+RADIUS,
        fill="#18121d", outline=ORANGE, width=2
    )

    # Clock face details
    draw_web(CX-70, CY-60, 40)
    draw_web(CX+65, CY+65, 34)

    # Blood drips
    for x, length in [(CX-60, 12), (CX-38, 7),
                      (CX+35, 15), (CX+58, 9)]:
        canvas.create_line(
            x, CY-RADIUS+2,
            x, CY-RADIUS+length,
            fill=RED, width=3
        )

    # Minute marks
    for i in range(60):
        angle = math.radians(i*6-90)
        outer = RADIUS-12
        inner = outer-(15 if i % 5 == 0 else 6)

        canvas.create_line(
            CX+outer*math.cos(angle),
            CY+outer*math.sin(angle),
            CX+inner*math.cos(angle),
            CY+inner*math.sin(angle),
            fill=ORANGE if i % 5 == 0 else "#a99aa7",
            width=3 if i % 5 == 0 else 1
        )

    # Roman numerals
    numerals = [
        "XII", "I", "II", "III", "IV", "V",
        "VI", "VII", "VIII", "IX", "X", "XI"
    ]

    for i, numeral in enumerate(numerals):
        angle = math.radians(i*30-90)
        distance = RADIUS-40

        canvas.create_text(
            CX+distance*math.cos(angle),
            CY+distance*math.sin(angle),
            text=numeral,
            fill=ORANGE if i % 3 == 0 else WHITE,
            font=("Times", 13, "bold")
        )

    # Current time
    now = datetime.now()
    sec = now.second + now.microsecond/1_000_000
    minute = now.minute + sec/60
    hour = (now.hour % 12) + minute/60

    def hand(value, divisions, length, color, width):
        angle = math.radians(value*360/divisions-90)
        x = CX + length*math.cos(angle)
        y = CY + length*math.sin(angle)

        canvas.create_line(
            CX, CY, x, y,
            fill=color, width=width,
            capstyle=tk.ROUND
        )

    hand(hour, 12, 76, WHITE, 7)
    hand(minute, 60, 112, ORANGE, 4)
    hand(sec, 60, 132, RED, 2)

    # Glowing centre pin
    glow_circle(CX, CY, 15, ["#451019", "#9d1324", RED])
    canvas.create_oval(
        CX-5, CY-5, CX+5, CY+5,
        fill="#fff0c0", outline=ORANGE
    )

    # Footer
    canvas.create_text(
        CX, 438,
        text="THE WITCHING HOUR",
        fill=ORANGE,
        font=("Times", 14, "bold")
    )

    canvas.create_text(
        CX, 461,
        text=now.strftime("%I:%M:%S %p  |  %d %b %Y"),
        fill=WHITE,
        font=("Courier", 10)
    )

    canvas.create_text(
        CX, 492,
        text="TRICK OR TIME 🎃",
        fill="#8e5ca8",
        font=("Times", 10, "italic")
    )

    # Keep the clock running
    root.after(100, draw_clock)


draw_clock()
root.mainloop()
