from tkinter import *
from tkinter import messagebox as mb
from random import randint, choice, shuffle
import pyperclip
import json

font_name = "Cambria"
font_size = 12

def generate_password():

    letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = (password_letters + password_symbols + password_numbers)

    # Shuffle the order of each character in the password.
    shuffle(password_list)

    # Append the results of the list to an empty string.
    password = "".join(password_list)

    print(f"Your password is: {password}")

    # Put password back into the password_entry object.
    password_entry.insert(0, password)

    pyperclip.copy(password)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode = "r") as file:
            data = json.load(file)

    except FileNotFoundError as error_message:
        mb.showinfo(title = f"{website} Error", message = f"No Data File Found for {error_message}.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            mb.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            mb.showinfo(title="Error", message=f"No details for {website} exists.")


def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if (len(website) == 0 or len(password) == 0):
        mb.showinfo(
        title="Please Retry",
        message=
        "write a website or password, don't leave either of these fields blank.")

    else:
        try:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=(font_name, font_size))
website.grid(row=1, column=0)

email = Label(text="Email/Username:", font=(font_name, font_size))
email.grid(row=2, column=0)

password = Label(text="Password:", font=(font_name, font_size))
password.grid(row=3, column=0)

password_button = Button(
    text="Generate Password",
    command=generate_password,
    width=12
)

password_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save_password, width=35)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password, width=12)
search_button.grid(row=1, column=2)

website_entry = Entry(width=23)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "my_email@email_provider.com")

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)

window.mainloop()