import math
import tkinter as tk
from tkinter import ttk


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError(
                "El valor debe ser un número positivo para calcular el logaritmo")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError(
                "El valor debe ser un número positivo para calcular la raíz cuadrada")
        return math.sqrt(valor)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.6 - Cálculos numéricos")
        self.geometry("460x240")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=8)
        C = CalculosNumericos
        self._crear_pestana("Logaritmo neperiano",
                            lambda v: f"ln({v:g}) = "
                                      f"{C.calcular_logaritmo_neperiano(v):.6f}")
        self._crear_pestana("Raíz cuadrada",
                            lambda v: f"√{v:g} = {C.calcular_raiz_cuadrada(v):.6f}")

    def _crear_pestana(self, titulo, accion):
        marco = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(marco, text=titulo)
        ttk.Label(marco, text="Valor numérico:").grid(row=0, column=0, padx=6, pady=4)
        entrada = ttk.Entry(marco, width=18)
        entrada.grid(row=0, column=1, pady=4)
        resultado = ttk.Label(marco, text="", justify="left", wraplength=400)

        def calcular():
            try:
                valor = float(entrada.get().strip().replace(",", "."))
                resultado.config(text=accion(valor), foreground="#1b7a2f")
            except ValueError:
                resultado.config(text="El valor debe ser numérico para calcular.",
                                 foreground="#b00020")
            except ArithmeticError as error:
                resultado.config(text=str(error), foreground="#b00020")

        ttk.Button(marco, text="Calcular", command=calcular).grid(
            row=1, column=0, columnspan=2, pady=10)
        resultado.grid(row=2, column=0, columnspan=2)


if __name__ == "__main__":
    App().mainloop()
