import time
from colorama import Fore, Back, Style
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()
engine.setProperty('rate',75)


rich= {'ART': 8,  #ancestral robe bottom
'ARB': 8,         #ancestral robe top
'AH': 8,          #ancestral hat
'PB': 12,         #pegasian boots
'PB2': 12,        #primordial boots
'AB': 8,          #abyssal bludgeon
'DHC': 8,         #dragon hunter crossbow
'ACP': 8,         #armadyl chest plate
'BT': 8,          #bandos tassets
'BCP': 8,         #bandos chest plate
'A': 50,           #anguish
'T': 8,           #torture
'TB': 50,          #tormented bracelet
'RB': 8,          #ranger boots
'AGS': 8,         #armadyl godsword
'SGS': 8,         #saradomin godsword
'DW': 8,          #dragonwarhammer
'DC': 8,          #dragon claws
'SSS': 8,         #spectral spirit shield
'ASS': 8,         #arcane spirit shield
'EM': 8,          #elder maul
'ACB': 8,         #armadyl crossbow
'IH': 8,          #imbued heart
'TB2': 8,         #twisted buckler
'DB': 8,          #dihns bulwark
'ZH': 8,          #zamorakian hasta
'ZS': 8,          #zamorakian spear
'ROS': 8,         #ring of suffering
'TS': 8,          #toxic staff
'SOTD': 8,        #staff of the dead
'DCB': 8,         #dragon crossbow
'GB': 8,          #guardian boots
'AD': 8,          #abyssal dagger
'BGS': 8,         #bandos godsword
'ACS': 8,         #armadyl chain skirt        
'KLT': 14,        #karils leathertop
'OP': 8,          #obsidian platebody
'AR': 8,          #archer ring
'TB3': 8,         #toxic blowpipe
'OW': 8,          #odium ward
'MB': 20,         #mages book
'MW2': 8,         #malediction ward
'IRT': 8,         #infinity robe top 
'HB': 8,          #heavy ballista
'IRB':8,          #infinity robe bottom
'VS': 8,          #verac set
'DFS': 8,         #dragonfire shield          
'VPS': 14,        #verac plateskirt
'ZB': 8,          #zamorak body
'MW': 8,          #master wand
'ERT': 20,        #elder robe  top
'F': 8,           #fury
'ERB': 20,        #elder robe bottom
'EB': 12,         #eternal boots
'SDB': 8,         #saradomin dhide boots       
'ZDB': 8,         #zamorak dhide boots
'TT': 8,          #toxic trident
'DCS': 50,        #dwarf cannon set
'BN': 10,         #berserker necklace
'ON': 8,          #occult necklace
'BR': 8,          #berserker ring
'GS': 8,          #guthan set
'ART2':14,        #ahrim robe top
'ARB2':14,        #ahrim robe bottom
'DS':8,           #dharok set
'DPL':14,         #dharok platebody
'DPB':14,         #dharok platelegs
'AH2':8,          #armadyl helmet
}          



poor = {'BCP': 8, #bandos chest plate
'A': 50,           #anguish
'T': 8,           #torture
'TB': 50,          #tormented bracelet
'TB2': 8,         #twisted buckler
'DB': 8,          #dihns bulwark
'ZH': 8,          #zamorakian hasta
'ZS': 8,          #zamorakian spear
'ROS': 8,         #ring of suffering
'TS': 8,          #toxic staff
'SOTD': 8,        #staff of the dead
'DCB': 8,         #dragon crossbow
'GB': 8,          #guardian boots
'AD': 8,          #abyssal dagger
'BGS': 8,         #bandos godsword   
'KLT': 14,        #karils leathertop
'OP': 8,          #obsidian platebody
'AR': 8,          #archer ring
'TB3': 8,         #toxic blowpipe
'OW': 8,          #odium ward
'MB': 20,          #mages book
'MW2': 8,         #malediction ward
'IRT': 8,         #infinity robe top 
'HB': 8,          #heavy ballista
'IRB':8,          #infinity robe bottom
'VS': 8,          #verac set
'DFS': 8,         #dragonfire shield          
'VPS': 14,        #verac plateskirt
'ZB': 8,          #zamorak body
'MW': 8,          #master wand
'ERT': 20,        #elder robe  top
'F': 8,           #fury
'ERB': 20,        #elder robe bottom
'EB': 12,         #eternal boots
'SDB': 8,         #saradomin dhide boots       
'ZDB': 8,         #zamorak dhide boots
'TT': 8,          #toxic trident
'DCS': 50,        #dwarf cannon set
'BN': 20,         #berserker necklace
'ON': 8,          #occult necklace
'BR': 8,          #berserker ring
'GS': 8,          #guthan set
'ART2':14,        #ahrim robe top
'ARB2':14,        #ahrim robe bottom
'DS':8,           #dharok set
'DPL':14,         #dharok platebody
'DPB':14,         #dharok platelegs
'AH2':8,          #armadyl helmet
'SB':8,           #saradomin body
'DB2':8,          #dark bow          
'AW':70,          #whip
'SH':8}           #serpentine helm

