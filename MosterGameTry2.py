from random import randint
import time

 

moves = ["left", "right", "up", "down", "grab", "fight", "run", "teleport", "help"]
#roomContains = ["sword", "monster", "magic stone", "nothing","magic stone"]
#testing
#roomContains = ["nothing","nothing","nothing","nothing","nothing"]
roomContains = ["sword", "nothing", "magic stone", "nothing","magic stone"]

defendedPharses = ["invaded", "blocked", "dodged"]

lvl = []
playerPos = []
mapArr = []

items = []

potions = []

amountInventorySpace = 3
coin = 20
health = 5
hasSword = 0
numMagicStones = 0
monstersDefeated = 0
numberOfDungeonsDefeated = 0
hasDungeonKey = True

isValidMoveVar = False

#stat var####################
numMagicStones = 0
monstersDefeated = 0
numberOfDungeonsDefeated = 0
#coin
totalNumberOfAttacks = 0
NumberOfAttacksThatLanded = 0
#############################
#can buy strength potions
#can buy health potions
#better swords
#more inventory
#the merchant 
def merchant(strengthPotion):
    print("You have found a merchant willing to sell you upgrades and potions")
    

def showStats():
    print("\n\nMagic stones collected: "+str(numMagicStones))
    print("Ending bank: "+str(coin))
    print("Total monsters defeated: "+str(monstersDefeated))
    print("Number of DungeonsDefeated: "+str(numberOfDungeonsDefeated))
    print("Hit percentage: "+str(NumberOfAttacksThatLanded/totalNumberOfAttacks))

def endGame(won):
    if(won):
        print("You have defeated all of the dungeons congrats!")
        print("You have saved the princess!")
        
    else:
        print("You were defeated :(")
    yn = False
    while (yn == False):
        answer = input("Do you want to see your stats?  y/n ")
        if(answer.lower() == "y" or answer.lower() == "n"):
            yn = True
    showStats()
    time.sleep(20)
    quit()

def restart():
    pass

def finalBoss():
    print("You are now fighting the final boss")
    hasWon = fight(4, 1, 15, 5)
    endGame(hasWon)
    

#definitly spelled that wrong lol
def nextDungeon():
    #upgrade shop
    global numberOfDungeonsDefeated
    numberOfDungeonsDefeated+=1
    
    if(numberOfDungeonsDefeated == 3):
        finalBoss()
    else:
        print("Teleporting...")
        time.sleep(3)
        init(5,5)
        gameLoop()

def placeDungeonKey():
    #made it 1 so that it does not get rid of the stairs for each of the lvls
    randomRow = randint(1, len(lvl)-1)
    #the -2 insures that it does not get rid of the next dungeon portal 
    randomColumn = randint(1, len(lvl[0])-2)

    #print("randomRow: "+str(randomRow))
    #print("randomColumn: "+str(randomColumn))
    #print("len(lvl[0]): "+str(len(lvl[0])))
    
    lvl[randomRow].pop(randomColumn)
    lvl[randomRow].insert(randomColumn, "Dungeon Key")

#parms are oppisite 
def makeBoard(numberRooms, amountLvls):
    tempFloor = ["stairs"]
    
    tempPlayerFloor = [0]
    tempMapFloor = [0]
    for i in range(0,amountLvls):
        if( i !=0):
            playerPos.append(tempPlayerFloor)
            lvl.append(tempFloor)
            mapArr.append(tempMapFloor)
            tempPlayerFloor = [0]
            tempMapFloor = [0]
            tempFloor = ["stairs"]
        for j in range(0,numberRooms):
            tempFloor.append(roomContains[randint(0,4)])
            tempPlayerFloor.append(0)
            tempMapFloor.append(0)
            
    lvl.append(tempFloor)
    lvl[amountLvls-1].pop()
    lvl[amountLvls-1].append("Next Dungeon")
    placeDungeonKey()
    playerPos.append(tempPlayerFloor)
    mapArr.append(tempMapFloor)
    playerPos[0][0] = 1
    mapArr[0][0] = 1
    #print(lvl)
    #print(mapArr)
    #print(playerPos)
    
    

