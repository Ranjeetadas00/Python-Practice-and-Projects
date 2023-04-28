from art import higher_Lower_logo
from art import vs
from Datas import data 
import random

print(higher_Lower_logo)
# print(data[0])

# def random_person():
winning=True
score=0
while(winning==True):
    A=(random.choice(data))
    print("Compare A " , A["name"] +", "+ A["description"], "from" , A["country"])
    print(vs)
    B=(random.choice(data))
    print("Against B " , B["name"] +", "+ B["description"], "from" , B["country"])
    choose = input("Who has more followers , Type 'A' or 'B' : " )

    # for i in range(len(data)):

    # print(A["follower_count"])
    # print(B["follower_count"])
    if A["follower_count"]>B["follower_count"]:
        winner='A'
        if winner==choose:
            score+=1
            print("Correct!! , Your Score  is ", score)
        else:
            print("You Loose!!")
            winning=False
            print(" Your Final Score is : " , score)
    elif A["follower_count"]<B["follower_count"]:
        winner='B'
        if winner==choose:
            score+=1
            print("Correct!! , Your Score  is ", score)
        else:
            print("You Loose!!")
            winning=False
            print(" Your Final Score is : " , score)
    else:
        print("You Loose!!")
        winning=False
        print(" Your Final Score is : " , score)
            # # print(data[i])
            # for key in ((data[i])):
            #     print(data[i][key])
            
