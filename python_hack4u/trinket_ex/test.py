#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry('700x550')
root.title("text() Widget")

def get_data():
    data = text_widget.get("1.0", tk.END) # Determinar desde donde obtener la información (linea.caracter, END=final)
    print(f"\n[+] Datos introducidos por el ususario:\n\n {data}")

text_widget = tk.Text(root)
text_widget.pack(pady=5, padx=15, fill=tk.X)

button = tk.Button(root, text='Recoger datos de entrada', command=get_data)
button.pack()



root.mainloop()
