#FINAL PROJECT - Pokemon Card Pricing and Collection Application - Luis Cotton

#finish card search menu
#finish search for sealed price menu
#finish buy list menu
#finish wishlist menu
#finish personal collection menu
#finish vendor collection menu
#finish quick percentage calculator menu

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
menuSelect = 0
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

#Wishlist Functions
def printWishList():
    print("print available wishlist dictionaries that can be printed and ask the user which one to print ")
    print("print entire wishlist","print wishlist price total")
    #print the wishlist dictionary from json file
def wishlistCardSearch():
    print("search for a card for your personal collection")
    print("if user wants to add card to wishlist ask which wishlist dictionary entry they would like to add it to")#return the chosen wishlist ID for the next function
    print("available wishlists to add card to")
    print("add:  ","charmander","to your collection? Y/N")#if no then search for a new card or go to main menu and saving the json file
def addToWishlist():
    print("card added to wishlist")
    #add card to json wishlist file
def removeFromWishlist():
    print("card removed from wishlist")
    #remove card from wishlist
def calculateWishListTotalPrice():
    print("return and update wishlist total price to dictionary file variable")
def saveNewWishlist():
    print("save wishlist+1 as a new dictionary in the wishlist json file")
    #ask for name for wishlist and save into ONE json file for all wishlists
def deleteWishlist():
    print("delete wishlist dictionary item list")
    print("ask again if they want it deleted")
    print("deleted wishlist#3 from json file")
    #delete and ask for permission to delete dictionary from wishlist json file

#Personal Collection Functions
def printPersonalCollection():
    print("print available personal collection dictionaries that can be printed and ask the user which one to print ")
    print("entire personal collection list","\nPersonal Collection Price")
    #read and print full personal collection from json file
def personalCollectionCardSearch():
    print("search for a card for your personal collection")
    print("ask user which personal collection dictionary entries to add the card to")#return the chosen personal collection ID for the next function
    print("add:  ","charmander","to your collection? Y/N")#if no then search for a new card or go to main menu and saving the json file
def addToPersonalCollection():
    print("added to collection")
    #add card to json personal collection json file
def removeFromPersonalCollection():
    print("removed from collection")
    #remove card from json personal collection json file
def calculatePersonalCollectionTotalPrice():
    print("calculate total price of personal collection in realtime prices and print the total price added")
    #calculate total price of all items in personal collection from json file
def calculatePersonalCollectionTotalProfit():
    print("calculate the profit of the total price of all the cards when they where first added and the difference between realtime updated pricing with a percent")
    print("Total Collection Percentage Increase")
    print("Total Collection Price")
    #calculate the percent and total cash profit of entire collection from the price they where first added to the new updated price
def calculatePersonalCollectionSingleTotalProfit():
    print("calculate the profit of the cards price when first added and the difference of the realtime updated price")
    #calculate the percent and total cash profit of a single card in your personal collection from the price they where first added to the new updated price
def saveNewPersonalCollection():
    print("create and save a new personal collection dictionary into the personal collection dictionary json file")
    #save new dictionary into personal collection dictionary with a new name for the dictionary called by a number
def deletePersonalCollection():
    print("delete specific saved dictionary in personal collection dicitonary ")
    print("ask if the user is sure they want to delete the dictionary")
    #delete personal collection dictionary in personal collection dictionary json file

#Vendor Collection Functions
def printVendorCollection():
    print("print available vendor collection dictionaries that can be printed and ask the user which one to print ")
    print("total vendor collection dictionary list")
    #read and print total vendor collection list from json file
def vendorCollectionCardSearch():
    print("Search and add or just view card price from Vendor Collection Menu")
    print("ask user which vendor collection dictionarie entries to add the card to")#return the chosen vendor collection ID for the next function
    print("add:  ","charmander","to your vendor collection? Y/N")#if no then search for a new card or go to main menu and saving the json file
def addToVendorCollection():
    print("flying pikachu","added to vendor collection")
    #add card to json vendor collection json file
def removeFromVendorCollection():
    print("flying pikachu","removed from vendor collection")
    #remove card from json vendor collection json file
def calculateVendorCollectionTotalProfit():
    print("total vendor collection profit from first price to price today")
    #calculcate total percentage and total profit price of vendor collection json file
def calculateVendorCollectionSingleTotalProfit():
    print("total profit and total percentage of profit of a single card in vendor collection")
    #calculate total percentage and total profit price of a single card from vendor collection json file
def saveNewVendorCollection():
    print("save new vendor collection dictionary to the vendor collection dictionary json file")
    #append new vendor collection dictionary to the vendor collection dictionary json file
