from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60  
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
REP = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label.config(text = "Timer")
    tick.config(text = " ")
    global REP
    REP = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REP
    REP += 1
    tick.config(text="✔"*(REP//2),fg="GREEN")
    if(REP != 0 and REP % 8 == 0):
        count_down(LONG_BREAK_MIN)
        label.config(text="BREAK", fg=RED)
    elif(REP % 2 == 0):
        count_down(SHORT_BREAK_MIN)
        label.config(text="BREAK", fg=PINK)
    else:
        count_down(WORK_MIN)
        label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    global REP

    if count <= 0:
        REP += 1
        start_timer()  # Move this to the end when the timer finishes
        return

    if count_min == 0:
        count_min = "00"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    global timer
    timer = screen.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro")
screen.minsize(400,400)
screen.config(padx=100, pady=100, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
v = PhotoImage(file=r"C:\Users\Lenovo\Hacktoberfest2024_2\pomodaro_app\tomato.png")
canvas.create_image(100,112, image=v)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


label=Label(text="TIMER", fg=GREEN, font=("Arial", 35), bg=YELLOW)
label.grid(column=1, row=0)

start = Button(text="START" , command=start_timer)
start.config(padx=10,pady=10)
start.grid(column=0,row=3)

reset = Button(text="RESET", command=reset_timer)
reset.config(padx=10, pady=10)
reset.grid(column=2, row=3)

tick = Label(text="", fg=GREEN, bg=YELLOW, font=("ARIAL",20))
tick.config(padx=20,pady=20)
tick.grid(column=1, row=4)




screen.mainloop()
