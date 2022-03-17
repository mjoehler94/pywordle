# app.py ----------------

import json
from wordle import Wordle


def main():

    # while True:
    #     try:
    #         # wl = input(word_length_prompt)
    #         wl = "5"
    #         if 5 <= int(wl) <= 10:
    #             break
    #         else:
    #             print("Word length must be between 5 and 10 (inclusive")
    #     except Exception as e:
    #         print(f"Invalid entry: {wl}")
    #         print("Value must be an integer between 5 and 10 inclusive")

    # initialize dictionaries
    # with open("word_files/wordle_guess_dictionary.txt", 'r') as f:
    #     guess_dict = [x for x in f.read().split()]
    with open("word_files/words_of_length.json", "r") as f:
        guess_dict = json.load(f)["5"]

    with open("word_files/wordle_game_dictionary.txt", "r") as f:
        game_dict = [x for x in f.read().split()]

    # initialize wordle object
    # game = Wordle(guess_dictionary=guess_dict, game_dictionary=['tiger'])#]game_dict)
    game = Wordle(guess_dictionary=guess_dict, game_dictionary=game_dict)

    # start game
    game.play_game()

    return


if __name__ == "__main__":
    main()
