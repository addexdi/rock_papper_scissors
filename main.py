"""Rock, Paper, Scissors, by Adam Ibrahim
   The classic hand game of luck.
   This code is available at https://github.com/addexdi/rock_papper_scissors
   Tags: short, game"""
  
import random, time, sys
  
print('''Rock, Paper, Scissors, by Adam Ibrahim
  - Rock beats scissors.
 - Paper beats rocks.
 - Scissors beats paper.
 ''')
 
 # These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0
 
while True:  # Main game loop.
	while True:  # Keep asking until player enters R, P, S, or Q.
		print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
		print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
		playerMove = input("Player's turn: ").upper()
		if playerMove == 'Q':
			print('Thanks for playing!')
			sys.exit()
 
		if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
			break
		else:
			print('Type one of R, P, S, or Q.')
 
    # Display what the player chose:
	if playerMove == 'R':
		playerMove = 'ROCK'
	elif playerMove == 'P':
		playerMove = 'PAPER'
	elif playerMove == 'S':
		playerMove = 'SCISSORS'

	# print user choice
	print("user choice is: " + playerMove)
 
	# Count to three with dramatic pauses:
	time.sleep(0.5)
	print('1...')
	time.sleep(0.25)
	print('2...')
	time.sleep(0.25)
	print('3...')
	time.sleep(0.25)
	print("\nNow its computer turn.......")
 
	# Display what the computer chose:
	myList = ["R", "P", "S"]
	randomNumber = random.choice(myList)
	if randomNumber == "R":
		computerMove = 'ROCK'
	elif randomNumber == "P":
		computerMove = 'PAPER'
	elif randomNumber == "S":
		computerMove = 'SCISSORS'
	time.sleep(0.5)

	print("Computer choice is: " + computerMove)
 
	print("Player " + (playerMove) + " : " + "CPU " + (computerMove))
 
	# Display and record the win/loss/tie:
	if playerMove == computerMove:
		print('It\'s a tie!')
		ties = ties + 1
	elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
		print('You win!')
		wins = wins + 1
	elif playerMove == 'PAPER' and computerMove == 'ROCK':
		print('You win!')
		wins = wins + 1
	elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
		print('You win!')
		wins = wins + 1
	elif playerMove == 'ROCK' and computerMove == 'PAPER':
		print('You lose!')
		losses = losses + 1
	elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
		print('You lose!')
		losses = losses + 1
	elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
		print('You lose!')
		losses = losses + 1
		
