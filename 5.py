import tkinter as tk
from tkinter import messagebox

import random

def info():
    if x == y :
        messagebox.showinfo("Respuesta","Empate")
        return True
    elif (x=="piedra" and y=="tijera") or (x=="papel" and y=="piedra") or (x=="tijera" and y=="papel"):
        messagebox.showinfo("Respuesta","Gana")
        return False
    else:
        messagebox.showinfo("Respuesta","Pierde")
        return False

empate = True
while empate:
    x = input("piedra, papel o tijera:")
    y = random.choice(["piedra","papel","tijera"])
    messagebox.showinfo("Opcion","Sistema: ",y)
    empate=info()

root = tk.Tk()
root.title("Juego Autonomo 2")
root.geometry("400x200")
# Colocar el texto
tk.Label(root, text="Piedra - Papel - Tijera").pack(pady=10)
# Colocar la celda de texto
x = tk.Entry(root)
x.pack(pady=5)
# Colocar el boton
tk.Button(root, text="Jugar",command=info).pack(pady=5)
root.mainloop()