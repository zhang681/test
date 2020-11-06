from tkinter import Label, font, Entry, Button
from tkinter.font import Font
from bg import *

l=Label(root,text='请输入用户',font=Font(family='Fixdsys', size=18, weight=font.BOLD,slant=font.ITALIC))
text=Entry(root,width=18,font=Font(family='Fixdsys', size=18,weight=font.BOLD,slant=font.ITALIC))
but=Button(root,text='加入',font=Font(family='Fixdsys', size=15,weight=font.BOLD,slant=font.ITALIC))
def init():
    root.wm_attributes("-alpha", 0.8)
    text.place(x=190,y=140)
    but.place(x=450,y=136)
    l.place(x=50,y=140)



