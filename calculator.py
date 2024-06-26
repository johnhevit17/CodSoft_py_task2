from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Calc")
frame = Frame(window, padx=10)
frame.pack()

entry = Entry(frame, relief=SUNKEN, bd=3, width=30)
entry.grid(row=0, column=0, columnspan=3)


def my_click(number):
    entry.insert(END, number)


def clear():
    entry.delete(0, END)


def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, y)
    except Exception:
        messagebox.showinfo(title="Error", message="Syntax Error")


button_1 = Button(frame, text="1", width=3, padx=15, pady=5, command=lambda: my_click(1))
button_1.grid(row=1, column=0)
button_2 = Button(frame, text="2", width=3, padx=15, pady=5, command=lambda: my_click(2))
button_2.grid(row=1, column=1)
button_3 = Button(frame, text="3", width=3, padx=15, pady=5, command=lambda: my_click(3))
button_3.grid(row=1, column=2)
button_4 = Button(frame, text="4", width=3, padx=15, pady=5, command=lambda: my_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(frame, text="5", width=3, padx=15, pady=5, command=lambda: my_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(frame, text="6", width=3, padx=15, pady=5, command=lambda: my_click(6))
button_6.grid(row=2, column=2)
button_7 = Button(frame, text="7", width=3, padx=15, pady=5, command=lambda: my_click(7))
button_7.grid(row=3, column=0)
button_8 = Button(frame, text="8", width=3, padx=15, pady=5, command=lambda: my_click(8))
button_8.grid(row=3, column=1)
button_9 = Button(frame, text="9", width=3, padx=15, pady=5, command=lambda: my_click(9))
button_9.grid(row=3, column=2)
button_0 = Button(frame, text="0", width=3, padx=15, pady=5, command=lambda: my_click(0))
button_0.grid(row=4, column=0)
button_add = Button(frame, text="+", width=3, padx=15, pady=5, command=lambda: my_click('+'))
button_add.grid(row=4, column=1)
button_sub = Button(frame, text="-", width=3, padx=15, pady=5, command=lambda: my_click('-'))
button_sub.grid(row=4, column=2)
button_multi = Button(frame, text="*", width=3, padx=15, pady=5, command=lambda: my_click('*'))
button_multi.grid(row=5, column=0)
button_div = Button(frame, text="/", width=3, padx=15, pady=5, command=lambda: my_click('/'))
button_div.grid(row=5, column=1)
button_clear = Button(frame, text="AC", width=3, padx=15, pady=5, command=clear)
button_clear.grid(row=5, column=2)
button_equal = Button(frame, text="=", width=9, padx=15, pady=5, command=equal)
button_equal.grid(row=6, column=0, columnspan=3)

window.mainloop()
