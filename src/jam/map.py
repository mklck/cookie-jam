from .tile	import Tile
from .model	import Point
from itertools	import product

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QRectF
import sys


class Map:
	def __init__(self, size : Point, default_colour="white"):
		self.size = size
		self.grid =[[Tile() for _ in range(size.x)] for _ in range(size.y)]

	def setTileColour(self, p : Point, colour):
		t = self.getTile(p)
		t.colour = colour

	def validPoint(self, p : Point):
		cond0 = 0 <= p.x < self.size.x
		cond1 = 0 <= p.y < self.size.y
		return cond0 and cond1

	def getTile(self, p : Point):
		if not self.validPoint(p):
			raise IndexError(f"Invalid position {p}")
		return self.grid[p.x][p.y]

	def everyTilePoint(self):
		for x, y in product(range(self.size.x), range(self.size.y)):
			yield Point(x, y)

class MapPainter:
	TILE_SIZE = 20
	def __init__(self):
		self.map = Map(size=Point(60, 60))
		self.app = QApplication(sys.argv)

		self.window = QMainWindow()
		self.window.setWindowTitle("Map Drawer")

		self.scene = QGraphicsScene()

	def draw(self):
		for p in self.map.everyTilePoint():
			self.drawRect(p)
		view = QGraphicsView(self.scene)
		self.window.setCentralWidget(view)
		self.window.resize(
			self.map.size.x * self.TILE_SIZE + 20,
			self.map.size.y * self.TILE_SIZE + 40
		)

		self.window.show()
		sys.exit(self.app.exec())

	def drawRect(self, p : Point):
		colour = self.map.getTile(p).colour
		rect = QGraphicsRectItem(
			p.x * self.TILE_SIZE, p.y * self.TILE_SIZE,
			self.TILE_SIZE, self.TILE_SIZE
		)
		rect.setBrush(QColor(colour))
		rect.setPen(QColor("black"))  # Opcjonalnie dodajemy obramowanie
		self.scene.addItem(rect)
