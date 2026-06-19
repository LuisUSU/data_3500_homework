user_balance = int(input("What is your Account Balance?  "))
deposit = 0
withdraw = 0
main_menu_sel = 4
main_menu_choice = []
main_menu_check = False
atm_active = 1

while atm_active > 0 :
    if main_menu_sel == 0:
        atm_active = 0
    elif main_menu_sel == 4:
        main_menu_choice = [3,2,1,0]
        if main_menu_check == False:
            print("\n3 - Account Balance")
            print("\n2 - Make a Deposit")
            print("\n1 - Make a Withdrawl")
            print("\n0 - Quit")
            main_menu_sel = int(input("\nMake your selection : "))
            main_menu_check = True
        while main_menu_check:
            for num in main_menu_choice:
                 if num == main_menu_sel:
                    main_menu_check = False
                    break
            if num != main_menu_sel:
                    print("\nThat number is invalid, please try again  ")
                    print("\n3 - Account Balance")
                    print("\n2 - Make a Deposit")
                    print("\n1 - Make a Withdrawl")
                    print("\n0 - Quit")
                    main_menu_sel = int(input("\nMake your selection:  "))

    elif main_menu_sel == 3:
        main_menu_choice = [4,2,1,0]
        if main_menu_check == False:
            print("\nYour Account Balance is: ", user_balance)
            print("\n4 - Return to Main Menu")
            print("\n2 - Make a Deposit")
            print("\n1 - Make a Withdrawl")
            print("\n0 - Quit")
            main_menu_sel = int(input("\nMake your selection:  "))
            main_menu_check = True
        while main_menu_check:
            for num in main_menu_choice:
                if num == main_menu_sel:
                    main_menu_check = False
                    break
            if num != main_menu_sel:
                    print("\nThat number is invalid, please try again  ")
                    print("\n4 - Return to Main Menu")
                    print("\n2 - Make a Deposit")
                    print("\n1 - Make a Withdrawl")
                    print("\n0 - Quit")
                    main_menu_sel = int(input("\nMake your selection:  "))

    elif main_menu_sel == 2:
        main_menu_choice = [4,3,2,1,0]
        if main_menu_check == False:
            deposit = int(input("\nHow much would you like to Deposit?  "))
            user_balance += deposit
            print("\nYour New Balance is: ", user_balance)
            print("\n4 - Return to Main Menu")
            print("\n3 - Account Balance")
            print("\n2 - Make Another Deposit")
            print("\n1 - Withdraw")
            print("\n0 - Quit")
            main_menu_sel = int(input("\nMake your Selection:  "))
            main_menu_check = True
        

    elif main_menu_sel == 1:
        withdraw = int(input("\nHow much would you like to Withdraw? "))
        if main_menu_check == False:
            if withdraw > user_balance:
                main_menu_choice = [4,3,2,0]
                print("\nInsufficient Funds, please deposit more money")
                print("\n4 - Return to Main Menu")
                print("\n3 - Account Balance")
                print("\n2 - Make a Deposit")
                print("\n0 - Quit")
                main_menu_sel = int(input("\nMake your Selection:  "))
                main_menu_check = True
                while main_menu_check:
                    for num in main_menu_choice:
                        if num == main_menu_sel:
                            main_menu_check = False
                            break
                    if num != main_menu_sel:
                        print("\nThat number is invalid, please try again ")
                        print("\nInsufficient Funds, please deposit more money")
                        print("\n4 - Return to Main Menu")
                        print("\n3 - Account Balance")
                        print("\n2 - Make another Deposit")
                        print("\n1 - Make a Withdrawl")
                        print("\n0 - Quit")
                        main_menu_sel = int(input("\nMake your selection:  "))
            else:
                main_menu_choice = [4,3,2,1,0]
                user_balance -= withdraw
                print("\nYou have Withdrawn ", withdraw)
                print("\nYour New Balance is: ", user_balance)
                print("\n4 - Return to Main Menu")
                print("\n3 - Account Balance")
                print("\n2 - Make a Deposit")
                print("\n1 - Make another Withdrawl")
                print("\n0 - Quit")
                main_menu_sel = int(input("\nMake your Selection:  "))
                main_menu_check = True
                while main_menu_check:
                    for num in main_menu_choice:
                        if num == main_menu_sel:
                            main_menu_check = False
                            break
                    if num != main_menu_sel:
                        print("\nThat number is invalid, please try again ")
                        print("\n4 - Return to Main Menu")
                        print("\n3 - Account Balance")
                        print("\n2 - Make another Deposit")
                        print("\n1 - Make a Withdrawl")
                        print("\n0 - Quit")
                        main_menu_sel = int(input("\nMake your selection:  "))
else:
    print("\nThank you for using this ATM, Please come again!")
    print()
