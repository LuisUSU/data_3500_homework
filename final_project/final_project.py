#FINAL PROJECT - Pokemon Card Pricing and Collection Application - Luis Cotton

#finish copying over code to functions and renaming variables

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
searchCardSingle_menu = False
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
    with open("/workspaces/data_3500_homework/final_project/new_card_search.json", "w", encoding = "utf-8") as file:
        newCardSearchQuery = json.loads(newCardSearchQuery)
        json.dump(newCardSearchQuery, file, ensure_ascii = False, indent = 4)
        print("\nSaved Card Search to newCardSearchQuery.json!")

    # Extract the list of objects inside the "data" key
    with open("/workspaces/data_3500_homework/final_project/new_card_search.json", "r") as file:
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
            cardRawPrice = item.get("prices").get("cardmarket").get("lowest_near_mint","")
            card30DayPriceAve = item.get("prices").get("cardmarket").get("30d_average","")
            card7DayPriceAve = item.get("prices").get("cardmarket").get("7d_average","")
            cardPSA10Price = item.get("prices",{}).get("ebay",{}).get("graded",{}).get("psa",{}).get("10",{}).get("median_price",{})
            currentFilteredCardSearchDictionary = {"name": cardNameKey, "set_name": cardSetKey,"code": cardSetAcronym,"card_number": cardNumberKey,"rarity": cardRarityKey,"lowest_near_mint_price": cardRawPrice,"30_Day_Price_Average": card30DayPriceAve,"7_Day Price_Average": card7DayPriceAve,"PSA_10_Card_Price": cardPSA10Price}
        return cardNameKey,currentFilteredCardSearchDictionary

#sealed search menu functions

def newSealedSearch(searchQuery):

    url = "/products?search="
    url2 = "&rapidapi-key=9253f78de8msh854c4d0e982097ep1c10f8jsn8fa2fb1ae50d"
    searchQueryString = searchQuery
    searchQuery = searchQueryString.replace(" ", "+")
    fullUrl = str(url + searchQuery + url2)
    #print(fullUrl)
    conn = http.client.HTTPSConnection("pokemon-tcg-api.p.rapidapi.com")
    conn.request("GET", fullUrl)
    response = conn.getresponse()
    newSealedSearchQuery = response.read().decode()
    conn.close()

    #write sealed search to json file
    with open("/workspaces/data_3500_homework/final_project/new_sealed_search.json", "w", encoding = "utf-8") as file:
        newSealedSearchQuery = json.loads(newSealedSearchQuery)
        json.dump(newSealedSearchQuery, file, ensure_ascii = False, indent = 4)
        print("\nSaved Sealed Search to new_sealed_search.json!")

    #open new sealed search json
    with open("/workspaces/data_3500_homework/final_project/new_sealed_search.json", "r") as file:
        print("\nOpening Current Sealed Search file....")
        currentSealedSearchJsonDictionary = json.load(file)
        currentFullSealedSearchDictionary = currentSealedSearchJsonDictionary.get("data", [])
    #getting the name of the sealed product and returning it in a variable
    for item in currentFullSealedSearchDictionary:
        sealedName = item.get("name", "")
        break
    #returning the name of product and the full search dictionary
    return (sealedName,currentFullSealedSearchDictionary)
    return

#filter sealed search keys for new dictionary
def newSealedSearchFilter(sealedName,currentFullSealedSearchDictionary):
    #print(currentFullSealedSearchDictionary)
    for item in currentFullSealedSearchDictionary:
        #get names of the card sets
        sealedNameKey = item.get("name", "")
        if sealedName == sealedNameKey:
            sealedSetKey = item.get("episode").get("name","")
            sealedSetAcronym = item.get("episode").get("code","")
            sealedRawPrice = item.get("prices", "").get("cardmarket").get("lowest","")
            sealedRawPriceUSD = round(item.get("prices", "").get("cardmarket").get("lowest","") * 1.15,2)
            print(sealedRawPriceUSD)
            sealed30DayPriceAve = item.get("prices").get("cardmarket").get("30d_average","")
            sealed7DayPriceAve = item.get("prices").get("cardmarket").get("7d_average","")
            currentFilteredSealedSearchDictionary = {"name": sealedNameKey, "set_name": sealedSetKey,"code": sealedSetAcronym,"lowest_price": sealedRawPrice,"30_Day_Price_Average": sealed30DayPriceAve,"7_Day Price_Average": sealed7DayPriceAve}
        return sealedNameKey,currentFilteredSealedSearchDictionary

#Sealed Search Menu Functions

#define personal sealed collection dictionary
def defineTargetCollection(jsonFileName):
    #looping through dictionary and retriving name of card, which is dictionary first name
    filePath = "/workspaces/data_3500_homework/final_project/"
    fileName = str(jsonFileName)
    #removing file suffic from name for dictionary key
    dictionaryFileName = fileName.removesuffix(".json")
    #removing _ for printed name and capitalizing first letters
    dictionaryFileNamePrinted = dictionaryFileName.replace("_"," ")
    dictionaryFileNamePrinted = dictionaryFileNamePrinted.title()
    fullFilePath = filePath + fileName
    return dictionaryFileName,dictionaryFileNamePrinted,fullFilePath

#add new collection to collection file
def addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary):
    #open wishilst file
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        jsonFile = json.load(file)
        jsonFile[dictionaryFileName][newDictionaryName] = {}
    with open(dictionaryFilePath, "w", encoding = "utf-8") as file:
        json.dump(jsonFile, file, ensure_ascii = False, indent = 4)
    return dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary

#add new item to collection in collection file
def addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newCollectionName,newItemName,newItemDictionary):
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        dictionary = json.load(file)
        updatedDictionary = dictionary
        addingNewItemToDictionary = True
        while addingNewItemToDictionary == True:
            dictionaryNames = dictionary.get(dictionaryFileName,[])
            for name in dictionaryNames:
                if name == newCollectionName:
                    updatedDictionary[dictionaryFileName][newCollectionName][newItemName] = newItemDictionary
                    with open(dictionaryFilePath, "w", encoding = "utf-8") as file:
                        json.dump(updatedDictionary,file,ensure_ascii = False, indent = 4)
                        addingNewItemToDictionary = False
                        break
    return

