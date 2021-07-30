from tkinter import *
import pandas as pd
import random

LANGUAGE = "German"                                     # LANGUAGE TO TRANSLATE
CSV_FILE = "data/german_words.csv"                      # CSV FILE THAT CONTAINS WORDS AND TRANSLATIONS
BACKGROUND_COLOR = "#B1DDC6"
GREEN = "#9bdeac"

current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(CSV_FILE)
    translations = original_data.to_dict(orient="records")
else:
    translations = data.to_dict(orient="records")


# PICKUP RANDOM WORDS IN CARDS
def words_generator():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(translations)
    canvas.itemconfig(card_title, text=LANGUAGE, font=("Arial", 30, "italic"), fill=GREEN)
    canvas.itemconfig(card_word, text=current_card[LANGUAGE], font=("Arial", 50, "bold"), fill=GREEN)
    canvas.itemconfig(card_bg, image=flashcard_front)
    flip_timer = window.after(3000, func=flip_card)


# FLIPS CARD TO REVEAL BACK SIDE AND ENGLISH TRANSLATION
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="White" )
    canvas.itemconfig(card_word, text=current_card['English'], fill="White")
    canvas.itemconfig(card_bg, image=flashcard_back)


# REMOVES THE CHECKED WORDS AND SAVES THE REST TO A NEW FILE
def save_words():
    translations.remove(current_card)
    to_learn = pd.DataFrame(translations)
    to_learn.to_csv("data/words_to_learn.csv", index=False)

    words_generator()


# SETS UP WINDOWS
window = Tk()
window.title(f'Flash Card {LANGUAGE}')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)         # SETS TIMER TO 3 SECONDS (3000MS)

# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=flashcard_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 120, text="", font=("Arial", 30, "italic"), fill=GREEN)
card_word = canvas.create_text(400, 263, text="", font=("Arial", 50, "bold"), fill=GREEN)

# BUTTONS
check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, command=save_words, bg=BACKGROUND_COLOR, highlightthickness=0)
check_button.grid(row=1, column=1)

cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, command=words_generator, bg=BACKGROUND_COLOR, highlightthickness=0)
cross_button.grid(row=1, column=0)

words_generator()

window.mainloop()
