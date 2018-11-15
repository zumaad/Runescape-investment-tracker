"""
The file that runs the application. It has a while loop that runs infinitely and queries
the user for input and updates the models accordingly.
"""
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
    """
    This is a utlity function to return an account based on the letter you pass it.
    the letter is also what a user inputs when performing any update on an account.
    """

    if name == "R":
        return richacc
    elif name == "M":
        return medacc
    elif name == "P":
        return pooracc



def main():
    """
    Main function that asks the user for input and takes the input and gives it to
    the correct methods to update the account's item lists along with displaying the lists.
    """
    
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



   















   





        






