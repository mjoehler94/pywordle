# got stuck on 3rd guess on 6_10_22
# after guessing trace, then slept I had e in the right spot and p,t in the wrong spots
# I couldn't think of another eligible word (hard mode)

import json

def is_eligible(word: str) -> bool:
    is_valid = False
    if (
        word[2] == "e"
        and "p" in word
        and "t" in word
        and "t" not in [word[0], word[4]]
        and "p" not in [word[3]]
        and "s" not in word
        and "r" not in word
        and "a" not in word
        and "c" not in word
        and "l" not in word
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
