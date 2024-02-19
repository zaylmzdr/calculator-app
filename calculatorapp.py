from tkinter import *

root = Tk()
root.title("Simple Calculator")


frame = Frame(root,padx=20, pady=20, bg="Lightgrey")
frame.pack()

e = Entry(frame, width=20,borderwidth=5,font=("Arial",20))
e.grid(row=0, column =0, columnspan=4, padx=10, pady=10,sticky="ew")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

  
def button_clear():
    e.delete(0, END)

def button_add():
    global f_num
    global sembol
    first_number = e.get()
    f_num = int(first_number)
    sembol = "+"
    e.delete(0, END)

def button_division():
    global f_num
    global sembol
    first_number = e.get()
    f_num = int(first_number)
    sembol = "/"
    e.delete(0, END)

def button_sub():
    global f_num
    global sembol
    first_number = e.get()
    f_num = int(first_number)
    sembol = "-"
    e.delete(0, END)

def button_multiple():
    global f_num
    global sembol
    first_number = e.get()
    f_num = int(first_number)
    sembol = "x"
    e.delete(0, END)


def button_equal():
    global f_num
    global sembol
    second_number = e.get()
    e.delete(0, END)
    try:
        if sembol == "+":
            e.insert(0, f_num + int(second_number))
        elif sembol == "/":
            sonuc = f_num / int(second_number)
            e.insert(0, sonuc)
        elif sembol == "-":
            sonuc = f_num - int(second_number)
            e.insert(0, sonuc)
        elif sembol == "x":
            sonuc = f_num * int(second_number)
            e.insert(0, sonuc)
    except ValueError:
        e.insert(0, "Error")
    except ZeroDivisionError:
        e.insert(0, "Cannot divide by zero!")


#define buttons
button_1 = Button(frame, text="1", padx=40, pady=20, command= lambda: button_click(1),bg="lightblue", fg="black", font=("Arial", 16))
button_2 = Button(frame, text="2", padx=40, pady=20, command= lambda: button_click(2),bg="lightblue", fg="black", font=("Arial", 16))
button_3 = Button(frame, text="3", padx=40, pady=20, command= lambda: button_click(3),bg="lightblue", fg="black", font=("Arial", 16))
button_4 = Button(frame, text="4", padx=40, pady=20, command= lambda: button_click(4),bg="lightblue", fg="black", font=("Arial", 16))
button_5 = Button(frame, text="5", padx=40, pady=20, command= lambda: button_click(5),bg="lightblue", fg="black", font=("Arial", 16))
button_6 = Button(frame, text="6", padx=40, pady=20, command= lambda: button_click(6),bg="lightblue", fg="black", font=("Arial", 16))
button_7 = Button(frame, text="7", padx=40, pady=20, command= lambda:  button_click(7),bg="lightblue", fg="black", font=("Arial", 16))
button_8 = Button(frame, text="8", padx=40, pady=20, command= lambda: button_click(8),bg="lightblue", fg="black", font=("Arial", 16))
button_9 = Button(frame, text="9", padx=40, pady=20, command= lambda: button_click(9),bg="lightblue", fg="black", font=("Arial", 16))
button_0 = Button(frame, text="0", padx=40, pady=20,command= lambda: button_click(0),bg="lightblue", fg="black", font=("Arial", 16))

button_add = Button(frame, text="+", padx=60, pady=20,bg="grey", fg="white", font=("Arial", 16),command=button_add)
button_equal = Button(frame, text="=", padx=40, pady=20,bg="orange", fg="white", font=("Arial", 16),command= button_equal)
button_division = Button(frame, text="/", padx=60, pady=20, bg="grey", fg="white", font=("Arial", 16),command= button_division)
button_sub = Button(frame, text="-", padx=60, pady=20,bg="grey", fg="white", font=("Arial", 16),command=button_sub)
button_multiple = Button(frame, text="x", padx=60, pady=20, bg="grey", fg="white", font=("Arial", 16),command= button_multiple)
button_clear = Button(frame, text="C", padx=40 , pady=20, bg="red", fg="white", font=("Arial", 16),command= button_clear)



button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=1)

button_clear.grid(row=4,column=0,padx=5, pady=5, sticky="ew")

button_add.grid(row=4,column=3,padx=5,pady=5, sticky="ew")
button_equal.grid(row=4,column=2,padx=5,pady=5, sticky="ew")
button_division.grid(row=1,column=3,padx=5,pady=5, sticky="ew")
button_sub.grid(row=2,column=3,padx=5,pady=5, sticky="ew")
button_multiple.grid(row=3,column=3,padx=5,pady=5, sticky="ew")


mainloop()