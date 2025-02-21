#The user can input atleast 3 contacts
#The array that you should is a nested dictionary

#Bonus if you would use a function

address_book = {}

name = input("Enter Name: ")
number = int(input("Enter Num: "))
address_book[name] = number

print(address_book)

lookup = input("Lookup name:")

if lookup in address_book:
    print(f"Number: {address_book[lookup]}")
else:
    print("Contact does not exist")

