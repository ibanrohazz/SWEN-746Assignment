""" 
@author: Ivan Rojas
"""
import random
from src.SpellingBee import SpellingBee

def get_user_input ():
    """
    Get the outer letters and center letter from the user.
    """
    outer_letters = input ("(without spaces): ").strip ().lower ()
    if len (outer_letters) != 6:
        print ("You must enter exactly 6 letters.")
        return None, None

    center_letter = input ("Enter the center letter: ").strip ().lower ()
    if len (center_letter) != 1:
        print ("You must enter exactly 1 letter.")
        return None, None

    letters = list (outer_letters) + [center_letter]
    return letters, center_letter

def main ():
    """ 
    Main function to run the Spelling Bee solver.
    """
    dictionary_path = '.\\src\\words_dictionary.json'  # Path to your dictionary file
    
    # Print the instructions
    print ("Welcome to the Spelling Bee solver!")
    print ("Enter the 6 outer letters")

    letters, center_letter = get_user_input ()
    if letters is None or center_letter is None:
        return
    
    game = SpellingBee (center_letter, letters, dictionary_path)
    best_words = game.return_best_word ()

    print ("Top 25 best words found:")
    for word in best_words:
        print (word)

if __name__ == "__main__":
    main ()