#add new item to target collection
def addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,newItemName,newItemDictionary):
    #opening the selected collection file
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        newFile = json.load(file)
        newFileNameDictionaryList = newFile.get(dictionaryFileName, [])
        dictionaryNameList = []
        for item in newFileNameDictionaryList:
            dictionaryNameList.append(item)
        print("\nSaved",dictionaryFileName,"Collections: ")
        print()
        for names in dictionaryNameList:
            print(names)
    #open wishilst file
    targetCollection = input("\nWhich Collection would you like to add to? ")
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        dictionary = json.load(file)
        updatedDictionary = dictionary
        addingNewItemToDictionary = True
        while addingNewItemToDictionary == True:
            dictionaryNames = dictionary.get(dictionaryFileName,[])
            for name in dictionaryNames:
                if name == targetCollection:
                    updatedDictionary[dictionaryFileName][targetCollection][newItemName] = newItemDictionary
                    with open(dictionaryFilePath, "w", encoding = "utf-8") as file:
                        json.dump(updatedDictionary,file,ensure_ascii = False, indent = 4)
                        addingNewItemToDictionary = False
                        break
    return targetCollection

#remove item from target collection
def removeItemFromSavedCollection(dictionaryFilePath,dictionaryFileName):
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        newFile = json.load(file)
        newFileNameDictionaryList = newFile.get(dictionaryFileName, [])
        dictionaryNameList = []
        for item in newFileNameDictionaryList:
            dictionaryNameList.append(item)
        print("\nSaved Collections in",dictionaryFileName,": ")
        print()
        for names in dictionaryNameList:
            print(names)
        print()
        targetCollection = input("Which Collection would you like to remove a card from?  ")
        startRemovingFromCollection = True
        while startRemovingFromCollection == True:
            with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
                rootDictionary = json.load(file)
                updatedDictionary = rootDictionary
                collectionNames = rootDictionary.get(dictionaryFileName,[])
                #print(collectionNames)
                for name in collectionNames:
                    if name == targetCollection:
                        cardNameList = []
                        for subdict in collectionNames.values():
                            for key, value in subdict.items():
                                cardNames = value.get("name")
                                cardNameList.append(cardNames)
                        print()
                        print("Cards in",targetCollection, dictionaryFileName,":",)
                        print()
                        for names in cardNameList:
                            print(names)
                        print()
                        targetItem = input("Which Card would you like to remove?  ")
                        for key, value in subdict.items():
                            if key == targetItem:
                                print()
                                print("Are you sure you want to delete", targetItem,"[Y/N]?",end="")
                                areYouSure = input()
                                if areYouSure in ("n","N","y","Y"):
                                    if areYouSure in ("n","N"):
                                        return
                                if areYouSure in ("y","Y"):
                                    del updatedDictionary[dictionaryFileName][targetCollection][targetItem]
                                    with open(dictionaryFilePath, "w", encoding = "utf-8") as file:
                                        json.dump(updatedDictionary,file,ensure_ascii = False, indent = 4)
                                        print()
                                        print(targetItem,"from",targetCollection,dictionaryFileName,"was deleted!")
                                        return
                                else:
                                    print("\nNot a valid Response")
                                    continue

#delete collection from collection json file
def removeCollection(dictionaryFilePath,dictionaryFileName):
    #opening the selected collection file
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        newFile = json.load(file)
        newFileNameDictionaryList = newFile.get(dictionaryFileName, [])
        dictionaryNameList = []
        for item in newFileNameDictionaryList:
            dictionaryNameList.append(item)
        print("\nSaved Collections: ")
        print()
        for names in dictionaryNameList:
            print(names)
    targetCollection = input("\nWhich Collection would you like to remove? ")
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        dictionary = json.load(file)
        updatedDictionary = dictionary
        addingNewItemToDictionary = True
        while addingNewItemToDictionary == True:
            dictionaryNames = dictionary.get(dictionaryFileName,[])
            for name in dictionaryNames:
                if name == targetCollection:
                    print("Are you sure you want to delete", targetCollection,"[Y/N]?",end="")
                    areYouSure = input()
                    if areYouSure in ("n","N","y","Y"):
                        if areYouSure in ("n","N"):
                            return
                        if areYouSure in ("y","Y"):
                            del updatedDictionary[dictionaryFileName][targetCollection]
                            with open(dictionaryFilePath, "w", encoding = "utf-8") as file:
                                json.dump(updatedDictionary,file,ensure_ascii = False, indent = 4)
                                print(targetCollection,"was deleted!")
                                addingNewItemToDictionary = False
                                break
                    else:
                        print("\nNot a valid response")
                        continue
    return targetCollection

