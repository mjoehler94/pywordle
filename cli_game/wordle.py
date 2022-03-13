# wordle.py --------------
import random
from blessings import Terminal


class Wordle:
    def __init__(self, guess_dictionary: list, game_dictionary=None) -> None:
        # TODO: consider making dictionary a dict to improve performance
        self.guess_dictionary = guess_dictionary
        self.game_words = (
            game_dictionary if game_dictionary is not None else guess_dictionary
        )
        self.game_word = random.choice(self.game_words).lower()
        self.word_len = len(self.game_word)
        self.max_guesses = self.determine_guess_count()
        self.current_guess_count = 0
        self.board = ["-" * self.word_len] * self.max_guesses
        self.is_game_over = False
        self.guessed_words = []
        self.term = Terminal()

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
            if word_to_guess == "quit":
                self.is_game_over = True
                return " " * self.word_len
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
        self.board[self.current_guess_count] = "".join([letter for letter in guess])
        # update guess count and guessed words list
        self.current_guess_count += 1
        self.guessed_words.append(guess)
        return

    def display_board(self):
        """
        use blessings module to display board with color hints
        Logic: if letter not in word print as normal

        """
        if self.current_guess_count:
            print(self.term.clear())

        # print(f"Game word is: {self.game_word}")  # TODO: remove after dev is complete

        colored_word = "\n"
        for word in self.board:
            already_found_letters = []
            for i, letter in enumerate(word):
                test = "norm"
                if letter == self.game_word[i]:
                    colored_word += (
                        self.term.green + letter.upper() + self.term.normal + " "
                    )
                    already_found_letters.append(letter)
                    test = "green"
                elif letter in self.game_word and letter not in already_found_letters:
                    colored_word += (
                        self.term.yellow + letter.upper() + self.term.normal + " "
                    )
                    already_found_letters.append(letter)
                    test = "yellow"
                else:
                    colored_word += letter.upper() + " "
                    test = "normal"
                # print(i, letter, self.game_word[i], test)

            colored_word += self.term.normal + "\n"

        print(colored_word)
        # print(*board, sep="\n")
        return

    def play_game(self):
        # print("Welcome to PyWordle! \U0001f600  \U0001F40D")
        print(self.term.clear())

        while not self.is_game_over:

            # display board
            self.display_board()

            # prompt for next guess
            guess = self.get_guess()

            # update board
            self.update_board(guess)

            # check if game is over
            if (
                self.current_guess_count == self.max_guesses
                or guess.lower() == self.game_word
            ):
                self.is_game_over = True
                self.display_board()

        if self.game_word in self.guessed_words:
            print("You won :)")
        else:
            print("You lost :(")
        print(f"The word was: {self.game_word}")

        return
