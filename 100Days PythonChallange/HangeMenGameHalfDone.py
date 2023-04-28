import random

dash='_'
letter=''
word_list = ["pegion" , "crow" , "tiger" , "parrot", "cat" , "lion" , "wolf"]
word = random.choice(word_list)
print(word)
word_length=len(word)
# print(dash*word_length)
group_dash=[]
end_of_game = False

for i in range(len(word)):
        group_dash.append('_')

while not end_of_game:
    guess_ch=(input("Enter a Letter that You guess may be present in the word  : ")).lower()
# ch= ch.lower()
    # group_dash=len(word)
    for i in range(len(word)):
        if word[i]==guess_ch:
            group_dash[i]=guess_ch
    
    
    print(group_dash)
    if '_' not in group_dash:
        end_of_game=True
        print("Congaturations You WON !!")