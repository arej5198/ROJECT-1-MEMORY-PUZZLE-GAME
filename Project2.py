import tkinter as tk
import random

window = tk.Tk()
window.title("Memory Puzzle Game")

numbers = list(range(1,9)) * 2
random.shuffle(numbers)

buttons = []
first = None
second = None

def click(i):
    global first, second

    buttons[i]["text"] = numbers[i]

    if first is None:
        first = i
    elif second is None:
        second = i

        if numbers[first] == numbers[second]:
            first = None
            second = None
        else:
            window.after(500, hide)

def hide():
    global first, second
    buttons[first]["text"] = ""
    buttons[second]["text"] = ""
    first = None
    second = None

for i in range(16):
    btn = tk.Button(window, text="", width=10, height=4,
                    command=lambda i=i: click(i))
    btn.grid(row=i//4, column=i%4)
    buttons.append(btn)

window.mainloop()