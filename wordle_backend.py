import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import string

class wordle():
    def __init__(self):
        path1 = "asset/wordle-words.txt"
        path2 = "asset/wordle-answers.txt"
        self.allword_list = []
        self.answer_list = []

        self.green_words = set()
        self.yellow_words = set()
        self.grey_words = set()

        self.green_current = []
        self.yellow_current = []
        self.grey_current = []

        self.trial = 0
        char_str = string.ascii_lowercase

        with open(path1) as file_obj:
            for line in file_obj:
                word = line.strip()
                self.allword_list.append(word)
        with open(path2) as file_obj:
            for line in file_obj:
                word = line.strip()
                self.answer_list.append(word)

    def choose_word(self):
        self.wordToday = random.choice(self.allword_list)

    def guess(self):
        guess_word = input("Enter your guess word: ")
        if guess_word not in self.allword_list:
            print("Not in word list")
            return

        green = [0] * 5
        yellow = [0] * 5
        grey = [0] * 5

        for i in range(5): # declare green, yellow and grey words
            if self.wordToday[i] == guess_word[i]:
                green[i] = guess_word[i]
                if guess_word[i] in self.yellow_words: # yellow turn into green
                    self.yellow_words.remove(guess_word[i])
                self.green_words.add(guess_word[i])
            elif guess_word[i] in self.wordToday:
                yellow[i] = guess_word[i]
                self.yellow_words.add(guess_word[i])
            else:
                grey[i] = guess_word[i]
                self.grey_words.add(guess_word[i])
        
        self.green_current.append(green)
        self.yellow_current.append(yellow)
        self.grey_current.append(grey)

        # remove all the word in the grey_char
        for grey_char in self.grey_words:
            for word in self.allword_list:
                if grey_char in word:
                    self.allword_list.remove(word)

        self.trial = self.trial +1

        print(green)
        print(yellow)
        print(grey)
        print("yellow words")
        print(self.yellow_words)
        print("grey words")
        print(self.grey_words)

                    
            


    







                


        





