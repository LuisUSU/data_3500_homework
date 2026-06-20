#FINAL PROJECT - Pokemon Card Pricing and Collection Application - Luis Cotton

#finish search for sealed price menu = search for sealed price and json file reading and writing
#finish copying over code to functions and renaming variables
#finish buy list menu = 1 new buylist dictionary json file that adds cards based on user card searches
#adds only the card name and raw near mint price, until they've told they do not want to add more,
#adds the prices up, and multiplies the total by the given percentage, gives a list with the total price and percentage of total price with card names

#IF I HAVE TIME
#update price function for wishlist, personal singles collection, personal sealed collection, vendor collection json files
#search and add names to a list from json files, then search the card names and append them to a new dictionary,
#and a newUpdatedPrices file, figure out how much things have changed then write to a new key in the cards history key
#wishlist json, personal singles collection, personal sealed collection, vendor collection

#Imports API Program

import json
from pathlib import Path #imports path function so we can see if files exist or not
import requests
import http.client

conn = http.client.HTTPSConnection("cardmarket-api-tcg.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "9253f78de8msh854c4d0e982097ep1c10f8jsn8fa2fb1ae50d",
    'x-rapidapi-host': "pokemon-tcg-api.p.rapidapi.com",
    'Content-Type': "application/json"
}

#Variables

personalCollectionDictionary = {} #personal collection dictionary
vendorCollectionDictionary = {} #vendor collection dictionary
buyListDictionary = {} #buying list, adds all cards searched to dictionary with their prices and clears it for a new transaction
wishlistDictionary = {}
searchHistoryDictionary = {} #search history dictionary
availableSetNames = []
availableSetPrices = []
availableSetsDictionary = {}
#Main Application Variables
programActive = True #boolean to check if you have quit the app
menuSelect = -1
menuSelect_numValidCheck = False
menuChoices = []

#Main Menu Variables
mainMenu = True #boolean to tell app to start on the main menu

#Search Card Price Menu Variables
searchCardPrice_menu = False
currentCardSearchDictionary = {}
currentFullCardSearchDictionary = {}
currentFilteredCardSearchDictionary = {}
cardSearchSaveToWishlist = False
cardSearchSaveToPersonalCollection = False
cardSearchSaveToVendorCollection = False


#Search Sealed Price Menu Variables
searchSealedPrice_menu = False

#Search Full Set Price Menu Variables
setPrices_menu = False
getNewSetData = False
setDataDictionary = {}
fullSetDictionary = {}
oldSetDataPrices = []
newSetDataPricies = []
fullSetDataDictionary = {}

setDataFileWrite = True
setDataFileChecks = False
setDataPriceChecks = False

#Buy List Menu Variables
buyList_menu = False

#Wishlist Menu Variables
wishlist_menu = False

#Personal Collection Menu Variables
personalCollection_menu = False

#Vendor Collection Menu Variables
vendorCollection_menu = False

#Quick Percentage Caclulator
quickPercentageCalculate_menu = False

#functions

#new card search functions
def newCardSearch(searchQuery):
    url = "/cards?search="
    url2 = "&rapidapi-key=9253f78de8msh854c4d0e982097ep1c10f8jsn8fa2fb1ae50d"
    searchQueryString = searchQuery
    searchQuery = searchQueryString.replace(" ", "+")
    fullUrl = str(url + searchQuery + url2)
    #print(fullUrl)
    conn = http.client.HTTPSConnection("pokemon-tcg-api.p.rapidapi.com")
    conn.request("GET", fullUrl)
    response = conn.getresponse()
    newCardSearchQuery = response.read().decode()
    #currentFullCardSearchDictionary = newCardSearchQuery
    #print(response.read().decode())
    conn.close()

    #write card search to json file
    with open("/workspaces/data_3500_homework/final_project/newCardSearchQuery.json", "w", encoding = "utf-8") as file:
        newCardSearchQuery = json.loads(newCardSearchQuery)
        json.dump(newCardSearchQuery, file, ensure_ascii = False, indent = 4)
        print("\nSaved Card Search to newCardSearchQuery.json!")

    # Extract the list of objects inside the "data" key
    with open("/workspaces/data_3500_homework/final_project/newCardSearchQuery.json", "r") as file:
        print("\nOpening Current Card Search file....")
        currentCardSearchJsonDictionary = json.load(file)
        currentFullCardSearchDictionary = currentCardSearchJsonDictionary.get("data", [])
    #We get the name of the card in the first dictionary position then we end this loop
    for item in currentFullCardSearchDictionary:
        cardName = item.get("name", "")
        break
    return (cardName,currentFullCardSearchDictionary)
#filter new card search keys for new dictionary
def newCardSearchFilter(cardName,currentFullCardSearchDictionary):
    for item in currentFullCardSearchDictionary:
        #get names of the card sets
        cardNameKey = item.get("name", "")
        if cardName == cardNameKey:
            cardSetKey = item.get("episode").get("name","")
            cardSetAcronym = item.get("episode").get("code","")
            cardNumberKey = item.get("card_number", "")
            cardRarityKey = item.get("rarity", "")
            currentRawPrice = item.get("prices").get("cardmarket").get("lowest_near_mint","")
            current30DayPriceAve = item.get("prices").get("cardmarket").get("30d_average","")
            current7DayPriceAve = item.get("prices").get("cardmarket").get("7d_average","")
            cardPSA10Price = item.get("prices",{}).get("ebay",{}).get("graded",{}).get("psa",{}).get("10",{}).get("median_price",{})
            currentFilteredCardSearchDictionary = {"name": cardNameKey, "set_name": cardSetKey,"code": cardSetAcronym,"card_number": cardNumberKey,"rarity": cardRarityKey,"current_near_mint_price": currentRawPrice,"30_Day_Price_Average": current30DayPriceAve,"7_Day Price_Average": current7DayPriceAve,"PSA_10_Card_Price": cardPSA10Price}
        return cardNameKey,currentFilteredCardSearchDictionary

