from PIL import ImageTk,Image
import tkinter as tk

def change(index):
    l.configure(image=frames[index])
    index+=1
    root.after(100, change, index % len(frames))
frames=[]
# global root
root = tk.Tk()
root.geometry('629x483')
root.resizable(width=False,height=False)   #大小不变
l=tk.Label(root)


# im = Image.open('gif.gif')    用于分解gif图片
# try:
#     i = 0
#     while True:
#         im.seek(i)
#         im.save(str(i) + ".png")
#         frames.append(ImageTk.PhotoImage(file=str(i) + ".png"))
#         i += 1
# except:
#     pass
def init():

    for i in range(0,36):
        frames.append(ImageTk.PhotoImage(file='img/'+str(i) + ".png"))
    l.place(x=0,y=0)
    return root.after(0,change,0)

