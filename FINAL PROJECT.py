from tkinter import *
from time import strftime

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("Error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("Arithmetic Error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""

#clock func
def time():
    string = strftime("%I:%M:%S %p")
    my_label.config(text=string)
    my_label.after(1000, time)

#painting window
def open2():
    window3=Toplevel()
    window3.title("PAINTING")
    window3.geometry("500x500",)
    window3.config(bg='#67595E')

    current_x, current_y = 0, 0

    def xy_pos(event):
        global current_x, current_y
        current_x, current_y = event.x, event.y

    def draw_line(event):
        global current_x, current_y
        canvas.create_line(current_x, current_y, event.x, event.y)
        current_x, current_y = event.x, event.y

    def clear_paint():
        canvas.delete('CLear Everything')

    window3.rowconfigure(0, weight=1)
    window3.columnconfigure(0, weight=1)

    Menubar = Menu(window3)
    window3.config(menu=Menubar)
    Menubar.add_command(label="Clear Everything", command=clear_paint)

    canvas = Canvas(window3)
    canvas.grid(row=0, column=0, sticky="nswe")
    canvas.bind("<Button-1>", xy_pos)
    canvas.bind("<B1-Motion>", draw_line)

    window3.mainloop()

#main window
window = Tk()
window.title("Rainbow Calculator")
window.geometry("500x750")
window.config(bg='#67595E')

equation_text = ""

equation_label = StringVar()

Label1 = Label(window, textvariable=equation_label, font=('consolas',20), background="#FFFFFF", width=20, height=2)
Label1.pack()

#create frame
frame = Frame(window)
frame.pack()

#Buttons
button1 = Button(frame, text=1, height=2, width=7, font=35, command=lambda: button_press(1))
button2 = Button(frame, text=2, height=2, width=7, font=35, command=lambda: button_press(2))
button3 = Button(frame, text=3, height=2, width=7, font=35, command=lambda: button_press(3))
button4 = Button(frame, text=4, height=2, width=7, font=35, command=lambda: button_press(4))
button5 = Button(frame, text=5, height=2, width=7, font=35, command=lambda: button_press(5))
button6 = Button(frame, text=6, height=2, width=7, font=35, command=lambda: button_press(6))
button7 = Button(frame, text=7, height=2, width=7, font=35, command=lambda: button_press(7))
button8 = Button(frame, text=8, height=2, width=7, font=35, command=lambda: button_press(8))
button9 = Button(frame, text=9, height=2, width=7, font=35, command=lambda: button_press(9))
button0 = Button(frame, text=0, height=2, width=7, font=35, command=lambda: button_press(0))

#buttons grid
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=3, column=0)

#create operators buttons
plus = Button(frame, text='+', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('+'))
minus = Button(frame, text='-', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('-'))
multiply = Button(frame, text='~', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('~'))
divide = Button(frame, text='/', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('/'))
modulus = Button(frame, text='%', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('%'))
double_div = Button(frame, text='//', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('//'))
bitewise_ope = Button(frame, text='&', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('&'))
bitewise_or = Button(frame, text='|', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('|'))
XOR = Button(frame, text='^', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('^'))
right_shift = Button(frame, text='>>', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('>>'))
left_shift = Button(frame, text='<<', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('<<'))
exponent_ass = Button(frame, text='*', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('*'))
decimal = Button(frame, text='.', height=2, width=7, font=35, bg="#B99095", command=lambda: button_press('.'))
equal = Button(frame, text='=', height=2, width=7, font=35, bg="#B99095", command=equals)

#operators grid
plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
multiply.grid(row=2, column=3)
divide.grid(row=3, column=3)
modulus.grid(row=3, column=1)
double_div.grid(row=3, column=2)
bitewise_ope.grid(row=4, column=0)
bitewise_or.grid(row=4, column=1)
XOR.grid(row=4, column=2)
right_shift.grid(row=4, column=3)
left_shift.grid(row=5, column=0)
exponent_ass.grid(row=5, column=1)
decimal.grid(row=5, column=2)
equal.grid(row=5, column=3)

#clear button
clear = Button(window, text='Delete', height=2, width=20, font=35, bg="#E8B4B8", command=clear)
clear.pack()

#create button to open other window
btnOpen2 = Button(window,text="Open Painting", bg="#EED6D3", command=open2).pack(pady=10)


#clock label
my_label = Label(window, font=("ds-digital", 50), background="#67595E", foreground="#F9F1F0", width=25, height=2)
my_label.pack()
time()

window.mainloop()