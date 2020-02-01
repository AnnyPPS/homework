import random

health = 5
food = 500
miles = 2000
days_past = 0
day = 1
month = 3
months_with_31 = [1, 3, 5, 7, 8, 10, 12]

def travel():
	daystravel = random.randint(3,7)
	add_day(daystravel)
	#print('days traveled',daystravel)
	eat(daystravel)
	healthcalc(daystravel)
	status()

def status():
	#print('Progress: 1000 Miles |--------------------------O-----------------------| 50%\n')
	print('Health:',health,'\n')
	print('Food:',food,'\n')
	print('Current Date:',month,'/',day,'/ 2020')

def rest():
	global health
	daysrest = random.randint(2,5)
	add_day(daysrest)
	#print('Days rested',daysrest)
	eat(daysrest)
	healthcalc(daysrest)
	
	if health < 5:
		health = health+1
	status()

def hunt():
	global food
	dayshunt = random.randint(2,5)
	add_day(dayshunt)
	#print('Days hunted',dayshunt)
	#print(food)
	eat(dayshunt)
	food = food+100
	#print(food)
	healthcalc(dayshunt)
	status()

def help():
	Commands = 'travel, hunt, status, rest, quit, and help'
	return Commands

def add_day(days):
	global day
	day = day+days

	#if day < 31:
		
    
def update_months(months):
	pass

def eat(daysoffood):
	global food
	food = food-(daysoffood*5)
	#print(food)
	
def healthcalc(days_past):
	global health
	for x in range(days_past):
		fivepercent = random.randint(1,100)
	
		if fivepercent < 6:
			health = health-1
			#print('health lost',fivepercent)
		
#name = input('\nEnter your name: ')

while health > 0 and food > 0 and days_past < 304:
	action = input('\nWhat would you like to do?: ')

	if action == 'travel':
		travel()

	elif action == 'hunt':
		hunt()    

	elif action == 'status':
		status()
    
	elif action == 'rest':
		rest()

	elif action == 'quit':
		break

	elif action == 'help':
		print(help)