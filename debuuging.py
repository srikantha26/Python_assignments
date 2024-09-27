print("welcome to the Pizza shop")
size = input("enter the size of the pizza!!\n")
#pepperoni = input("do you want pepperoni on the pizza? enter y or n:\n")
#extra_cheese = input("do you want extra cheese on the pizza? enter y or n:\n")
bill = 0

if size == "s":
    bill = 15
    print("Enjoy the small size pizza!!")
    pepperoni = input("do you want pepperoni on the pizza? enter y or n:\n")
    if pepperoni == "y":
        bill = bill+2
        print("pepperoni is added")
    extra_cheese = input("do you want extra cheese on the pizza? enter y or n:\n")
    if extra_cheese == "y":
        bill = bill+1
        print("extra cheese is added")
        print(f"Thanks for ordering the Pizza!! your total bill is {bill}")
elif size == "m":
    bill = 20
    print("Enjoy the medium size pizza your bill is")
    pepperoni = input("do you want pepperoni on the pizza? enter y or n:\n")
    if pepperoni == "y":
        bill = bill+3
        print("pepperoni is added")
    extra_cheese = input("do you want extra cheese on the pizza? enter y or n:\n")
    if extra_cheese == "y":
        bill = bill+1
        print("extra cheese is added")
        print(f"Thanks for ordering the Pizza!! your total bill is {bill}")
elif size == "l":
    bill = 25
    print("Enjoy the large size pizza your bill is")
    pepperoni = input("do you want pepperoni on the pizza? enter y or n:\n")
    if pepperoni == "y":
        bill = bill + 3
        print("pepperoni is added")
    extra_cheese = input("do you want extra cheese on the pizza? enter y or n:\n")
    if extra_cheese == "y":
        bill = bill + 1
        print("extra cheese is added")
        print(f"Thanks for ordering the Pizza!! your total bill is {bill}")
else:
    print("sorry give the exact size of pizza in S/M/L")