import getpass
import random
from colorama import Fore, Back, Style
from colorama import init
init()

#Obtain word from user(1)
def getword():
    word = ''
    while len(word) != 5 or all(chr.isalpha() for chr in word) == False:
        
        word = getpass.getpass(prompt = 'Enter a (5) Letter word: ' )
        word = word.upper()
        if len(word) < 5 or len(word) > 5 or all(chr.isalpha() for chr in word) == False: 
            print(Fore.RED + '\nNot the correct number or invalid characters!\n' + Style.RESET_ALL)
            
    return list(word)
    
#Get guess from user(2)
def getguess():
    guess = ''
    while len(guess) != 5 or all (chr.isalpha() for chr in guess) == False:
        guess = input('\nWhat is your five letter guess _ _ _ _ _? ')
        guess = guess.upper()
        if len(guess) < 5 or len(guess) > 5 or all(chr.isalpha() for chr in guess) == False: 
            print(Fore.RED + '\nNot the correct number or invalid characters!' + Style.RESET_ALL)
    return list(guess)
    
    
#Player Class
class Player:
    def __init__ (self, score):
        self.score = score
        
gameon = True  

while gameon == True:     
    #Game Logic
    #Initialize game variables
    correct_guess = False
    player1 = Player(5)
    results = ['_', '_','_','_','_']

    #Title Screen
    print(Fore.GREEN + '\nWelcome to PyWordle!\n' + Style.RESET_ALL)
    print(f'Guess the word in {player1.score} tries.\n')
    
    #Player supplied word
    #word = getword()
    
    #Word from Word list
    word = random.choice(open('words.txt').readlines())
    word = word.upper()
    word = list(word)

    #Gameplay
    while correct_guess == False: 
        guess = getguess()
        
        if guess == word: 
            print(Fore.GREEN + '\nYou win!\nYou win!\nYou win!\n' + Style.RESET_ALL)
            choice = input('Would you like to play again (Y)? ')
            choice = choice.upper()
            if choice == 'Y':
                break
            else: 
                gameon = False
                break
        
        elif player1.score <=1: 
            go_word = ''.join(word)
            print(Fore.RED + f'\nYou lose!\nThe word was {go_word}You lose!\n' + Style.RESET_ALL)
            choice = input('Would you like to play again (Y)? ')
            choice = choice.upper()
            if choice == 'Y':
                break
            else: 
                gameon = False
                break
            break
            
        else: 
            player1.score-=1
            
            #Check for O's - Correct letter wrong place
            for x in range (len(guess)): 
                for y in range(len(word)):
                    if guess[x] == word[y]:
                        results[x] = 'O'
            
            #Check for X's - Correct letter correct place
            for x in range (len(guess)): 
                if guess[x] == word[x]:
                    results[x] = 'X'
            
            print('\n' + str(results))
            print(f'\nYou have {player1.score} guesses left.')
            results = ['_', '_','_','_','_']

#Game Bug - fails when there is a single letter in the right spot and in the wrong spot (i.e. title would show O_XX__ for the word ditch)
