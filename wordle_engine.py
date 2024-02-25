
#######################################################
# wordle_engine
#########################################################


# Container for color control codes.
class wordle_colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

wordle_alphabet = "abcdefghijklmnopqrstuvwxyz"

def welcome_string():
    return (f"Welcome to {wordle_colors.GREEN}W{wordle_colors.RED}o{wordle_colors.BLUE}r{wordle_colors.YELLOW}d"
            f"{wordle_colors.CYAN}l{wordle_colors.MAGENTA}e{wordle_colors.ENDC}"
            )

def create_letter_status():
    """ Initialize and Return a new dictionary that maps each letter to
        wordle_colors.BLUE """
    letter_status = {}
    for i in range(len(wordle_alphabet)):
        letter_status[wordle_alphabet[i]] = wordle_colors.BLUE
    return letter_status

def load_words(filename: str):
    """ Load the words from the specified file and place them
        in a set.
        Ignore any lines that begin with "#"
        """
    set_of_words = set()  # create a set to put each word from file
    with open(filename, 'rt') as file:  # open file
        for row in file:
            r = row.strip()
            if not r.startswith("#"):  # if the line in the file starts with # skip that line
                set_of_words.add(row.rstrip())  # otherwise add that line to the set
    return set_of_words

def format_guess(target, guess):
    """ Return a string that contains the user's guess formatted
        so that each letter is colored
        * GREEN:  The letter is placed correctly.
        * YELLOW: The letter appears in the target word,
                  but in a different location.
        * RED:    The letter does not appear in the target word
        Also, the string should end with wordle_colors.ENDC """
    new_string = ''
    for i in range(len(guess)):  # iterate through the guess
        if guess[i] == target[i]:  # if there is a letter placed correctly
            new_string += wordle_colors.GREEN + guess[i]
        elif guess[i] in target:  # if the letter is in the target word
            new_string += wordle_colors.YELLOW + guess[i]
        else:  # the letter doesn't exist in the target word
            new_string += wordle_colors.RED + guess[i]
    return new_string + wordle_colors.ENDC

def update_letter_status(letter_status, target, guess):
    """ Update the letter status dictionary to show which letters
        have been used and whether they appear in the target word.
        Specifically:
        * BLUE:   Letter has not been used in a guess
        * GREEN:  Letter appears in the correct location in some guess.
        * YELLOW: Letter is in the target word and appears in some guess
                  (but not in the correct location)
        * RED:    Letter does  not appear in the target word, but has
                  been used in at least one guess."""
    for i in range(len(guess)):  # iterate through the guess
        if guess[i] == target[i]:  # if there is a letter placed correctly
            letter_status[guess[i]] = wordle_colors.GREEN
        elif guess[i] in target:  # if the letter is in the target word
            letter_status[guess[i]] = wordle_colors.YELLOW
        else:  # the letter doesn't exist in the target word
            letter_status[guess[i]] = wordle_colors.RED
    return letter_status

def format_letters(alphabet_dict):
    """ Generate a string that lists all the letters of the alphabet
        colored according to the rules given in update_letter_status.
        the string should end with wordle_colors.ENDC """
    new_string = ''
    for letter in alphabet_dict:  # iterate through the dict
        new_string += alphabet_dict[letter] + letter  # add what color and the letter that each char in the string should be
    return new_string + wordle_colors.ENDC
