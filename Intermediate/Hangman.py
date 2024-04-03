"""
Summary:
This Python script implements a Hangman game where the player guesses letters or words to uncover a hidden word. The game randomly selects a word from a predefined list and allows the player to guess until they either guess the word correctly or run out of attempts. It utilizes ASCII art for displaying the Hangman's status and handles various user inputs and game states.

Libraries Used:
- random: For randomly selecting a word from the predefined list.
- predefined (custom module): Contains a list of words for the game.
- MAX_TRIES: Defines the maximum number of attempts allowed in the game.

Functions:
1. get_word(): Chooses a random word from the predefined list.
2. play(word): Executes the Hangman game logic.
3. update_word_completion(word, word_completion, guess): Updates the word completion based on the guessed letter.
4. display_hangman(tries): Displays Hangman ASCII art based on the remaining attempts.
5. main(): Main function to initiate the game, allowing the player to play multiple rounds.

Execution:
The script initiates the game by calling the main() function. After each round, it prompts the player if they want to play again and continues accordingly.
"""

import json
import random


MAX_TRIES = 6


def get_words_from_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data["word_list"]

word_list = get_words_from_json("intermediate/words.json")


def get_word():
    """Choose a random word from the list."""
    return random.choice(word_list).upper()


def play(word):
    """Play Hangman game."""
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = MAX_TRIES

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word, or type 'HINT' for a hint: ").upper()

        if guess == "HINT":
            print("Here's a hint: The word starts with '{}' and has {} letters.".format(word[0], len(word)))
            continue

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_completion = update_word_completion(word, word_completion, guess)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")


def update_word_completion(word, word_completion, guess):
    """Update word completion based on guessed letter."""
    updated_completion = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        updated_completion[index] = guess
    return "".join(updated_completion)


def display_hangman(tries):
    """Display Hangman ASCII art based on remaining tries."""
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """,
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
