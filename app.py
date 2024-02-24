import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        Numero_ingresado = prompt("Ingrese un número", "Número")
        Numero_ingresado = int(Numero_ingresado)
        divisores = []
        for numero in range(1, Numero_ingresado + 1):
            if Numero_ingresado % numero == 0:
                divisores.append(numero)
                alert(str(numero))
                Mensaje = f"Se encontraron {len(divisores)} numeros divisores hasta el {Numero_ingresado}"
                alert("Mensaje", Mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()