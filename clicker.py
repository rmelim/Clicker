"""
Este módulo contienen una clase para crear un juego visual simple en 
donde el jugador hará clic en todos los botones, los cuales se generas 
con números aleatorios únicos entre 1 y 999, en el orden impuesto por 
los números, desde el más bajo hasta el más alto.

El tablero generado consta de un temporizador que inicialmente muestra 0 
y se inicia cuando el usuario hace clic en el tablero por primera vez.

El juego busca ayudar al jugador a mejorar sus habilidades de percepción y 
memoria visual.

Autor
-----
Rui Duarte dos Santos Melim (rui.santos.melim@gmail.com)

Licencia
--------
Este proyecto está licenciado bajo los términos de la Licencia MIT.
"""

import tkinter as tk
from random import randint


class Clicker:
    """
    Una clase para crear el tablero del juego Clicker.

    Atributos
    ----------
    size : int
        El tamaño inicial del tablero (size x size).

    Métodos
    -------
    __init__(size=3):
        Inicializa el tablero con el tamaño dado.
    """

    def __init__(self, size=3):
        """
        Inicializa el tablero con el tamaño dado.

        Parámetros
        ----------
        size : int, opcional
            El tamaño inicial del tablero (por defecto es 3).
        """
        try:
            size = int(size)
            size = min(size, 10)  # Devuelve 10 si size es mayor a 10.
            size = max(size, 3)  #  Devuelve 3 si size es menor a 3.
        except (TypeError, ValueError):
            size = 3
        self.size = size
        self.__board = tk.Tk()
        self.__board.title("Clicker")
        self.__board.resizable(width=False, height=False)
        self.__numbers = self.__nums_generator__(size * size)
        self.__create_buttons__()
        self.__counter = tk.StringVar(value="0")
        self.__timer = tk.Label(self.__board, textvariable=self.__counter)
        self.__timer.grid(row=size + 1, column=0, columnspan=size)
        self.__id_job = ""

    def __nums_generator__(self, size):
        """
        Genera los números aleatorios únicos.

        Arguments:
            size -- Tamaño del tablero que indica la cantidad de números a generar.

        Returns:
            Una lista con los números generados.
        """
        nums = []
        i = 0
        while i < size:
            num = randint(1, 999)
            while num in nums:
                num = randint(1, 999)
            nums.append(num)
            i += 1
        return nums

    def __create_buttons__(self):
        """
        Crea todos los botones que ocuparán el tablero.
        """
        buttons = []
        size = len(self.__numbers)
        for i in range(size):
            row = i % int(size ** (1 / 2))
            col = i // int(size ** (1 / 2))
            buttons.append(tk.Button(self.__board, width=10))
            buttons[i].grid(row=row, column=col)
            buttons[i].bind("<Button-1>", self.__click__)
            buttons[i]["text"] = str(self.__numbers[i])
        self.__numbers.sort()

    def __update_timer__(self):
        """
        Establece el temporizador.
        """
        self.__counter.set(str(int(self.__counter.get()) + 1))
        self.__id_job = self.__board.after(1000, self.__update_timer__)

    def __click__(self, ev=None):
        """
        Controla el evento Click para cada uno de los botones en el tablero.

        Keyword Arguments:
            ev -- Referencia al objeto Button (default: {None}).
        """
        if self.__counter.get() == "0":
            self.__update_timer__()
        if int(ev.widget["text"]) == self.__numbers[0]:
            ev.widget.unbind("<Button-1>")
            ev.widget["state"] = tk.DISABLED
            del self.__numbers[0]
        if len(self.__numbers) == 0:
            self.__board.after_cancel(self.__id_job)

    def start(self):
        """
        Inicia el juego.
        """
        self.__board.mainloop()


def __main__():
    """
    Código Main Guard para hacer pruebas.
    """
    size = input("Tamaño de tablero: ")
    game = Clicker(size)
    game.start()


if __name__ == "__main__":
    __main__()
