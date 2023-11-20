import os
from StringDatabase import StringDatabase
from Guess import Guess

class Game:
    def __init__(self):
        self.games_played = []

    def play_game(self, test_mode):
        playing = True
        while playing:
            string_database = StringDatabase()
            word = string_database.get_random_word()
            guess = Guess(word)
            score = guess.play(test_mode)
            self.games_played.append((word, score))

            play_again = input("\t\t\tPlay again (y/n)? ")
            if play_again.lower() != "y":
                playing = False
                self.display_summary()

    def display_summary(self):
        print(f"\n\t\t\t{'-' * 25}")
        print("\t\t\tFINAL REPORT")
        
        total_score = 0
        for word, score in self.games_played:
            if score:
                score = score * 100
                print(f"{word}: {score:.2f}")
                total_score += score
            else: score = 0
        print(f"\n\t\t\tTotal Score: {total_score:.2f}")
        print(f"\t\t\t{'-' * 25}")


