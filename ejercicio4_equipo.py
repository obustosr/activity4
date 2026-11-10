import tkinter as tk
from tkinter import ttk, messagebox


class Programador:
    def __init__(self, nombre, apellidos):
        self.__nombre = EquipoMaratonProgramacion.validar_campo(nombre, "nombre")
        self.__apellidos = EquipoMaratonProgramacion.validar_campo(
            apellidos, "apellido")

    def __str__(self):
        return f"{self.__nombre} {self.__apellidos}"


class EquipoMaratonProgramacion:
    TAMANO_MAXIMO = 3

    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.__nombre_equipo = self.validar_campo(nombre_equipo, "nombre del equipo",
                                                  permitir_digitos=True)
        self.__universidad = self.validar_campo(universidad, "nombre de la universidad")
        self.__lenguaje = self.validar_campo(lenguaje, "lenguaje de programación",
                                             permitir_digitos=True)
        self.__programadores = []

    @property
    def programadores(self):
        return list(self.__programadores)

    def esta_lleno(self):
        return len(self.__programadores) >= self.TAMANO_MAXIMO

    def _anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo ya tiene el máximo de 3 integrantes.")
        self.__programadores.append(programador)

    def agregar_programador(self, nombre, apellidos):
        self._anadir(Programador(nombre, apellidos))

    @staticmethod
    def validar_campo(campo, etiqueta="nombre", permitir_digitos=False):
        campo = campo.strip()
        if not campo:
            raise Exception(f"El {etiqueta} no puede estar vacío.")
        if not permitir_digitos and any(c.isdigit() for c in campo):
            raise Exception(f"El {etiqueta} no puede tener dígitos.")
        return campo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.7 - Equipo de maratón de programación")
        self.geometry("460x470")
        self.equipo = None
        self._crear_widgets()

    def _crear_widgets(self):
        marco = ttk.Frame(self, padding=10)
        marco.pack(fill="both", expand=True)

        datos = ttk.LabelFrame(marco, text="Datos del equipo")
        datos.pack(fill="x", pady=4)
        self.ent_equipo = self._campo(datos, "Nombre del equipo:", 0)
        self.ent_univ = self._campo(datos, "Universidad:", 1)
        self.ent_leng = self._campo(datos, "Lenguaje de programación:", 2)
        ttk.Button(datos, text="Crear equipo",
                   command=self._crear_equipo).grid(row=3, column=0, columnspan=2,
                                                    pady=6)

        integrante = ttk.LabelFrame(marco, text="Datos de los integrantes")
        integrante.pack(fill="x", pady=8)
        self.ent_nombre = self._campo(integrante, "Nombre del integrante:", 0)
        self.ent_apellidos = self._campo(integrante, "Apellidos del integrante:", 1)
        ttk.Button(integrante, text="Añadir integrante",
                   command=self._anadir_integrante).grid(row=2, column=0,
                                                          columnspan=2, pady=6)

        self.lbl_equipo = ttk.Label(marco, text="Aún no se ha creado el equipo.")
        self.lbl_equipo.pack(anchor="w")
        self.lista = tk.Listbox(marco, height=5)
        self.lista.pack(fill="x", pady=4)

    @staticmethod
    def _campo(padre, texto, fila):
        ttk.Label(padre, text=texto).grid(row=fila, column=0, sticky="e",
                                          padx=6, pady=4)
        entrada = ttk.Entry(padre, width=24)
        entrada.grid(row=fila, column=1, pady=4)
        return entrada

    def _crear_equipo(self):
        try:
            self.equipo = EquipoMaratonProgramacion(
                self.ent_equipo.get(), self.ent_univ.get(), self.ent_leng.get())
            self.lista.delete(0, tk.END)
            self.lbl_equipo.config(text=f"Equipo creado: {self.ent_equipo.get()}")
        except Exception as error:
            messagebox.showerror("Error al crear el equipo", str(error))

    def _anadir_integrante(self):
        if self.equipo is None:
            messagebox.showwarning("Equipo", "Primero debe crear el equipo.")
            return
        try:
            self.equipo.agregar_programador(self.ent_nombre.get(),
                                            self.ent_apellidos.get())
            self.lista.insert(tk.END, str(self.equipo.programadores[-1]))
            self.ent_nombre.delete(0, tk.END)
            self.ent_apellidos.delete(0, tk.END)
        except Exception as error:
            messagebox.showerror("Error al añadir integrante", str(error))


if __name__ == "__main__":
    App().mainloop()