#sealed search functions
def newSealedSearch(searchQuery):
    return
#filter sealed search keys for new dictionary
def newSealedSearchFilter(sealedName,currentFullSealedSearchDictionary)
    return

#IF I HAVE TIME
#search and save new search queries of names of cards in json file
def updatePrices():
    return

#commit and write update list to JSON file, that is named after where the call originated, based on the menu that was active
def commitNewUpdatedPrices()
    return
#Buy List Functions

#print saved buy list
def printBuyList()
    return

#add cards to new buy list
def addToBuyList():
    print("added:  ","surfing pikachu","to Buy List","\nadd another card? Y/N")
    #add card to buy list and ask if they want to add another or calculate price and percentage

#remove cards from new buy list
def removeFromBuyList():
    print("removed:  ","surfing pikachu","from Buy List","\nadd another card? Y/N")

#calculate the new buy list total price and ask if they want to divide by a certain percentage
def calculateBuyListTotalPrice():
    print("calculated buy list total of all added card prices in dictionary")
    #calculate and add the total price of all cards in list and ask if they want a percentage

#save new buy list to old buy list json file
def saveNewBuyList():
    print("buy list saved to json file")
    #save buy list to json file

#clear new buy list 
def clearCurrentBuyList():
    print("delete buy list dictionary from buy list dictionary json file")

#delete old buy list json file dictionary
def deleteBuyList():
    print("buy list is cleared")
    #delete all information in dynamic buy list so it's ready for a new list that is not saved to json file


#wishlist functions

#print wishlist as a list
def printWishList():
    with open("/workspaces/data_3500_homework/final_project/wishlist.json", "r", encoding = "utf-8") as file:
        wishlist = json.load(file)
        wishlistDictionary = wishlist
        wishlistNameList = wishlist.get("wishlist", [])
        cardNameList = []
        for item in wishlistNameList:
            cardNameList.append(item)
        print("\nCards in your Wishlist:")
        print()
        for names in cardNameList:
            print(names)
    return

#search for a card and add it to wishlist json
def addToWishlist(newCardName,newCardSearchDictionary):
    #open wishilst file
    with open("/workspaces/data_3500_homework/final_project/wishlist.json", "r", encoding = "utf-8") as file:
        wishlist = json.load(file)
        wishlist["wishlist"][newCardName]= newCardSearchDictionary
    with open("/workspaces/data_3500_homework/final_project/wishlist.json", "w", encoding = "utf-8") as file:
        json.dump(wishlist, file, ensure_ascii = False, indent = 4)   
    return newCardName

#remove a card from the wishlist
def removeFromWishlist():
    with open("/workspaces/data_3500_homework/final_project/wishlist.json", "r", encoding = "utf-8") as file:
        wishlist = json.load(file)
        wishlistDictionary = wishlist
        wishlistNameList = wishlist.get("wishlist", [])
        cardNameList = []
        for item in wishlistNameList:
            cardNameList.append(item)
        print("\nCards in your Wishlist:")
        print()
        for names in cardNameList:
            print(names)
    cardNameRemove = input("\nWhich card would you like to remove?  ")
    removeFromWishlist = True
    while removeFromWishlist == True:
            wishlistDictionaryNames = wishlistDictionary.get("wishlist",[])
            for name in wishlistDictionaryNames:
                print(name)
                if name == cardNameRemove:
                    del wishlistDictionary["wishlist"][name]
                    print()
                    print(cardNameRemove,"was removed from your wishlist!")
                    with open("/workspaces/data_3500_homework/final_project/wishlist.json", "w", encoding = "utf-8") as file:
                        json.dump(wishlistDictionary,file,ensure_ascii = False, indent = 4)
                        removeFromWishlist = False
                    break
    return

#ask user if they are sure they want to delete wishlist contents
def deleteWishlist():
    areYouReallySure = True
    while areYouReallySure == True:
        areYouSure = input("Are you sure you want to delete your entire Wishlist[Y/N]?")
        if areYouSure in ("n","N","y","Y"):
            if areYouSure in ("n","N"):
                areYouReallySure = False
                break
            if areYouSure in ("y","Y"):
                with open("/workspaces/data_3500_homework/final_project/wishlist.json", "r", encoding = "utf-8") as file:
                    wishlistDictionary = json.load(file)
                    del wishlistDictionary["wishlist"]
                with open("/workspaces/data_3500_homework/final_project/wishlist.json", "w", encoding = "utf-8") as file:
                    wishlistDictionary["wishlist"] = {}
                    json.dump(wishlistDictionary,file,ensure_ascii = False, indent = 4)
                    print("\nAll cards in Wishlist have been removed!")
                    areYouReallySure = False
            else:
                print("that is not a valid selection")
                continue
    return