def getCurrentPos():
    #print("len(lvl): "+str(len(playerPos)))
    #print("len(lvl[0]): "+str(len(playerPos[0])))
    for i in range(0,len(lvl)):
        for j in range(0,len(lvl[0])):
            #print("I: "+str(i))
            #print("J: "+str(j))
            if(playerPos[i][j]==1):
                #print("Found Player")
                return (i,j)
    #print("Didn't find player")
    return(0,0)

def isValidMove(move): 
    for i in range(0, len(moves)):
        if(move.lower() == moves[i]):
            return True
    return False



def changePos(newX,newY):
    oldX,oldY = getCurrentPos()
    #print("newX: "+str(newX))
    #print("newY: "+str(newY))
    playerPos[oldX][oldY] = 0
    playerPos[newX][newY] = 1
    mapArr[newX][newY] = 1

def showMap():
    x,y = getCurrentPos()
    
    
    for i in range(len(mapArr)-1,-1,-1):
        print()
        for j in range(0, len(mapArr[0])):
            if(mapArr[i][j] == 1):
                if(j==0):
                    print("{:6s}".format("Floor "+str(i)+": "), end="")
                print("{:11s}".format(lvl[i][j]), end=" | ")
            
    print()
def locateItem(item):
    for i in range(0,len(items)):
        if(items[i] == item):
            return i
    return -1

def didLand(num):
    one = randint(0,num)
    two = randint(0,num)
    if(one == two):
        return True
    else:
        return False
    
def useHealthPotion(buying):
    global coin
    global health
    
    if(buying == True):
        wantHealthPotion = input("Do you want a health potion it costs 10 coins but it raises your health by 3 y/n? ")
        if (wantHealthPotion.lower() == "y" and coin >= 10):
            coin -= 10
            potions.append("health potion")
            print("Health potion was added to your inventory")
        elif(wantHealthPotion.lower() == "y" or wantHealthPotion.lower() != "n"):
            print("You don't have enough coin") if coin<10 else print()
    else:
        useNow = input("Current health: "+str(health)+"\nDo you want to use a health potion y/n? ")
        if(useNow.lower() == "y"):
            health += 3
            potions.pop()
        #False          True
def run(fightAtTheEnd, askingToRun, usedValue):
    isRunning = usedValue

    x,y = getCurrentPos()

    hasRan = False

    didLandBoo = didLand(4)
    
    if(askingToRun == True):
        isRunning = input("Do you want to try to run y/n? ")

    if(isRunning.lower() == "y" and didLandBoo):
        print("isRunning: "+isRunning)
        hasRan = True
        print("You got safely ran away")
        lvl[x][y] = "nothing"
        return hasRan
    elif(didLandBoo == False and isRunning=="y"):
        print("You didn't get away...")
        if(fightAtTheEnd == True):
            print("You are now fighting a monster")
            fight(3, 1, randint(1,6), 10)
        return False
        
            

