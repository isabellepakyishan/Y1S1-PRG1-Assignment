#Isabelle Pak Yi Shan | S10222456 | Simp City (Final)

#We first import random to generate random integers from 0 to 4 (in the form of indexes, basically generating numbers from
# 1 to 5). This will help in the randomising of the buildings available in the options
import random
#This variable gameMap is an empty layout of the map that will be used for the players to input the various buildings into
#each of the cells during the course of the game
gameMap = [ ['   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   '],\
            ['   ', '   ', '   ', '   ']]

#This variable stores the number of copies for each building available at the start of the game
#There are 5 nested lists, each for a different type of a building. Within each nested list, there is a value of 8 stored, 
#which is the number of copies for each building available at the start of the game, and will be decremented during the
#course of the game
buildingListWithCopies = [["BCH", 8], ["FAC", 8], ["HSE", 8], ["SHP", 8], ["HWY", 8]]

#Since the map to be printed is a 4x4 grid, the first 4 letters of the alphabet is stored in the variable alphabets
alphabets = "ABCD"

#main menu functions
def mmfunc():
    #main menu options
    mmc1 = "1. Start new game"
    mmc2 = "2. Load saved game"
    mmc3 = "0. Exit"
    #printing main menu options
    print(mmc1)
    print(mmc2)
    print()
    print(mmc3)

#print map function
def printMap():
    #Print the Turn number for the user to see which turn they are at, which increments for every time they build a building
    print(f"Turn {counter}")
    print("  ", end="")
    for alpha in range(len(gameMap[0])):
        print("{:^6s}".format(alphabets[alpha]), end="")
        
    #Prints the type of buildings and each of the building's remaining number of buildings in a table together 
    print("{:>10s} {:>13s}".format("Building", "Remaining"))
    print(" ", end="")
    for sym in range(len(gameMap[0])):
        print("+-----", end = "")
    print("+", end = "")
    print("{:>10s} {:>13s}".format("--------", "---------"))
    
    count = 1
    br1 = -1
    br2 = 0
    for i in range(len(gameMap)):
        print(count, end="")
        for element in range(len(gameMap[i])):
              print(f"| {gameMap[i][element]} ", end = "")
        print("|", end="")
        if br1 <= 4:
            print("{:>5s} {:>10d}".format(buildingListWithCopies[br1+1][0], buildingListWithCopies[br1+1][1]))
        else:
            print()
        print(" ", end="")
        for sym in range(len(gameMap[0])):
            print("+-----", end = "")
        print("+", end="")
        if br2 <= 3:
            print("{:>5s} {:>10d}".format(buildingListWithCopies[br2+1][0], buildingListWithCopies[br2+1][1]))
        else:
            print()
        count += 1
        br1 += 2
        br2 += 2

#This function saves current game to be resumed later 
def savingGame():
    #accesses the building txt file and opens the file in the variable buildingsFile
    with open("Buildings.txt", "w") as buildingsFile:
        for index in range(len(buildingListWithCopies)):
            tempLine = "{},{}\n".format(buildingListWithCopies[index][0], buildingListWithCopies[index][1])
            buildingsFile.write(tempLine)
    #accesses the Game Map txt file and opens the file in the variable gameFile
    with open("Game Map.txt", "w") as gameFile:
        for element in gameMap:
            anotherLine = "{},{},{},{}\n".format(element[0], element[1], element[2], element[3])
            gameFile.write(anotherLine)
    #accesses the building txt file and opens the file in the variable turnFile
    with open("Turn Number.txt", "w") as turnFile:
        turnFile.write(str(counter))

