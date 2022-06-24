

# 1. Create a program that will play the “cows and bulls” game with the user.

import random

def getdigits(num):
    return [int(i) for i in str(num)]

def noduplicates(num):
    num_list = getdigits(num)
    if len(num_list) == len(set(num_list)):
        return True
    else:
        return False

def gennum():
    while True:
        num = random.randint(1000, 9999)
        if noduplicates(num):
            return num

def numcowsbulls(num,guess):
    cow_bull = [0,0]
    num_list = getdigits(num)
    guess_list = getdigits(guess)
    for i, j in zip(num_list, guess_list):
        if j in num_list:
            if j == i:
                cow_bull[0] += 1
            else:
                cow_bull[1] += 1
    return cow_bull

print('Welcome to the Cows and Bulls Game! ')
num = gennum()
tries = int(input('Enter the number of tries: '))
while tries > 0:
    guess = int(input('Enter your best Guess!! '))
    if not noduplicates(guess):
        print('Number should not have repeated digits ')
        continue

    cow_bull = numcowsbulls(num, guess)
    print('You have ', cow_bull[0], 'cows and ', cow_bull[1], 'bulls.')
    tries -= 1
    print('You have {} tries left!'.format(tries))

    if cow_bull[0] == 4:
        print('You guessed right!! ')
        break

else:
    print('You ran out of tries. Number was {}'.format(num))


# 2. Write a python code to read the file and store the words in the list
# Write a function to guess a word randomly from the list.
# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter.
# Display  letters in the clue word that were guessed correctly.


my_file = open('wordlist.text', 'r')
data = my_file.read()
data_into_list = data.replace('\n', ' ').split()
print(data_into_list)
my_file.close()

def hangman():
    words = ['hands', 'legs', 'india', 'crow', 'rain']
    word = random.choice(words)
    print('Guess the characters ')
    guesses = ''
    turns = 6
    print('Welcome to hangman!')
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_')
                failed += 1

        if failed == 0:
            print('\n You win!!')
            print('The word is:', word)
            break

        print()
        guess = input('Guess a letter in the word: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('Incorrect')
            print('You have', turns, 'more guesses.')

            if turns == 0:
                print('You lose. The word is: ', word)

    print('Do you want to play Hangman again? ')
    play = input('Enter "y" for yes or "n" for no ')
    if play == 'y':
        hangman()
    else:
        print('Thanks for playing.')


hangman()










































