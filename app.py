# app.py ----------------

import json
import curses
import time
from wordle import Wordle
import random


def main():

    print("Welcome to PyWordle! \U0001f600  \U0001F40D")
    word_length_prompt = "Enter your desired word length: "
    while True:
        try:
            # wl = input(word_length_prompt)
            wl = '5'
            if 5 <= int(wl) <= 10:
                break
            else:
                print("Word length must be between 5 and 10 (inclusive")
        except Exception as e:
            print(f"Invalid entry: {wl}")
            print("Value must be an integer between 5 and 10 inclusive")

    # initialize word bank
    with open("words_of_length.json", 'r') as f:
        word_bank = json.load(f)[wl]
    print(len(word_bank))
    

    # initialize wordle object
    game = Wordle(word_bank=word_bank, word_len=int(wl))
    
    # start game
    game.play_game()





    return


if __name__ == "__main__":
    main()