def deleteVendorCollection():
    print("delete specific saved vendor collection dictionary entry in vendor collection dicitonary ")
    print("ask if the user is sure they want to delete the dictionary")
    #delete vendor dictionary in vendor collection dictionary json file


#Buy List Functions
def printBuyList():
    print("print available buy list dictionaries that can be printed and ask the user which one to print ")
    print("total buy list dictionary list of buy list id")
    #read and print total vendor collection list from json file
def buyListCardSearch():
    print("Search for a card for Buy List")
    print("ask user which buylist dictionary entries to add the card to")#return the chosen buylist ID for the next function
    print("add:  ","charmander","to your buy list? Y/N")#if no then search for a new card or go to main menu and saving the json file
def addToBuyList():
    print("added:  ","surfing pikachu","to Buy List","\nadd another card? Y/N")
    #add card to buy list and ask if they want to add another or calculate price and percentage
def removeFromBuyList():
    print("removed:  ","surfing pikachu","from Buy List","\nadd another card? Y/N")
def calculateBuyListTotalPrice():
    print("calculated buy list total of all added card prices in dictionary")
    #calculate and add the total price of all cards in list and ask if they want a percentage
def calculateBuyListPercentage():
    print("the percentage total for the total price of buy list is:  ")
    #calculate the price of the total price multiplied by percentage of the buy list
def saveNewBuyList():
    print("buy list saved to json file")
    #save buy list to json file
def deleteBuyList():
    print("delete buy list dictionary from buy list dictionary json file")
def clearBuyList():
    print("buy list is cleared")
    #delete all information in dynamic buy list so it's ready for a new list that is not saved to json file

