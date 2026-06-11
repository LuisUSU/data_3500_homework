#Week 5 Activity 2
address = input("Please input your address:  ")
address.strip()
address.replace(" ", "")
address.replace(".", "")
address.replace(",", "")
if address.isalnum:
    print("Address:", address, "is Alpha Numeric")