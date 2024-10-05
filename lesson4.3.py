# range using the range function

# when we take range(1,10) it will print from 1 to 9
# when we take range(1,11) it will print from 1 to 10

# for number in range(1,11):
#     print(number)
# # using step with range function will skip that step numbers in between as below
#
# for number in range(1,11,3):
#     print(number)

# taking the Gauss challenge to add the number with in the range
total = 0
for number in range(1,101):
    total += number
    print(number)
print(total)
