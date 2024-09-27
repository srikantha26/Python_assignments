print("welcome to Rollercoaster!!")
height_level = int(input("enter the height_level\n"))

if height_level >= 120:
    print("yes you can ride the RollerCoaster")
    age= int(input("what is your age?"))
    if age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry your height is less than the required height, better luck next time!!")
