""" 
@author: Ivan Rojas
"""

import json

class SpellingBee:
    """ 
    In the NYT Spelling bee game, 7 letters are arranged in a honeycomb shape.
    The player must form words using the 7 letters with the special caveat that
    the word must contain the center letter. The player must also form a word
    that uses at least 4 letters and exists in the english language.  In the 
    online version of the game, no profane words are allowed, however in this system
    we will not be checking for that.
    """
    
    def __init__(self, center, letters, dictionary_path):
        self.center = center
        self.letters = letters
        self.dictionary_path = dictionary_path
        self.load_dictionary()
        self.found_words = set()
        self.valid_words = []

    def load_dictionary(self):
        with open(self.dictionary_path, 'r') as file:
            self.words_dictionary = json.load(file)

    def is_valid_word(self, word):
        """
        A valid word must contain the center letter and be at least 4 letters long.
        word (string): The word to check. 
        return (int) 1 if the word is valid, 0 if the word is invalid,
        -1 if the word has already been found.
        """
        if len(word) < 4:
            return 0
        if self.center not in word:
            return 0
        if word in self.found_words:
            return -1
        if not self.is_in_library(word):
            return 0
        for letter in word:
            if letter not in self.letters:
                return 0
        self.found_words.add(word)
        return 1

    def is_in_library(self, word):
        """
        Check if a word is in the library of valid words.
        """
        return word in self.words_dictionary
    
    def return_found_words(self):
        """
        Return the set of found words.
        """
        return self.found_words
    
    def solve(self):
        """
        This method will solve the spelling bee game by finding all the possible
        words that can be formed using the 7 letters and the center letter.
        """
        self.valid_words = []
        for word in self.words_dictionary:
            if self.is_valid_word(word) == 1:
                self.valid_words.append(word)
        self.valid_words.sort(key=len, reverse=True)
        
    def return_best_word(self):
        """
        Return the best word that can be formed using the 7 letters and the center letter.
        """
        if not self.valid_words:
            self.solve()
        return self.valid_words[:25]  # Return the top 25 longest words