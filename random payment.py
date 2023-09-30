import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_names= len(names)
a=random.randint(0,num_names - 1)

a=(names[a])
print(f"{a} is going to buy the meal today!")