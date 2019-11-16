import requests 
from tkinter import *

url = "https://api.scryfall.com/cards/random?q=has:flavor"

def clicked():
    r = requests.get(url=url)

    data = r.json()
    text = data["flavor_text"]
    text = text.replace("/", "\n")
    print(text)
    lbl.configure(text=text)

window = Tk()
window.title("Flavor Text Generator")

window.geometry('350x200')

lbl = Label(window, text="", wraplength=200)
lbl.place(x=175, y=120, anchor="center")

btn = Button(window, text="Generate!", command=clicked)

btn.place(x=175, y=50, anchor="center")

window.mainloop()