
import time
from colorama import Fore, Back, Style
from staticvars import *

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

        
    


