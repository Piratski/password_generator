from random import *
from tkinter import *


sym = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym2 = "abcdefghijklmnopqrstuvwxyz"
chars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
num = "0123456789"
all = sym + sym2 + chars + num


def get_password():    
    lengthPassword = e.get()
    e.delete(0, END)
    for i in range(int(lengthPassword)):
        e.insert(0, choice(all))


root = Tk()
root.title("Password generator")
root.geometry("300x160")
root.resizable( width = False, height = False )

e = Entry(root)
e.place(relx = 0.5, y = 50, anchor = CENTER) 

btn = Button(root, text = 'Get password', font = (15), command = get_password)
btn.place(relx = 0.5, y = 100, anchor = CENTER)

root.mainloop()