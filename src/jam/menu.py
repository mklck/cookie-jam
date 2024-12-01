import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from .menuEngine import ButtonIfClicked


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.riddlemaker = ButtonIfClicked()
        # Ustawienia okna (kwadratowe)
        self.setWindowTitle("Menu")
        self.setFixedSize(400, 400)  # Okno kwadratowe
        self.setStyleSheet("background-color: #21201B;")  # Tło w kolorze ciemnym

        # Layout główny
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Logo
        logo_label = QLabel(self)
        pixmap = QPixmap('graphics/logo.png')  # Ścieżka do obrazka logo
        pixmap = pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        # Tekst
        text_label = QLabel("Wybierz poziom trudności:\n\n")
        text_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #f0e68c; font-family: 'Comic Sans MS';")
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(text_label)

        # Przyciski
        button_style = """
            QPushButton {
                background-color: #f0e68c;
                border: 1px solid black;
                border-radius: 25px;
                font-size: 18px;
                font-weight: bold;
                font-family: 'Comic Sans MS';
                color: black;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: beige;
            }
        """
        # Przyciski: Łatwy i Trudny
        latwy_button = QPushButton("Łatwy")
        trudny_button = QPushButton("Trudny")
        latwy_button.clicked.connect(lambda: self.handle_easy())
        trudny_button.clicked.connect(lambda: self.handle_hard())

        # Stylizacja i rozmiar przycisków
        latwy_button.setStyleSheet(button_style)
        trudny_button.setStyleSheet(button_style)

        latwy_button.setFixedSize(220, 75)  # Przyciski węższe i wyższe
        trudny_button.setFixedSize(220, 75)

        # Dodanie przycisków do layoutu
        layout.addWidget(latwy_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(trudny_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Ustawienie layoutu w oknie
        self.setLayout(layout)

    def handle_easy(self):
        self.riddlemaker.Easy()  # Wywołanie metody Easy
        self.close()  # Zamknięcie okna

    def handle_hard(self):
        self.riddlemaker.Hard()  # Wywołanie metody Hard
        self.close()  # Zamknięcie okna

# Główna aplikacja
#app = QApplication(sys.argv)
#window = MenuWindow()
#window.show()
#app.exec()
#print(ButtonIfClicked.PickRiddle(window.riddlemaker))
#sys.exit()