import tkinter
from tkinter import Label, font, Entry, Text, messagebox
from tkinter.font import Font

import bg
from bg import *
import main
import dao

ft = Font(family='Fixdsys', size=13, weight=font.BOLD, slant=font.ITALIC)
userT = Entry(root, width=15, font=ft, borderwidth=1)
numberT = Entry(root, width=8, font=ft)
trueT = Entry(root, width=8, font=ft)

var = tk.StringVar()  # 定义一个var用来接受radiobutton的值.
varA = tk.StringVar()
varB = tk.StringVar()
varC = tk.StringVar()
varD = tk.StringVar()
varTrue = tk.StringVar()
text = Text(root, width=37, height=4, borderwidth=0, font=Font(family='Fixdsys', size=14, weight=font.BOLD, ))




def hide():
    main.but.place_forget()
    main.text.place_forget()
    main.l.place_forget()
    # bg.root.after_cancel(after)
    # bg.l.place_forget()

def changeN(n):
    numberT.config(state='normal')
    old = numberT.get()
    numberT.delete(0)
    numberT.insert(0, int(old) + 1)
    numberT.config(state='disable')
    if (n == 1):
        trueT.config(state='normal')
        old = trueT.get()
        trueT.delete(0)
        trueT.insert(0, int(old) + 1)
        trueT.config(state='disable')
    dao.Update(n,userT.get())


def Login():
    if len(main.text.get().replace(' ', '')) != 0:
        f = dao.check(main.text.get())
        if (len(list(f))) != 0:
            userT.insert(0, main.text.get())
            userT.config(state='disabled')
            f = dao.check(main.text.get())    #不知为何len（list())之后原查询对象不能用了？？？？？？？
            for a in f:
                numberT.insert(0, a[1])
                numberT.config(state='disabled')
                trueT.insert(0, a[2])
                trueT.config(state='disabled')
            inti()


        else:

            if messagebox.askyesnocancel('用户不存在', '将添加新用户'):
                if dao.add(main.text.get()):
                    messagebox.showinfo('添加成功', '欢迎答题')
                    userT.insert(0, main.text.get())
                    userT.config(state='disabled')
                    numberT.insert(0, 0)
                    numberT.config(state='disabled')
                    trueT.insert(0, 0)
                    trueT.config(state='disabled')
                    inti()
    else:
        messagebox.showerror('错误', '用户名不能为空!')


def check():
    if var.get() == varTrue.get():
        messagebox.showinfo('正确', '回答正确')
        hit_me()
        changeN(1)
    else:
        if (var.get() != 'cha'): ##真正选择的时刻而不是刷新题目
            messagebox.showerror('错误', '回答错误!')
            changeN(0)


def hit_me():
    cursor1 = dao.select()
    for row in cursor1:
        varTrue.set(row[6])
        # l['text'] = row[1]
        text.config(state='normal')
        text.delete(1.0, tkinter.END)
        text.insert("insert",row[1])
        text.config(state='disabled')
        varA.set(row[2])
        varB.set(row[3])
        varC.set(row[4])
        varD.set(row[5])
    var.set('cha')  # 开始啥也不选

    check()


def inti():
    hide()
    bg.root.unbind("<Return>")  #解除绑定
    user = Label(root, font=ft)

    user['text'] = '用户'
    number = Label(root, text='答题总数', font=ft)

    trueNumber = Label(root, text='答题正确数目', font=ft)
    user.place(x=10, y=10)
    userT.place(x=60, y=10)
    number.place(x=230, y=10)
    numberT.place(x=320, y=10)
    trueNumber.place(x=400, y=10)
    trueT.place(x=530, y=10)
    text.place(x=110, y=50)
    r1 = tk.Radiobutton(root, textvariable=varA, variable=var, value='A',font=ft ,command=check)
    r1.place(x=200, y=130)
    r2 = tk.Radiobutton(root, textvariable=varB, variable=var, value='B',font=ft ,command=check)
    r2.place(x=200, y=180)
    r3 = tk.Radiobutton(root, textvariable=varC, variable=var, value='C',font=ft ,command=check)
    r3.place(x=200, y=230)
    r4 = tk.Radiobutton(root, textvariable=varD, variable=var, value='D',font=ft ,command=check)
    r4.place(x=200, y=280)
    #
    but1 = tk.Button(root, text='跳 过', font=Font(family='Fixdsys', size=18, weight=font.BOLD, slant=font.ITALIC),
                     command=hit_me)
    but1.place(x=530, y=60)
    hit_me()
def aaa(event):
    Login()

after=bg.init()    #用于清除背景，但没有成功，就直接去label了
main.init()
main.but.config(command=Login)
bg.root.bind("<Return> ",aaa)
# inti()
bg.root.mainloop()