#Quick Percentage Calculator
def percentageCalculator (): #need variables, card price and what percentage to calculate
    print("original card price:  ","0","\n ")

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
        print("\nWelcome to Luis Cotton's Pokemon Card Management Program")
        print("\nMain Menu")
        print("\n1 - Search for Card Price")
        print("\n2 - Search for Sealed Product Price")
        print("\n3 - Set Prices")
        print("\n4 - Buy List Menu")
        print("\n5 - Wishlist Menu")
        print("\n6 - Personal Collection Menu")
        print("\n7 - Vendor Collection Menu")
        print("\n8 - Quick Percentage Calculation")
        print("\n9 - Quit Program")

        #set main menu choices
        menuChoices = [1,2,3,4,5,6,7,8,9]

        #ask what menu option the user wants to select
        menuSelect = int(input("\nPlease input your selection[1-9]:  "))
        menuSelect_numValidCheck = True

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
                    personalCollection_menu = False
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
                    personalCollection_menu = False
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
                    personalCollection_menu = False
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
                    personalCollection_menu = False
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
                    personalCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Personal Collection Menu
                if menuSelect == 6:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalCollection_menu = True
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Vendor Collection Menu
                if menuSelect == 7:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalCollection_menu = False
                    vendorCollection_menu = True
                    quickPercentageCalculate_menu = False
                    programActive = True
                    mainMenu = False
                    break
                #Quick Percentage Calculator Menu
                if menuSelect == 8:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = True
                    programActive = True
                    mainMenu = False
                    break
                #Quit Selected
                if menuSelect == 9:
                    searchCardPrice_menu = False
                    searchSealedPrice_menu = False
                    setPrices_menu = False
                    buyList_menu = False
                    wishlist_menu = False
                    personalCollection_menu = False
                    vendorCollection_menu = False
                    quickPercentageCalculate_menu = False
                    programActive = False
                    mainMenu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print("\n1 - Search for Card Price")
                print("\n2 - Search for Sealed Product Price")
                print("\n3 - Set Prices")
                print("\n4 - Buy List Menu")
                print("\n5 - Wishlist Menu")
                print("\n6 - Personal Collection Menu")
                print("\n7 - Vendor Collection Menu")
                print("\n8 - Quick Percentage Calculation")
                print("\n9 - Quit Program")
                menuSelect = int(input("\nPlease input your selection[1-9]:  "))
    
    #If you are searching for a specific card price
    while searchCardPrice_menu == True:#Card Search Menu Interactions, Menu Selections
        url = "/cards?search="
        url2 = "&rapidapi-key=9253f78de8msh854c4d0e982097ep1c10f8jsn8fa2fb1ae50d"
        searchQueryString = input("What card are you lookign for?  ")
        searchQuery = searchQueryString.replace(" ", "+")
        fullUrl = str(url + searchQuery + url2)
        print(fullUrl)
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
            currentFullCardSearchDictionary = json.load(file)
            currentFullCardSearchDictionary = currentFullCardSearchDictionary.get("data", [])
        #We get the name of the card in the first dictionary position then we end this loop
        for item in currentFullCardSearchDictionary:
                cardName = item.get("name", "")
                break
        # Iterate through each item in the json list pulling our keys and adding to new dictionary
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
                currentFilteredCardSearchDictionary = [cardNameKey, cardSetKey, cardSetAcronym, cardNumberKey, cardRarityKey, currentRawPrice, current30DayPriceAve,current7DayPriceAve,cardPSA10Price]
                currentCardSearchDictionary = currentFilteredCardSearchDictionary
                cardSearchSaveToWishlist = True
                if cardSearchSaveToWishlist == True:
                    saveSearchCardToWishlist = input("Would you like to save this card to your Wishlist[Y/N]?")
                    if saveSearchCardToWishlist in ("n","N","y","Y"):
                        if saveSearchCardToWishlist in ("n","N"):
                            cardSearchSaveToPersonalCollection = True
                            cardSearchSaveToWishlist = False
                        if saveSearchCardToWishlist in ("y","Y"):
                            #code for appending to wishlist json file here
                            print("saved to wishlist")
                            #searchAgain = input("Search for another card[Y/N]?") #search for another card code and input check here
                            print("search another card[Y/N]?")
                if cardSearchSaveToPersonalCollection == True:
                    saveSearchCardToPersonalCollection = input("Would you like to save this card to your Personal Collection[Y/N]?")
                    if saveSearchCardToPersonalCollection in ("n","N","y","Y"):
                        if saveSearchCardToPersonalCollection in ("n","N"):
                            cardSearchSaveToVendorCollection = True
                            cardSearchSaveToPersonalCollection = False
                        if saveSearchCardToPersonalCollection in ("y","Y"):
                            #code for appending to personal collection json file here
                            print("saved to personal collection")
                            print("search another card[Y/N]?")
                if cardSearchSaveToVendorCollection == True:
                    saveSearchCardToVendorCollection = input("Would you like to save this card to your Vendor Collection[Y/N]?")
                    if saveSearchCardToVendorCollection in ("n","N","y","Y"):
                        if saveSearchCardToVendorCollection in ("n","N")
                            cardSearchSaveToVendorCollection = False
                        if saveSearchCardToVendorCollection in ("y","Y")
                            #code for appending to vendor collection json file here
                            print("saved to vendor collection")
                            print("search another card[Y/N]?")
                            break
                break
            mainMenu = True
            searchCardPrice_menu = False
            break
            #write the lists into the full set prices dictionary
            print(currentCardSearchDictionary)
        
        #currentCardSearchDictionary.update(json.load(currentCardSearch))
        #print("\nSearched for: ",searchQueryString,"Found: ",currentCardSearchDictionary)

        #print("Would you like to add this card to your Wishlist[Y/N]?")
        #print("Would you like to add this card to your Personal Collection[Y/N]?")
        mainMenu = True
        searchCardPrice_menu = False

    while setPrices_menu == True:
        menuSelect = 0
        if menuSelect == 0:
            print("\nSet Prices Menu")
            print("\n1 - Get New Set Prices")
            print("\n2 - Check Newest Saved Prices")
            print("\n3 - Check Oldest Saved Prices")
            print("\n4 - Check Price Changes")
            print("\n5 - Main Menu")
            print("\n6 - Quit Program")
            menuChoices = [1,2,3,4,5,6]
            menuSelect = int(input("\nPlease input your selection[1-4]:  "))
            menuSelect_numValidCheck = True
            while menuSelect_numValidCheck == True:
                if menuSelect in menuChoices:#if the inputed number is in the valid number choices list then run code that cooresponds with the number
                    if menuSelect == 0:
                        print("\nSet Prices Menu")
                        print("\n1 - Get New Set Prices")
                        print("\n2 - Check Newest Saved Prices")
                        print("\n3 - Check Oldest Saved Prices")
                        print("\n4 - Check Price Changes")
                        print("\n5 - Main Menu")
                        print("\n6 - Quit Program")
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
                    print("\n1 - Get New Set Prices")
                    print("\n2 - Check Newest Saved Prices")
                    print("\n3 - Check Oldest Saved Prices")
                    print("\n4 - Check Price Changes")
                    print("\n5 - Main Menu")
                    print("\n6 - Quit Program")
                    menuChoices = [1,2,3,4,5,6]
                    menuSelect = int(input("\nPlease input your selection[1-4]:  "))
else:#if the user has chose to quit the program
    print("\nThank you for using Luis' Pokemon Management Program!!!")

