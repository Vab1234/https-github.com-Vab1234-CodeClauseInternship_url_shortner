from tkinter import *
import pyshorteners
import pyperclip

def shorten_url():
    url = text1.get()
    shortner = pyshorteners.Shortener()
    short_url = shortner.tinyurl.short(url)
    text2.insert(0 , short_url)
    pyperclip.copy(short_url)


root = Tk()
root.geometry("300x380")
root.title("URL Shortner")

canvas = Canvas(width=300 , height=256)
stock_img = PhotoImage(file="url shortner/icon-256x256.png")
canvas.create_image(152 , 128 , image = stock_img)
canvas.grid(row=0 , column=0)

label1 = Label(text = "Enter your url")
label1.config(padx=5 , pady=5)
label1.grid(row=1 , column=0)

text1 = Entry(width=50 )
text1.grid(row=2 , column=0)

generate_button = Button(text = "Generate url" , command= shorten_url)
generate_button.config(padx=5 , pady=5)
generate_button.grid(row=4 , column=0)

text2 = Entry(width=50)
text2.grid(row=5 , column=0)

root.mainloop()