from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Ops", message="You cannot leave the Website or Password field empty")
        # else:
        #     is_ok = messagebox.askokcancel(title=f"{website}",
        #                                    message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it Ok "
        #                                            f"to Save")
        #
        #     if is_ok:
    else:
        try:
            with open("data.json", 'r') as data_file:
                # reading the old data
                data = json.load(data_file)
                # updating the old data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        with open("data.json", 'w') as data_file:
            # saving the updated data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox._show(message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showerror(message=f"No details for the website {website} exists.")

    except FileNotFoundError:
        messagebox.showerror(message="No Data File of Found")

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "kkishere@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

gener_pass_button = Button(text="Generate Password", width=11, command=generate_pass)
gener_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)

screen.mainloop()
