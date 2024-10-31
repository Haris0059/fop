# Develop a Hangman game where the player guesses letters of a hidden word. 
# Implement functions to handle guessing logic, tracking wrong guesses, and displaying the current state of the word.
import os

def clear_terminal():
    # Check the operating system and run the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


def hidden():    
    hidden_word = str(input("Enter your hidden word for hangman game: "))
    return hidden_word

def display(hidden_word):
    print("This is Hangman game!")
    length_word = "_ " * len(hidden_word)
    print(length_word)
    return hidden_word

def guess(hidden_word):
    
    while True:       
        letter = str(input("Enter one letter: "))
        test_word = ""
    
        for i in hidden_word:
            if letter == i:
                test_word = test_word + letter + " "
                # print(letter ,end=" ")
            else:
                test_word  = test_word + "_" + " "
                # print("_", end=" ")
        print(test_word)

guess(display(hidden()))



