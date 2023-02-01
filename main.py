import random


def word_extracting():
    stop_point = random.randint(1, 201)
    counter = 0
    with open("words.txt", "rt") as words:
        for word in words:
            counter += 1
            if counter == stop_point:
                return word



