import random

op=random.randint(1,3)
print(op)
your_Choice= int(input("Enter your Choice :- 1- Rock, 2-Paper, 3-sesors \n"))
# print(f"your choice is {your_Choice}")

computer_choice = op
if your_Choice==1 or op==1:
    your_Choice=str("Rock")
    computer_choice=str("Rock")
elif your_Choice==2 or op==2:
    your_Choice=str("Paper")
    computer_choice=str("Paper")
elif your_Choice==3 or op==3:
    your_Choice=str("Seasors")
    computer_choice=str("Seasors")

print(f"your choice is {your_Choice}")
print(f"computer's choise is {computer_choice}")
if (your_Choice==1 and op==2 or your_Choice==2 and op==3 or your_Choice==3 and op==1):
    print(f"You Lose Your choice is {your_Choice} and computer's choice was {computer_choice}")
elif your_Choice==2 and op==1 or your_Choice==3 and op==2 or your_Choice==1 and op==3:
    print(f" Wahh!! you WON!! your choice is {your_Choice} and Computer's choice is {computer_choice}")
elif op==1 and your_Choice==1 or your_Choice==2 and op==2 or your_Choice==3 and op==3:
    print(f" ohh it's a DRAW!! Match your choice was {your_Choice} and computer's choise is {computer_choice}")
