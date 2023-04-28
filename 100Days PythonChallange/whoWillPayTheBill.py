# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

names_len= len(names)-1
random_no=random.randint(0,names_len)

print(f"{names[random_no]} is going to buy the meal today!")

