from gtts import *
from playsound import playsound
import random
import os
r1 = random.randint(1,10000000)
r2 = random.randint(1,10000000)
f=open("C:\\Python\\myfile.txt","w")
f.write(input())
f.close()
f=open("C:\\Python\\myfile.txt","r")
x=f.read()
language='en'
audio=gTTS(text=x,lang=language,slow=False)
filename = str(r2)+"randomtext"+str(r1) +".mp3"
audio.save(filename)
os.system(filename)
playsound(filename)
os.remove(filename)