#calculate total price of cards within wishlist
def calculateWishListTotalPrice():
    with open("/workspaces/data_3500_homework/final_project/wishlist.json", "r", encoding = "utf-8") as file:
        wishlist = json.load(file)
        wishlistPriceList = []
        for subdict in wishlist.values():
            for key, value in subdict.items():
                wishlistCardPrice = round(value.get("current_near_mint_price"),2)
                wishlistPriceList.append(wishlistCardPrice)
        totalWishlistPrice = sum(wishlistPriceList)
        print("Wishlist Total Price:", totalWishlistPrice)
    return

#Personal Singles Collection Functions

#print personal singles collection json as a list
def printPersonalSinglesCollection():
    print("print available personal collection dictionaries that can be printed and ask the user which one to print ")
    print("entire personal collection list","\nPersonal Collection Price")
    #read and print full personal collection from json file

#search for a card and add it to personal singles collection json
def addToPersonalSinglesCollection(newCardName,newCardSearchDictionary):
    #open personal collection file
    with open("/workspaces/data_3500_homework/final_project/personal_collection.json", "r", encoding = "utf-8") as file:
        personalCollection = json.load(file)
        personalCollection["personal_collection"][newCardName]= newCardSearchDictionary
    with open("/workspaces/data_3500_homework/final_project/personal_collection.json", "w", encoding = "utf-8") as file:
        json.dump(personalCollection, file, ensure_ascii = False, indent = 4)   
    return newCardName

#remove card from personal singles collection
def removeFromPersonalSinglesCollection():
    print("removed from collection")
    #remove card from json personal collection json file

#delete personal singles collection
def deletePersonalSinglesCollection():
    print("search for a card for your personal collection")
    print("ask user which personal collection dictionary entries to add the card to")#return the chosen personal collection ID for the next function
    print("add:  ","charmander","to your collection? Y/N")#if no then search for a new card or go to main menu and saving the json file

#calculate total price of all cards in personal singles collection json
def calculatePersonalSinglesCollectionTotalPrice():
    print("calculate total price of personal collection in realtime prices and print the total price added")
    #calculate total price of all items in personal collection from json file

#Personal Sealed Collection Functions

#print personal sealed collection json as a list
def printPersonalSealedCollection():
    print("print available personal collection dictionaries that can be printed and ask the user which one to print ")
    print("entire personal collection list","\nPersonal Collection Price")
    #read and print full personal collection from json file

#search for a card and add it to personal sealed collection json
def addToPersonalSealedCollection(newCardName,newCardSearchDictionary):
    #open personal collection file
    with open("/workspaces/data_3500_homework/final_project/personal_collection.json", "r", encoding = "utf-8") as file:
        personalCollection = json.load(file)
        personalCollection["personal_collection"][newCardName]= newCardSearchDictionary
    with open("/workspaces/data_3500_homework/final_project/personal_collection.json", "w", encoding = "utf-8") as file:
        json.dump(personalCollection, file, ensure_ascii = False, indent = 4)   
    return newCardName

#remove card from personal sealed collection
def removeFromPersonalSealedCollection():
    print("removed from collection")
    #remove card from json personal collection json file

#delete personal sealed collection
def deletePersonalSealedCollection():
    print("search for a card for your personal collection")
    print("ask user which personal collection dictionary entries to add the card to")#return the chosen personal collection ID for the next function
    print("add:  ","charmander","to your collection? Y/N")#if no then search for a new card or go to main menu and saving the json file

#calculate total price of all cards in personal sealed collection json
def calculatePersonalSealedCollectionTotalPrice():
    print("calculate total price of personal collection in realtime prices and print the total price added")
    #calculate total price of all items in personal collection from json file


#Vendor Collection Functions

#print vendor collection json as a list with prices attached
def printVendorCollection():
    print("print available vendor collection dictionaries that can be printed and ask the user which one to print ")
    print("total vendor collection dictionary list")
    #read and print total vendor collection list from json file

#search for a card and add it to vendor collection
def addToVendorCollection(newCardName,newCardSearchDictionary):
    #open vendor collection file
    with open("/workspaces/data_3500_homework/final_project/vendor_collection.json", "r", encoding = "utf-8") as file:
        vendorCollection = json.load(file)
        vendorCollection["vendor_collection"][newCardName]= newCardSearchDictionary
    with open("/workspaces/data_3500_homework/final_project/vendor_collection.json", "w", encoding = "utf-8") as file:
        json.dump(vendorCollection, file, ensure_ascii = False, indent = 4)   
    return newCardName
    #add card to json vendor collection json file

#remove a card from vendor collection json file
def removeFromVendorCollection():
    print("Search and add or just view card price from Vendor Collection Menu")
    print("ask user which vendor collection dictionarie entries to add the card to")#return the chosen vendor collection ID for the next function
    print("add:  ","charmander","to your vendor collection? Y/N")#if no then search for a new card or go to main menu and saving the json file

#delete vendor collection
def deleteVendorCollection():
    print("flying pikachu","removed from vendor collection")
    #remove card from json vendor collection json file