def printCollection(dictionaryFileName,dictionaryFilePath):
    with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
        collectionFile = json.load(file)
        collectionName = dictionaryFileName.replace("_"," ")
        collectionName = collectionName.title()
        collectionNames = collectionFile.get(dictionaryFileName,[])
        findCollectionNames = True
        while findCollectionNames == True:
            print()
            print("Saved Collections in",collectionName,":")
            print()
            collectionNamesList = []
            for name in collectionNames:
                collectionNamesList.append(name)
            for name in collectionNamesList:
                print(name)
            findCollectionNames = False
        print()
        findItems = True
        collectionSelect = True
        while collectionSelect == True:
            collectionSelection = input("\nWhich collection do you want to see?  ")
            if collectionSelection in collectionNamesList:
                targetCollectionToPrint = True
                collectionSelect = False
            else:
                print("\nThat is not a valid response")
                continue
            while targetCollectionToPrint == True:
                with open(dictionaryFilePath, "r", encoding = "utf-8") as file:
                    rootDictionary = json.load(file)
                    collectionNames = rootDictionary.get(dictionaryFileName).get(collectionSelection,[])
                    collectionItemList = []
                    collectionPriceList = []
                    for name in collectionNames.values():
                        collectionItemList.append(name.get("name",[]))
                    for lowest_near_mint_price in collectionNames.values():
                        collectionPriceList.append(lowest_near_mint_price.get("lowest_near_mint_price",[]))
                    print("\nItems in",collectionSelection,collectionName,":")
                    print()
                    for names in collectionItemList:
                        print(names)
                    print()
                    print("Collection Total Price:  ","$",sum(collectionPriceList))
                    collectionItemList.clear()
                    collectionPriceList.clear()
                openJson = input("\nDo you want to see full JSON file[Y/N]?")
                openJsonFile = True
                while openJsonFile == True:
                    if openJson in ("n","N","y","Y"):
                        if openJson in ("n","N"):
                            targetCollectionToPrint = False
                            openJsonFile = False
                        if openJson in ("y","Y"):
                            print()
                            print("Full",collectionName,".JSON Data:")
                            print()
                            collectionFileData = json.dumps(collectionFile.get(dictionaryFileName,[]),indent=4)
                            print()
                            print(collectionFileData)
                            print()
                            targetCollectionToPrint = False
                            openJsonFile = False
                            break
                    else:
                        print("\nNot a valid response")
                        continue
    return


#Buy List Functions




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
    #looping through dictionary and retriving name of card, which is dictionary first name
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
                wishlistCardPrice = round(value.get("lowest_near_mint_price"),2)
                wishlistPriceList.append(wishlistCardPrice)
        totalWishlistPrice = sum(wishlistPriceList)
        print("Wishlist Total Price:", totalWishlistPrice)
    return

#Personal Singles Collection Functions

#print personal singles collection json as a list, ask which personal collection dictionaries to print
#function to go through and read which available collections 
def definePersonalSinglesCollection():
    #loop through personal_collection file and retrieve the names of the collections, print out the names, add key to variable
    #looping through dictionary and retriving name of card, which is dictionary first name
    with open("/workspaces/data_3500_homework/final_project/personal_collection.json", "r", encoding = "utf-8") as file:
        personalCollection = json.load(file)
        personalCollection = personalCollection
        personalCollectionList = personalCollection.get("wishlist", [])
        collectionNameList = []
        for item in personalCollectionList:
            cardNameList.append(item)
        print("\nCards in your Wishlist:")
        print()
        for names in cardNameList:
            print(names)
    
def printPersonalSinglesCollection():
    print("print available personal collection dictionaries that can be printed and ask the user which one to print ")
    print("entire personal collection list","\nPersonal Collection Price")
    #read and print full personal collection from json file

def addNewPersonalSinglesCollection():
    return


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

#add new sealed search to a new dictionary in the dictionary json file
def addSealedToNewSealedCollection(newSealedCollectionTitle,newSealedName,newSealedSearchDictionary):
    #open wishilst file
    with open("/workspaces/data_3500_homework/final_project/sealed_collection.json", "r", encoding = "utf-8") as file:
        sealedCollection = json.load(file)
        sealedCollection["sealed_colelction"][newSealedCollectionTitle][newSealedName]= newSealedSearchDictionary
    with open("/workspaces/data_3500_homework/final_project/sealed_collection.json", "w", encoding = "utf-8") as file:
        json.dump(sealedCollection, file, ensure_ascii = False, indent = 4)
    return newSealedName

    
    return sealedDictionaryCollectionName
