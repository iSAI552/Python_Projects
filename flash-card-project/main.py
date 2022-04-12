from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/german_lang.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canva_image, image=card_f_img)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    flip_timer = window.after(3000, answer_card)


def answer_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canva_image, image=card_b_img)


def known_word():
    to_learn.remove(current_card)
    new = pandas.DataFrame(to_learn)
    new.to_csv("./data/to_learn.csv", index=False)
    next_card()

# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, answer_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_b_img = PhotoImage(file="./images/card_back.png")
card_f_img = PhotoImage(file="./images/card_front.png")
canva_image = canvas.create_image(400, 263, image=card_f_img)
card_title = canvas.create_text(400, 150, text="German", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="trauve", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

w_button_img = PhotoImage(file="./images/wrong.png")
w_button = Button(image=w_button_img, highlightthickness=0, bd=0, command=next_card)
w_button.grid(column=0, row=1)

r_button_img = PhotoImage(file="./images/right.png")
r_button = Button(image=r_button_img, highlightthickness=0, bd=0, command=known_word)
r_button.grid(column=1, row=1)

next_card()
print(len(data))

window.mainloop()