green = Fore.GREEN + Style.BRIGHT
red = Fore.RED
magenta = Fore.MAGENTA 


class Account:

    def __init__(self,name):
        self.name = name
        self.itemlist = self.initializelist(name)
        

    def initializelist(self,name):
        L = []
        for k,v in name.items():
            a =Item(k,v,0)
            L.append(a)
        return L

    
    def update(self,name,quantity="NA"):
        for item in self.itemlist:
            if item.name == name:
                item.done = "Y"
                if item.quantity == 0:
                    item.time = time.localtime()
                item.quantity = item.quantity + int(quantity)
                
                


    def display(self):
        for item in self.itemlist:
            if item.done == "Y":
                buytime = str(item.time.tm_hour)+ ':' + str(item.time.tm_min)
                currenttime = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min)
                buylimitrefresh = str((item.time.tm_hour + 4) % 24) + ':' + str(item.time.tm_min)

            
                if int(item.quantity)/item.limit <= .5:
                    
                    print(magenta + item.name + "--------" + str(item.quantity) + '/' + str(item.limit)
                    + "  started buying at hour:" + str(buytime) + "  current time:" + str(currenttime)
                    + "  buy limit restarts at: " + str(buylimitrefresh))


                else:
                    print(red + item.name + "--------" + str(item.quantity) + '/' + str(item.limit)
                    + "  started buying at hour:" + str(buytime) + "  current time:" + str(currenttime)
                    + "  buy limit restarts at: " + str(buylimitrefresh))
            else:
                print(green + item.name + "--------" + str(item.quantity) + '/' + str(item.limit))


    #used in the text version
    def updatewithlist(self,list):
        for i in range(len(list)-1):
            self.update(list[i],list[i+1])
    
    def updatewithspeech(self,list):
        for i in range(len(list)):
            self.update(list[i],0)

    def refresh(self):
        currentmin = time.localtime().tm_min
        currenthour = time.localtime().tm_hour 
        currentday = time.localtime().tm_mday
        for item in self.itemlist:
            if item.done == "Y":
                if currentday == item.time.tm_mday:
                
                    if abs((currenthour + (currentmin/60))- (item.time.tm_hour + (item.time.tm_min/60))) >= 4:
                        item.reset()
                else:
                
                    distancefromnextday = 24 - item.time.tm_hour + item.time.tm_min/60
                    distancefromprevday = currenthour + currentmin/60
                    if distancefromnextday + distancefromprevday >= 4:
                        item.reset()


              

            



            

    
    


    
        

        



class Item:
    def __init__(self, name, limit,quantity = 0,done = "N",time = None):
        self.name = name 
        self.quantity = quantity
        self.limit = limit
        self.time = time
        self.done = done

    def reset(self):
        self.quantity = 0
        self.done = "N"
        self.time = None

        
    




def returnacc(name):
    if name == "R":
        return richacc
    elif name == "M":
        return medacc
    elif name == "P":
        return pooracc

def start():
    first =input("what do you want to do ")
    if first == "SHORTCUT":
        shortcutz()
    elif first == "SPEECH":
        updatestate()
    elif first == "read":
        readstate()
    else :
        start()




def updatestate():
    account = input("which account do you want to update  ")
    returnacc(account).refresh()
    
    
    with mic as source:
        audio = r.listen(source,phrase_time_limit = None)
    speech = r.recognize_google(audio)
    upperspeech = [word.upper() for word in speech.split()]
    returnacc(account).updatewithspeech(upperspeech)
    print("these are the items you updated ")
    print(upperspeech)
    done = input("are you done updating items?  ")
    if done == "yes":
        start()
    elif done == "no":
        updatestate()
    
def shortcutz():
    while True:
        items = input("update items,display items,read, or go back ")
        iandq = items.split()
        
        if len(iandq) < 2:
            if iandq[0] == "HOME":
                shortcutz()

            else:
                shortcutz()
                

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
                    shortcutz()
            else:
                shortcutz()
        






            
         





    

# def readstate():
#     account = input("which account do you want to read from  ")
#     if account == "rich" or account =="poor" or  account =="medium":
#         returnacc(account).refresh()
    
#     else:
#         readstate()
#     for item in returnacc(account).itemlist:
#         if item.done == "N":
#             engine.say(item.name)

#     returnacc(account).display()    
#     engine.runAndWait()
    
#     question = input("are you done  ")
#     if question == "yes":
#         start()
#     else:
#         readstate()


richacc= Account(rich)
medacc = Account(rich)
pooracc = Account(poor)

start()

   















   





        






