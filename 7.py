import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("Juego Autonomo 2")
root.geometry("400x200")

tk.Label(root, text="Piedra - Papel - Tijera").pack(pady=10)

x = tk.Entry(root)
x.pack(pady=5)
y = random.choice(["piedra","papel","tijera"])

def info():
    if x.get() == y :
        messagebox.showinfo("Respuesta","Empate")
        return True
    elif (x.get()=="piedra" and y=="tijera") or (x.get()=="papel" and y=="piedra") or (x.get()=="tijera" and y=="papel"):
        messagebox.showinfo("Respuesta","Ganaste")
        return False
    else:
        messagebox.showinfo("Respuesta","Perdiste")
        return False

def jugar():
    global y
    y = random.choice(["piedra","papel","tijera"])
    messagebox.showinfo("Opcion",f"Sistema: {y}")
    empate=info()

tk.Button(root, text="Jugar",command=jugar).pack(pady=5)
root.mainloop()