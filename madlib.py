#string concatenation
# suppose we want to create a string that says "subscribe to _______"
# youtuber = "Abhiram little hero" #some string variable
#
# #few ways to do this
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

#command+/ is used to comment multiple lines of code

language = input("Adjective: ")
verb1 = input("verb1: ")
verb2 = input("verb2: ")
verb3 = input("verb3: ")
verb4 = input("verb4: ")
verb5 = input ("verb5: ")

madlib = (f"{language} computer programming is so good! It makes me so excited all the time because \n"
f"I love you to {verb1}\n"
f"I am living here for sometime {verb2}\n"
f"I like this so much {verb3}\n"
f"I know this guy so much and so like to continue {verb4}\n"
f"I like to play this more often and know to get more {verb5}\n")
print(madlib)