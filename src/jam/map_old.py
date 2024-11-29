from .tile import Tile

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QRectF
import sys


class Map:
    def __init__(self, n, m, default_colour="white"):
        #Inicjalizujacja obiektu Map jako tablicy n x m, gdzie kazda komorka to obiekt Tile.
        self.n = n
        self.m = m
        self.grid =[[Tile() for _ in range(m)] for _ in range(n)]

    def set_tile_colour(self, x, y, colour):
        if 0 <= x < self.n and 0 <= y < self.m:
            self.grid[x][y].colour = colour;
        else:
            raise IndexError("Invalid tile position.")

    def get_tile_colour(self, x, y):
        """
        Zwraca kolor płytki na pozycji (x, y).
        :param x: Indeks wiersza.
        :param y: Indeks kolumny.
        :return: Kolor płytki (string).
        """
        if 0 <= x < self.n and 0 <= y < self.m:
            return self.grid[x][y].colour
        else:
            raise IndexError("Invalid tile position.")
    def draw(self):
        app = QApplication(sys.argv)

        # Tworzymy główne okno aplikacji
        window = QMainWindow()
        window.setWindowTitle("Map Drawer")

        # Tworzymy scenę graficzną
        scene = QGraphicsScene()
        tile_size = 20  # Rozmiar każdej płytki w pikselach

        # Rysujemy każdą płytkę jako prostokąt na scenie
        for i in range(self.n):
            for j in range(self.m):
                colour = self.grid[i][j].colour
                rect = QGraphicsRectItem(j * tile_size, i * tile_size, tile_size, tile_size)
                rect.setBrush(QColor(colour))
                rect.setPen(QColor("black"))  # Opcjonalnie dodajemy obramowanie
                scene.addItem(rect)

        # Tworzymy widok sceny
        view = QGraphicsView(scene)
        window.setCentralWidget(view)

        # Ustawiamy rozmiar okna na podstawie rozmiaru mapy
        window.resize(self.m * tile_size + 20, self.n * tile_size + 40)

        # Wyświetlamy okno
        window.show()
        sys.exit(app.exec())

    def __repr__(self):
        return '\n'.join([' '.join([tile.colour for tile in row]) for row in self.grid])

