import  random
statesOfIndia = ["AP","karnataka","MP","HP","UP"]

print(statesOfIndia[0])
print(statesOfIndia[1])
print(statesOfIndia[2])
print(statesOfIndia[-0])
statesOfIndia.append("Telangana")
print(statesOfIndia)
statesOfIndia.extend(["Delhi","Goa"])
print(statesOfIndia)
statesOfIndia.insert(2,"Haryana")
print(statesOfIndia)

# random_state = random.randint(1,9)
#random_state = random.choice(statesOfIndia)
# if random_state == "AP":
#     print("AP")
# elif random_state == "karnataka":
#     print("karnataka")
# elif random_state == "Haryana":
#     print("Haryana")
#
# else:
#     print("Hyderabad")
print(len(statesOfIndia))