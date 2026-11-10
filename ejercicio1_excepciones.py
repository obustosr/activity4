import tkinter as tk
from tkinter import ttk


class PruebaExcepciones:
    @staticmethod
    def ejecutar():
        salida = []
        try:
            salida.append("Ingresando al primer try")
            _ = 10 / 0
        except ZeroDivisionError:
            salida.append("División por cero")
        finally:
            salida.append("Ingresando al primer finally")

        try:
            salida.append("Ingresando al segundo try")
            _ = int("abc")
        except ArithmeticError:
            salida.append("Excepción aritmética")
        except Exception:
            salida.append("Ocurrió una excepción")
        finally:
            salida.append("Ingresando al segundo finally")
        return salida


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.4 - Prueba de excepciones")
        self.geometry("480x280")
        self.resizable(False, False)

        marco = ttk.LabelFrame(self, text="Ejercicio 6.4: try / except / finally")
        marco.pack(fill="both", expand=True, padx=10, pady=10)
        ttk.Button(marco, text="Ejecutar prueba",
                   command=self._ejecutar_prueba).pack(pady=8)
        self.txt_salida = tk.Text(marco, height=8, width=52, state="disabled")
        self.txt_salida.pack(padx=8, pady=(0, 8))

    def _ejecutar_prueba(self):
        lineas = PruebaExcepciones.ejecutar()
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, "\n".join(lineas))
        self.txt_salida.config(state="disabled")


if __name__ == "__main__":
    App().mainloop()
