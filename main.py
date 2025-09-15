from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for let in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password) #replace password field with generated password
    pyperclip.copy(password) #copy generated password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you didn't leave a field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it OK to save?")

        if is_ok:
            with open("Passwords", "a") as passwords:
                passwords.write(f"{website} | {email} | {password}\n")

                # Clear fields after data was saved
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)
username_lbl = Label(text="Email/Username:")
username_lbl.grid(column=0, row=2)
password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)

#Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

website_input.focus()
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "test@gmail.com") #this is the default provided email incase you have the same email for every login
password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)

#Buttons
generate_pass_btn = Button(text="Generate Password", width=30, command=generate_password)
generate_pass_btn.grid(column=1, row=4, columnspan=2)
add_btn = Button(text="Add", width=30,command=save)
add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()
