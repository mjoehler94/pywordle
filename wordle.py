# wordle.py --------------
import json
from mimetypes import guess_all_extensions
import random
from unittest.util import sorted_list_difference
import blessings

class Wordle():
    def __init__(self, word_bank: list, word_len: int=5) -> None:
        # TODO: consider making wordbank a dict to improve performance
        self.word_bank = word_bank
        self.word_len = word_len
        self.max_guesses = self.determine_guess_count()
        self.current_guess = 1
        self.board = ["- " * self.word_len] * self.max_guesses
        self.game_word = random.choice(self.word_bank)
        self.is_game_over = False
        with open("words_dictionary.json") as f:
            self.dictionary = json.load(f)
        return

    def determine_guess_count(self):
        if self.word_len <= 6:
            self.max_guesses = 6
        elif self.word_len <= 8:
            self.max_guesses = 7
        elif self.word_len <= 10:
            self.max_guesses = 8
        return self.max_guesses

    def get_guess(self):
        """
        get and validate guess from the user
        """
        while True:
            prompt = "Enter your guess: "
            word_to_guess = input(prompt)
            if len(word_to_guess) != self.word_len:
                print(f"Invalid Entry: Guess must be {self.word_len} characers")
            elif word_to_guess not in self.word_bank:
                print("Invalid Guess: Guess is not in dictionary")
            else:
                break
        return word_to_guess


        return word_to_guess

    def update_board(self, guess):
        """
        add word to board
        update guess count
        check if game is over
        """



        return


    def is_valid_word(self, word):
        return word in self.dictionary

    def play_game(self):
        while not self.is_game_over:
            # display board
            print(f"Game word is: {self.game_word}")
            print(*self.board, sep='\n')
            print()

            # prompt for next guess
            guess = self.get_guess()

            # update board
            self.update_board(guess)

            # check if game is over

            if self.is_game_over:
                break
            

        if self.max_guesses:
            print('You won!')
        else:
            print("You lost :(")
        return
