import tkinter as tk 

def hola():
    lb.config(text="you clicked")

ventana=tk.Tk()
ventana.geometry("300x300")
ventana.title("Jesus Eduardo Nolasco Flores")

lb=tk.Label(ventana,text="HELLO TREVI")
lb.pack()

bt=tk.Button(ventana,text="PRESS ME",command=hola)
bt.pack()

ventana.mainloop()