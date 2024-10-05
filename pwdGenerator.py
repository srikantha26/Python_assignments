import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
numbers = ['0','1','2','3','4','5','6','7','8','9','10']
specialCharacters = ['!','@','#','$']

print("welcome to Password Generator!!")

no_of_characters = int(input("How Many Characters do you want to keep in your password?\n"))
no_of_numeric_digits = int(input("How Many numbers do you want to keep in your password?\n"))
no_of_special_symbols = int(input("How Many special symbols do you want to keep in your password?\n"))

#Easy level
pwd = ""
#no_of_characters =4
for char in range(1,no_of_characters+1):
    #1-4
    #random_char = random.choice(letters)
    #print(random_char)
    #pwd = pwd+random_char
    pwd += random.choice(letters)
    #print(pwd)
print(pwd)

for num in range(1,no_of_numeric_digits+1):
    #sym = random.choice(specialCharacters)
    #print(sym)
    pwd += random.choice(numbers)
print(pwd)

#no_of_special_symbols=4
for sym in range(1,no_of_special_symbols+1):
    #sym = random.choice(specialCharacters)
    #print(sym)
    pwd += random.choice(specialCharacters)
print(pwd)