def fight(playerChance, monsterChance, monsterHealthPar, monsterDamagePar):
    global coin
    global health
    global monstersDefeated
    global totalNumberOfAttacks

    monsterHealth = 0
    monsterDamage = 0
    x,y = getCurrentPos()
    isFightGoing = True
    bonusDamage = 0
    numSword = 0
    monsterHealth = monsterHealthPar
    monsterDamage = monsterDamagePar

    for i in range(0,len(items)):
        if(items[i] == "magic stone"):
            bonusDamage+=1.5
        if(items[i] == "sword"):
            numSword+=1
    #this add because you are dueling weilding swords
    if(numSword==2):
        bonusDamage += 2.5
    
    damage = 2.5 + bonusDamage

    hasRun = False

    print("Bank Balance: "+str(coin))

    useHealthPotion(True)

    
    
    while (isFightGoing == True):
        print("Monster Health: "+str(monsterHealth))
        print("Your Health: "+str(health))
        print("Number of Health Potions: "+str(len(potions))+"\n\n")
        totalNumberOfAttacks+=1
        print("Attacking...")
        time.sleep(1.5)

        #player fighting part

        if(didLand(playerChance)):
            print("Your attack landed!")
            print("You did "+str(damage)+" damage")

            NumberOfAttacksThatLanded+=1
            
            if(locateItem("sword") != -1):
                monsterHealth -= damage
                print("Monster health: 0") if monsterHealth<0 else print("Monster health: "+str(monsterHealth))
                
            else:
                monsterHealth -= bonusDamage/2
                print("You have no more swords")
                print("You had to use your fists")
        else:
            print("Your attack didn't land :(")
        if(monsterHealth >0):
            if(len(potions) != 0):
                useHealthPotion(False)
            if(coin>=10):
                useHealthPotion(True)
        if(monsterHealth<=0):
            print("Defeated monster!")
            print("+10 coins")
            coin+=10
            lvl[x][y] = "nothing"
            monstersDefeated += 1
            return True
        
        #monster fighting part
        hasRun = run(False, True,"n")
        time.sleep(1)

        if(hasRun == True):
            break
        
        print("\nMonster is attacking...\n")
        
        if(didLand(monsterChance)):
            print("Monster attack landed! :(")
            health -= monsterDamage
            print("You loss "+str(monsterDamage)+" health")
            
        else:
            print("You "+defendedPharses[randint(0,2)]+" the monster's attack")
            print("You have gained 1 coin")
            coin+=1

        if(health<=0):
            print("You were defeated!!")
            print("The monster has won!")
            endGame(False)

        time.sleep(1)
                



def moveAction(move, room):
    x,y = getCurrentPos()
    #print(playerPos)
    global hasSword
    global numMagicStones
    global hasDungeonKey
    global hasDied
    
    if(room != "monster" and room != "stairs" and room != "Next Dungeon" and move != "fight" and move != "run"):
        if(move == "left" and y<=len(lvl[0]) and y>0):
            changePos(x,y-1)
            print("Moved left")
        elif(move == "right" and y>=0 and y <len(lvl[0])-1):
            changePos(x,y+1)
            print("Moved right")
        elif(room != "sword" and move != "grab" ):
            print("You can not move because you are too close to the side")

        if (move == "grab" and len(items) != amountInventorySpace or move == "grab" and room == "Dungeon Key"):
            if(room == "sword"):
                hasSword+=1
                items.append("sword")
                lvl[x][y] = "nothing"
                print("Picked up a sword")
            elif(room == "magic stone"):
                items.append("magic stone")
                lvl[x][y] = "nothing"
                print("Picked up a magic stone")
            elif(room == "Dungeon Key"):
                hasDungeonKey = True
                lvl[x][y] = "nothing"
                print("Picked up the dungeon key!")
                print("Now find the dungeon portal!")
                
        elif(move == "grab"):
            isInInventory = False
            #maybe add a function if I want to drop items or not
            print("You are carrying too many items")
            print("You are currently carrying...")
            for i in range(0,len(items)):
                print(items[i])
            doesWantToDropItem = input("Do you want to drop an item? y/n ")
            if(doesWantToDropItem.lower() == "y"):
                while(isInInventory == False):
                    itemWantsToDrop = input("What Item do you want to drop? ")
                    for i in range(0, len(items)-1):
                        if(items[i] == itemWantsToDrop):
                            isInInventory = True
                            break
                print("You dropped "+ itemWantsToDrop)
                print("You added "+room+" to your inventory")
                lvl[x][y] = itemWantsToDrop
                items.pop(locateItem(itemWantsToDrop))
                items.append(room)
                print(items)
    elif(room == "stairs"):
        if(move == "up" and x != len(lvl)-1):
            changePos(x+1, y)
            print("Moved up to floor "+str(x+1))
        elif(move == "down" and x != 0):
            changePos(x-1, y)
            print("Moved down to floor "+str(x-1))
        elif(move == "right" and y>=0):
            changePos(x,y+1)
            print("Moved right")
        else:
            print("You can't go that direction") if move == "left" else print("You are too close to the top" if x==len(lvl) else "You are too close to the bottom")
    elif(room == "monster"):
        print()
        hasRan = False
        if(move == "run"):
            hasRan = run(True, False, "y")
        elif(move == "fight" and hasRan == False):
            print("You are fighting a monster")
            hasDied = fight(2, 2, randint(1,6), randint(1,5))
        else:
            print("You have to fight or you could to run")
            
    elif(room == "Next Dungeon"):
        
        if(move == "left" and y<=len(lvl[0]) and y>0):
            changePos(x,y-1)
            print("Moved left")
        elif(move == "teleport" and hasDungeonKey == True):
            nextDungeon()
        elif(hasDungeonKey == False):
            print("You don't have the dungeon key")
            print("Find the key somewhere in the dungeon")
        
    #print(playerPos)

