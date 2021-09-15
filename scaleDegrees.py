#!/usr/bin/env python3

from gtts import gTTS
from random import shuffle
from time import sleep
from sys import exit
import os

'''
	from datetime import datetime
	possibly use the datetime module to come up with a clever way to 
	make notes appear at chosen bpm's.
	or use some other method 

for later
majorPentatonic = ['1', '2', '3', '5', '6']
minorScaleDegrees = ['1', '2', 'b3', '4', '5', 'b6', 'b7']
minorScaleThirds = ['1', 'b3', '5', 'b7']
minorPentatonic = ['1', 'b3', '4', '5', 'b7']
'''

#TODO: ability to choose bpm   
#TODO: GUI Interface



keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Gb', 'Db', 'C#', 'Ab',
         'Eb', 'Bb', 'F']

majorScaleDegrees = ['1', '2', '3', '4', '5', '6', '7']
majorScaleThirds = ['1', '3', '5', '7']


# Chooses a random key and displays scale degrees randomly after a
# sleep period for 25 turns and then switches keys. loops until ctrl+c
def quiz(key, degrees, timer):
	while True:
		shuffle(keys)
		print(f'Key is {keys[0]}')
		for i in range(25):
			shuffle(degrees)
			print(f'Play {degrees[0]}')
			sleep(timer)
		print('Key Change!')


# Displays random key every 10 seconds. to be used as a tool to memorize
# all the notes in the key.
def randomNotes(timer):
	while True:
		shuffle(keys)
		for i in keys:
			print(i)
			audioObj = gTTS(
#			os.system(f'cvlc ./audio/{i}.mp3 vlc://quit')
			sleep(timer)


if __name__ == "__main__":
	# loops until the input made is a number.
	while True:
		try:
			choice = int(input('Enter the Number of your choice: \n\
    1. Major Triads\n    2. All Major Notes\n    3. Minor Triads\n\
    4. All Minor Notes\n    5. Root Notes Only\n'))
			break
		except ValueError:
			print('You need to input a number')
	# input for the sleep duration between notes
	while True:
		try:
			timerChoice = int(input('Enter the time for sleep in \
seconds: '))
			break
		except ValueError:
			print('You need to input a number')
	# if elif statements to call the correct  function with the correct
	# parameters
	try:
		if choice == 1:
			quiz(keys, majorScaleThirds, timerChoice)
		elif choice == 2:
			quiz(keys, majorScaleDegrees, timerChoice)
		elif choice == 5:
			randomNotes(timerChoice)
		# minor scale thirds to be added
		# minor scale degrees to be added

	except KeyboardInterrupt:
		print('Good Job!')
