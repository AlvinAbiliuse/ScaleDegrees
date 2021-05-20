#!/usr/bin/env python3


import random
from time import sleep
from sys import exc_info
from datetime import datetime

def quiz(key, degrees):
	while True:
		random.shuffle(keys)
		print(f'Key is {keys[0]}')
		for i in range(25):
			print(f'Play {random.shuffle(degrees)[0]}')
			sleep(2)
		print('Key Change!')

keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Gb', 'Db', 'C#', 'Ab', 'Eb', 'Bb', 'F']

majorScaleDegrees = [1, 2, 3, 4, 5, 6, 7]
majorScaleThirds = [1, 3, 5, 7]
minorScaleDegrees = list()


if __name__ == "__main__":
#	try:
	input1 = input('Major or Minor!:   ').lower()
	input2 = input('Thirds or all!:   ').lower()
	print(input1 + '  ' + input2)
	if input1 == "major":
		if input2 == "thirds":
			quiz(keys, majorScaleThirds)
		elif input2 == "all":
			quiz(keys, majorScaleDegrees)
	elif input1 == "minor":
		print('', end='')
		
#	except:
#		with open('log.txt', 'a+') as log:
#			log.write('Logging date:' + str(datetime.now().strftime("%d-%b-%Y %H:%M")) + '\n\n' + str(exc_info()[0]) + '\n\n\n')