#search for a card and add it to sealed collection json
def addToSealedCollection(newSealedName,newSealedSearchDictionary):
    #open personal collection file
    with open("/workspaces/data_3500_homework/final_project/personal_collection.json", "r", encoding = "utf-8") as file:
        sealedCollection = json.load(file)
        sealedCollection["sealed_collection"][newSealedName]= newSealedSearchDictionary
    with open("/workspaces/data_3500_homework/final_project/personal_collection.json", "w", encoding = "utf-8") as file:
        json.dump(sealedCollection, file, ensure_ascii = False, indent = 4)   
    return newSealedName

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
        searchCardSingle_menu = False
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
        print("1 - Search for Card Single")
        print("2 - Search for Sealed Product")
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
                print("1 - Search for Card Single")
                print("2 - Search for Sealed Product")
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
                    searchCardSingle_menu = True
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                    searchCardSingle_menu = False
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
                print("1 - Search for Card Single")
                print("2 - Search for Sealed Product")
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
    while searchCardSingle_menu == True:#Card Search Menu Interactions, Menu Selections
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
                    saveToNewWishlist = input("Save to a new Wishlist Collection[Y/N]?  ")
                    saveCardToNewWishlist = True
                    while saveCardToNewWishlist == True:
                        if saveToNewWishlist in ("n","N","y","Y"):
                            if saveToNewWishlist in ("n","N"):
                                saveCardToSavedWishlist = True
                                saveCardToNewWishlist = False
                                break
                            if saveToNewWishlist in ("y","Y"):
                                newWishlistCollectionName = input("What would you like to name the new Wishlist Collection?  ")
                                newWishlistCollectionName.replace(" ","_")
                                jsonFile = "wishlist_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newWishlistCollectionName,currentCardSearchDictionary)
                                print("\nNew Wishlist Collection Created")
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,cardName,newDictionary)
                                print("\n",cardName,"was added to new",newDictionaryName,"!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?")
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        cardSearchSaveToPersonalCollection = True
                                        cardSearchSaveToWishlist = False
                                        saveCardToNewWishlist = False
                                        break
                                    if cardSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        cardSearchSaveToPersonalCollection = False#go back to beginning of menu search loop
                                        break
                                break
                    while saveCardToASavedWishlist == True:
                        saveCardToSavedWishlistCollection = input("Would you like to save this card to a Saved Wishlist[Y/N]?  ")
                        if saveCardToSavedWishlistCollection in ("n","N","y","Y"):
                            if saveCardToSavedWishlistCollection in ("n","N"):
                                cardSearchSaveToPersonalCollection = True
                                cardSearchSaveToWishlist = False
                                saveCardToASavedWishlist = False
                                break
                            if saveCardToSavedWishlistCollection in ("y","Y"):
                                jsonFile = "wishlist_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"!")
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
                            break
    
        #ask to save to personal collection file
        while cardSearchSaveToPersonalCollection == True:
            saveSearchCardToPersonalCollection = input("\nWould you like to save this card to your Personal Collection[Y/N]?")
            if saveSearchCardToPersonalCollection in ("n","N","y","Y"):
                if saveSearchCardToPersonalCollection in ("n","N"):
                    cardSearchSaveToVendorCollection = True
                    cardSearchSaveToPersonalCollection = False
                if saveSearchCardToPersonalCollection in ("y","Y"):
                    saveToNewPersonalCollection = input("Save to a new Personal Collection[Y/N]?  ")
                    saveCardToNewPersonalCollection = True
                    while saveCardToNewPersonalCollection == True:
                        if saveToNewPersonalCollection in ("n","N","y","Y"):
                            if saveToNewPersonalCollection in ("n","N"):
                                saveCardToASavedPersonalCollection = True
                                saveCardToNewPersonalCollection = False
                                break
                            if saveToNewPersonalCollection in ("y","Y"):
                                newPersonalCollectionName = input("What would you like to name new Personal Collection?  ")
                                newPersonalCollectionName.replace(" ","_")
                                jsonFile = "personal_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newPersonalCollectionName,currentCardSearchDictionary)
                                print("\nNew Personal Collection Created")
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,cardName,newDictionary)
                                print("\n",cardName,"was added to new",newDictionaryName,"!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?")
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        cardSearchSaveToVendorCollection = True
                                        saveCardToNewPersonalCollection = False
                                        cardSearchSaveToPersonalCollection = False
                                        break
                                    if cardSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        cardSearchSaveToPersonalCollection = False#go back to beginning of menu search loop
                                        break
                                break
                                break
                    while saveCardToASavedPersonalCollection == True:
                        saveCardToSavedPersonalCollection = input("Would you like to save this card to a Saved Personal Collection[Y/N]?  ")
                        if saveCardToSavedPersonalCollection in ("n","N","y","Y"):
                            if saveCardToSavedPersonalCollection in ("n","N"):
                                cardSearchSaveToVendorCollection = True
                                saveCardToASavedPersonalCollection = False
                                break
                            if saveCardToSavedPersonalCollection in ("y","Y"):
                                jsonFile = "personal_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"!")
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
                            break

        #ask to save to vendor collection json file
        while cardSearchSaveToVendorCollection == True:
            saveSearchCardToVendorCollection = input("\nWould you like to save this card to your Vendor Collection[Y/N]?")
            if saveSearchCardToVendorCollection in ("n","N","y","Y"):
                if saveSearchCardToVendorCollection in ("n","N"):
                    mainMenu = True
                    searchCardSingle_menu = False
                    cardSearchSaveToVendorCollection = False
                if saveSearchCardToVendorCollection in ("y","Y"):
                    saveToNewVendorCollection = input("Save to a new Vendor Collection[Y/N]?  ")
                    saveCardToNewVendorCollection = True
                    #save card to new vendor collection
                    while saveCardToNewVendorCollection == True:
                        if saveToNewVendorCollection in ("n","N","y","Y"):
                            if saveToNewVendorCollection in ("n","N"):
                                saveCardToASavedVendorCollection = True
                                saveCardToNewVendorCollection = False
                                break
                            if saveToNewVendorCollection in ("y","Y"):
                                newVendorCollectionName = input("What would you like to name new Vendor Collection?  ")
                                newVendorCollectionName.replace(" ","_")
                                jsonFile = "vendor_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newVendorCollectionName,currentCardSearchDictionary)
                                print("\nNew Vendor Collection Created")
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,cardName,newDictionary)
                                print("\n",cardName,"was added to new",newDictionaryName,"!")
                                saveCardToASavedVendorCollection = False
                                saveCardToNewVendorCollection = False
                                break
                    #save card to saved vendor collection
                    while saveCardToASavedVendorCollection == True:
                        saveCardToSavedVendorCollection = input("Would you like to save this card to a Saved Vendor Collection[Y/N]?  ")
                        if saveCardToSavedVendorCollection in ("n","N","y","Y"):
                            if saveCardToSavedVendorCollection in ("n","N"):
                                mainMenu = True
                                searchCardSingle_menu = False
                                saveCardToASavedVendorCollection = False
                                break
                            if saveCardToSavedVendorCollection in ("y","Y"):
                                jsonFile = "vendor_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?")
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        mainMenu = True
                                        searchCardSingle_menu = removeFromPersonalSinglesCollection
                                        cardSearchSaveToVendorCollection = False
                                        break
                                    if cardSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        cardSearchSaveToVendorCollection = False#go back to beginning of menu search loop
                                        break
                                break
                            break
        continue

    #Search for Sealed Card Menu
    while searchSealedPrice_menu == True:
        searchingForSealed = True
        #start sealed search function
        while searchingForSealed == True:
            searchQueryString = input("\nWhat sealed product do you want to search for?  ")
            sealedName,currentFullSealedSearchDictionary = newSealedSearch(searchQueryString)
            sealedName,newSealedDictionary = newSealedSearchFilter(sealedName,currentFullSealedSearchDictionary)
            print("\n",sealedName)
            print("\n",newSealedDictionary)
            sealedSearchSaveToSealedCollection = False
            sealedSearchSaveToNewSealedCollection = True
            searchingForSealed = False

        #ask to if the user wants to save to new dictionary or old dictionary in sealed collection json file
        while sealedSearchSaveToNewSealedCollection == True:
            saveSearchSealed= input("\nWould you like to save this Sealed Product to a New Sealed Collection[Y/N]?")
            if saveSearchSealed in ("n","N","y","Y"):
                if saveSearchSealed in ("n","N"):
                    sealedSearchSaveToSealedCollection = True
                    sealedSearchSaveToNewSealedCollection = False
                if saveSearchSealed in ("y","Y"):
                    newSealedCollectionName = input("What would you like to name the new Sealed Collection?  ")
                    newSealedCollectionName.replace(" ","_")
                    jsonFile = "sealed_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newSealedCollectionName,newSealedDictionary)
                    print("\nNew Collection Created")
                    addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,sealedName,newDictionary)
                    print("\n",sealedName,"was added to new",newDictionaryName,"!")
                    sealedSearchAgain = input("\nSearch for another Sealed Product[Y/N]?") 
                    if sealedSearchAgain in ("n","N","y","Y"):
                        if sealedSearchAgain in ("n","N"):
                            mainMenu = True
                            searchSealedPrice_menu = False
                            sealedSearchSaveToSealedCollection = True
                            sealedSearchSaveToNewSealedCollection = False
                            break
                        if sealedSearchAgain in ("y","Y"):
                            searchingForSealed = True
                            sealedSearchSaveToNewSealedCollection = False#go back to beginning of menu search loop
                            break
                break
        
        #ask to save to sealed collection file
        while sealedSearchSaveToSealedCollection == True:
            saveSearchSealedToSealedCollection = input("Would you like to save this sealed product to a Saved Sealed Collection[Y/N]?")
            if saveSearchSealedToSealedCollection in ("n","N","y","Y"):
                if saveSearchSealedToSealedCollection in ("n","N"):
                    mainMenu = True
                    searchingForSealed = True
                    sealedSearchSaveToSealedCollection = False
                if saveSearchSealedToSealedCollection in ("y","Y"):
                    jsonFile = "sealed_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,sealedName,newSealedDictionary)
                    print("\n",sealedName,"was added to",addItemToSavedCollection,"!")
                    sealedSearchAgain = input("\nSearch for another Sealed Product[Y/N]?") 
                    if sealedSearchAgain in ("n","N","y","Y"):
                        if sealedSearchAgain in ("n","N"):
                            mainMenu = True
                            searchSealedPrice_menu = False
                            sealedSearchSaveToSealedCollection = False
                            break
                        if sealedSearchAgain in ("y","Y"):
                            searchingForSealed = True
                            sealedSearchSaveToSealedCollection= False#go back to beginning of menu search loop
                            break
                break
        continue

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
    while buyList_menu == True:
        print()
        print("Buy List Menu")
        print()
        print("1 - Start New Buy List")
        print("2 - Show Saved Buy Lists")
        print("3 - Remove a Card From Saved Buy Lists")
        print("4 - Delete Saved Buy List")
        print("5 - Main Menu")
        print("0 - Quit Program")
        #set main menu choices
        menuChoices = [0,1,2,3,4,5]
        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[0-5]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("1 - Start New Buy List")
                print("2 - Show Saved Buy Lists")
                print("3 - Edit Saved Buy Lists")
                print("4 - Delete Saved Buy List")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                #Search Single Card Price Menu
                if menuSelect == 1:
                    searchingForCard = True
                    while searchingForCard == True:
                        searchQueryString = input("\nWhat card do you want to add to Buy List?  ")
                        cardName,currentFullCardSearchDictionary = newCardSearch(searchQueryString)
                        cardName,currentCardSearchDictionary = newCardSearchFilter(cardName,currentFullCardSearchDictionary)
                        print("\n",cardName)
                        print("\n",currentCardSearchDictionary)
                        addToNewBuyList = True
                        searchingForCard = False
                    while addToNewBuyList == True:
                        saveSearchCardToBuyList = input("\nWould you like to add this to a new Buy List[Y/N]?")
                        if saveSearchCardToBuyList in ("n","N","y","Y"):
                            if saveSearchCardToBuyList in ("n","N"):
                                addToSavedBuyList = True
                                addToNewBuyList = False
                            if saveSearchCardToBuyList in ("y","Y"):
                                #save to new buy list
                                newBuyListName = input("\nWhat would you like to name the new Buy List?  ")
                                newBuyListName.replace(" ","_")
                                jsonFile = "buy_list.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newBuyListName,{})
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to new",newDictionaryName,"!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        addToSavedBuyList = False
                                        addToNewBuyList = False

                                        break
                                    if cardSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        addToNewBuyList = False#go back to beginning of menu search loop
                                        break
                                break
                    while addToSavedBuyList == True:
                        saveToSavedBuyList = input("\nWould you like to save this card to Saved Buy List[Y/N]?")
                        if saveToSavedBuyList in ("n","N","y","Y"):
                            if saveToSavedBuyList in ("n","N"):
                                mainMenu = True
                                menuSelect_numValidCheck = False
                                addToSavedBuyList = False
                            if saveToSavedBuyList in ("y","Y"):
                                jsonFile = "buy_list.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"Buy List!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        mainMenu = True
                                        buyList_menu = False
                                        menuSelect_numValidCheck = False
                                        addToSavedBuyList= False
                                    break
                                if cardSearchAgain in ("y","Y"):
                                    searchingForCard = True
                                    addToSavedBuyList = False#go back to beginning of menu search loop
                                    break
                    break
                if menuSelect == 2:
                    jsonFile = "buy_list.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    showSavedBuyLists = printCollection(dictionaryFileName,dictionaryFilePath)
                    break
                if menuSelect == 3:
                    jsonFile = "buy_list.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    editBuyList = removeItemFromSavedCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 4:
                    jsonFile = "buy_list.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    deleteSavedBuyList = removeCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 5:
                    mainMenu = True
                    buyList_menu = False
                    break
                if menuSelect == 0:
                    programActive = False
                    buyList_menu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Start New Buy List")
                print("2 - Show Saved Buy Lists")
                print("3 - Edit Saved Buy Lists")
                print("4 - Delete Saved Buy List")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
    
    #Wishlist Menu
    while wishlist_menu == True:
        #print options and which menu you are in
        print("\nWishlist Menu")
        print()
        print("1 - Show Saved Wishlist")
        print("2 - Add Card to Saved Wishlist")
        print("3 - Remove Card Saved from Wishlist")
        print("4 - Delete Saved Wishlist")
        print("5 - Main Menu")
        print("0 - Quit Program")
        #set main menu choices
        menuChoices = [0,1,2,3,4,5]
        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[0-5]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("1 - Show Saved Wishlist")
                print("2 - Add Card to Saved Wishlist")
                print("3 - Remove Card Saved from Wishlist")
                print("4 - Delete Saved Wishlist")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                if menuSelect == 1:
                    jsonFile = "wishlist_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    showSavedWishists = printCollection(dictionaryFileName,dictionaryFilePath)
                    break
                #Search Single Card Price Menu
                if menuSelect == 2:
                    searchingForCard = True
                    while searchingForCard == True:
                        searchQueryString = input("\nWhat card do you want to add to WishList?  ")
                        cardName,currentFullCardSearchDictionary = newCardSearch(searchQueryString)
                        cardName,currentCardSearchDictionary = newCardSearchFilter(cardName,currentFullCardSearchDictionary)
                        print("\n",cardName)
                        print("\n",currentCardSearchDictionary)
                        addToNewWishlist = True
                        searchingForCard = False
                    while addToNewWishlist == True:
                        saveSearchCardToWishlist = input("\nWould you like to add this to a new Wishlist[Y/N]?")
                        if saveSearchCardToWishlist in ("n","N","y","Y"):
                            if saveSearchCardToWishlist in ("n","N"):
                                addToSavedWishlist = True
                                addToNewWishlist = False
                            if saveSearchCardToWishlist in ("y","Y"):
                                #save to new buy list
                                newWishlistName = input("\nWhat would you like to name the new Wishlist?  ")
                                newWishlistName.replace(" ","_")
                                jsonFile = "wishlist_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newWishlistName,{})
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to new",newDictionaryName,"!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        addToSavedWishlist = False
                                        addToNewWishlist = False
                                        break
                                    if cardSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        addToNewWishlist = False#go back to beginning of menu search loop
                                        break
                                break
                    while addToSavedWishlist == True:
                        saveToSavedWishlist = input("\nWould you like to save this card to Saved Wishlist[Y/N]?")
                        if saveToSavedWishlist in ("n","N","y","Y"):
                            if saveToSavedWishlist in ("n","N"):
                                mainMenu = True
                                menuSelect_numValidCheck = False
                                addToSavedWishlist = False
                            if saveToSavedWishlist in ("y","Y"):
                                jsonFile = "wishlist_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"Wishlist!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        mainMenu = True
                                        buyList_menu = False
                                        menuSelect_numValidCheck = False
                                        addToSavedWishlist= False
                                    break
                                if cardSearchAgain in ("y","Y"):
                                    searchingForCard = True
                                    addToSavedBuyList = False#go back to beginning of menu search loop
                                    break
                    break
                if menuSelect == 3:
                    jsonFile = "wishlist_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    editWishList = removeItemFromSavedCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 4:
                    jsonFile = "wishlist_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    deleteSavedWishList = removeCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 5:
                    mainMenu = True
                    buyList_menu = False
                    break
                if menuSelect == 0:
                    programActive = False
                    buyList_menu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Show Saved Wishlist")
                print("2 - Add Card to Saved Wishlist")
                print("3 - Remove Card Saved from Wishlist")
                print("4 - Delete Saved Wishlist")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
    
    
    #Personal Singles Collection Menu
    while personalSinglesCollection_menu == True:
        print()
        print("Personal Singles Collection Menu")
        print()
        print("1 - Show Personal Singles Collection")
        print("2 - Add Card to Personal Singles Collection")
        print("3 - Remove Card from Personal Singles Collection")
        print("4 - Delete Personal Singles Collection")
        print("5 - Main Menu")
        print("0 - Quit Program")
        #set main menu choices
        menuChoices = [0,1,2,3,4,5]
        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[0-5]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("1 - Show Personal Singles Collection")
                print("2 - Add Card to Personal Singles Collection")
                print("3 - Remove Card from Personal Singles Collection")
                print("4 - Delete Personal Singles Collection")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                if menuSelect == 1:
                    jsonFile = "personal_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    showSavedWishists = printCollection(dictionaryFileName,dictionaryFilePath)
                    break
                #Search Single Card Price Menu
                if menuSelect == 2:
                    searchingForCard = True
                    while searchingForCard == True:
                        searchQueryString = input("\nWhat card do you want to add to Personal Collection?  ")
                        cardName,currentFullCardSearchDictionary = newCardSearch(searchQueryString)
                        cardName,currentCardSearchDictionary = newCardSearchFilter(cardName,currentFullCardSearchDictionary)
                        print("\n",cardName)
                        print("\n",currentCardSearchDictionary)
                        addToNewPersonalCollection = True
                        searchingForCard = False
                    while addToNewPersonalCollection == True:
                        saveSearchCardToPersonalCollection = input("\nWould you like to add this to a new Personal Collection[Y/N]?")
                        if saveSearchCardToPersonalCollection in ("n","N","y","Y"):
                            if saveSearchCardToPersonalCollection in ("n","N"):
                                addToSavedPersonalCollection = True
                                addToNewPersonalCollection = False
                            if saveSearchCardToPersonalCollection in ("y","Y"):
                                #save to new buy list
                                newPersonalCollectionName = input("\nWhat would you like to name the new Personal Collection?  ")
                                newPersonalCollectionName.replace(" ","_")
                                jsonFile = "personal_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newPersonalCollectionName,{})
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to new",newDictionaryName,"!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        addToSavedPersonalCollection = False
                                        addToNewPersonalCollection = False
                                        break
                                    if cardSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        addToNewPersonalCollection = False#go back to beginning of menu search loop
                                        break
                                break
                    while addToSavedPersonalCollection == True:
                        saveToSavedPersonalCollection = input("\nWould you like to save this card to Saved Personal Collection[Y/N]?")
                        if saveToSavedPersonalCollection in ("n","N","y","Y"):
                            if saveToSavedPersonalCollection in ("n","N"):
                                mainMenu = True
                                menuSelect_numValidCheck = False
                                personalSinglesCollection_menu = False
                                addToSavedPersonalCollection = False
                            if saveToSavedPersonalCollection in ("y","Y"):
                                jsonFile = "personal_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"Personal Collection!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        mainMenu = True
                                        personalSinglesCollection_menu = False
                                        menuSelect_numValidCheck = False
                                        addToSavedPersonalCollection= False
                                    break
                                if cardSearchAgain in ("y","Y"):
                                    searchingForCard = True
                                    addToSavedPersonalCollection = False #go back to beginning of menu search loop
                                    break
                    break
                if menuSelect == 3:
                    jsonFile = "personal_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    editWishList = removeItemFromSavedCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 4:
                    jsonFile = "personal_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    deleteSavedWishList = removeCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 5:
                    mainMenu = True
                    buyList_menu = False
                    break
                if menuSelect == 0:
                    programActive = False
                    buyList_menu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Show Personal Singles Collection")
                print("2 - Add Card to Personal Singles Collection")
                print("3 - Remove Card from Personal Singles Collection")
                print("4 - Delete Personal Singles Collection")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
    
    #Personal Sealed Collection Menu
    while personalSealedCollection_menu == True:
        print()
        print("Personal Sealed Collection Menu")
        print()
        print("1 - Show Personal Sealed Collection")
        print("2 - Add Card to Personal Sealed Collection")
        print("3 - Remove Product from Personal Sealed Collection")
        print("4 - Delete Personal Sealed Collection")
        print("5 - Main Menu")
        print("0 - Quit Program")
        #set main menu choices
        menuChoices = [0,1,2,3,4,5]
        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[0-5]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("Personal Sealed Collection Menu")
                print()
                print("1 - Show Personal Sealed Collection")
                print("2 - Add Card to Personal Sealed Collection")
                print("3 - Remove Product from Personal Sealed Collection")
                print("4 - Delete Personal Sealed Collection")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                if menuSelect == 1:
                    jsonFile = "sealed_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    showSavedWishists = printCollection(dictionaryFileName,dictionaryFilePath)
                    break
                #Search Single Card Price Menu
                if menuSelect == 2:
                    searchingForCard = True
                    while searchingForCard == True:
                        searchQueryString = input("\nWhat card do you want to add to Sealed Collection?  ")
                        sealedName,currentFullSealedSearchDictionary = newSealedSearch(searchQueryString)
                        sealedName,currentSealedSearchDictionary = newSealedSearchFilter(sealedName,currentFullSealedSearchDictionary)
                        print("\n",cardName)
                        print("\n",currentCardSearchDictionary)
                        addToNewSealedCollection = True
                        searchingForCard = False
                    while addToNewSealedCollection == True:
                        saveSearchCardToSealedCollection = input("\nWould you like to add this to a new Sealed Collection[Y/N]?")
                        if saveSearchCardToSealedCollection in ("n","N","y","Y"):
                            if saveSearchCardToSealedCollection in ("n","N"):
                                addToSavedSealedCollection = True
                                addToNewSealedCollection = False
                            if saveSearchCardToSealedCollection in ("y","Y"):
                                #save to new buy list
                                newSealedCollectionName = input("\nWhat would you like to name the new Sealed Collection?  ")
                                newSealedCollectionName.replace(" ","_")
                                jsonFile = "sealed_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newSealedCollectionName,{})
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,sealedName,currentSealedSearchDictionary)
                                print("\n",sealedName,"was added to new",newDictionaryName,"!")
                                sealedSearchAgain = input("\nSearch for another Sealed Product[Y/N]?") 
                                if sealedSearchAgain in ("n","N","y","Y"):
                                    if sealedSearchAgain in ("n","N"):
                                        addToSavedSealedCollection = False
                                        addToNewSealedCollection = False
                                        break
                                    if sealedSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        addToNewSealedCollection = False#go back to beginning of menu search loop
                                        break
                                break
                    while addToSavedSealedCollection == True:
                        saveToSavedSealedCollection = input("\nWould you like to save this card to Saved Sealed Collection[Y/N]?")
                        if saveToSavedSealedCollection in ("n","N","y","Y"):
                            if saveToSavedSealedCollection in ("n","N"):
                                mainMenu = True
                                menuSelect_numValidCheck = False
                                personalSealedCollection_menu = False
                                addToSavedSealedCollection = False
                            if saveToSavedSealedCollection in ("y","Y"):
                                jsonFile = "sealed_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,sealedName,currentSealedSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"Sealed Collection!")
                                sealedSearchAgain = input("\nSearch for another Sealed Product[Y/N]?") 
                                if sealedSearchAgain in ("n","N","y","Y"):
                                    if sealedSearchAgain in ("n","N"):
                                        mainMenu = True
                                        personalSealedCollection_menu = False
                                        menuSelect_numValidCheck = False
                                        addToSavedSealedCollection= False
                                    break
                                if sealedSearchAgain in ("y","Y"):
                                    searchingForSealed = True
                                    addToSavedSealedCollection = False #go back to beginning of menu search loop
                                    break
                    break
                if menuSelect == 3:
                    jsonFile = "personal_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    editWishList = removeItemFromSavedCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 4:
                    jsonFile = "personal_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    deleteSavedWishList = removeCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 5:
                    mainMenu = True
                    buyList_menu = False
                    break
                if menuSelect == 0:
                    programActive = False
                    buyList_menu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Show Personal Sealed Collection")
                print("2 - Add Card to Personal Sealed Collection")
                print("3 - Remove Product from Personal Sealed Collection")
                print("4 - Delete Personal Sealed Collection")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
    
    #Vendor Collection Menu
    while vendorCollection_menu == True:
        print()
        print("Vendor Collection Menu")
        print()
        print("1 - Show Vendor Collection")
        print("2 - Add Card to Vendor Collection")
        print("3 - Remove Card from Vendor Collection")
        print("4 - Delete Vendor Collection")
        print("5 - Main Menu")
        print("0 - Quit Program")
        #set main menu choices
        menuChoices = [0,1,2,3,4,5]
        #ask what menu option the user wants to select
        menuString = input("\nPlease input your selection[0-5]:  ")
        menuStringIsNum = menuString.isnumeric()
        menuStringCheck = True
        while menuStringCheck == True:
            if menuStringIsNum == False:
                #ask for menu selection again
                print("\nMust be a number, that is not a valid selection, please try again")
                print()
                print("1 - Show Vendor Collection")
                print("2 - Add Card to Vendor Collection")
                print("3 - Remove Card from Vendor Collection")
                print("4 - Delete Vendor Collection")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()
                continue#goes back to check if it's a number at the top of while statement if it is then it turns to an int and goes to menu functions
            else:
                menuSelect = int(menuString)
                menuSelect_numValidCheck = True
                menuStringCheck = False
        while menuSelect_numValidCheck == True:
            if menuSelect in menuChoices:
                #if it gets through the number validity check this group of code changes the booleans to the inputed number that cooresponds with the menu selection choice
                if menuSelect == 1:
                    jsonFile = "vendor_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    showSavedWishists = printCollection(dictionaryFileName,dictionaryFilePath)
                    break
                #Search Single Card Price Menu
                if menuSelect == 2:
                    searchingForCard = True
                    while searchingForCard == True:
                        searchQueryString = input("\nWhat card do you want to add to Personal Collection?  ")
                        cardName,currentFullCardSearchDictionary = newCardSearch(searchQueryString)
                        cardName,currentCardSearchDictionary = newCardSearchFilter(cardName,currentFullCardSearchDictionary)
                        print("\n",cardName)
                        print("\n",currentCardSearchDictionary)
                        addToNewVendorCollection = True
                        searchingForCard = False
                    while addToNewVendorCollection == True:
                        saveSearchCardToVendorCollection = input("\nWould you like to add this to a new Vendor Collection[Y/N]?")
                        if saveSearchCardToVendorCollection in ("n","N","y","Y"):
                            if saveSearchCardToVendorCollection in ("n","N"):
                                addToSavedVendorCollection = True
                                addToNewVendorCollection = False
                            if saveSearchCardToVendorCollection in ("y","Y"):
                                #save to new buy list
                                newVendorCollectionName = input("\nWhat would you like to name the new Vendor Collection?  ")
                                newVendorCollectionName.replace(" ","_")
                                jsonFile = "vendor_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                dictionaryFilePath,dictionaryFileName,newDictionaryName,newDictionary = addNewDictionaryToFile(dictionaryFilePath,dictionaryFileName,newVendorCollectionName,{})
                                addNewItemToNewCollection = addItemToNewCollection(dictionaryFilePath,dictionaryFileName,newDictionaryName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to new",newDictionaryName,"!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        addToSavedVendorCollection = False
                                        addToNewVendorCollection = False
                                        break
                                    if cardSearchAgain in ("y","Y"):
                                        searchingForCard = True
                                        addToNewVendorCollection = False#go back to beginning of menu search loop
                                        break
                                break
                    while addToSavedVendorCollection == True:
                        saveToSavedVendorCollection = input("\nWould you like to save this card to Saved Vendor Collection[Y/N]?")
                        if saveToSavedVendorCollection in ("n","N","y","Y"):
                            if saveToSavedVendorCollection in ("n","N"):
                                mainMenu = True
                                menuSelect_numValidCheck = False
                                personalSinglesCollection_menu = False
                                addToSavedPersonalCollection = False
                            if saveToSavedVendorCollection in ("y","Y"):
                                jsonFile = "vendor_collection.json"
                                dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                                addItemToSavedCollection = addNewItemToSavedCollection(dictionaryFilePath,dictionaryFileName,cardName,currentCardSearchDictionary)
                                print("\n",cardName,"was added to",addItemToSavedCollection,"Vendor Collection!")
                                cardSearchAgain = input("\nSearch for another card[Y/N]?") 
                                if cardSearchAgain in ("n","N","y","Y"):
                                    if cardSearchAgain in ("n","N"):
                                        mainMenu = True
                                        personalSinglesCollection_menu = False
                                        menuSelect_numValidCheck = False
                                        addToSavedVendorCollection= False
                                    break
                                if cardSearchAgain in ("y","Y"):
                                    searchingForCard = True
                                    addToSavedVendorCollection = False #go back to beginning of menu search loop
                                    break
                    break
                if menuSelect == 3:
                    jsonFile = "vendor_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    editWishList = removeItemFromSavedCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 4:
                    jsonFile = "vendor_collection.json"
                    dictionaryFileName,dictionaryFileNamePrinted,dictionaryFilePath = defineTargetCollection(jsonFile)
                    deleteSavedWishList = removeCollection(dictionaryFilePath,dictionaryFileName)
                    break
                if menuSelect == 5:
                    mainMenu = True
                    buyList_menu = False
                    break
                if menuSelect == 0:
                    programActive = False
                    buyList_menu = False
                    break
            else:
                #variables print checks
                print("That is not a valid selection, please try again")
                print()
                print("1 - Show Vendor Collection")
                print("2 - Add Card to Vendor Collection")
                print("3 - Remove Card from Vendor Collection")
                print("4 - Delete Vendor Collection")
                print("5 - Main Menu")
                print("0 - Quit Program")
                #set main menu choices
                menuChoices = [0,1,2,3,4,5]
                #ask what menu option the user wants to select
                menuString = input("\nPlease input your selection[0-5]:  ")
                menuStringIsNum = menuString.isnumeric()

    #Quick Percentage Calculator menu
    while quickPercentageCalculate_menu == True:
        percentageCalculator()
        mainMenu = True
        quickPercentageCalculate_menu = False

else:#if the user has chosen to quit the program
    print("\nThank you for using Luis' Pokemon Management Program!!!")
    print()
    print("\nGotta Catch Em All!!!!")
    print()

