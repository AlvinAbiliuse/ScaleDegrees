#!/usr/bin/env python3


from random import shuffle
from time import sleep
from sys import exc_info, stdout
from datetime import datetime


def quiz(key, degrees):
	while True:
		shuffle(keys)
		print(f'Key is {keys[0]}')
		for i in range(25):
			shuffle(degrees)
			print(f'Play {degrees[0]}')
			sleep(2)
		print('Key Change!')

keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Gb', 'Db', 'C#', 'Ab',
		 'Eb', 'Bb', 'F']

majorScaleDegrees = [1, 2, 3, 4, 5, 6, 7]
majorScaleThirds = [1, 3, 5, 7]



# TODO: majorPentatonic = list()
# TODO: minorScaleDegrees = list()
# TODO: minorScaleThirds = list()
# TODO: minorPentatonic = list()
# TODO: ability to choose bpm

if __name__ == "__main__":
	while True:
		input1 = input('Major or Minor!:   ').lower()
		if input1 in ['major', 'minor']:
			break
		else:
			print('Try Again!')
			continue
	while True:
		input2 = input('Thirds or all!:   ').lower()
		if input2 in ['thirds', 'all']:
			break
		else:
			print('Try Again!')
			continue

	print(input1 + '  ' + input2)
	if input1 == "major":
		if input2 == "thirds":
			quiz(keys, majorScaleThirds)
		elif input2 == "all":
			quiz(keys, majorScaleDegrees)
	elif input1 == "minor":
		print('', end='')
		
