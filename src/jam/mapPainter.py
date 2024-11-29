from .map	import Map
from .model	import Point

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QRectF
import sys

class MapPainter(Map):
	TILE_SIZE = 20
	def __init__(self, size : Point):
		super().__init__(size)
		self.app = QApplication(sys.argv)

		self.window = QMainWindow()
		self.window.setWindowTitle("Map Drawer")

		self.scene = QGraphicsScene()

	def draw(self):
		for p in self.everyTilePoint():
			self.drawRect(p)
		view = QGraphicsView(self.scene)
		self.window.setCentralWidget(view)
		self.window.resize(
			self.size.x * self.TILE_SIZE + 20,
			self.size.y * self.TILE_SIZE + 40
		)

		self.window.show()
		sys.exit(self.app.exec())

	def drawRect(self, p : Point):
		colour = self.getTile(p).colour
		rect = QGraphicsRectItem(
			p.x * self.TILE_SIZE, p.y * self.TILE_SIZE,
			self.TILE_SIZE, self.TILE_SIZE
		)
		rect.setBrush(QColor(colour))
		rect.setPen(QColor("black"))  # Opcjonalnie dodajemy obramowanie
		self.scene.addItem(rect)
