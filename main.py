import tkinter as tk
from tkinter import messagebox
import subprocess

root = tk.Tk()
bg_color = "#ffffff"
main_color ="#ffffff"
def cm():
    path = entry.get()
    command = f'pyinstaller --onefile --noconsole "{path}"'
    

    if path == "Введите путь к вашему файлу":
        messagebox.showerror("Ошибка", "Введите коррекнтый путь к файлу")

    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        if result.returncode == 0:
            messagebox.showinfo("Успех", "Ковертация успешно завершена")
        else:
            messagebox.showerror("Отказ", "При конвертации произошла ошибка, попробуйте опять")

    except Exception as e:
        messagebox.showerror("Ошибка", "Ошибка при конвертации")
root.configure(bg= bg_color)
root.title("Конвертатор python файлов")
root.geometry("360x450")
lab = tk.Label(root, text="Конвертатор .py в .exe", bg = main_color, font=("16"))
lab.pack(pady=5)


entry = tk.Entry(root, width=30, font=(10), bd=1)
entry.insert(0, "Введите путь к вашему файлу")
entry.pack(pady=70)

but = tk.Button(root, text="Конвертировать файл", command=cm, bg= main_color, font=("Arial, 16") )
but.pack(pady=80)


root.mainloop()
