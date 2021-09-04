from tkinter import *
from tkinter import messagebox
import pyautogui as pag
import keyboard
import time

width = 400
height = 400

root = Tk()
root.title("MacrosPy")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)

def afk():
    stop_key = message.get()
    try:
        while True:
            pag.keyDown('w')
            time.sleep(0.5)
            pag.keyUp('w')
            pag.keyDown('d')
            time.sleep(0.5)
            pag.keyUp('d')
            pag.keyDown('s')
            time.sleep(0.5)
            pag.keyUp('s')
            pag.keyDown('a')
            time.sleep(0.5)
            pag.keyUp('a')

            if keyboard.is_pressed(stop_key):
                break
    except ValueError as e:
        messagebox.showerror("Ошибка", "Заполните поля")
def autoclick():
    stop_key = message.get()
    key = message_1.get()
    try:
        left = ('Левая', 'Левая кнопка мыши', 'left', 'лкм', 'ЛКМ')
        right = ('ПКМ', 'пкм', 'Правая', 'right', 'Правая кнопка мыши')
        middle = ('СКМ', 'скм', 'Средняя', 'middle', 'Средняя кнопка мыши')

        while True:
            if key in left:
                pag.click(button='left')
            elif key in right:
                pag.click(button='right')
            elif key in middle:
                pag.click(button='middle')
            else:
                pass

            if keyboard.is_pressed(stop_key):
                break
    except ValueError as e:
        messagebox.showerror("Ошибка", "Заполните поля")

def autopush():
    stop_key = message.get()
    key = message_1.get()
    try:
        while True:
            pag.keyDown(key)
            pag.keyUp(key)

            if keyboard.is_pressed(stop_key):
                break
    except ValueError as e:
        messagebox.showerror("Ошибка", "Заполните поля")

def help():
    messagebox.askquestion("Помощь", "1 поле нужно для кнопки,которая остановит процесс(без нее будет трудновато)\n 2 поле нужно для действия,которое будет производить бот,как например:\n \n Буква для автопуша(подразумевается постоянное нажатие на клавишу клавиатуры) \n \n Левая, Левая кнопка мыши, left, лкм, ЛКМ - Левая кнопка мыши для автокликера \n ПКМ, пкм, Правая, right, Правая кнопка мыши - Правая кнопка мыши для автокликера \n СКМ, скм, Средняя, middle, Средняя кнопка мыши - Средняя кнопка мыши для автокликера \n \nP.S. AFK функция закрывается некорректно.В случае зависания программы - ALT + F4.")


message = StringVar()
message_1 = StringVar()

message_label = Label(text = "Впишите букву,для остановки процесса")
message_label.place(relx=.2, rely=.0)

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c",width="40",height="25")

message_label = Label(text = "Впишите букву или слово,для действия")
message_label.place(relx=.2, rely=.2)

message_entry_1 = Entry(textvariable=message_1)
message_entry_1.place(relx=.5, rely=.3, anchor="c",width="40",height="25")

message_button = Button(text="AFK",padx="20", pady="15",background="#555",foreground="#fff", command=afk)
message_button.place(relx=.5, rely=.5, anchor="c")

message_button_1 = Button(text="Автокликер",padx="20", pady="15",background="#555",foreground="#fff", command=autoclick)
message_button_1.place(relx=.5, rely=.7, anchor="c")

message_button_1 = Button(text="Автопуш",padx="20", pady="15",background="#555",foreground="#fff", command=autopush)
message_button_1.place(relx=.5, rely=.9, anchor="c")

main_menu = Menu()
main_menu.add_cascade(label="Помощь", command=help)
root.config(menu=main_menu)

root.mainloop()