import os
# from Game import Game
import time

class Guess:
    def __init__(self, word):
        self.word = word
        self.current_guess = ["-" for _ in word]
        self.letters_guessed = set()

    def display_menu(self):
        print("\n\t\t\t1. Guess\n\t\t\t2. Tell me\n\t\t\t3. Letter\n\t\t\t4. Quit")

    def display_status(self):
        print("\n\t\t\tCurrent Guess:", " ".join(self.current_guess))
        print("\t\t\tLetters Guessed:", ", ".join(sorted(self.letters_guessed)))

    def guess_word(self, guessed_word):
        if guessed_word.lower() == self.word.lower():
            return True
        return False

    def guess_letter(self, letter):
        if letter.lower() in self.letters_guessed:
            print(f"\t\t\tYou already guessed the letter '{letter}'. Try again.")
        elif letter.lower() in self.word.lower():
            print(f"\t\t\tGood guess! '{letter}' is in the word.")
            self.update_current_guess(letter.lower())
            self.display_letter_frequency(letter.lower())  # Uncomment if needed
        else:
            print(f"\t\t\tSorry, '{letter}' is not in the word.")
        self.letters_guessed.add(letter.lower())

    def display_letter_frequency(self, letter):
        frequency = self.calculate_letter_points(letter)
        print(f"\t\t\tFrequency of '{letter}': {frequency:.2%}")

    def update_current_guess(self, letter):
        for i in range(len(self.word)):
            if self.word[i].lower() == letter:
                self.current_guess[i] = letter

    def tell_me(self):
        
        os.system("cls")
        # # print(f"\t\t{'#'*(40+25)}{'#'*40}")
        print(f"\t\t{'#'*40} The Great Guessing Game {'#'*40}")
        # print(f"\t\t{'#'*(40+25)}{'#'*40}")
        
        print("\n\n\t\t\t###############################################################################")
        print("\t\t\tYou give up and ask the game to show you the correct word.")
        print(f"\t\t\tThe correct word is: {self.word}")

    def calculate_score(self):
        total_letters = len(self.word)
        if total_letters == 0:
            return 0

        return sum([self.calculate_letter_points(letter) for letter in self.word]) / 4

    def display_final_report(self, score):
        
        print("\n\t\t\tFinal Report:")
        print(
            "\t\t\t{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                "Word", "Status", "Bad Guesses", "Missed Letters", "Latest Result"
            )
        )
        word = self.word
        current_guess = self.current_guess
        letters_guessed = self.letters_guessed
        final_status = "Correct" if "-" not in current_guess else "Give Up"
        bad_guesses = (len(letters_guessed) - current_guess.count("-")) - 4
        missed_letters = current_guess.count("-")
        negativescore = bad_guesses * 0.10
        scoree = score
        # print("SCOREEE",scoree)
        new_rsl = (scoree * 100) - (negativescore)
        # print("SCOREEE",scoree)
        # print("Negative Score ",negativescore)
        # print("NEW SCORE: ",new_rsl)
        # f"{score:.2%}"
        print(
            "\t\t\t{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                word, final_status, bad_guesses, missed_letters, new_rsl
            )
        )
        

    def display_letter_frequencies(self):
        letter_frequencies = self.calculate_letter_frequencies()
        print("Letter Frequencies:")
        for letter, frequency in letter_frequencies.items():
            print(f"{letter}: {frequency:.2%}")

    def calculate_letter_frequencies(self):
        letter_frequencies = {}
        for letter in self.word:
            if letter.isalpha():
                letter_frequencies[letter] = letter_frequencies.get(letter, 0) + 1

        total_occurrences = sum(letter_frequencies.values())
        letter_frequencies_percentage = {
            letter: count / total_occurrences
            for letter, count in letter_frequencies.items()
        }

        return letter_frequencies_percentage

    def calculate_letter_points(self, letter):
        letter_frequencies = {
            "a": 8.17,
            "b": 1.49,
            "c": 2.78,
            "d": 4.25,
            "e": 12.70,
            "f": 2.23,
            "g": 2.02,
            "h": 6.09,
            "i": 6.97,
            "j": 0.15,
            "k": 0.77,
            "l": 4.03,
            "m": 2.41,
            "n": 6.75,
            "o": 7.51,
            "p": 1.93,
            "q": 0.10,
            "r": 5.99,
            "s": 6.33,
            "t": 9.06,
            "u": 2.76,
            "v": 0.98,
            "w": 2.36,
            "x": 0.15,
            "y": 1.97,
            "z": 0.07,
        }

        return letter_frequencies.get(letter.lower(), 0.0) / 100

    def play(self, test_mode):
        os.system("cls")
        if test_mode:
            print("\n\t\t\tTest Mode: The correct word is:", self.word)
            print("\t\t\tNow you can continue with the game.")

        while "-" in self.current_guess:
            print("\033[2J\033[;H", end="")
            print(f"\t\t{'#'*40} The Great Guessing Game {'#'*40}")
            
            if test_mode:
                print("\n\t\t\tTest Mode: The correct word is:", self.word)
                print("\t\t\tNow you can continue with the game.")
            
            self.display_status()
            self.display_menu()
            choice = input("\n\t\t\tEnter your choice (1-4): ")

            if choice == "1":
                print(f"\n\t\t\t{'#'*80}")
                guessed_word = input("\t\t\t### Enter your guess for the whole word: ")
                if self.guess_word(guessed_word):
                    print("\t\t\tCongratulations! You guessed the word.")
                    score = self.calculate_score()
                    print(f"\t\t\tYour score for this game is: {score:.2f}")
                    self.display_final_report(score)
                    print(f"\t\t\t{'#'*80}")
                    return
                else:
                    print("\t\t\tSorry, incorrect guess. Keep trying!")
                    print(f"\t\t\t{'#'*80}")
                    time.sleep(2)
                

            elif choice == "2":
                self.tell_me()
                score = self.calculate_score()
                print(f"\n\t\t\tYour score for this game is: {score:.2f}")
                self.display_final_report(score)
                print(f"\n\t\t\t{'#'*80}")
                return

            elif choice == "3":
                print(f"\n\t\t\t{'#'*45}")
                letter = input("\t\t\tEnter a letter to guess: ")
                self.guess_letter(letter)
                print(f"\n\t\t\t{'#'*45}")

            elif choice == "4":
                print(f"\n\t\t\t{'#'*45}")
                print("\t\t\tTHANKS FOR PLAYING! GOODBYE...")
                print(f"\t\t\t{'#'*45}\n")
                return

            else:
                print("\t\t\tInvalid choice. Please choose again.")

        print("\t\t\tCongratulations! You guessed the word:", self.word)
        score = self.calculate_score()
        print("\t\t\tYour score for this game is ", score * 100)
        self.display_final_report(score)
        return score