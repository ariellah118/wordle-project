
#######################################################
# wordle
#########################################################

# This is the "main" portion of your game.
# Any code that uses stdin or stdout (i.e., input() and print())
# should go in this file.

import wordle_engine
import random
import sys


# Print a greeting
print(wordle_engine.welcome_string())

# Load the list of valid words
valid_words = wordle_engine.load_words("combined_wordlist.txt")

# Use the target word provided on the command line,
# or, choose a random word if no target word given.
if len(sys.argv) >= 2:
    target = sys.argv[1]
else:
    # TODO choose a random word from valid_words
    target = 'alter'  # <== change this

# TODO Implement the rest of the game.
# Remember:
#   * Guesses must be exactly 5 letters
#   * Guesses must be valid words
#   * Players get at most 6 guesses
#   * Please display the entire history of guesses before each prompt.
#   * Print a message at the end of the game indicating whether the player won or lost.
#      * If the player wins, display the entire sequence of guesses as part of the final message.
    turns = 0
    guesses = ''
    letter_status = wordle_engine.create_letter_status()
    while turns < 6:
        turns += 1  # increment the amount of turns
        guess = input(f"Make a guess ({wordle_engine.format_letters(letter_status)}): ")  # get a guess from the user
        while guess not in valid_words:  # if the guess isn't in the list of valid words then keep asking until get a valid guess
            if len(guess) != 5:
                print("Your guess must be 5 letters.")
            else:
                print("Your guess is not a valid word.")
            guess = input(f"Make a guess ({wordle_engine.format_letters(letter_status)}): ")
        formatted_guess = wordle_engine.format_guess(target, guess)
        wordle_engine.update_letter_status(letter_status, target, guess)
        guesses += str(turns) + '. ' + formatted_guess + '\n'
        if guess == target:
            print(guesses + 'You win!')
            break
        print(guesses)
    if turns == 6:
        print("You lose!")
