import random

class StringDatabase:
    def __init__(self):
        self.words = None
        self.load_words()

    def load_words(self):
        try:
            with open("four_letters.txt", "r") as file:
                words = file.read().split()
                self.words = words
            return words
        except FileNotFoundError:
            print("Error: 'four_letters.txt' not found.")
            return []

    def get_random_word(self):
        val = random.choice(self.words)
        print(val)
        return val