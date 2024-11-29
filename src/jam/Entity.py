from .model import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QRectF
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsPixmapItem
from PyQt6.QtGui import QColor, QPixmap
from PyQt6.QtCore import QTimer


class Entity:
    def __init__(self, image_path):
        self.image_path = image_path  # Ścieżka do obrazka reprezentującego obiekt
        self.graphics_item = None
    def setPos(self, pos : Point):
        self.pos=pos;
    def initialize_graphics(self, scene, tile_size):
        #Dodaje graficzną reprezentację obiektu do sceny.
        pixmap = QPixmap(self.image_path)
        if pixmap.isNull():
            raise FileNotFoundError(f"Image file '{self.image_path}' not found or invalid.")
        pixmap = pixmap.scaled(tile_size, tile_size)  # Skalujemy obrazek do rozmiaru płytki
        self.graphics_item = QGraphicsPixmapItem(pixmap)
        self.graphics_item.setPos(self.pos.y * tile_size, self.pos.x * tile_size)  # Ustawiamy początkową pozycję
        scene.addItem(self.graphics_item)

    def move(self, new_x, new_y, duration_ms):
        if self.graphics_item is None:
            raise RuntimeError("Entity graphics not initialized. Call initialize_graphics first.")

        steps = 50  # Liczba kroków animacji
        dx = (new_x - self.pos.x) / steps
        dy = (new_y - self.pos.y) / steps
        interval = duration_ms / steps

        def update_position():
            nonlocal steps
            if steps > 0:
                self.pos.x += dx
                self.pos.y += dy
                self.graphics_item.setPos(self.pos.y * 40, self.pos.x * 40)
                steps -= 1
            else:
                timer.stop()

        timer = QTimer()
        timer.timeout.connect(update_position)
        timer.start(interval)