#This function checks the building surroundings
def checkSurroundings():
    #counter needs to be a global variable so that it continues to increment despite it being within a function
    global counter
    #When the option which the user chooses is either 1 or 2, meaning that they want to build a building on the map,
    #the if statement will run and ask the user where they want to build the building
    if userInput == 1 or userInput == 2:
        userBuild = input("Build where? ")
        print()
        #from the user input, we will take the alphabet and find the index of the alphabet from the string of alphabets
        column = alphabets.find(userBuild[0].upper())
        #based on the integer given in the user input, we negate it by 1 to find it in terms of integers
        row = int(userBuild[1]) - 1
        #if the player is on the first turn, they can build the building anywhere on the game map.
        #The value of both the buildings generated from the randomiser will be negated by 1, and this happend for all 16
        #turns of the game
        if counter == 1:
            gameMap[row][column] = selectedBuilding
            buildingListWithCopies[ranNum1][1] -= 1
            buildingListWithCopies[ranNum2][1]-= 1
            counter += 1
        #this checks for whether the place where the player would like to place the building has at least one building around it
        #this also depends on whether the buildings are on the left, right, top or bottom. according to the conditions, if all of the
        #cells surrounding the place where the user wants to place the building is empty, then an error message will be displayed,
        #otherwise the 2 types of buildings generated using the randomiser will have the number of copies decremented by 1 and the building
        #will be displayed in the cell which the player chose in "Build where?"
        else:
            #if the column which the user wants to build in is column A
            if column == 0:
                if row == 0 and gameMap[row+1][column] == "   " and gameMap[row][column+1] == "   ": #for 1A
                    print(errorMsg)
                    print()
                elif (row == 1 or row == 2) and gameMap[row-1][column] == "   " and gameMap[row+1][column] == "   " and gameMap[row][column+1] == "   ": #for 2A
                    print(errorMsg)
                    print()
                elif row == 3 and gameMap[row-1][column] == "   " and gameMap[row][column+1] == "   ": #for 4A
                    print(errorMsg)
                    print()
                else:
                    buildingListWithCopies[ranNum1][1] -= 1
                    buildingListWithCopies[ranNum2][1]-= 1                           
                    gameMap[row][column] = selectedBuilding
                    counter += 1
            #if the column which the user wants to build in is column B or C
            elif column == 1 or column == 2:
                if row == 0 and gameMap[row][column-1] == "   " and gameMap[row][column+1] == "   " and gameMap[row+1][column] == "   ": #for 1B
                    print(errorMsg)
                    print()             
                elif (row == 1 or row == 2) and gameMap[row-1][column] == "   " and gameMap[row+1][column] == "   " and gameMap[row][column-1] == "   " and gameMap[row][column+1] == "   ": #for 2B
                    print(errorMsg)
                    print()
                elif row == 3 and gameMap[row][column-1] == "   " and gameMap[row][column+1] == "   " and gameMap[row-1][column] == "   ": #for 4B
                    print(errorMsg)
                    print()
                else:
                    buildingListWithCopies[ranNum1][1] -= 1
                    buildingListWithCopies[ranNum2][1]-= 1                  
                    gameMap[row][column] = selectedBuilding
                    counter += 1
           #if the column which the user wants to build in is column D                     
            elif column == 3:
                if row == 0 and gameMap[row][column-1] == "   " and gameMap[row+1][column] == "   ": #for 1D
                    print(errorMsg)
                    print()
                elif (row == 1 or row == 2) and gameMap[row-1][column] == "   " and gameMap[row+1][column] == "   " and gameMap[row][column-1] == "   ": #for 2D
                    print(errorMsg)
                    print()
                elif row == 3 and gameMap[row][column-1] == "   " and gameMap[row-1][column] == "   ": #for 4D
                    print(errorMsg)
                    print()
                else:
                    buildingListWithCopies[ranNum1][1] -= 1
                    buildingListWithCopies[ranNum2][1]-= 1                          
                    gameMap[row][column] = selectedBuilding
                    counter += 1    

