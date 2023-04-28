import random
from art import guessing_game_logo

print(guessing_game_logo)
print(" Welcome to Guess the number game !!")
print(" I'm Thinking of a number between 1-100 , can you Guess it 😎 ")
number= random.randint(1,100)
# print(number)
level = input( "Enter the level you want to play with , type 'easy' or 'hard' : ")


def play_game(chance):
    print(f" You have {chance} chances to guess the number ")
    while chance !=0:
        guess=int(input("Enter the number you guessed : "))
        if guess==number:
            print(f"Congratulations !! 🤩 , You have Guessed correctly, 🤩 The number I thought was {number}")
        elif number<guess:
            print("Your Guess is Too High") 
        elif number>guess:
            print("Your Guess is Too Low")
        else:
            print("Not a valid guess ")
        chance-=1
        print(f" You have {chance} chances left to guess the number ")
        if chance==0:
            print("You Lost!! Try your Luck Next Time 😏")
        # print(f"You have {chance} chances left ")


if level=='easy':
    chance=10
    play_game(chance)
elif level=='hard':
    chance=5
    play_game(chance)

    # play_game(chance)

    


