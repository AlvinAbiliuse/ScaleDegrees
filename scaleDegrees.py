from random import randint
from time import sleep
from sys import exc_info
from datetime import datetime

def quiz(scaleDict):
	for i in range(25):
		print(f'Play {scaleDict[str(randint(1, 7))]}')
		sleep(2)


GmajorScale = {'1':'G', '2':'A', '3':'B', '4':'C', '5':'D', '6':'E',
				 '7':'F#'}

if __name__ == "__main__":
	try:
		quiz(GmajorScale)
	except:
		with open('log.txt', 'a+') as log:
			log.write('Logging date:' + str(datetime.now().strftime("%d-%b-%Y %H:%M")) + '\n\n' + str(exc_info()[0]) + '\n\n\n')
