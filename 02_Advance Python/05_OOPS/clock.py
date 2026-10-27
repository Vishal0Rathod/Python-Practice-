import tkinter as tk
import math
from datetime import datetime

WIDTH = 400
HEIGHT = 440
CENTER_X = WIDTH // 2
CENTER_Y = 210
RADIUS = 160

root = tk.Tk()
root.title("Analog Wall Clock")
root.resizable(False, False)
root.configure(bg="#f3eee4")

canvas = tk.Canvas(
    root, width=WIDTH, height=HEIGHT,
    bg="#f3eee4", highlightthickness=0
)
canvas.pack()

def draw_clock():
    canvas.delete("all")

    # Outer frame and clock face
    canvas.create_oval(
        CENTER_X - RADIUS - 8, CENTER_Y - RADIUS - 8,
        CENTER_X + RADIUS + 8, CENTER_Y + RADIUS + 8,
        fill="#292929", outline="#111111", width=3
    )
    canvas.create_oval(
        CENTER_X - RADIUS, CENTER_Y - RADIUS,
        CENTER_X + RADIUS, CENTER_Y + RADIUS,
        fill="#fffdf7", outline="#d6cfc2", width=2
    )

    # Tick marks and numerals
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        outer = RADIUS - 12
        inner = outer - (18 if i % 5 == 0 else 7)

        x1 = CENTER_X + outer * math.cos(angle)
        y1 = CENTER_Y + outer * math.sin(angle)
        x2 = CENTER_X + inner * math.cos(angle)
        y2 = CENTER_Y + inner * math.sin(angle)

        canvas.create_line(
            x1, y1, x2, y2,
            fill="#292929",
            width=3 if i % 5 == 0 else 1
        )

    for number in range(1, 13):
        angle = math.radians(number * 30 - 90)
        distance = RADIUS - 42
        x = CENTER_X + distance * math.cos(angle)
        y = CENTER_Y + distance * math.sin(angle)
        canvas.create_text(
            x, y, text=str(number),
            fill="#222222", font=("Helvetica", 16, "bold")
        )

    now = datetime.now()
    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + seconds / 60
    hours = (now.hour % 12) + minutes / 60

    def hand(angle_degrees, length, color, width):
        angle = math.radians(angle_degrees - 90)
        x = CENTER_X + length * math.cos(angle)
        y = CENTER_Y + length * math.sin(angle)
        canvas.create_line(
            CENTER_X, CENTER_Y, x, y,
            fill=color, width=width, capstyle=tk.ROUND
        )

    # Smoothly moving hands
    hand(hours * 30, RADIUS * 0.48, "#222222", 7)
    hand(minutes * 6, RADIUS * 0.70, "#333333", 4)
    hand(seconds * 6, RADIUS * 0.79, "#c0392b", 2)

    # Center pin
    canvas.create_oval(
        CENTER_X - 7, CENTER_Y - 7,
        CENTER_X + 7, CENTER_Y + 7,
        fill="#c0392b", outline="#c0392b"
    )

    # Digital date and time beneath the clock face
    canvas.create_text(
        CENTER_X, 395,
        text=now.strftime("%A, %d %B %Y"),
        fill="#4d4942", font=("Helvetica", 10)
    )

    root.after(50, draw_clock)

draw_clock()
root.mainloop()
