"""
File: hangman.py
Name: 雲筱涵
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    word = random_word()  # give a random word
    dash = ''  # create a box to save word to '-'
    for i in range(len(word)):
        dash += '-'
    print('The word looks like: '+str(dash), end='')
    print('')
    print('You have '+str(N_TURNS)+' guesses left.')
    hangman(word)


def hangman(word):
    chance = N_TURNS
    dash = ''  # create a box to save word to '-'
    for i in range(len(word)):
        dash += '-'
    while chance > 0:  # if still have chance go in to while loop to guess
        guess = input('Your guess: ')
        guess = guess.upper()  # uppercase the input letter
        guess_open = False  # a checkpoint to go in or out to the while loop
        new_dash = ''  # save guess word
        if len(guess) != 1:  # exclude input more than one letter
            print('illegal format.')
        elif not str.isalpha(guess):
            print('illegal format.')  # exclude input is not alphabet
        else:
            for i in range(len(dash)):  # check every site of word if there is any guess letter
                if word[i] == guess:
                    new_dash += guess  # if guess correct, add guessed letter to dash become new dash
                    guess_open = True
                else:
                    new_dash += dash[i]  # if guess incorrect, just add dash to new dash
            dash = new_dash  # re-assign new dash to dash in next round
            if not guess_open:  # if guess wrong, one less chance
                chance -= 1
                print('There is no ' + str(guess) + '\'s in the word.')
                print('You have ' + str(chance) + ' guesses left.')
                print('The word look like: ' + dash)
            else:  # if guess correct, print new word
                print('You are correct!')
                print('The word looks like: ' + new_dash)
                print('You have ' + str(chance) + ' guesses left.')
            if chance == 0:  # if there is no chance, go out of the while loop
                print('You are completely hang:(')
                print('The word was:' + word)
                break
            if '-' not in dash:  # if guess all the letters right
                print('you win')
                print('The word was:' + new_dash)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
