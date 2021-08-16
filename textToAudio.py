from typing import Text
from gtts import gTTS
from playsound import playsound
folderName= input("Folder name: ")
audio = folderName + '.mp3'
language = 'en' 
text= input("Write something: ")
sp = gTTS (text= text , lang= language, slow= False ) 
sp.save (audio) 
playsound (audio) 
