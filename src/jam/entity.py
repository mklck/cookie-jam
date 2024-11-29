from .model import *

from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap

class Entity:
	def __init__(self, path : str):
		self.path = path
		self.pixmap = QPixmap(self.path)
		if self.pixmap.isNull():
			raise FileNotFoundError(path)

	def setPos(self, pos : Point):
		self.pos=pos

	def getGItem(self, tileSize):
		pixmap = self.pixmap.scaled(tileSize, tileSize)
		graphicsItem = QGraphicsPixmapItem(pixmap)
		graphicsItem.setPos(
			self.pos.y * tileSize,
			self.pos.x * tileSize
		)
		return graphicsItem
