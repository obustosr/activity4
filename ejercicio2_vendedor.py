import tkinter as tk
from tkinter import ttk, messagebox


class Vendedor:
    EDAD_MINIMA = 18
    EDAD_MAXIMA = 120

    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = 0

    def verificar_edad(self, edad):
        if edad < self.EDAD_MINIMA:
            raise ValueError("El vendedor debe tener 18 años o más.")
        if edad > self.EDAD_MAXIMA:
            raise ValueError("La edad del vendedor no puede ser mayor a 120 años.")
        self.__edad = edad

    def imprimir(self):
        return (f"Nombre: {self.__nombre}\n"
                f"Apellidos: {self.__apellidos}\n"
                f"Edad: {self.__edad}")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.5 - Vendedor")
        self.geometry("400x330")
        self.resizable(False, False)

        marco = ttk.LabelFrame(self, text="Datos del vendedor")
        marco.pack(fill="x", padx=12, pady=12)
        etiquetas = ["Nombre del vendedor:", "Apellidos del vendedor:",
                     "Edad del vendedor:"]
        self.entradas = []
        for fila, texto in enumerate(etiquetas):
            ttk.Label(marco, text=texto).grid(row=fila, column=0, sticky="e",
                                              padx=6, pady=6)
            entrada = ttk.Entry(marco, width=22)
            entrada.grid(row=fila, column=1, padx=6)
            self.entradas.append(entrada)

        ttk.Button(self, text="Verificar edad e imprimir",
                   command=self._verificar).pack(pady=4)
        self.lbl_resultado = ttk.Label(self, text="", justify="left",
                                       wraplength=360)
        self.lbl_resultado.pack(padx=12, pady=10)

    def _verificar(self):
        nombre, apellidos, edad_txt = (e.get().strip() for e in self.entradas)
        if not nombre or not apellidos:
            messagebox.showwarning("Datos incompletos",
                                   "Ingrese el nombre y los apellidos.")
            return
        try:
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(int(edad_txt))
            self.lbl_resultado.config(text=vendedor.imprimir(),
                                      foreground="#1b7a2f")
        except ValueError as error:
            mensaje = str(error)
            if mensaje.startswith("invalid literal"):
                mensaje = "La edad debe ser un número entero."
            self.lbl_resultado.config(text=f"Excepción: {mensaje}",
                                      foreground="#b00020")


if __name__ == "__main__":
    App().mainloop()
