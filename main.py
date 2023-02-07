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

alphabet = list(ascii_lowercase)
word = word_extracting()
word_letters = [letter for letter in word]
hidden_word = ["_" for x in word_letters]
tries = 10

game_on = True


while game_on:
    print(f"You have {tries} tries")
    print(hidden_word)
    guess_letter = input("Guess a letter: ")

    if guess_letter == word:
        print("You Win!")
        tries = 0

    elif len(guess_letter) > 1:
        print(f"Sorry the word was {word}, you lost")
        tries = 0

    elif guess_letter in word_letters and guess_letter in alphabet:
        alphabet.remove(guess_letter)
        for x in range(len(word_letters)):
            if word_letters[x] == guess_letter:
                hidden_word[x] = guess_letter

    elif guess_letter not in alphabet and len(guess_letter) == 1:
        print("You already try that letter, try again")

    elif guess_letter not in word_letters:
        tries -= 1
        if tries == 0:
            print(f"Sorry the word was {word}, you lost")

    if tries == 0:
        while True:
            try_again = input("Do you want to try again? (y/n)").lower()
            if try_again == "n":
                game_on = False
                print("Thanks for playing!")
                break
            if try_again == "y":
                alphabet = list(ascii_lowercase)
                word = word_extracting()
                word_letters = [letter for letter in word]
                hidden_word = ["_" for x in word_letters]
                tries = 10
                break