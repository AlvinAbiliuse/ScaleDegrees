from gtts import gTTS
import os

mytext = "Hello World! C#"

myobj = gTTS(text=mytext, lang='en', slow=False)

myobj.save("welcome.mp3")
# while True:
while True:
	os.system("cvlc ./welcome.mp3 vlc://quit")
	print('Hello World!')
