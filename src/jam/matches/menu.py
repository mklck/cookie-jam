import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from .menuEngine import ButtonIfClicked


class MenuWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.riddlemaker = ButtonIfClicked()
		self.riddle = None
		self.ready = False

		self.setWindowTitle("Menu")
		self.setStyleSheet("background-color: #21201B;")

		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

		self.initLogo()
		self.initText()
		self.initButtons()
		self.setLayout(self.layout)

	def initLogo(self):
		logo_label = QLabel(self)
		pixmap = QPixmap('graphics/logo.png')
		pixmap = pixmap.scaled(
			300, 300,
			Qt.AspectRatioMode.KeepAspectRatio,
			Qt.TransformationMode.SmoothTransformation
		)
		logo_label.setPixmap(pixmap)
		logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.layout.addWidget(logo_label)

	def initText(self):
		text_label = QLabel("Wybierz poziom trudności:\n\n")
		text_label.setStyleSheet("font-size: 40px; font-weight: bold; color: #f0e68c; font-family: 'Comic Sans MS';")
		text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.layout.addWidget(text_label)

	def initButtons(self):
		button_style = """
		    QPushButton {
		        background-color: #f0e68c;
		        border: 1px solid black;
		        border-radius: 25px;
		        font-size: 40px;
		        font-weight: bold;
		        font-family: 'Comic Sans MS';
		        color: black;
		        padding: 50px;
		    }
		    QPushButton:hover {
		        background-color: beige;
		    }
		"""
		latwy_button = QPushButton("Łatwy")
		trudny_button = QPushButton("Trudny")
		latwy_button.clicked.connect(self.handleEasy)
		trudny_button.clicked.connect(self.handleHard)

		latwy_button.setStyleSheet(button_style)
		trudny_button.setStyleSheet(button_style)

		self.layout.addWidget(latwy_button, alignment=Qt.AlignmentFlag.AlignCenter)
		self.layout.addWidget(trudny_button, alignment=Qt.AlignmentFlag.AlignCenter)

	def handleEasy(self):
		self.riddlemaker.Easy()
		self.ready = True

	def handleHard(self):
		self.riddlemaker.Hard()
		self.ready = True

	def getRiddle(self):
		return self.riddlemaker.PickRiddle()
