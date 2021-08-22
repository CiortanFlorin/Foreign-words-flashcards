from tkinter import *
import pandas
import random

random_word={}
BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except:
    df = pandas.read_csv("data/french_words.csv")
finally:
    dict = df.to_dict(orient="records")
    new_dict = dict




def generate_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=my_img)
    canvas.itemconfig(language_word, text="French", fill='black')
    random_word = random.choice(dict)
    # random_french = dict[random_number]["French"]
    # random_english = dict[random_number]["English"]
    canvas.itemconfig(french_word, text=random_word["French"], fill='black')
    flip_timer = window.after(3000, change_word)

def change_word():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_word, text="English", fill="white")
    canvas.itemconfig(french_word, text=random_word["English"], fill="white")

def generate_word_right():
    generate_word()
    new_dict.remove(random_word)
    df = pandas.DataFrame(new_dict)
    df.to_csv("data/words_to_learn.csv", mode='w', index=False)

window = Tk()
window.title("Flash-Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, change_word)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=my_img)
language_word = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french_word = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_buton = Button(image=right_image, highlightthickness=0, command=generate_word_right)
right_buton.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_buton = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_buton.grid(row=1, column=0)

generate_word()

window.mainloop()