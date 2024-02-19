from tkinter import *;
import csv;
import json 
from tkinter import messagebox;
import pandas as pd;
import random;

BACKGROUND_COLOR = "#B1DDC6";

##pandas
dict_data = {};
try:
    data = pd.read_csv("./data/words_to_learn.csv");
except FileNotFoundError:
    original_data = pd.read_csv("./data/japanese_words.csv");
    dict_data = original_data.to_dict(orient="records");
else: 
    dict_data = data.to_dict(orient="records");

##functions
random_row = {};
def next_card():
    global random_row, flip_timer;
    window.after_cancel(flip_timer);
    random_row = random.choice(dict_data);
    canvas.itemconfig(card_title,text="Japanese", fill = "black");
    canvas.itemconfig(card_word,text=random_row["Japanese"], fill="black");
    canvas.itemconfig(current_card_side, image= card_front_img);
    flip_timer = window.after(3000, func = card_flip);
    print(len(dict_data));


def card_flip():
    canvas.itemconfig(card_title,text="English", fill="white");
    canvas.itemconfig(card_word,text=random_row["English"], fill="white");
    canvas.itemconfig(current_card_side, image = card_back_img);

def is_known():
    dict_data.remove(random_row);
    next_card();
    data = pd.DataFrame(dict_data);
    data.to_csv("./data/words_to_learn.csv", index = False);


window = Tk();
window.title("Japanese flashcards");
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);
flip_timer = window.after(3000, func = card_flip)
canvas = Canvas(width=800, height=526);
card_back_img = PhotoImage(file="./images/card_back.png");
card_front_img = PhotoImage(file="./images/card_front.png");
current_card_side = canvas.create_image(400,263, image=card_front_img);
card_title = canvas.create_text(400,150,text="Japanese", font=("Ariel", 40, "italic"));
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel",60, "bold"));
# canvas.create_text(400, 363, text="pronouncation", font=("Ariel",20, "italic"));



canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0);
canvas.grid(column=0,row=0, columnspan=2);

##Buttons

X_IMAGE= PhotoImage(file="./images/wrong.png");
x_button = Button(image=X_IMAGE, command= next_card);
x_button.grid(row=1, column=0);
x_button.config(highlightthickness=0);


Y_IMAGE= PhotoImage(file="./images/right.png");
y_button = Button(image=Y_IMAGE, command=is_known);
y_button.grid(row=1, column=1);
y_button.config(highlightthickness=0);

next_card();



window.mainloop();
