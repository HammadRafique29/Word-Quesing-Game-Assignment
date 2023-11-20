import os
from StringDatabase import StringDatabase
from Guess import Guess
from Game import Game

def main():
    os.system("cls")
    print(f"\t\t{'#'*40} The Great Guessing Game {'#'*40}")
    
    mode_choice = input("\n\t\tChoose a mode (1 for Play mode, 2 for Test mode): ")

    if mode_choice == "1":
        test_mode = False
    elif mode_choice == "2":
        test_mode = True
    else:
        print("Invalid choice. Exiting.")
        return

    game = Game()
    game.play_game(test_mode)


if __name__ == "__main__":
    main()