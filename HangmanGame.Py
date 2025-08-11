#Hangman Game Project

# Import the wanted Pyhton Module Python 3
import random
# from handman_guessing import guess_list # This line is commented out as the file is not available

# Pick and save the words to be guessed as a list
# Note: (all the words to be guessed consist of six letters)
# You need to define guess_list here or import it from a file.
guess_list = ["python", "coding", "colab", "pandas", "numpy"] # Example guess_list

# Use the imported Python module to pick a random word from the words you save.
guessing_word = random.choice(guess_list)
word_letters = len(guessing_word) # Corrected syntax for len()

# keep the game running until the game is over
game_over = False

# Applt tries to the PLayers to use to try to win
tries = 6
guessed_letters = []

# Hangman ASCII art stages
hangman_stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]


# Save game shapes in hangman_life.py file and import those shapes from file.
# You need to define game_name or import it from a file.
game_name = "Hangman" # Example game_name
print (game_name)

# Test the code you written until now using python print function.
print (f'The word you guessed is {guessing_word}')

# Game loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in guessing_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        tries -= 1
        print(f"Wrong guess! {guess} is not in the word. Tries left: {tries}")

    # Show current progress
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in guessing_word])
    print("Word: ", display_word)

    # Display hangman stage
    print(hangman_stages[6 - tries])


    # Check win condition
    if "_" not in display_word:
        print("🎉 You win! The word was:", guessing_word)
        game_over = True

    # Check lose condition
    if tries == 0:
        print("💀 You lost! The word was:", guessing_word)
        game_over = True

# Words for Hangman (all six letters)
# guess_list = ["lentil", "pepper", "onions", "tomato", "pickle", "garlic"] # This seems to be redefining guess_list after the game loop.
