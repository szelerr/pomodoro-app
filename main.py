import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeats = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global repeats, timer
    window.after_cancel(timer)
    lbl_timer.config(text="Timer")
    lbl_checkmarks.config(text="")
    canvas.itemconfig(canvas_timer, text="00:00")
    repeats = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global repeats
    repeats += 1

    if repeats == 8:
        lbl_timer.config(text="Big Break")
        decrement_timer(LONG_BREAK_MIN * 60)
    elif repeats % 2 == 0:
        lbl_timer.config(text="Break")
        decrement_timer(SHORT_BREAK_MIN * 60)
    else:
        lbl_timer.config(text="Work")
        decrement_timer(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def decrement_timer(count):
    global repeats
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(canvas_timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, decrement_timer, count - 1)
    else:
        start_timer()
        if repeats % 2 == 0:
            lbl_checkmarks.config(text=repeats // 2 * "✔")
        if repeats % 8 == 0:
            repeats = 0
        if repeats % 9 == 1:
            lbl_checkmarks.config(text="")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)


canvas = tkinter.Canvas(width=206, height=224, bg=PINK, highlightthickness=0)

img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas_timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

lbl_timer = tkinter.Label(text="Timer", fg=GREEN, bg=PINK, font=(FONT_NAME, 36, "bold"))
lbl_timer.grid(row=0, column=1)

lbl_checkmarks = tkinter.Label(fg=GREEN, bg=PINK)
lbl_checkmarks.grid(row=3, column=1)

btn_start = tkinter.Button(text="Start", command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = tkinter.Button(text="Reset", command=reset_timer)
btn_reset.grid(row=2, column=2)




window.mainloop()
