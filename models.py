"""
The models of the application. This is how the app stores data. Through the methods available in these 
classes, data is updated.
"""
import time
from colorama import Fore, Back, Style
from staticvars import *

green = Fore.GREEN + Style.BRIGHT
red = Fore.RED
magenta = Fore.MAGENTA 

class Account:
    """
    This class represents an account with a name and a list of items
    that that account can invest in. Through the methods available in this class
    the item list is updated.
    """

    def __init__(self,name):
        self.name = name
        self.itemlist = self.initializelist(name)
        

    def initializelist(self,name):
        """
        Initializes a item list from the given dictionary of items

        Parameters:
        name: refers to the dictionary of items passed into this account
        """
        L = []
        for k,v in name.items():
            a =Item(k,v,0)
            L.append(a)
        return L

    
    def update(self,name,quantity="NA"):
        """
        updates an item in the item list so its quantity and status reflects the user's input

        Parameters:
        name:the name of the item as given in the dictionary that was used to inialize the list.
        quantity: the amount of items the user inputs. This refers to the amount of that item
                  the account has purchased.
        """
        for item in self.itemlist:
            if item.name == name:
                item.done = "Y"
                if item.quantity == 0:
                    item.time = time.localtime()
                item.quantity = item.quantity + int(quantity)
                
                


    def display(self):
        """
        displays the items in the console in different colors based on their status. If 
        the account has purchased more than half the buy limit, the item is displayed in 
        magenta. If the account has hit the buy limit, the items is printed out in red. Else,
        the item is printed out in green.
        """
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


    
    def updatewithspeech(self,list):
        """
        This function updates the item list with a list of items its given. It does so
        by calling update with every item in the list its given.

        Parameters:
        list: the list of items its given to update. The list contains item names
        """
        for i in range(len(list)):
            self.update(list[i],0)

    def refresh(self):
        """
        Every four hours the buy limit for an item is reset. This method, checks the item list
        to see if there were items bought > 4 hours ago and if so, clears the times they have 
        been bought as now they can be bought again up until the buy limit
        """
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
    """
    This class represents an item. An item has a name, a limit which represents how many times
    it can be bought in a four hour period, and a quantity which represents how many times
    it has been bought currently, and a time which represents when it was first bought
    """

    def __init__(self, name, limit,quantity = 0,done = "N",time = None):
        """
        Initializes an item object

        Parameters:
        name : the name of the item as a string.
        limit : the amount of times it can be bought in a 4 hour period
        quantity: the amount of times it has currently been bought.
        done : whether it has been bought before.
        time: the time it was first bought.
        """
        self.name = name 
        self.quantity = quantity
        self.limit = limit
        self.time = time
        self.done = done

    def reset(self):
        """
        resets an item by setting the times it was bought to 0 and the field representing
        wether it has been bought to show it hasn't and the time to none - as it hasn't been bought yet,
        this method is typically called every four hours, when the buy limit resets.
        """
        self.quantity = 0
        self.done = "N"
        self.time = None

        
    


