import tkinter as tk
ventana = tk.Tk()
ventana.title("Jesus Eduardo Nolasco Flores")
ventana.geometry("530x350")
ventana.configure(bg="gray")

Label=tk.Label(ventana, text="Ingresa un Número Entero", bg="#1C1C1E", fg="#C0C0C0", font=("Arial", 20, "bold"))
Label.pack()
resultado_label = tk.Label(ventana, text="", bg="#1C1C1E", fg="#D4AF37", font=("Arial", 14))
resultado_label.pack()
def toBin():
    try:
        num = int(entrada.get())
        resultado = ""
        while num > 0:
            resultado = str(num % 2) + resultado
            num //= 2
        resultado_label.config(text=f"Binario: {resultado}")
    except ValueError:
        resultado_label.config(text="Error: Por favor, introduce un número entero.")
def toOctal():
    try:
        num = int(entrada.get())
        resultado = ""
        while num > 0:
            resultado = str(num % 8) + resultado
            num //= 8
        resultado_label.config(text=f"Octal: {resultado}")
    except ValueError:
        resultado_label.config(text="Error: Por favor, introduce un número entero.")
def toHexa():
    try:
        num = int(entrada.get())
        resultado = "" if num != 0 else "0"
        while num > 0:
            residuo = num % 16
            resultado = ("ABCDEF"[residuo - 10] if residuo > 9 else str(residuo)) + resultado
            num //= 16
        resultado_label.config(text=f"Hexadecimal: {resultado}")
    except ValueError:
        resultado_label.config(text="Error: Por favor, introduce un número entero.")


entrada=tk.Entry(ventana, justify="center", bg="#2C2C2E", fg="#F2F2F2", insertbackground="#F2F2F2", width=20, font=("Arial", 14), relief="solid", bd=2)
entrada.pack(pady=(5, 20))


boton = tk.Button(ventana, text="Convertir A Binario", bg="white", fg="black", width=15, height=2, command=toBin)
boton.pack()
boton2 = tk.Button(ventana, text="Convertir A Octal", bg="white", fg="black", width=15, height=2, command=toOctal)
boton2.pack()
boton3 = tk.Button(ventana, text="Convertir A Hexadecimal", bg="white", fg="black", width=20, height=2, command=toHexa)
boton3.pack()

ventana.mainloop()
