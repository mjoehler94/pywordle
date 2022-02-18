# wordle.py --------------
import json
from mimetypes import guess_all_extensions
import random
from unittest.util import sorted_list_difference
import blessings


class Wordle:
    def __init__(self, guess_dictionary: list, game_dictionary=None) -> None:
        # TODO: consider making dictionary a dict to improve performance
        self.guess_dictionary = guess_dictionary
        self.game_words = game_dictionary if game_dictionary is not None else guess_dictionary
        self.game_word = random.choice(self.game_words).lower()
        self.word_len = len(self.game_word)
        self.max_guesses = self.determine_guess_count()
        self.current_guess_count = 0
        self.board = ["- " * self.word_len] * self.max_guesses
        self.is_game_over = False
        self.guessed_words = []

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
            word_to_guess = input(prompt).lower()
            if len(word_to_guess) != self.word_len:
                print(f"Invalid Entry: Guess must be {self.word_len} characers")
            elif word_to_guess not in self.guess_dictionary:
                print("Invalid Guess: Guess is not in dictionary")
            elif word_to_guess in self.guessed_words:
                print(f"'{word_to_guess}' has already been guessed")
            else:
                break
        return word_to_guess

    def update_board(self, guess):
        """
        add word to board
        update guess count
        check if game is over
        """
        # add word to board
        self.board[self.current_guess_count] = ''.join([letter.upper() + ' ' for letter in guess])
        # update guess count and guessed words list
        self.current_guess_count += 1
        self.guessed_words.append(guess)
        return

    def display_board(self):
        """use blessings module to display board with color hints
        """
        print(f"Game word is: {self.game_word}")  #TODO: remove after dev is complete
        print(*self.board, sep="\n")
        print()
        pass

    def play_game(self):
        print("Welcome to PyWordle! \U0001f600  \U0001F40D")

        while not self.is_game_over:

            # display board
            self.display_board()

            # prompt for next guess
            guess = self.get_guess()

            # update board
            self.update_board(guess)

            # check if game is over
            if self.current_guess_count == self.max_guesses or guess.lower() == self.game_word:
                self.is_game_over = True
        
        if self.game_word in self.guessed_words:
            print("You won :)")
        else:
            print("You lost :(")

            
        return
