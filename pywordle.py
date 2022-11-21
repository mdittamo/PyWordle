import getpass
import colorama
from colorama import Fore, Back, Style
from colorama import init
init()

#Obtain word from user(1)
def getword():
    word = ''
    while len(word) != 5:
        
        word = getpass.getpass(prompt = 'Enter a (5) Letter word: ' )
        word = word.upper()
        if len(word) < 5 or len(word) > 5: 
            print(Fore.RED + '\nNot the correct number of characters!\n' + Style.RESET_ALL)
            
    return list(word)
    
#Get guess from user(2)
def getguess():
    guess = ''
    while len(guess) != 5:
        guess = input('\nWhat is your five letter guess _ _ _ _ _? ')
        guess = guess.upper()
        if len(guess) < 5 or len(guess) > 5: 
            print(Fore.RED + '\nNot the correct number of characters!' + Style.RESET_ALL)
    return list(guess)
    
    
#Player Class
class Player:
    def __init__ (self, score):
        self.score = score
        
#Game Logic
#Initialize game variables
correct_guess = False
player1 = Player(5)
results = ['_', '_','_','_','_']

#Title Screen
print(Fore.GREEN + '\nWelcome to PyWordle!\n' + Style.RESET_ALL)
print(f'Guess the word in {player1.score} tries.\n')
word = getword()

#Gameplay
while correct_guess == False: 
    guess = getguess()
    
    if guess == word: 
        print(Fore.GREEN + '\nYou win!\nYou win!\nYou win!' + Style.RESET_ALL)
        break
    
    elif player1.score <=0: 
        print(Fore.RED + '\nYou lose!\nYou lose!\nYou lose!' + Style.RESET_ALL)
        break
        
    else: 
        player1.score-=1
        
        #Check for O's - Correct letter wrong place
        for x in range (len(guess)): 
            for y in range(len(word)):
                if guess[x] == word[y]:
                    results[x] = 'O'
        
        for x in range (len(guess)): 
            if guess[x] == word[x]:
                results[x] = 'X'
        
        print('\n' + str(results))
        print(f'\nYou have {player1.score} guesses left.')
        results = ['_', '_','_','_','_']
