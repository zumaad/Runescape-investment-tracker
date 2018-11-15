import time
from colorama import Fore, Back, Style
import speech_recognition as sr
import pyttsx3
from models import *


r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()
engine.setProperty('rate',75)

richacc= Account(rich)
medacc = Account(rich)
pooracc = Account(poor) 


# utility function to return an account.
def returnacc(name):
    if name == "R":
        return richacc
    elif name == "M":
        return medacc
    elif name == "P":
        return pooracc



def main():
    
    while True:
        items = input("update items,display items,read, or go back ")
        iandq = items.split()
        
        if len(iandq) < 2:
            main()
                
        else:
            if iandq[0] == "R" or iandq[0] == "M" or iandq[0] == "P" :

                if iandq[1] =="DISPLAY":
                    returnacc(iandq[0]).refresh()
                    returnacc(iandq[0]).display()

                elif iandq[1] == "READ":
                    for item in returnacc(iandq[0]).itemlist:
                        if item.done == "N":
                            engine.say(item.name)
                            
                    engine.runAndWait()
                
                elif iandq[1] == "SPEECH":
                    
                    with mic as source:
                        audio = r.listen(source,phrase_time_limit = None)
                    speech = r.recognize_google(audio)
                    upperspeech = [word.upper() for word in speech.split()]
                    returnacc(iandq[0]).updatewithspeech(upperspeech)
                    print("these are the items you updated ")
                    print(upperspeech)
                    
                elif len(iandq) == 3:
                    returnacc(iandq[0]).refresh()
                    returnacc(iandq[0]).update(iandq[1],iandq[2])
                    
                else: 
                    main()
            else:
                main()
main()



   















   





        






