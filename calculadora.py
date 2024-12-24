import tkinter as tk
from tkinter import messagebox
import math
import threading
import time

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora boris")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#17181A")
        
        self.entrada = tk.StringVar()
        self.historial = tk.StringVar()
        self.mensaje_visible = False
        self.crear_widgets()
        
    def mostrar_mensaje_temporal(self):
        if not self.mensaje_visible:
            self.mensaje_visible = True
            mensaje = messagebox.showinfo("Mensaje", "Esta calculadora esta hecho por boris dixon valverde arreaga =)")
            threading.Thread(target=self.cerrar_mensaje, args=(5,)).start()

    def cerrar_mensaje(self, delay):
        time.sleep(delay)
        self.mensaje_visible = False
        self.root.quit()

    def crear_widgets(self):
        fuente_historial = ("Comic Sans MS", 14)
        fuente_entrada = ("Comic Sans MS", 36, "italic")
        fuente_boton = ("Comic Sans MS", 20,"italic")

        main_frame = tk.Frame(self.root, bg="#17181A")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        historial_label = tk.Label(
            main_frame,
            textvariable=self.historial,
            font=fuente_historial,
            bg="#17181A",
            fg="#666666",
            anchor="e",
            justify="right"
        )
        historial_label.pack(fill="x", pady=(0, 10))

        entrada_frame = tk.Frame(main_frame, bg="#17181A")
        entrada_frame.pack(fill="x", pady=(0, 20))
        
        entrada_cuadro = tk.Entry(
            entrada_frame,
            textvariable=self.entrada,
            font=fuente_entrada,
            justify="right",
            bd=0,
            bg="#17181A",
            fg="white",
            insertbackground="white"
        )
        entrada_cuadro.pack(fill="x")

        tk.Frame(main_frame, height=2, bg="#333333").pack(fill="x", pady=(0, 20))

        botones_frame = tk.Frame(main_frame, bg="#17181A")
        botones_frame.pack(expand=True, fill="both")

        for i in range(5):
            botones_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            botones_frame.grid_columnconfigure(i, weight=1)

        botones = [
            ("C", 0, 0, "#E0B0FF"),
            ("⌫", 0, 1, "#FF5252"),
            ("()", 0, 2, "#FFD700"),
            ("÷", 0, 3, "#4CAF50"),
            ("7", 1, 0, "#2D2D2D"),
            ("8", 1, 1, "#2D2D2D"),
            ("9", 1, 2, "#2D2D2D"),
            ("×", 1, 3, "#4CAF50"),
            ("4", 2, 0, "#2D2D2D"),
            ("5", 2, 1, "#2D2D2D"),
            ("6", 2, 2, "#2D2D2D"),
            ("−", 2, 3, "#4CAF50"),
            ("1", 3, 0, "#2D2D2D"),
            ("2", 3, 1, "#2D2D2D"),
            ("3", 3, 2, "#2D2D2D"),
            ("+", 3, 3, "#4CAF50"),
            ("🚜", 4, 0, "#2D2D2D"),
            ("0", 4, 1, "#2D2D2D"),
            (".", 4, 2, "#2D2D2D"),
            ("=", 4, 3, "#2196F3")
        ]

        for texto, fila, columna, color in botones:
            boton = tk.Button(
                botones_frame,
                text=texto,
                font=fuente_boton,
                bg=color,
                fg="white",
                bd=0,
                relief="flat",
                activebackground="#444444",
                activeforeground="white",
                command=self.obtener_comando(texto)
            )
            boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

    def obtener_comando(self, texto):
        comandos = {
            "=": self.calcular,
            "C": self.limpiar,
            "⌫": self.borrar_ultimo,
            "()": self.agregar_parentesis,
            "×": lambda: self.agregar_texto("*"),
            "÷": lambda: self.agregar_texto("/"),
            "−": lambda: self.agregar_texto("-"),
            "🚜": self.mostrar_mensaje_temporal
        }
        return comandos.get(texto, lambda: self.agregar_texto(texto))

    def agregar_texto(self, texto):
        self.entrada.set(self.entrada.get() + texto)

    def limpiar(self):
        self.entrada.set("")
        self.historial.set("")

    def borrar_ultimo(self):
        actual = self.entrada.get()
        self.entrada.set(actual[:-1])

    def agregar_parentesis(self):
        actual = self.entrada.get()
        if actual.count("(") > actual.count(")"):
            self.entrada.set(actual + ")")
        else:
            self.entrada.set(actual + "(")

    def calcular(self):
        try:
            expresion = self.entrada.get()
            self.historial.set(expresion)
            resultado = eval(expresion)
            self.entrada.set(str(resultado))
        except Exception:
            self.entrada.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()