#calculate the total price of all items in vendor collection json
def calculateVendorCollectionTotalProfit():
    print("total vendor collection profit from first price to price today")
    #calculcate total percentage and total profit price of vendor collection json file

    print("delete specific saved vendor collection dictionary entry in vendor collection dicitonary ")
    print("ask if the user is sure they want to delete the dictionary")
    #delete vendor dictionary in vendor collection dictionary json file


#Quick Percentage Calculator Function
def percentageCalculator(): #need variables, card price and what percentage to calculate
    print()
    total= round(int(input("Input price:  ")),2)
    percentage = round(int(input("Enter your percentage(ex: 80):  ")),2)
    percentage = percentage / 100
    totalPercentage = total * percentage
    print()
    print("Original price: ",total)
    print("Your percentage price is:  ", totalPercentage)

while programActive == True: #checking if the application is currently running

    while mainMenu == True: #Main Menu Interactions, Menu Selections, Menu Navigation

        #make all the other menu options inactive
        searchCardPrice_menu = False
        searchSealedPrice_menu = False
        searchFullSetPrice_menu = False
        buyList_menu = False
        wishlist_menu = False
        personalCollection_menu = False
        vendorCollection_menu = False
        appActive = True

        #print options and welcome message
        print()
        print("\nWelcome to Luis Cotton's Pokemon Card Management Program")
        print("\nMain Menu")
        print()
        print("1 - Search for Card Price")
        print("2 - Search for Sealed Product Price")
        print("3 - Set Prices")
        print("4 - Buy List Menu")
        print("5 - Wishlist Menu")
        print("6 - Personal Singles Collection Menu")
        print("7 - Personal Sealed Collection Menu")
        print("8 - Vendor Collection Menu")
        print("9 - Quick Percentage Calculation")
        print("0 - Quit Program")

        #set main menu choices
        menuChoices = [0,1,2,3,4,5,6,7,8,9]

        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[0-9]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        #check if the input is a number or a string of letters
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("1 - Search for Card Price")
                print("2 - Search for Sealed Product Price")
                print("3 - Set Prices")
                print("4 - Buy List Menu")
                print("5 - Wishlist Menu")
                print("6 - Personal Singles Collection Menu")
                print("7 - Personal Sealed Collection Menu")
                print("8 - Vendor Collection Menu")
                print("9 - Quick Percentage Calculation")
                print("0 - Quit Program")
                menuString = input("\nPlease input your selection[0-9]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        #checks if the number inputed is available in the menu selection choices
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                #Search Single Card Price Menu
                if menuSelect == 1:
                    searchCardPrice_menu = True
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Search Sealed Price Menu
                if menuSelect == 2:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = True
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                    #Search Full Set Price Menu
                if menuSelect == 3:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = True
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Buy List Menu
                if menuSelect == 4:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = True
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Wishlist Menu
                if menuSelect == 5:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = True
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Personal Singles Collection Menu
                if menuSelect == 6:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = True
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Personal Sealed Collection Menu
                if menuSelect == 7:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = True
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Vendor Collection Menu
                if menuSelect == 8:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = True
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Quick Percentage Calculator Menu
                if menuSelect == 9:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = True
                    programActive = True
                    mainMenu = False
                    break
                #Quit Selected
                if menuSelect == 0:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalSinglesCollection_menu = False
                    personalSealedCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = False
                    mainMenu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Search for Card Price")
                print("2 - Search for Sealed Product Price")
                print("3 - Set Prices")
                print("4 - Buy List Menu")
                print("5 - Wishlist Menu")
                print("6 - Personal Singles Collection Menu")
                print("7 - Personal Sealed Collection Menu")
                print("7 - Vendor Collection Menu")
                print("8 - Quick Percentage Calculation")
                print("9 - Quit Program")
                menuString = input("\nPlease input your selection[0-9]:  ")
                menuSelect = menuString.isnumeric()
    
    #Search for Card Price Menu
    while searchCardPrice_menu == True:#Card Search Menu Interactions, Menu Selections
        searchingForCard = True
        while searchingForCard == True:
            searchQueryString = input("\nWhat card do you want to search for?  ")
            cardName,currentFullCardSearchDictionary = newCardSearch(searchQueryString)
            cardName,currentCardSearchDictionary = newCardSearchFilter(cardName,currentFullCardSearchDictionary)
            print("\n",cardName)
            print("\n",currentCardSearchDictionary)
            cardSearchSaveToWishlist = True
            searchingForCard = False

        #ask to save to wishlist json file
        while cardSearchSaveToWishlist == True:
            saveSearchCardToWishlist = input("\nWould you like to save this card to your Wishlist[Y/N]?")
            if saveSearchCardToWishlist in ("n","N","y","Y"):
                if saveSearchCardToWishlist in ("n","N"):
                    cardSearchSaveToPersonalCollection = True
                    cardSearchSaveToWishlist = False
                if saveSearchCardToWishlist in ("y","Y"):
                    cardName = addToWishlist(cardName,currentCardSearchDictionary)
                    print("\n",cardName,"was added to Wishlist!")
                    cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                    if cardSearchAgain in ("n","N","y","Y"):
                        if cardSearchAgain in ("n","N"):
                            cardSearchSaveToPersonalCollection = True
                            cardSearchSaveToWishlist = False
                            break
                        if cardSearchAgain in ("y","Y"):
                            searchingForCard = True
                            cardSearchSaveToWishlist = False#go back to beginning of menu search loop
                            break
                break
    
        #ask to save to personal collection file
        while cardSearchSaveToPersonalCollection == True:
            saveSearchCardToPersonalCollection = input("Would you like to save this card to your Personal Collection[Y/N]?")
            if saveSearchCardToPersonalCollection in ("n","N","y","Y"):
                if saveSearchCardToPersonalCollection in ("n","N"):
                    cardSearchSaveToVendorCollection = True
                    cardSearchSaveToPersonalCollection = False
                if saveSearchCardToPersonalCollection in ("y","Y"):
                    cardName = addToPersonalCollection(cardName,currentCardSearchDictionary)
                    print("\n",cardName,"was added to Personal Collection!")
                    cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                    if cardSearchAgain in ("n","N","y","Y"):
                        if cardSearchAgain in ("n","N"):
                            cardSearchSaveToVendorCollection = True
                            cardSearchSaveToPersonalCollection = False
                            break
                        if cardSearchAgain in ("y","Y"):
                            searchingForCard = True
                            cardSearchSaveToPersonalCollection = False#go back to beginning of menu search loop
                            break
                break

        #ask to save to vendor collection json file
        while cardSearchSaveToVendorCollection == True:
            saveSearchCardToVendorCollection = input("Would you like to save this card to your Vendor Collection[Y/N]?")
            if saveSearchCardToVendorCollection in ("n","N","y","Y"):
                if saveSearchCardToVendorCollection in ("n","N"):
                    print("\nReturning to Main Menu")
                    mainMenu = True
                    searchCardPrice_menu = False
                if saveSearchCardToVendorCollection in ("y","Y"):
                    cardName = addToVendorCollection(cardName,currentCardSearchDictionary)
                    print("\n",cardName,"was added to Vendor Collection!")
                    cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                    if cardSearchAgain in ("n","N","y","Y"):
                        if cardSearchAgain in ("n","N"):
                            print("\nReturning to Main Menu")
                            mainMenu = True
                            searchCardPrice_menu = False
                            break
                        if cardSearchAgain in ("y","Y"):
                            searchingForCard = True
                            cardSearchSaveToVendorCollection = False#go back to beginning of menu search loop
                            break
                break
        continue

    #Search for Sealed Card Menu
    #while personalSealedCollection_menu == True:

    #Search and View Full Set Prices Menu
    while setPrices_menu == True:
        menuSelect = 0
        if menuSelect == 0:
            print("\nSet Prices Menu")
            print()
            print("1 - Get New Set Prices")
            print("2 - Check Newest Saved Prices")
            print("3 - Check Oldest Saved Prices")
            print("4 - Check Price Changes")
            print("5 - Main Menu")
            print("6 - Quit Program")
            menuChoices = [1,2,3,4,5,6]
            menuString = input("\nPlease input your selection[1-9]:  ")
            menuStringIsNum = menuString.isnumeric()
            menuStringCheck = True
            #check if the input is a number or a string of letters
            while menuStringCheck == True:
                if menuStringIsNum == False:
                    #ask for menu selection again
                    print("\nMust be a number, that is not a valid selection, please try again")
                    print()
                    print("\nSet Prices Menu")
                    print("1 - Get New Set Prices")
                    print("2 - Check Newest Saved Prices")
                    print("3 - Check Oldest Saved Prices")
                    print("4 - Check Price Changes")
                    print("5 - Main Menu")
                    print("6 - Quit Program")
                    menuChoices = [1,2,3,4,5,6]
                    menuString = input("\nPlease input your selection[1-9]:  ")
                    menuStringIsNum = menuString.isnumeric()
                    continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
                else:
                    menuSelect = int(menuString)
                    menuSelect_numValidCheck = True
                    menuStringCheck = False
            while menuSelect_numValidCheck == True:
                if menuSelect in menuChoices:#if the inputed number is in the valid number choices list then run code that cooresponds with the number
                    if menuSelect == 0:
                        print("\nSet Prices Menu")
                        print()
                        print("1 - Get New Set Prices")
                        print("2 - Check Newest Saved Prices")
                        print("3 - Check Oldest Saved Prices")
                        print("4 - Check Price Changes")
                        print("5 - Main Menu")
                        print("6 - Quit Program")
                        menuChoices = [1,2,3,4,5,6]
                        menuSelect = int(input("\nPlease input your selection[1-4]:  "))
                        break
                    if menuSelect == 1:
                        print("\nGetting New Set Prices...")

                        #connect to api and get response
                        conn = http.client.HTTPSConnection("cardmarket-api-tcg.p.rapidapi.com")
                        conn.request("GET","https://pokemon-tcg-api.p.rapidapi.com/episodes?rapidapi-key=9253f78de8msh854c4d0e982097ep1c10f8jsn8fa2fb1ae50d")
                        response = conn.getresponse()
                        newFullSetData = response.read().decode()
                        conn.close()

                        #write the fullSetsData to json
                        with open("/workspaces/data_3500_homework/final_project/newFullSetData.json", "w", encoding = "utf-8") as file:
                            newFullSetData = json.loads(newFullSetData)
                            json.dump(newFullSetData, file, ensure_ascii = False, indent = 4)
                        
                        #open file again and save the names of the sets and prices into new dictionary and then creates a new json file for the data
                        with open("/workspaces/data_3500_homework/final_project/newFullSetData.json", "r") as file:
                            print("\nOpening new full set data file....")
                            fullSetDictionaryData = json.load(file)
                            #fullSetDictionaryData = json.loads(fullSetDictionaryDataStrings)
                            #print(fullSetDataJSON)
                            # Extract the list of objects inside the "data" key
                            fullSetDictionaryData = fullSetDictionaryData.get("data", [])
                            # Iterate through each item in the json list pulling our keys and adding to new dictionary
                            for item in fullSetDictionaryData:
                                #get names of the card sets
                                fullSetDataNameKey = item.get("name", "")
                                #get prices of the card sets and convert to USD from EUR
                                fullSetDataPriceKey = round(item.get("prices", "").get("cardmarket").get("total") * 1.15,2) #to get USD price we multiply price by our exchange rate
                                setDataDictionaryPriceKey = round(item.get("prices", "").get("cardmarket").get("total") * 1.15,2) #to get USD price we multiply price by our exchange rate
                                #append set prices without dollar sign to list
                                #format the price key to append a $ to the front of the key
                                fullSetDataPriceKey = f"${fullSetDataPriceKey}"
                                #write the lists into the full set prices dictionary
                                fullSetDataDictionary = [fullSetDataNameKey, fullSetDataPriceKey]
                                fullSetDataDictionaryNoDollarSign = [fullSetDataNameKey, setDataDictionaryPriceKey]
                                setDataDictionary.update([fullSetDataDictionaryNoDollarSign])
                                fullSetDictionary.update([fullSetDataDictionary])
                                #at the end we write the specific data into the newSetData json file
                                setDataFileWrite = True

                            #We write the new dictionary we created from the response json file into new json files for new and current prices
                            while setDataFileWrite == True:
                                print("\nWriting new set data to files....")
                                #we write new set data into new set data file and current set data file
                                with open("/workspaces/data_3500_homework/final_project/newSetData.json", "w", encoding = "utf-8") as file:
                                    json.dump(setDataDictionary, file, ensure_ascii = False, indent = 4)
                                    print("\nSaved New Set Prices to newSetData.json!")
                                with open("/workspaces/data_3500_homework/final_project/currentSetData.json", "w", encoding = "utf-8") as file:
                                    json.dump(fullSetDictionary, file, ensure_ascii = False, indent = 4)
                                    print("\nSaved New Set Prices to currentSetData.json!")
                                with open("/workspaces/data_3500_homework/final_project/currentSetData.json", "r", encoding = "utf-8") as file:
                                    currentSetPrices = json.load(file)
                                    print("\nCurrent Prices:  ", json.dumps(currentSetPrices, indent=4))#print all the set prices and their. names
                                setDataFileChecks = True#start new while loop after this one ends
                                #Now we check to see these files exist and to create them if they don't
                                while setDataFileChecks == True:
                                    print("\nChecking if set files exist....")
                                    #We set our file paths into variables so we can check them
                                    oldSetDataPath = Path("/workspaces/data_3500_homework/final_project/oldSetData.json")
                                    newSetDataPath = Path("/workspaces/data_3500_homework/final_project/newSetData.json")
                                    adjustSetDataPath = Path("/workspaces/data_3500_homework/final_project/adjustSetData.json")
                                    currentFullSetDataPath = Path("/workspaces/data_3500_homework/final_project/currentSetData.json")

                                    #we check to see if there is a old set data file, if there isn't we create it
                                    if oldSetDataPath.is_file():
                                        overwriteOldPrices = input("\nWould you like to overwrite old prices[Y/N]?:  ")
                                        if overwriteOldPrices in ("n","N","y","Y"):
                                            if overwriteOldPrices in ("n","N"):
                                                print("\n Returning to Set Prices Menu")
                                                menuSelect = 0
                                                menuSelect_numValidCheck = False
                                                setDataFileWrite = False
                                                setDataFileChecks = False
                                                break
                                            if overwriteOldPrices in ("y","Y"):
                                                with open("/workspaces/data_3500_homework/final_project/oldSetData.json", "w", encoding="utf-8") as file:
                                                    json.dump(setDataDictionary, file, ensure_ascii = False, indent = 4)
                                                    print("\nOld Prices have been rewritten")
                                                    menuSelect = 0
                                                    menuSelect_numValidCheck = False
                                                    setDataFileWrite = False
                                                    setDataFileChecks = False
                                        else:
                                            print("\nThat is not a valid selection, please try again")
                                            overwriteOldPrices = input("\nWould you like to overwrite old prices[Y/N]?:  ")
                                            continue
                                    else:
                                        with open("/workspaces/data_3500_homework/final_project/oldSetData.json", "w", encoding="utf-8") as file:
                                            json.dump(setDataDictionary, file, ensure_ascii = False, indent = 4)
                                            print("\nCreated oldSetData.json File")
                                            menuSelect = 0
                                            setDataFileWrite = False
                                            setDataFileChecks = False
                                        continue
                                    #we check to see if there is a current set data json file, if there isn't we create it
                                    if currentFullSetDataPath.is_file():
                                        with open("/workspaces/data_3500_homework/final_project/currentSetData.json", "r", encoding = "utf-8") as file:
                                            currentSetPrices = json.load(file)
                                            print("\nCurrent Prices:  ", json.dumps(currentSetPrices, indent=4))#print all the set prices and their. names
                                    else:
                                        with open("/workspaces/data_3500_homework/final_project/currentSetData.json", "w", encoding = "utf-8") as file:
                                            json.dump(fullSetDataDictionary, file, ensure_ascii = False, indent = 4)
                                            print("\ncreated new current set data JSON file")
                                    menuSelect = 0
                                    setDataFileWrite = False
                                    setDataFileChecks = False #ends the loop returns to main set menu
                        break
                    #opening newest saved set data prices
                    if menuSelect == 2:
                        with open("/workspaces/data_3500_homework/final_project/newSetData.json") as file:
                            newestSavedSetPrices = json.load(file)
                            print("\nNewest Saved Prices:  ","\n",json.dumps(newestSavedSetPrices,indent = 4))
                        menuSelect = 0
                        break
                    #opening oldest saved set data prices
                    if menuSelect == 3:
                        with open("/workspaces/data_3500_homework/final_project/oldSetData.json") as file:
                            oldestSavedSetPrices = json.load(file)
                            print("\nOldest Saved Prices:  ","\n",json.dumps(oldestSavedSetPrices,indent = 4))
                        menuSelect = 0
                        break
                    #check price changes
                    if menuSelect ==4:
                        print("\nChecking price changes....")
                        with open("/workspaces/data_3500_homework/final_project/newSetData.json") as file:
                            newDataSetPriceChange = json.load(file)
                        with open("/workspaces/data_3500_homework/final_project/oldSetData.json", "r") as file:
                            oldDataSetPriceChange = json.load(file)
                        if newDataSetPriceChange == oldDataSetPriceChange:
                            print("\nPrice have not changed!")
                            menuSelect = 0
                            break
                        else:
                            print("\nPrices have changed!")
                            #creates a new dictionary for the price change and calculates the difference of the two keys in the two json files and appends it
                            priceChange = {
                            key: {"New Set Price Data": newDataSetPriceChange[key], "Old Set Price Data": oldDataSetPriceChange[key],"Difference": newDataSetPriceChange[key] - oldDataSetPriceChange[key]}
                                for key in oldDataSetPriceChange
                                    if oldDataSetPriceChange[key] != newDataSetPriceChange[key]
                            }
                            print("\nPrice Changes:","\n", json.dumps(priceChange, indent = 4))
                            menuSelect = 0
                        break
                    if menuSelect == 5:
                        mainMenu = True# set the menu to main menu
                        setPrices_menu = False #ends set prices menu loop and goes to main menu
                        menuSelect = -1
                        break
                    if menuSelect == 6:
                        programActive = False #closes the program
                        mainMenu = True
                        setPrices_menu = False
                        break
                else:
                    #variables print checks
                    print("\nThat is not a valid selection, please try again")
                    print()
                    print("1 - Get New Set Prices")
                    print("2 - Check Newest Saved Prices")
                    print("3 - Check Oldest Saved Prices")
                    print("4 - Check Price Changes")
                    print("5 - Main Menu")
                    print("6 - Quit Program")
                    menuChoices = [1,2,3,4,5,6]
                    menuString = input("\nPlease input your selection[1-9]:  ")
                    menuStringIsNum = menuString.isnumeric()

    #Buy List Menu
    #while buyList_menu == True:

    #Wishlist Menu
    while wishlist_menu == True:
        #print options and which menu you are in
        print("\nWishlist Menu")
        print()
        print("1 - Show Wishlist")
        print("2 - Add Card to Wishlist")
        print("3 - Remove Card from Wishlist")
        print("4 - Delete Wishlist")
        print("5 - Total Price of Wishlist")
        print("6 - Main Menu")
        print("0 - Quit Program")

        #set main menu choices
        menuChoices = [0,1,2,3,4,5,6]

        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[1-7]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        #check if the input is a number or a string of letters
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("1 - Show Wishlist")
                print("2 - Add Card to Wishlist")
                print("3 - Remove Card from Wishlist")
                print("4 - Delete Wishlist")
                print("5 - Total Price of Wishlist")
                print("6 - Main Menu")
                print("0 - Quit Program")

                #set main menu choices
                menuChoices = [0,1,2,3,4,5,6]

                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[1-7]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        #checks if the number inputed is available in the menu selection choices
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                #Search Single Card Price Menu
                if menuSelect == 1:
                    showWishlist = printWishList()
                    break
                if menuSelect == 2:
                    searchingForCard = True
                    while searchingForCard == True:
                        searchQueryString = input("\nWhat card do you want to search for?  ")
                        cardName,currentFullCardSearchDictionary = newCardSearch(searchQueryString)
                        cardName,currentCardSearchDictionary = newCardSearchFilter(cardName,currentFullCardSearchDictionary)
                        print("\n",cardName)
                        print("\n",currentCardSearchDictionary)
                        cardSearchSaveToWishlist = True
                        searchingForCard = False
                    while cardSearchSaveToWishlist == True:
                        saveSearchCardToWishlist = input("\nWould you like to save this card to your Wishlist[Y/N]?")
                        if saveSearchCardToWishlist in ("n","N","y","Y"):
                            if saveSearchCardToWishlist in ("n","N"):
                                cardSearchSaveToWishlist = False
                            if saveSearchCardToWishlist in ("y","Y"):
                                cardName = addToWishlist(cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to Wishlist!")
                            cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                            if cardSearchAgain in ("n","N","y","Y"):
                                if cardSearchAgain in ("n","N"):
                                    menuSelect_numValidCheck = False
                                    searchingForCard = False
                                    cardSearchSaveToWishlist = False
                                    break
                                if cardSearchAgain in ("y","Y"):
                                    searchingForCard = True
                                    cardSearchSaveToWishlist = False#go back to beginning of menu search loop
                                    break
                            break
                if menuSelect == 3:
                    removeCardFromWishlist = removeFromWishlist()
                    break
                if menuSelect == 4:
                    deleteWishList = deleteWishlist()
                    break
                if menuSelect == 5:
                    wishlistPrice = calculateWishListTotalPrice()
                    break
                if menuSelect == 6:
                    mainMenu = True
                    wishlist_menu = False
                    break
                if menuSelect == 0:
                    programActive = False
                    wishlist_menu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Show Wishlist")
                print("2 - Add Card to Wishlist")
                print("3 - Remove Card from Wishlist")
                print("4 - Delete Wishlist")
                print("5 - Total Price of Wishlist")
                print("6 - Main Menu")
                print("0 - Quit Program")
                menuString = input("\nPlease input your selection[0-7]:  ")
                menuSelect = menuString.isnumeric()
    
    #Personal Singles Collection Menu
    while personalSinglesCollection_menu == True:
        print()
        print("Personal Singles Collection Menu")
        print()
        print("1 - Show Personal Singles Collection")
        print("2 - Add Card to Personal Singles Collection")
        print("3 - Remove Card from Personal Singles Collection")
        print("4 - Delete Personal Singles Collection")
        print("5 - Total Price of Personal Singles Collection")
        print("6 - Main Menu")
        print("0 - Quit Program")
        #set main menu choices
        menuChoices = [0,1,2,3,4,5,6]
        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[0-6]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        #check if the input is a number or a string of letters
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("1 - Show Wishlist")
                print("2 - Add Card to Wishlist")
                print("3 - Remove Card from Wishlist")
                print("4 - Delete Wishlist")
                print("5 - Total Price of Wishlist")
                print("6 - Main Menu")
                print("0 - Quit Program")

                #set main menu choices
                menuChoices = [0,1,2,3,4,5,6]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-6]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        #checks if the number inputed is available in the menu selection choices
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                #Search Single Card Price Menu
                if menuSelect == 1:
                    showWishlist = printPersonalSinglesCollection()
                    break
                if menuSelect == 2:
                    searchingForCard = True
                    while searchingForCard == True:
                        searchQueryString = input("\nWhat card do you want to search for?  ")
                        cardName,currentFullCardSearchDictionary = newCardSearch(searchQueryString)
                        cardName,currentCardSearchDictionary = newCardSearchFilter(cardName,currentFullCardSearchDictionary)
                        print("\n",cardName)
                        print("\n",currentCardSearchDictionary)
                        cardSearchSaveToPSiC = True
                        searchingForCard = False
                    while cardSearchSaveToPSiC == True:
                        saveSearchCardToPSiC = input("\nWould you like to save this card to your Personal Singles Collection[Y/N]?")
                        if saveSearchCardToPSiC in ("n","N","y","Y"):
                            if saveSearchCardToPSiC in ("n","N"):
                                cardSearchSaveToPSiC = False
                            if saveSearchCardToPSiC in ("y","Y"):
                                cardName = addToPersonalSinglesCollection(cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to Personal Singles Collection!")
                            cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                            if cardSearchAgain in ("n","N","y","Y"):
                                if cardSearchAgain in ("n","N"):
                                    menuSelect_numValidCheck = False
                                    searchingForCard = False
                                    cardSearchSaveToPSiC = False
                                    break
                                if cardSearchAgain in ("y","Y"):
                                    searchingForCard = True
                                    cardSearchSaveToPSiC = False#go back to beginning of menu search loop
                                    break
                            break
                if menuSelect == 3:
                    removeCardFromWishlist = removeFromPersonalSinglesCollection()
                    break
                if menuSelect == 4:
                    deleteWishList = deletePersonalSinglesCollection()
                    break
                if menuSelect == 5:
                    wishlistPrice = calculatePersonalSinglesCollectionTotalPrice()
                    break
                if menuSelect == 6:
                    mainMenu = True
                    personalSinglesCollection_menu = False
                    break
                if menuSelect == 0:
                    programActive = False
                    personalSinglesCollection_menu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Show Personal Singles Collection")
                print("2 - Add Card to Personal Singles Collection")
                print("3 - Remove Card from Personal Singles Collection")
                print("4 - Delete Personal Singles Collection")
                print("5 - Total Price of Personal Singles Collection")
                print("6 - Main Menu")
                print("0 - Quit Program")
                menuString = input("\nPlease input your selection[0-7]:  ")
                menuSelect = menuString.isnumeric()

    #Personal Sealed Collection Menu
    #while personalSealedCollection_menu == True:

    #Vendor Collection Menu
    #while vendorCollection_menu == True:
    
    #Quick Percentage Calculator menu
    while quickPercentageCalculate_menu == True:
        percentageCalculator()
        mainMenu = True
        quickPercentageCalculate_menu = False

else:#if the user has chosen to quit the program
    print("\nThank you for using Luis' Pokemon Management Program!!!")
    print()

