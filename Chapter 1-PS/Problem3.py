#  Install an external module and use it to perform an operation of your interest. 

import os, pyttsx3

engine = pyttsx3.init()
dir = os.getcwd()
engine.say("Current working directory is " + dir)

engine.runAndWait()