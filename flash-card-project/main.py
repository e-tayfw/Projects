from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

to_learn = {}
current_card = {}

try:
    data = pd.read_csv("flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("flash-card-project/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
finally:
    current_card = random.choice(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("flash-card-project/data/words_to_learn.csv", index=False)
    next_card()


# UI SETUP --------------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="flash-card-project/images/card_front.png")
card_back_img = PhotoImage(file="flash-card-project/images/card_back.png")
card_background = canvas.create_image(400, 270, image=card_front_img)

lang = canvas.create_text(400, 150, text="French", font=LANG_FONT)
word = canvas.create_text(400, 263, text=current_card["French"], font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="flash-card-project/images/wrong.png")
wrong_btn = Button(
    image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card
)
wrong_btn.grid(padx=50, column=0, row=1)

right_img = PhotoImage(file="flash-card-project/images/right.png")
right_btn = Button(
    image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known
)
right_btn.grid(padx=50, column=1, row=1)

window.mainloop()
