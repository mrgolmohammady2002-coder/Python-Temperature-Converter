import ttkbootstrap as tb
from tkinter import *
from tkinter import messagebox
from time import sleep

root = tb.Window(themename = "solar")   
root.geometry("560x350")
root.title("BMI برنامه")

gender = tb.StringVar(value="gg")
tb.Radiobutton(root, text="خانم", variable=gender, value="خانم", bootstyle="danger-round-toggle").place(x=190, y=27)
tb.Radiobutton(root, text="آقا", variable=gender, value="آقا", bootstyle="info-round-toggle").place(x=135, y=27)
tb.Label(root, text=": جنسيت خود را وارد کنيد", font=("Arial", 16, "bold")).place(x=255, y=20)



tb.Label(root, text=": قدتون رو وارد کنید", font=("Arial", 14, "bold")).place(x=275, y=60)
entry = tb.Entry(root, font=("Arial", 12,""))
entry.place(x=20, y=67)


tb.Label(root, text=": وزنتون رو وارد کنید", font=("Arial", 14, "bold")).place(x=275, y=100)
entry_2 = tb.Entry(root, font=("Arial", 12))
entry_2.place(x=20, y=105)


tb.Label(root, text=": محدوده سن خودتون رو وارد کنید", font=("Arial", 14, "bold")).place(x=255, y=145)
age = tb.StringVar(value="بالا 19")
tb.Radiobutton(root, text="بالا 19 سال", variable=age, value="بالا 19 سال", bootstyle="success-round-toggle").place(x=133, y=150)
tb.Radiobutton(root, text="کمتر 19 سال", variable=age, value="کمتر 19 سال", bootstyle="warning-round-toggle").place(x=15, y=150)


def get_entry_error():
    messagebox.showinfo("خطا", "لطفا فقط عدد وارد کنید")


def math():
    text = entry.get()
    text2 = entry_2.get()
    gens = gender.get()
    newText = int(text) / 10

    if text.isdigit() or text2.isdigit():
        if age.get() == "بالا 19 سال":
            if gens == "آقا":
                mat = round(int(text2) / (int(text) * int(text)) * 10000, 2)
                ming = round(newText ** 2 * 19 / 100, 1)
                maxg = round(newText ** 2 * 25.5 / 100, 1)
                a = mat-maxg
                if mat < 19:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار کمبود وزنيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 19 < mat < 25.5:
                    messagebox.showinfo("BMI محاسبه", f"وزن شما نرمال هست BMI : {mat}")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 25.5 < mat < 31.5:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما اضافه وزن داريد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 31.5 < mat < 100:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار چاقي هستيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif mat < 0:
                    messagebox.showinfo("BMI محاسبه", "BMI شما زير 0 هست و اشتباهه")
            else:
                mat = round(int(text2) / (int(text) * int(text)) * 10000, 2)
                ming = round(newText ** 2 * 18.5 / 100, 1)
                maxg = round(newText ** 2 * 24.9 / 100, 1)
                if mat < 18.5:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار کمبود وزنيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 18.5 < mat < 24.9:
                    messagebox.showinfo("BMI محاسبه", f"وزن شما نرمال هست BMI : {mat}")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 18.5 < mat < 30.5:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما اضافه وزن داريد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 30.5 < mat < 100:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار چاقي هستيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif mat < 0:
                    messagebox.showinfo("BMI محاسبه", "BMI شما زير 0 هست و اشتباهه")
        else:
            if gens == "آقا":
                mat = round(int(text2) / (int(text) * int(text)) * 10000, 2)
                ming = round(newText ** 2 * 17.5 / 100, 1)
                maxg = round(newText ** 2 * 25 / 100, 1)
                if mat < 17.5:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار کمبود وزنيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 17.5 < mat < 25:
                    messagebox.showinfo("BMI محاسبه", f"وزن شما نرمال هست BMI : {mat}")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 25 < mat < 31:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما اضافه وزن داريد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 31 < mat < 100:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار چاقي هستيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif mat < 0:
                    messagebox.showinfo("BMI محاسبه", "BMI شما زير 0 هست و اشتباهه")
            else:
                mat = round(int(text2) / (int(text) * int(text)) * 10000, 2)
                ming = round(newText ** 2 * 17 / 100, 1)
                maxg = round(newText ** 2 * 24 / 100, 1)
                if mat < 17:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار کمبود وزنيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 17 < mat < 24:
                    messagebox.showinfo("BMI محاسبه", f"وزن شما نرمال هست BMI : {mat}")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 24 < mat < 29:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما اضافه وزن داريد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif 29 < mat < 100:
                    messagebox.showinfo("BMI محاسبه", f"شما برابر با BMI : {mat} شما دچار چاقي هستيد")
                    sleep(1)
                    messagebox.showinfo("BMI برنامه", f"وزن ایده‌آل شما از {ming} تا {maxg} کیلوگرم هست")
                elif mat < 0:
                    messagebox.showinfo("BMI محاسبه", "BMI شما زير 0 هست و اشتباهه")
    else:
        get_entry_error()


button = tb.Button(root, text="محاسبه", command = math, bootstyle="primary,outline", width=15)
button.place(x=120, y=190)

root.mainloop()