#This function calculates the scores for each of the different type of buildings based on certain conditions specified for each of the buildings
def calculateScores():
    #this stores all the scores for each of the types of buildings based on certain conditions
    beachScores = []
    factoryScores = []
    factoryNum = 0
    houseScores = []
    shopScores = []
    highwayScores = []
    #this loop and nested loop steps through every building in the cell and has various outputs based on the type of building within each cell
    for line in range(len(gameMap)):
        for element in range(len(gameMap)):
            #this loop runs if the building in the cell is a house
            if gameMap[line][element] == "HSE": #house points calculation
                houseList = []
                tempHouseScore = 0
                
                up = True
                down = True
                left = True
                right = True
                #if the row is 1, then don't check above it since there is no row above it
                if line == 0:
                    up = False
                #if the row is 4, then don't check below it since there is no row below it
                if line == 3:
                    down = False
                #if the column is A, then don't check left of it since there is no column to the left of it
                if element == 0:
                    left = False
                #if the column is D, then don't check left of it since there is no column to the left of it
                if element == 3:
                    right = False

                if up == True: #stores rows 2, 3, 4
                    houseList.append(gameMap[line-1][element])
                if down == True: #stores rows 1, 2, 3
                    houseList.append(gameMap[line+1][element])
                if left == True: #stores columns b, c, d
                    houseList.append(gameMap[line][element-1])
                if right == True: #stores columns a, b, c
                    houseList.append(gameMap[line][element+1])

                #this loop iterates through each of the buildings in the houseList
                for x in houseList:
                    #if the building is a factory, then the house score to be stored in the house score list will be 1 and it will break out of the loop,
                    #otherwise, if the buildings surrounding the house is another house or a shop, then each will be able to be incremented by 1 and
                    #if the house is next to a beach then its overall score will be incremented by 2 instead
                    if x == "FAC":
                        tempHouseScore = 1
                        break
                    elif x == "HSE":
                        tempHouseScore += 1
                    elif x == "SHP":
                        tempHouseScore += 1
                    elif x == "BCH":
                        tempHouseScore += 2
                        
                houseScores.append(tempHouseScore)

            #this loop will run if the building is a shop.
            if gameMap[line][element] == "SHP": #shop points calculation
                shopList = []
                tempShopScore = 0

                #this list will store the unique buildings surrounding each shop
                unique = []
                
                up = True
                down = True
                left = True
                right = True 
                if line == 0:
                    up = False
                if line == 3:
                    down = False
                if element == 0:
                    left = False
                if element == 3:
                    right = False

                if up == True: #stores rows 2, 3, 4
                    shopList.append(gameMap[line-1][element])
                if down == True: #stores rows 1, 2, 3
                    shopList.append(gameMap[line+1][element])
                if left == True: #stores columns b, c, d
                    shopList.append(gameMap[line][element-1])
                if right == True: #stores columns a, b, c
                    shopList.append(gameMap[line][element+1])

                #for every unique building next to the shop, the shop will earn a score based on the number of unique buildings around it
                for shop in shopList:
                    if shop not in unique:
                        unique.append(shop)
                shopScores.append(len(unique))
            #this loop runs if the building is a beach
            if gameMap[line][element] == "BCH": #beach points calculation
                #if the beach is in column A or D, the beach will earn 3 points
                if element == 0 or element == 3:
                    beachScores.append(3)
                #otherwise, the beach will earn only 1 point
                else:
                    beachScores.append(1)
            #this loop runs if the building is a factory and the counter counting the number of factories within the map will be incremented by 1
            if gameMap[line][element] == "FAC": #factory counter
                factoryNum += 1

    #if there are 4 or less factories, then the points achieved will be the square of the number of factories in the map
    if factoryNum <= 4: #factory points calculation
        for i in range(factoryNum):
            factoryScores.append(factoryNum)
    #otherwise, if there are more than 4 factories, then the points achieved will be 4 squared (4**2) and (x-4) for each of the additional factories
    elif factoryNum > 4:
        for i in range(4):
            factoryScores.append(4)
        for x in range(factoryNum - 4):
            factoryScores.append(1)
    #this loop will always run to check if the building in each cell is a highway
    for row in gameMap: #highway points calculation
        #this counter will count the number of highways that are in the same row
        highwayCounter = 0
        #this temporarily stores the points scored by each row of highways before being appended to the main highwayScores list
        tempHighway = []
        for building in row:
            if building == "HWY":
                highwayCounter += 1
            else:
                #if the counter is not 0, then you add it to the tempHighway and then clear the counter before the next row
                if highwayCounter != 0:
                    tempHighway.append(highwayCounter)
                    highwayCounter = 0
        #this check if the last element in the building map (d4) is a highway, just in case it gets missed out
        if highwayCounter != 0:
            tempHighway.append(highwayCounter)
        #for the length of the highway, loop it for that number of times to display what score each of the highways earn
        for score in tempHighway:
            for i in range(score):
                highwayScores.append(score)

    #this will print the scores breakdown for each of the buildings and the final total score earned by the player
    print("BCH:", end = " ")
    BCHsum = 0
    for beachscore in beachScores:
        BCHsum += beachscore
    for bchScore in range(len(beachScores)):
        if bchScore > 0:
            print("+", end=' ')
        print(beachScores[bchScore], end=' ')
    print('=', BCHsum)

    print("FAC:", end = " ")
    FACsum = 0
    for factoryscore in factoryScores:
        FACsum += factoryscore
    for facScore in range(len(factoryScores)):
        if facScore > 0:
            print("+", end=' ')
        print(factoryScores[facScore], end=' ')
    print('=', FACsum)

    print("HSE:", end = " ")
    HSEsum = 0
    for housescore in houseScores:
        HSEsum += housescore
    for hseScore in range(len(houseScores)):
        if hseScore > 0:
            print("+", end=' ')
        print(houseScores[hseScore], end=' ')
    print('=', HSEsum)

    print("SHP:", end = " ")
    SHPsum = 0
    for shopscore in shopScores:
        SHPsum += shopscore
    for shpScore in range(len(shopScores)):
        if shpScore > 0:
            print("+", end=' ')
        print(shopScores[shpScore], end=' ')
    print('=', SHPsum)

    print("HWY:", end = " ")
    HWYsum = 0
    for highwayscore in highwayScores:
        HWYsum += highwayscore
    for hwyScore in range(len(highwayScores)):
        if hwyScore > 0:
            print("+", end=' ')
        print(highwayScores[hwyScore], end=' ')
    print('=', HWYsum)

    totalSum = BCHsum + FACsum + HSEsum + SHPsum + HWYsum
    print(f"Total score: {totalSum}")