def openingRemarks():
    print("Unquie things about my game: swords never break, you can dual wield swords for extra damage, you can buy health potions.")
    print("Your quest is to defeat all of the dungeons by getting swords, magic stones and the dungeon key.")
    print("The key is hidden somewhere in the dungeon.")
    print("Good luck.\n\n\n")

def init(numberRooms, amountLvls):
    global lvl
    global playerPos
    global hasDungeonKey
    global mapArr
    hasDungeonKey = False
    lvl = []
    playerPos = []
    mapArr = []
    print("This is going to happen")
    openingRemarks()
    makeBoard(numberRooms, amountLvls)

def gameLoop():
    global isValidMoveVar
    room = ""
    inputMove = ""
    hasDied = False
    
    while (hasDied == False):
        
        while (isValidMoveVar == False):
            x,y = getCurrentPos()
            room = lvl[x][y]
            print(playerPos)
            print("\n**************************************\n")
            showMap()
            print("\n")
            print("You are currently in a "+room+" room\n")
            print("You can go up, down or right") if room == "stairs" else print("You can go left or right") if room == "nothing" else print("You can go left, right or grab the item") if room == "magic stone" or room == "sword" else print("You can try and run or fight") if room == "monster" else print("You can teleport or left") if room == "Next Dungeon" else print("You can go left or right or grab")
            inputMove = input("What is your move? ")
            isValidMoveVar = isValidMove(inputMove)
            if(isValidMoveVar == False):
                print("\nYou have enter an invalid move please try again.\n")
        isValidMoveVar = False
        moveAction(inputMove, room)
        #print("hasDied: "+str(hasDied))
        print()
    #restart feature

#Goal to finsih the merchant class but got distracted by openCV
#can buy strength potions
#can buy health potions
#better swords
#more inventory
#the merchant 
class Merchant:

    global merchantInventory
    merchantInventory = ["health potion", "strength potion", "steel sword", "more inventory"]
    
    
    def __init__(self):
        pass

    def buyStrengthPotion(self):
        pass
    
    def buyHealthPotion(self):
        pass
    def buySword():
        pass
    def buyMoreInventory(self):
        print("asdf")
    

    def inBetweenDungeons(self):
        isThingSelling = False
        whatBuying = ""
        
        print("You have found a merchant!")
        isGoingToBuy = input("The merchangt sells goodies would you like to buy some y/n? ")
        if(isGoingToBuy.lower() == "y"):
            isGoingToBuy = True
            while (isGoingToBuy==True):
                print(f"{'Health Potion :':<5}{'5':>10}",
                      f"\n{'Strength Potion :':<5}{'8':>8}",
                      f"\n{'Steel Sword :':<5}{'10':>12}",
                      f"\n{'More Inventory :':<5}{'13':>9}",
                      f"\n{'Exit':<5}{'':>10}"
                    )
            
                while(isThingSelling == False):
                    whatBuy = input("What do you want to buy? ")
                    for i in range(0, len(merchantInventory)):
                        if(merchantInventory[i] == whatBuy.lower()):
                            isThingSelling = True
                        elif (whatBuy.lower() == "exit"):
                            isGoingToBuy = False
                            isThingSelling = True
                            break
                  
            buyStrengthPotion() if whatBuying.lower() == "strength potion" else buyHealthPotion() if whatBuying.lower() == "health potion" else buySword() if whatBuying.lower() else buyMoreInventory()
                    
        else:
            print("Good luck, see you soon!")
                
    
        

    

init(3,3)
showMap()
gameLoop()
