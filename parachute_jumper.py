# CSE 210 Week 03 Teach Designer: parachute_jumper game. Author: David A. Fajardo.
"""Jumper is a game in which the player seeks to solve a puzzle 
by guessing the letters of a secret word one at a time.
Rules of the game:
The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over.
If the player has no more parachute the game is over."""
import csv
import random
words = []
guessable_words = []
hidden_word = []
guessed_letters = ['_', '_', '_', '_', '_']
guessed_letters_original = ['_', '_', '_', '_', '_']
parachute_items =['  ___', ' /___\\', (' \\   /'), ('  \\ /'), ('   O'), ('  /I\\'), ('  / \\')]
parachute_items_original = ['  ___', ' /___\\', (' \\   /'), ('  \\ /'), ('   O'), ('  /I\\'), ('  / \\')]
class All_words:
    def __init__(self):
        """Get one thousand words from the file 
        http://www.rupert.id.au/resources/1000-words-csv.csv"""
        self.file =  "thousand-words.csv"  
        self.words_data_base()    
    def words_data_base(self):
        with open ("thousand-words.csv", "r") as self.file:
            csv_reader = csv.reader(self.file)
            for row in csv_reader:
                new_row = list(row)
                words.append(new_row[-1])
        #print(words)

class Five_letters_words(All_words):
    """Make an array with  five-letters words."""
    
    def __init__(self):
        
        self.five_letters_words()
        
    def five_letters_words(self):
        for i in range(len(words)):
            if len(words[i]) == 5:
                guessable_words.append(words[i])
        # print(guessable_words)
        
class Word_to_guess(Five_letters_words):
    """Choose the word to guess form the guessable_words array
    with the random.choice() method."""
  
    def __init__ (self): 
                
        self.word = random.choice(guessable_words)
        hidden_word.append(self.word)
        # print(hidden_word)
        
class Start (Word_to_guess):
    """Class that starts and ends the game."""
    
    def __init__(self):
        
        self.word_to_guess = hidden_word[-1]
        print(self.word_to_guess)
        self.letters_of_word = list(self.word_to_guess)
        print(self.letters_of_word)
        self.start_game()
    
    def start_game(self):
        while len(parachute_items)>2:
            self.start = input(f'Guess a letter [a-z]: ')
            print()
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == self.start:
                    guessed_letters[i] = self.start
            print(guessed_letters)
            print()
            letter_added = ' '.join(guessed_letters)
            print(letter_added)
            print()
            for i in parachute_items_original:
                print(i)
            print()
            
            if guessed_letters == guessed_letters_original:
                parachute_items.pop(0)
                parachute_items_original.pop(0)
                for i in range(len(parachute_items_original)):
                    parachute_items_original[i] = parachute_items[i]
                print(letter_added)
                print()        
                for i in parachute_items_original:
                    print (i)
            else:
                for i in range(len(guessed_letters_original)):
                    guessed_letters_original[i] = guessed_letters[i]
                print(guessed_letters_original)
                print()    
                if guessed_letters == self.letters_of_word:
                    print(f'Good job! Game over!')
                    exit()
            
            
        

def main():
    All_words()
    Five_letters_words()
    Word_to_guess()
    Start()

print('_ _ _ _ _')

print('  ___')
print(' /___\\')
print(' \\   /')
print('  \\ /')
print('   O')
print('  /I\\')
print('  / \\')

if   __name__ == "__main__":
    main()
      
    