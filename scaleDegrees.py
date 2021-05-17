from random import randint
from time import sleep

def quiz(scaleDict):
	for i in range(25):
		print('Play {scaleDict[randint(1, 8)]}')


GmajorScale = {'1':'G', '2':'A', '3':'B', '4':'C', '5':'D', '6':'E',
				 '7':'F#'}
quiz(GmajorScale)
