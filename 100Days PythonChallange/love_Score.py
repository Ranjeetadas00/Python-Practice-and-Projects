# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3
# Print: "Your score is 53."

# ==========================================
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower =name2.lower()

total=name1_lower.count('t')+name1_lower.count('r')+name1_lower.count('u')+name1_lower.count('e')+name2_lower.count('t')+name2_lower.count('r')+name2_lower.count('u')+name2_lower.count('e')


total2=name2_lower.count('l')+name2_lower.count('o')+name2_lower.count('v')+name2_lower.count('e')+name1_lower.count('l')+name1_lower.count('o')+name1_lower.count('v')+name1_lower.count('e')
score=str(total)+str(total2)
score=int(score)
if((score)<=10 or score>=90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

