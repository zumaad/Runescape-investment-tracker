# Runescape-investment-tracker
A tool that offers functionality to help with runescape in-game investing through text and speech-to-text based updates to items.

## Why does it exist?

Runescape is a game with a complex and player driven economy. The main way people trade with others is through an in-game feature
called the Grand Exchange (abbreviated to GE). The GE allows players to buy and sell items for the price they set and the only way these
offers complete(the item gets sold or bought) is when other players put compatible offers(compatible doesn't mean exactly the same price).

Due to the natural impatience in wanting to get items and sell items, there arises an oppurtunity to buy from the impatient
sellers and sell to the impatient buyers. But, there are a lot of items you can carry out this very general process with and there is a lot
to keep track of when doing this investing. That's where this tool comes in.

Before we delve into the functionality of the app, when investing in runescape in this way, to maximize your profit, these are the main
things you need to keep track of:


## What you need to keep track of

- the list of items you want to do (1)
- the buy limit of each item (the GE places a cap on the amount of certain items you can buy every four hours and this cap refreshes 4 hours since you bought the first of the item)(2)
- the quantity that you have currently bought and thus how many more of that item can you buy before you hit the cap. (3)
- whether you can do an item (4)
- whether you have already done an item (similiar to above) (5)
- when the buy limit refreshes so you can do items you have already done, again. (6)
- since you need to know when the buy limit refreshes, you also need to know when you bought the first of that item. (7)
- all of the above but for potentially several accounts (if you want to really make money). (8)


##How does the app keep track of all that stuff?

There are two classes in models.py
-Account
-Item


Account
```

def __init__(self,name):
        self.name = name
        self.itemlist = self.initializelist(name)
```

Item
```
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
```

(1) is kept track of by having the Account class have a field called itemlist in which there are a bunch of Item objects in a list with
each of those Item objects is referring to an item the Account can invest in.

(2)





