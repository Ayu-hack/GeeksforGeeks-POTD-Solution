from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = float(height_tf.get())
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Underweight. Stay strong and consider a balanced diet!')
    elif (bmi >= 18.5) and (bmi <= 24.9):
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Normal. Great job! Keep maintaining a healthy lifestyle.')
    elif (bmi >= 25) and (bmi <= 29.9):
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Overweight. Stay active and focus on fitness.')
    elif bmi >= 30:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Obesity. Don’t worry! Take small steps towards better health.')
    else:
        messagebox.showerror('BMI Result', 'Something went wrong!')

ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x400')
ws.config(bg='#A9CCE3')
ws.resizable(False, False)

frame = Frame(ws, padx=10, pady=10, bg='#A9CCE3')
frame.pack(expand=True)

age_lb = Label(frame, text="Enter Age (2 - 120)", bg='#A9CCE3', font=('Arial', 12, 'bold'))
age_lb.grid(row=1, column=1)
age_tf = Entry(frame)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(frame, text='Select Gender', bg='#A9CCE3', font=('Arial', 12, 'bold'))
gen_lb.grid(row=2, column=1)
var = IntVar()

frame2 = Frame(frame, bg='#A9CCE3')
frame2.grid(row=2, column=2, pady=5)
male_rb = Radiobutton(frame2, text='Male', variable=var, value=1, bg='#A9CCE3')
male_rb.pack(side=LEFT)
female_rb = Radiobutton(frame2, text='Female', variable=var, value=2, bg='#A9CCE3')
female_rb.pack(side=RIGHT)

height_lb = Label(frame, text="Enter Height (m)", bg='#A9CCE3', font=('Arial', 12, 'bold'))
height_lb.grid(row=3, column=1)
height_tf = Entry(frame)
height_tf.grid(row=3, column=2, pady=5)

weight_lb = Label(frame, text="Enter Weight (kg)", bg='#A9CCE3', font=('Arial', 12, 'bold'))
weight_lb.grid(row=4, column=1)
weight_tf = Entry(frame)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(frame, bg='#A9CCE3')
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3, text='Calculate', command=calculate_bmi, font=('Arial', 10, 'bold'), bg='green', fg='white')
cal_btn.pack(side=LEFT)
reset_btn = Button(frame3, text='Reset', command=reset_entry, font=('Arial', 10, 'bold'), bg='orange', fg='white')
reset_btn.pack(side=LEFT)
exit_btn = Button(frame3, text='Exit', command=lambda: ws.destroy(), font=('Arial', 10, 'bold'), bg='red', fg='white')
exit_btn.pack(side=RIGHT)

ws.mainloop()