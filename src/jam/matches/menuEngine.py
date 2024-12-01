import json
import random

class ButtonIfClicked:
    def __init__(self):
        self.riddles = []
        self.used = []
    def Easy(self):
        """Funkcja wybierająca zagadki łatwe."""
        try:
            with open('scenes/matches.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.riddles = data['args_easy']['arg']
        except FileNotFoundError:
            print("Plik JSON nie został znaleziony.")
        except json.JSONDecodeError:
            print("Błąd wczytywania pliku JSON.")

    def Hard(self):
        """Funkcja uruchamiająca wybór zagadki trudnej."""
        try:
            with open('scenes/matches.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.riddles = data['args_hard']['arg']
        except FileNotFoundError:
            print("Plik JSON nie został znaleziony.")
        except json.JSONDecodeError:
            print("Błąd wczytywania pliku JSON.")

    def PickRiddle(self):
        """Wybiera losową zagadkę z listy bez powtarzania."""
        niewybrany = True
        while(niewybrany):
            riddle = random.choice(self.riddles)
            if riddle not in self.used:
                niewybrany=False
        self.used.append(riddle)  # Dodajemy do użytych
        riddle=(riddle['_arg1'],riddle['_arg2'])
        return riddle