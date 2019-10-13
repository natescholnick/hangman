import os
from random import choice

word_bank = open('good_words.txt', 'r').read().upper().split()

class Hangman:
    def __init__(self, word='0Error', strikes=0, guesses=[]):
        self.word = word
        self.strikes = strikes
        self.guesses = guesses

    def generateWord(self):
        userInput = input('Would you like to play with 1 or 2 players? Type \'QUIT\' to leave. ').lower()
        if userInput == '2' or userInput == 'two':
            word = input('Type a word. Make sure your opponent doesn\'t see! ').upper()
            return word
        elif userInput == '1' or userInput =='one':
            word = choice(word_bank).upper()
            return word
        elif userInput == 'quit':
            global terminate
            terminate = True
            return 'quit'
        else:
            return '0Error'

    def showHangman(self):
        file_name = f'strike{self.strikes}.txt'
        print(open(file_name, 'r').read())
        print(f'You\'ve got {7-self.strikes} wrong guess(es) left. \n')

    def showGuesses(self):
        print('Your guesses:')
        for char in sorted(self.guesses):
            print(char, end=' ')
        print('\n')

    def showWord(self):
        for char in self.word:
            if char in self.guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print('\n')

    def guessLetter(self):
        letter = input('Please guess a letter. ').upper()
        while len(letter) != 1 or not letter.isalpha() or letter in self.guesses:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.showHangman()
            self.showGuesses()
            self.showWord()
            letter = input('Please guess a letter. ').upper()
        if letter not in self.word:
            self.strikes += 1
            print(f'The isn\'t any {letter} in the word.')
        else:
            print('Good guess!')
        self.guesses.append(letter)

    def checkIfWon(self):
        hasWon = True
        for char in self.word:
            if char not in self.guesses:
                hasWon = False
        return hasWon

    def victoryScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.showHangman()
        self.showGuesses()
        self.showWord()
        print('\n\n Congratulations! You figured out the word! \n')


    def defeatScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.showHangman()
        self.showGuesses()
        print('Oh no! You let him die! \n')
        for letter in self.word:
            self.guesses.append(letter)
        print('The word was:')
        self.showWord()

    def playGame(self):
        while self.word == '0Error':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.word = self.generateWord()
        if self.word == 'quit':
            return
        self.guesses = []
        self.strikes = 0
        while self.strikes < 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.showHangman()
            self.showGuesses()
            self.showWord()
            self.guessLetter()
            if self.checkIfWon():
                self.victoryScreen()
                break
            elif self.strikes == 7:
                self.defeatScreen()
            else:
                continue
        userInput = input('Would you like to play again? ' ).lower()
        if userInput == 'no':
            global terminate
            terminate = True


terminate = False

if __name__ == '__main__':
    while not terminate:
        os.system('cls' if os.name == 'nt' else 'clear')
        game = Hangman()
        game.playGame()
