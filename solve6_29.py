# got stuck after 3 guesses: trace, aloud, and hanky
# a, k, y are in the right spot


import json


def is_eligible(word: str) -> bool:
    is_valid = False
    gray = "trceloudhn"
    if (
        word[1] == "a"
        and word[3] == "k"
        and word[4] == "y"
        and not any([letter in word for letter in gray])
    ):
        is_valid = True
    return is_valid


def main():
    # create list of words
    # with open("word_files/wordle_guess_dictionary.txt") as f:
    #     guesses = [word.strip() for word in f.readlines()]
    with open("word_files/words_of_length.json") as f:
        guesses = json.load(f)["5"]

    valid_guesses = []
    for g in guesses:
        if is_eligible(g):
            valid_guesses.append(g)
    print(f"Total words that fit: {len(valid_guesses)}")
    print(valid_guesses)

    return


if __name__ == "__main__":
    main()
