 # <12 ----$5
 # 12-18 --------$7
 # >18 --------$12
bill=0

print("welcome to Rollercoaster!!")
height_level = int(input("enter the height_level\n"))

if height_level >= 120:
    print("yes you can ride the RollerCoaster")
    age= int(input("what is your age?"))
    if age <=5:
        bill=5
        print("Child tickets are $5")
    elif age<=18:
        bill = 7
        print("Child tickets are $7")
    elif age <= 22:
        bill = 8
        print("Child tickets are $8")
    else:
        print("Adult tickets are $12")
        bill = 12
    wants_photo = input("do you want to take photo take ? Type yes are no\n")
    if wants_photo == "y":
        #Add $3 to the bill amount
      #bill +=3
      bill = bill+3

    print(f"your final bill is {bill}")

else:
    print("Sorry your height is less than the required height, better luck next time!!")
