import random
import time
from enum import IntEnum

def choiceCheck(chChamber):
    
    if(chChamber == Menu.North):
        checkResult = "You chose the north chamber"
        
    elif(chChamber == Menu.South):
        checkResult = "You chose the south chamber"

    elif(chChamber == Menu.East):
        checkResult = "You chose the east chamber"

    elif(chChamber == Menu.West):
        checkResult = "You chose the west chamber"

    elif(chChamber == Menu.Exit):
        checkResult = "See you soon!"
        
    else:
        checkResult ="Wrong"
        
    return checkResult

def chestCheck(chest, gold):
    
    if(chest == ["common"]):
        print("You found a common chest.")
        gold[0] += 1000
        
    elif(chest == ["rare"]):
        print("You have luck, you found a rare chest!")
        gold[0] += 4000

    elif(chest == ["epic"]):
        print("Wow, you found an epic chest!!!")
        gold[0] += 9000

    elif(chest == ["legendary"]):
        print("You're godlike, you found a LEGENDARY chest!!!")
        gold[0] += 16000
        
    sum(gold)
        
    
Menu = (IntEnum('Chamber Menu', 'North, South, East, West, Exit'))

chestFound = ["You found a chest!", "You didn't find the chest"]
treasureChest = ["common", "rare", "epic", "legendary"]


print ('''
Welcome to Treasure Chest!
You are in the castle with 4 chambers. 
In each chamber you take 5 steps and can find a maximum of 5 chests of different rarity.
Choose one of the chambers and search for the chests to find as much gold as possible!
''')

endLoading = False;

while(endLoading == False):
    
    chosenChamber = int(input('''Choose chamber:
1 - North chamber
2 - South chamber
3 - East chamber
4 - West chamber
5 - Exit
Insert number ->'''))
    
    message = choiceCheck(chosenChamber)

    if(message == "Wrong"):
        print("Enter the correct value!!!\n")
        continue
    
    else:
        print(message, "\n")
        endLoading = True

if(endLoading == True and chosenChamber != Menu.Exit):
    goldAmount = [0]
    chestAmount = 0

    print("Your current gold amount is:", goldAmount,"\n")

    for step in range(5):
    
        print("Step:",step+1)
        
        result = random.choices(chestFound,[0.60,0.40])
        print(result)
    
        if(result == ["You found a chest!"]):
            chestAmount += 1
            print("Congratulations. I'm checking the chest...\n")
            time.sleep(5)
            whichChest = random.choices(treasureChest,[0.75, 0.20, 0.04, 0.01])
            chestCheck(whichChest, goldAmount)
        
        print("Your current gold amount is:", goldAmount,"\n")
        time.sleep(5)

    print("You finished the game with", chestAmount,"chests found and",goldAmount,"gold.")


                   
