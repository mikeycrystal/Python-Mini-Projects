from numbers import Number
import random
import string

## Create a word
def rand_word():

    with open("Hangman/words.txt", "r") as file:
        data = file.read()
        words = data.split()

    word_pos = random.randint(0, len(words)-1)
    return words[word_pos]

## Display the blank letters of the word
def blank_word(word):
    final_word = []
    for i in range(len(word)):
        final_word.append('_')
    return final_word
        
## Change a list to a string
def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 = str1 + ele + " "
    return str1

## Allow user to guess, check if guess is right, and display the updated work and guesses.
def guess(word):

    used_letters = []
    wrong_count = 0
    temp = blank_word(word)
    print(list_to_string(temp))

    while True:
        if "_" not in temp:
            print("You win")
            break
        if wrong_count == 5:
            print("Careful, if you miss again, you lose!")
        if wrong_count > 5:
            print(f"You lose, the word was {word}.")
            break
        else:
            letter_check = input("Guess a letter. ")
            if letter_check is int:
                print("Guess a letter, not a number.")
            elif letter_check in word:
                used_letters.append(letter_check)
                for i, letter in enumerate(temp):
                    if letter_check == word[i]:
                        temp[i] = letter_check
                    else:
                        continue
                print(list_to_string(temp))
                print(f"So far, you've guessed {used_letters} and have {wrong_count} incorrect guesses.")
            else:
                print("Incorrect guess.")
                print(list_to_string(temp))
                used_letters.append(letter_check)
                wrong_count += 1
                print(f"So far, you've guessed {used_letters} and have {wrong_count} incorrect guesses.")


##Play the game
def main():
    print("Ready to play? Here is the length of the word.")
    word = rand_word()
    guess(word)

main()