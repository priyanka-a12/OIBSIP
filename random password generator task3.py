from tkinter import *
from tkinter import messagebox
from random import *
from string import *

win = Tk()
wid = 0
# configuring the window
win.geometry("700x500")
win.configure(bg="#d5dEEf")
win.title("PASSWORD GENERATOR")
font1 = ("Sans-serif", 12)

# creating necessary label widgets
title_label = Label(win, text="PASSWORD GENERATOR", padx=30, pady=15, bg="#d5dEEf", font=("Sans-serif", 15, "bold"),
                    fg="#395886")
len_label = Label(win, text="Enter the length for your Password : ", padx=13, pady=10, bg="#d5dEEf", font=font1,
                  fg="#395886")
alp_label = Label(win, text="Number of Alphabets :", padx=13, pady=10, bg="#d5dEEf",
                  font=font1, fg="#395886")
num_label = Label(win, text="Number of Digits :", padx=13, pady=10, bg="#d5dEEf",
                  font=font1, fg="#395886")
special_label = Label(win, text="Number of special characters : ", padx=13, pady=10,
                      bg="#d5dEEf", font=font1, fg="#395886")
exc_label = Label(win, text="Characters to be excluded from your password (separated by spaces) : ", padx=30, pady=20,
                  bg="#d5dEEf", font=font1, fg="#395886")
res_label = Label(win, text="Generated Password : ", padx=30, pady=20, bg="#d5dEEf", font=font1, fg="#395886")


# creating necessary entry widgets
len_entry = Entry(win, width=8, font=font1)
alp_entry = Entry(win, width=8, font=font1)
num_entry = Entry(win, width=8, font=font1)
special_entry = Entry(win, width=8, font=font1)
exc_entry = Entry(win, width=8, font=font1)
res_entry = Entry(win, width=wid, font=font1)


# function definitions
def generate_pwd():
    """this function generates random password according to users preferences"""
    # setting the lists
    letters = list(ascii_letters)
    # print(letters)
    numbers = list(digits)
    # print(numbers)
    special_characters = list(punctuation)
    # print(special_characters)

    password = []
    alpha_n = num_n = special_n = 0
    # print("**********Let's Create a Custom Password For You !************")

    res_entry.delete(0, END)

    try:
        length = int(len_entry.get())
        if length < 8:
            messagebox.showinfo("INPUT WARNING", "A password must have at least 8 characters")
    except ValueError:
        messagebox.showerror(" ERROR", "Length Value must be numeric")

    # alpha_n = num_n = special_n = 0
    # while alpha_n + num_n + special_n != length:
    try:
        alpha_n = int(alp_entry.get())
        if alpha_n > length:
            raise Exception
        num_n = int(num_entry.get())
        if num_n > length:
            raise Exception
        special_n = int(special_entry.get())
        if special_n > length:
            raise Exception
        if alpha_n + num_n + special_n != length:
            messagebox.showwarning(" INPUT ERROR", "Total number of characters must be equal to selected length")
    except ValueError:
        messagebox.showerror(" INPUT ERROR", "values must be numeric")
    except Exception:
        messagebox.showerror(" INPUT ERROR", " entered value must be less than or equal to selected length")
    else:
    # adding random alphabet to the password

        exclude = list(exc_entry.get().split())

        # loop to remove characters to be excluded

        for i in exclude:
            if i in letters:
                letters.remove(i)
            if i in numbers:
                numbers.remove(i)
            if i in special_characters:
                special_characters.remove(i)

        # loops to generate password

        for i in range(alpha_n):
            password += choice(letters)
        # adding random digits to the password
        for i in range(num_n):
            password += choice(numbers)
        # adding random special characters to the password
        for i in range(special_n):
            password += choice(special_characters)

        # print(password)
        # shuffling the elements in the list randomly
        shuffle(password)
        # converting the list into string
        result = ""
        for i in password:
            result += i

        # print("*********************************************************************")
        # print(f"Your Custom Generated Password is : {result}")
        # print("*********************************************************************")
        res_entry.insert(0, result)


def clear_values():
    len_entry.delete(0, END)
    alp_entry.delete(0, END)
    num_entry.delete(0, END)
    special_entry.delete(0, END)
    exc_entry.delete(0, END)
    res_entry.delete(0, END)


# creating buttons
gen_btn = Button(win, text="GENERATE", padx=10, pady=10, bg="#395886", fg="#8AaEE0", font=("Sans-serif", 12, "bold"),
                 command=generate_pwd)
reset_btn = Button(win, text="RESET", padx=10, pady=10, bg="#395886", fg="#8AaEE0", font=("Sans-serif", 12, "bold"),
                 command=clear_values)

# placing widgets on the window
title_label.grid(row=0, column=0, columnspan=2)
len_label.grid(row=1, column=0)
alp_label.grid(row=2, column=0)
num_label.grid(row=3, column=0)
special_label.grid(row=4, column=0)
exc_label.grid(row=5, column=0)

# placing entries on window
len_entry.grid(row=1, column=1)
alp_entry.grid(row=2, column=1)
num_entry.grid(row=3, column=1)
special_entry.grid(row=4, column=1)
exc_entry.grid(row=5, column=1)
reset_btn.grid(row=6, column=0)
gen_btn.grid(row=6, column=1)
res_label.grid(row=7, column=0)
res_entry.grid(row=7, column=1)


win.mainloop()
