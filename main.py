import random
from string import ascii_lowercase


def word_extracting():
    stop_point = random.randint(1, 201)
    counter = 0
    with open("words.txt", "rt") as words:
        for word in words:
            clean_word = word.strip()
            counter += 1
            if counter == stop_point:
                return clean_word


word = word_extracting()
word_letters = [letter for letter in word]

alphabet = list(ascii_lowercase)
game_on = True

print(word_letters)


