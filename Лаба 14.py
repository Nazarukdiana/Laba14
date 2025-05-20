from tkinter import *
from tkinter import messagebox
from random import *

a = []

def mas():
    n = edit1.get()
    if not n:
        messagebox.showerror("Помилка", "Введіть кількість елементів")
        return
    n = int(n)
    a.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    for i in range(n):
        a.append(randint(-50, 50))
        listbox1.insert(END, a[i])

def sort():
    n = len(a)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    listbox2.delete(0, END)
    for i in a:
        listbox2.insert(END, i)

def count_negative():
    count = sum(1 for x in a if x < 0)
    label4.config(text=f"Кількість від’ємних: {count}")

def apply_theme(bg, fg, btn_bg, entry_bg, listbox_bg):
    root.config(bg=bg)
    for w in widgets_to_color:
        w.config(bg=bg, fg=fg)
    for b in all_buttons + theme_buttons:
        b.config(bg=btn_bg, fg=fg, activebackground=btn_bg)
    edit1.config(bg=entry_bg, fg=fg, insertbackground=fg)
    listbox1.config(bg=listbox_bg, fg=fg)
    listbox2.config(bg=listbox_bg, fg=fg)

def set_mint_theme():
    apply_theme(bg='#e0f7f1', fg='#004d40', btn_bg='#a7ffeb', entry_bg='white', listbox_bg='white')

def set_neon_theme():
    apply_theme(bg='#121212', fg='#00e676', btn_bg='#1b1b1b', entry_bg='#2a2a2a', listbox_bg='#2a2a2a')

def set_lavender_theme():
    apply_theme(bg='#f3e5f5', fg='#4a148c', btn_bg='#ce93d8', entry_bg='white', listbox_bg='white')

def set_paper_theme():
    apply_theme(bg='#fefae0', fg='#5f4339', btn_bg='#d7ccc8', entry_bg='white', listbox_bg='white')

def about_author():
    messagebox.showinfo("Про автора", "Автор: Ді\nEmail: example@email.com")

def problem_statement():
    messagebox.showinfo("Умова задачі", "Підрахувати кількість від’ємних елементів\nта відсортувати масив за зростанням.")

def do_popup(event):
    popupmenu.tk_popup(event.x_root, event.y_root)

def enter_pressed(event):
    mas()

root = Tk()
root.title("Масиви з темами")
root.geometry("620x400")

label1 = Label(text="Вихідний масив")
label2 = Label(text="Відсортований масив")
label3 = Label(text="Кількість елементів:")
label4 = Label(text="Кількість від’ємних: ")

label1.place(x=20, y=20)
label2.place(x=200, y=20)
label3.place(x=400, y=20)
label4.place(x=400, y=200)

listbox1 = Listbox(width=20, height=10)
listbox2 = Listbox(width=20, height=10)
listbox1.place(x=20, y=50)
listbox2.place(x=200, y=50)

edit1 = Entry()
edit1.place(x=400, y=50)
edit1.bind("<Return>", enter_pressed)

button1 = Button(text="Заповнити", command=mas)
button2 = Button(text="Сортувати", command=sort)
button3 = Button(text="Підрахувати від’ємні", command=count_negative)

button1.place(x=400, y=90)
button2.place(x=400, y=130)
button3.place(x=400, y=170)

theme_buttons = []

btn_mint = Button(root, text="М'ятна тема", command=set_mint_theme)
btn_neon = Button(root, text="Неонова тема", command=set_neon_theme)
btn_lavender = Button(root, text="Лавандова тема", command=set_lavender_theme)
btn_paper = Button(root, text="Паперовий стиль", command=set_paper_theme)

btn_mint.place(x=50, y=320, width=120)
btn_neon.place(x=180, y=320, width=120)
btn_lavender.place(x=310, y=320, width=120)
btn_paper.place(x=440, y=320, width=120)

theme_buttons.extend([btn_mint, btn_neon, btn_lavender, btn_paper])

widgets_to_color = [label1, label2, label3, label4]
all_buttons = [button1, button2, button3]

main_menu = Menu(root)
root.config(menu=main_menu)

array_menu = Menu(main_menu, tearoff=0)
array_menu.add_command(label='Заповнити', command=mas)
array_menu.add_command(label='Сортувати', command=sort)
array_menu.add_command(label='Підрахувати від’ємні', command=count_negative)
main_menu.add_cascade(label='Масив', menu=array_menu)

info_menu = Menu(main_menu, tearoff=0)
info_menu.add_command(label='Про автора', command=about_author)
info_menu.add_command(label='Умова задачі', command=problem_statement)
main_menu.add_cascade(label='Про програму', menu=info_menu)

popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="М'ятна тема", command=set_mint_theme)
popupmenu.add_command(label="Нічна неонова тема", command=set_neon_theme)
popupmenu.add_command(label="Лавандова тема", command=set_lavender_theme)
popupmenu.add_command(label="Паперовий стиль", command=set_paper_theme)
root.bind("<Button-3>", do_popup)

set_mint_theme()

root.mainloop()
