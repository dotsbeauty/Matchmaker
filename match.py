import random
import time
from tkinter import Tk , Button , DISABLED
from tkinter import * 
  
from time import strftime

class Warspyking(Button):
    def __init__(self, master=None, **kwargs):
        self.img = PhotoImage()
        Button.__init__(self, master, image=self.img, compound='center', **kwargs)

def show_symbol(x,y):
    global first
    global previousx , previousy
    global n
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy != y:
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
            n = n + 1
            string = str(n)
            lbl.config(text = string)
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
            
        first = True

win = Tk()
win.title('Matchmaker')
win.resizable(width=False , height=False)
lbl = Label(win,font = ('calibri', 40, 'bold'))
  
lbl.grid(column = 5, row = 0 )
n = 0
string = str(n)
lbl.config(text = string)

first = True
previousx = 0
previousy = 0
buttons = { }
button_symbols = { }
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbols)

for x in range(6):
    for y in range(1,5):
        button = Warspyking(command = lambda x=x , y=y: show_symbol(x,y) , width = 100, height = 150, font = ('Helvetica', '20'))
        button.grid(column = x , row = y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()


    
win.mainloop()
