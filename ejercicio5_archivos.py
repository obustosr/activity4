import tkinter as tk
from tkinter import ttk, filedialog


class LeerArchivo:
    @staticmethod
    def leer(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return archivo.read()
        except (OSError, UnicodeDecodeError):
            raise IOError("No se pudo leer el archivo.")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.8 - Lectura de archivos")
        self.geometry("560x430")

        superior = ttk.Frame(self, padding=8)
        superior.pack(fill="x")
        ttk.Label(superior, text="Nombre del archivo:").grid(row=0, column=0)
        self.ent_ruta = ttk.Entry(superior, width=34)
        self.ent_ruta.insert(0, "ejemplo.txt")
        self.ent_ruta.grid(row=0, column=1, padx=6)
        ttk.Button(superior, text="Examinar...",
                   command=self._examinar).grid(row=0, column=2)

        botones = ttk.Frame(self, padding=(8, 0))
        botones.pack(fill="x")
        ttk.Button(botones, text="Leer archivo",
                   command=self._leer).pack(side="left", padx=2)

        cuerpo = ttk.Frame(self, padding=8)
        cuerpo.pack(fill="both", expand=True)
        self.txt = tk.Text(cuerpo, wrap="word", state="disabled")
        barra = ttk.Scrollbar(cuerpo, command=self.txt.yview)
        self.txt.config(yscrollcommand=barra.set)
        barra.pack(side="right", fill="y")
        self.txt.pack(side="left", fill="both", expand=True)

    def _examinar(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Archivos de texto", "*.txt"), ("Todos", "*.*")])
        if ruta:
            self.ent_ruta.delete(0, tk.END)
            self.ent_ruta.insert(0, ruta)

    def _leer(self):
        try:
            contenido = LeerArchivo.leer(self.ent_ruta.get().strip())
        except IOError as error:
            contenido = str(error)
        self.txt.config(state="normal")
        self.txt.delete("1.0", tk.END)
        self.txt.insert(tk.END, contenido)
        self.txt.config(state="disabled")


if __name__ == "__main__":
    App().mainloop()