#this opens a file for the game to load the saved game
def openingFile():
    global gameMap
    accessingBuildings = open("Buildings.txt", "r")
    newBuildingList = []
    for type in accessingBuildings:
        type = type.strip("\n")
        type = type.split(",")
        type[-1] = int(type[-1])
        newBuildingList.append(type[-1])
    buildingCopies = newBuildingList
    print(buildingCopies)

    accessingGameMap = open("Game Map.txt", "r")
    newGameMap = [[], [], [], []]
    counter = 0
    for row in accessingGameMap:
        row = row.strip("\n")
        newGameMap[counter].append(row)
        counter +=1
    gameMap = newGameMap
    print(gameMap)

    with open("Turn Number.txt", "r") as turnFile:
        counter = int(turnFile.read()) 

    return buildingCopies, gameMap, counter



#counter
count = 1

#starting title of game
print("Welcome, mayor of Simp City!")
print("----------------------------")
mmfunc()
1
userInput = int(input("Your choice? "))

#if the user chooses to start a new game, this loop will run
if userInput == 1:
    #this is the counter that counts as the number of turns increases through the game
    counter = 1
    #this loop runs for as long as the game runs
    while counter <= 16:
        noCopiesLeft = []
        lastCopyLeft = []
        
        #this checks if the buildings has only one or 0 copies left
        ranNum1 = random.randint(0, len(buildingListWithCopies)-1)
        ranNum2 = random.randint(0, len(buildingListWithCopies)-1)
        for i in range(len(buildingListWithCopies)):
            if buildingListWithCopies[i][1] == 0:
                noCopiesLeft.append(i)
        while ranNum1 in noCopiesLeft:
            ranNum1 = random.randint(0, len(buildingListWithCopies)-1)
        while ranNum2 in noCopiesLeft or ranNum2 in lastCopyLeft:
            ranNum2 = random.randint(0, len(buildingListWithCopies)-1)
            
        printMap()
        
        #game options
        c1 = f"1. Build a {buildingListWithCopies[ranNum1][0]}"
        c2 = f"2. Build a {buildingListWithCopies[ranNum2][0]}"
        c3 = "3. See current score"
        c4 = "4. Save game"
        c5 = "0. Exit to main menu"
        
        print(c1)
        print(c2)
        print(c3)
        print("")
        print(c4)
        print(c5)
        userInput = int(input("Your choice? "))
        #this error is shown when the building is built around empty spaces
        errorMsg = "You must build next to an existing building."
        
        selectedBuilding = ''
        if userInput==1:
            selectedBuilding = buildingListWithCopies[ranNum1][0]
        elif userInput==2:
            selectedBuilding = buildingListWithCopies[ranNum2][0]
            
        if userInput == 1 or userInput == 2:
            checkSurroundings()
                  
        elif userInput == 3: #calculates the current score of the game should the game at that point
            calculateScores()
            
        elif userInput == 4: #saves game to be resumed later on
            savingGame()
            print("Game saved!")
            mmfunc()
            break
            
        elif userInput == 0:
            mmfunc()
            userInput = int(input("Your choice? ")) 
            continue
        
    if counter > 16:
        print("Final layout of Simp City")
        printMap()
        calculateScores()

elif userInput == 2:
    fileOpen = openingFile() 
    buildingCopies = fileOpen[0]
    gameMap = fileOpen[1]
    counter = fileOpen[2]

elif userInput == 0:
    print("Exiting game...")
    
