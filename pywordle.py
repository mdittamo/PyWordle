import getpass
import pyfiglet
import random
from colorama import Fore, Back, Style
from colorama import init
import os
init()

os.system('cls' if os.name == 'nt' else 'clear')

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

logo = pyfiglet.figlet_format("PyWordle" )
print(Fore.GREEN + logo + Style.RESET_ALL)    
    
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
    print(f'\nGuess the word in {player1.score} tries.\n')
    print('Any spot with a # is the correct letter, but in a wrong spot.\n')
    
    #Player supplied word
    #word = getword()
    
    #Word from Word list
    word = random.choice(open('words.txt').readlines())
    word = word.upper()
    word = word[0:5]
    #Update alpha dictionary - reset game
    alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    for x in range(len(word)): 
        alphabet[word[x]]+=1
    #print(word)
    l_word = list(word)
    #print(alphabet)

    #Gameplay
    while correct_guess == False: 
        guess = getguess()
        
        if guess == l_word: 
            print(Fore.GREEN + '\nYou win!\nYou win!\nYou win!\n' + Style.RESET_ALL)
            choice = input('Would you like to play again (Y)? ')
            choice = choice.upper()
            if choice == 'Y':
                break
            else: 
                gameon = False
                break
        
        elif player1.score <=1: 
            go_word = ''.join(l_word)
            print(Fore.RED + f'\nYou lose!\nThe word was {go_word}\nYou lose!\n' + Style.RESET_ALL)
            choice = input('Would you like to play again (Y)? ')
            choice = choice.upper()
            if choice == 'Y':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else: 
                gameon = False
                break
            break
            
        else: 
            player1.score-=1
                  
            #Check for X's - Correct letter correct place
            for x in range (len(guess)): 
                if guess[x] == l_word[x]:
                    results[x] = guess[x]
                    alphabet[guess[x]]-=1
            
            #Check for O's - Correct letter wrong place
            for x in range (len(guess)): 
                for y in range(len(l_word)):
                    if guess[x] == l_word[y] and alphabet[guess[x]] > 0 and results[x] != '#' and results[x] != guess[x]:
                        results[x] = '#'
                        alphabet[guess[x]]-=1

            alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
            for x in range(len(word)): 
                alphabet[word[x]]+=1
                        
            print('\n' + str(results))
            print(f'\nYou have {player1.score} guesses left.')
            results = ['_', '_','_','_','_']
