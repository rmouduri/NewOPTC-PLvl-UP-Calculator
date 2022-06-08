from numpy import spacing
import sys


levelTab = {}
informations = {}

currLevel = 1
maxStam = 20
currStam = 20
xpLeft = 0
stamPerRun = 0
xpPerRun = 0
timePerRun = 0
meats = 0
totalGemsUsed = 0
levelLimit = 2998
totalTime = 0
runs = 0
xpGained = 0
totalRuns = 0
mode = 0

if sys.argv[1] == "--format=Sheets":
	mode = 1


readFile = open("xpRequired.txt", "r").readlines()

for i in range(len(readFile)):
	levelTab[i] = int(readFile[i].replace('\n', ''))

readFile = open("yourInfos.txt", "r").readlines()

for i in range(len(readFile)):
	informations[i] = readFile[i].replace('\n', '').split('=')

for i in informations:
	if informations[i][0] == 'currentLevel':
		currLevel = int(informations[i][1])
	elif informations[i][0] == 'maximumStamina':
		maxStam = int(informations[i][1])
	elif informations[i][0] == 'currentStamina':
		currStam = int(informations[i][1])
	elif informations[i][0] == 'xpLeftToLevelUP':
		xpLeft = int(informations[i][1])
	elif informations[i][0] == 'staminaPerRun':
		stamPerRun = int(informations[i][1])
	elif informations[i][0] == 'xpPerRun':
		xpPerRun = int(informations[i][1])
	elif informations[i][0] == 'timePerRunInSeconds':
		timePerRun = int(informations[i][1])
	elif informations[i][0] == 'meats':
		meats = int(informations[i][1])

if mode == 1:
	print("P-Lvl,", "Runs,", "Total Runs,", "Meats,", "Used Gems,", "Current XP,", "Time to level UP,", "Total time elapsed")

while currLevel < levelLimit:
	if int(currStam / stamPerRun) * xpPerRun < xpLeft:
		while int(currStam / stamPerRun) * xpPerRun < xpLeft:
			if meats:
				meats -= 1
			else:
				totalGemsUsed += 1
			currStam += maxStam

	runs = int(xpLeft / xpPerRun) + 1
	totalRuns += runs
	xpGained = runs * xpPerRun
	totalTime += timePerRun * runs

	currStam -= runs * stamPerRun
	meats += 1
	xpLeft = levelTab[currLevel] - (runs * xpPerRun - xpLeft)
	xpGained -= xpLeft
	currLevel += 1
	if currLevel % 2:
		maxStam += 1

	while xpGained >= levelTab[currLevel]:
		xpGained -= levelTab[currLevel]
		meats += 1
		currLevel += 1
		if currLevel % 2:
			maxStam += 1
		xpLeft = levelTab[currLevel] - xpGained

	if mode == 0:
		print('P-Lvl= ', f'{currLevel:<4}', ' | Runs= ', f'{runs:<3}', ' | totalRuns= ', f'{totalRuns:<6}', ' | Meats= ', f'{meats:<3}', ' | gemsUsed= ', f'{totalGemsUsed:<4}', ' | XP->(', f'{levelTab[currLevel - 1] - xpLeft:<6}', '/', f'{levelTab[currLevel - 1]:9}', ") | Time= ", int(timePerRun * runs / 3600), 'h', int(timePerRun * runs / 60 % 60), 'm', timePerRun * runs % 60, "s\t| totalTime= ", int(totalTime / 3600), 'h', int(totalTime / 60 % 60), 'm', totalTime % 60, 's', sep='')
	else:
		print(currLevel, runs, totalRuns, meats, totalGemsUsed, '(' + str(levelTab[currLevel - 1] - xpLeft) + ' / ' + str(levelTab[currLevel - 1]) + ')', str(int(timePerRun * runs / 3600)) + 'h' + str(int(timePerRun * runs / 60 % 60)) + 'm' + str(timePerRun * runs % 60) + 's', str(int(totalTime / 3600)) + 'h' + str(int(totalTime / 60 % 60)) + 'm' + str(totalTime % 60) + 's', sep=',')