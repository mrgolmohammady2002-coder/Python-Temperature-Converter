
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb

root = tb.Window(themename = "solar")
root.geometry("400x300")
root.title("مبدل دما")

mod = tb.StringVar(value = "k")
tb.Radiobutton(root, text="سلسيوس به فارنهايت", variable=mod, value="سلسيوس به فارنهايت", bootstyle="success-round-toggle").place(x=115, y=130)
tb.Radiobutton(root, text="فارنهايت به سلسيوس", variable=mod, value="فارنهايت به سلسيوس", bootstyle="warning-round-toggle").place(x=115, y=165)
tb.Label(root,text = " : دما را وارد کنيد",font = ("",15,"bold")).place(x = 115, y = 40)
entry_1 = tb.Entry(root,font=("",11,""))
entry_1.place(x=95, y=80)

def mobadel():
    text = entry_1.get()
    value = float(text)
    text2 = mod.get()
    if text2 == "سلسيوس به فارنهايت":
        f = (9/5)*value+32
        messagebox.showinfo("مبدل دما",f" فارنهايت : {round(f,1)}")
    elif text2 == "فارنهايت به سلسيوس":
        c = (5/9)*(value-32)
        messagebox.showinfo("مبدل دما",f"سلسيوس : {round(c,1)}")
    else:
        messagebox.showinfo("مبدل دما","در ورودي دادن دقت کنيد")
        


button = tb.Button(root, text="محاسبه", command = mobadel, bootstyle="primary,outline", width=15)
button.place(x=130, y=205)

root.mainloop()

    


    
    
