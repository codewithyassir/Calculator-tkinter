import tkinter as tk

# Create Window
wind = tk.Tk()

# Set window configuration
wind.title("Calculator")
wind.config(bg='black')
wind.geometry("400x500")
wind.resizable(False,False)

# Title
title = tk.Label(wind,text='Calculator',font=("Arial",20), bg='#B30E0E', fg='white')
title.place(x=0,y=0, width=420, height=50)

# Entry Box
box = tk.Entry(wind, width=35,bd=1,font=("Arial",20))
box.place(x=50,y=60, width=300, height=30)


# Function for Numers Insert
def button_click(button_number):
    current_number = box.get()
    box.delete(0, tk.END)
    box.insert(0, str(current_number) + str(button_number))


# Function Clear
def button_clear():
    box.delete(0, tk.END)


# Function add
def button_add():
    first_number_str = box.get()
    global first_num
    global operation
    first_num = float(first_number_str)
    operation = "+"
    box.delete(0, tk.END)

# Function subtract
def button_subtract():
    first_number_str = box.get()
    global first_num
    global operation
    first_num = float(first_number_str)
    operation = "-"
    box.delete(0, tk.END)


# Function multiply
def button_multiply():
    first_number_str = box.get()
    global first_num
    global operation
    first_num = float(first_number_str)
    operation = "x"
    box.delete(0, tk.END)


# Function divide
def button_divide():
    first_number_str = box.get()
    global first_num
    global operation
    first_num = float(first_number_str)
    operation = "/"
    box.delete(0, tk.END)

# Function for result
def button_equal():
    second_num = box.get()
    box.delete(0, tk.END)

    if operation == "+":
        box.insert(0, first_num + float(second_num))

    elif operation == "-":
        box.insert(0, first_num - float(second_num))

    elif operation == "x":
            box.insert(0, first_num * float(second_num))

    elif operation == "/":
        box.insert(0, first_num / float(second_num))


# Define Buttons

button_1 = tk.Button(wind, text="1",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(1))
button_2 = tk.Button(wind, text="2",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(2))
button_3 = tk.Button(wind, text="3",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(3))
button_4 = tk.Button(wind, text="4",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(4))
button_5 = tk.Button(wind, text="5",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(5))
button_6 = tk.Button(wind, text="6",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(6))
button_7 = tk.Button(wind, text="7",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(7))
button_8 = tk.Button(wind, text="8",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(8))
button_9 = tk.Button(wind, text="9",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(9))
button_0 = tk.Button(wind, text="0",bd=1, bg='#B30E0E',font=("Arial",20), fg='white', command=lambda: button_click(0))

button_add = tk.Button(wind, text="+",bd=1, bg='white',font=("Arial",20), fg='black', command=button_add)
button_subtract = tk.Button(wind, text="-",bd=1, bg='white',font=("Arial",20), fg='black', command=button_subtract)
button_multiply = tk.Button(wind, text="x",bd=1, bg='white',font=("Arial",20), fg='black', command=button_multiply)
button_divide = tk.Button(wind, text="/",bd=1, bg='white',font=("Arial",20), fg='black', command=button_divide)

button_equal = tk.Button(wind, text="=",bd=1, bg='black',font=("Arial",20), fg='white', command=button_equal)
button_clear = tk.Button(wind, text="C",bd=1, bg='black',font=("Arial",20), fg='white', command=button_clear)

# Show Buttons

button_1.place(x=0, y=100, width=100, height=100)
button_2.place(x=100, y=100, width=100, height=100)
button_3.place(x=200, y=100, width=100, height=100)

button_4.place(x=0, y=200, width=100, height=100)
button_5.place(x=100, y=200, width=100, height=100)
button_6.place(x=200, y=200, width=100, height=100)

button_7.place(x=0, y=300, width=100, height=100)
button_8.place(x=100, y=300, width=100, height=100)
button_9.place(x=200, y=300, width=100, height=100)

button_0.place(x=100, y=400, width=100, height=100)

button_clear.place(x=0, y=400, width=100, height=100)
button_equal.place(x=200, y=400, width=100, height=100)

button_add.place(x=300, y=100, width=100, height=100)
button_subtract.place(x=300, y=200, width=100, height=100)
button_multiply.place(x=300, y=300, width=100, height=100)
button_divide.place(x=300, y=400, width=100, height=100)


wind.mainloop()