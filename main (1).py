# Author: Jacob Beebe
# Creation Date: 7/30/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave(): # In the function below there is a mix of boths tabs and spaces that needs to be corrected.
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves # "caves" is undefined and should be "cave".

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3) # This sleep time is 3 seconds instead of 2.
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' # Missing parentheses for print.

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': # Incorrect syntax, = should be changed to ==.
	displayIntro()
	caveNumber = choosecave() # "choosecave" is undefined and should be "chooseCave".
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no": # I would also add the option for the user to type 'n' to quit playing, since they can type 'y' to                            continue.
		print("Thanks for planing") # mispelled playing.

  # I would add an else statement to address if the user types an input other than yes or no.