from random import randint
sides = input('How many sides should we use? ')
sides = int(sides)
print(randint(1,sides))
userchoice = input('roll again? ')
while userchoice != 'no':
	sides = input('How many sides should we use? ')
	sides = int(sides)
	print(randint(1,sides))
	userchoice = input('roll again? ')
else:
	print('Thanks!')
	exit()
