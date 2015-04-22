""" --- Jeu de la roulette d'un casino --- """
from random import randrange
from math import ceil

# Check the game over ?
isOver = False

# How much does the player want to bet ?
money = input("How much do you want to play with ? ")
print " " 

# Is the amount right ?
try:
	money = int(money)
	if money <= 0:
		raise ValueError("Impossible to play with this amount. Reload the game.")
except ValueError as e:
	print money, "$ :",e
	quit()
	
# Is there any dollars left ?
while isOver == False:
	# Display the left money
	print "You have ", money, "$ left."

	# Ask the player a number to play
	# Check the number (between 0 and 49)
	numberIsCorrect = False
	while numberIsCorrect == False:
		number = input("Choose a number between 0 et 49 : ")
		print " "
		try:
			number = int(number)
			if number < 0 or number > 49:
				raise ValueError("This number is out of range.")
		except ValueError as e:
			print "You chose : ", number, e
		
		# Everything is OK
		else: 
			numberIsCorrect = True
		
	# Number chosen is correct, we can go on
	if numberIsCorrect == True:
		# Check the amount for the game (between 1 and 'money left')
		amountIsCorrect = False
		while amountIsCorrect == False:
			amount = input("How much do you want to bet for this game ? ")
			print " "
			try:
				amount = int(amount)
				if amount > money or amount < 1:
					raise ValueError("To important amount or negative (including 0) amount")
			except ValueError as e:
				print "You want to bet ",amount,"$ whereas you have ",money,"$ left.", e
			
			# Everything is OK
			else:
				amountIsCorrect = True
		
		# Amount bet is correct. We can play the game
		if amountIsCorrect == True:
			# Random number: the result of the game
			result = randrange(50)
			print "The number to win is : ",result
			
			# The player won the game
			if result == number:
				money += 3*amount
			
			# The player chose the right color (Black or Red)
			elif number%2 == result%2:
				money -= ceil(amount/2)
				
			else:
				money -= amount
				
			# Is there money left ?
			if money <= 0:
				isOver = True

# Game Over.
print "Game Over ..."