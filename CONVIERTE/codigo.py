import tkinter as tk
root = tk.Tk()
root.title("Jesus Eduardo Nolasco Flores")
root.geometry("530x300")
root.resizable(False, False)
root.configure(bg="blue")

tk.Label(root, text="Ingresa un Número Entero", bg="#1C1C1E", fg="#C0C0C0", font=("Arial", 20, "bold"), justify="center").pack(pady=(20, 10))
resultado_label = tk.Label(root, text="", bg="#1C1C1E", fg="#D4AF37", font=("Arial", 14)); resultado_label.pack(pady=(10, 20))

def toBin():
    try:
        num = int(entrada.get())
        resultado = ""
        while num > 0:
            resultado = str(num % 2) + resultado
            num //= 2
        resultado_label.config(text=f"Binario: {resultado}")
    except ValueError:
        resultado_label.config(text="Error: Por favor, introduce un número entero.", fg="red")

def toOctal():
    try:
        num = int(entrada.get())
        resultado = ""
        while num > 0:
            resultado = str(num % 8) + resultado
            num //= 8
        resultado_label.config(text=f"Octal: {resultado}")
    except ValueError:
        resultado_label.config(text="Error: Por favor, introduce un número entero.", fg="red")

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
        resultado_label.config(text="Error: Por favor, introduce un número entero.", fg="red")



entrada = tk.Entry(root, justify="center", bg="#2C2C2E", fg="#F2F2F2", insertbackground="#F2F2F2", width=20, font=("Arial", 14), relief="solid", bd=2)
entrada.pack(pady=(5, 20))


boton = tk.Button(root, text="Convertir A Binario", bg="white", fg="black", width=15, height=2, command=toBin, relief="flat").pack(side="left", padx=(75, 5), pady=10)
boton2 = tk.Button(root, text="Convertir A Octal", bg="white", fg="black", width=15, height=2, command=toOctal, relief="flat").pack(side="left", padx=5, pady=10)
boton3 = tk.Button(root, text="Convertir A Hexadecimal", bg="white", fg="black", width=20, height=2, command=toHexa, relief="flat").pack(side="left", padx=5, pady=10)



root.mainloop()
