from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if (
        len(password.strip()) == 0
        or len(email.strip()) == 0
        or len(website.strip()) == 0
    ):
        messagebox.showwarning(
            title="Warning", message="Please do not leave any fields empty"
        )

    else:
        is_ok = messagebox.askokcancel(
            title={website},
            message=f"These are the details entered: \nEmail : {email}\n Password : {password}\n Is it okay to save? ",
        )

        if is_ok:
            with open("password-manager/data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="password-manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", highlightthickness=0)
website_label.grid(column=0, row=1)

website_input = Entry(width=35, highlightthickness=0)
website_input.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username:", highlightthickness=0)
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=35, highlightthickness=0, justify="left")
email_username_input.insert(END, "ethantay321@gmail.com")
email_username_input.grid(column=1, row=2, columnspan=2, pady=10)

password_label = Label(text="Password:", highlightthickness=0)
password_label.grid(column=0, row=3)

password_input = Entry(width=21, highlightthickness=0, justify="left")
password_input.grid(column=1, row=3)

password_btn = Button(
    text="Generate Password", highlightthickness=0, command=generate_password
)
password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, highlightthickness=0, command=save_password)
add_btn.grid(column=1, columnspan=2, row=4)

window.mainloop()
