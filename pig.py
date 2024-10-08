import random

roll_num = int(input("Enter how many times you wanna roll the die: "))
user_score = 0
comp_score = 0
target = 50

def roll():
    return random.randint(1,6)


i = 0
while i < roll_num:
    print(f"{i+1} iteration")
    print(f"Your current score {user_score}")     
    print(f"Computer's current score {comp_score}")   
    user_dice_num = roll()
    comp_dice_num = roll()
    print(f"Your dice num: {user_dice_num}")
    print(f"Computer's dice num: {comp_dice_num}")
    if user_dice_num != 1:
        user_score += user_dice_num
    else:
        user_score = 0

    if comp_dice_num != 1:
        comp_score += comp_dice_num
    else:
         comp_score = 0
    print(f"Your current score {user_score}")     
    print(f"Computer's current score {comp_score}")     
    i += 1    


if user_score >= target or user_score > comp_score :
    print("yay you win!!")
else:
    print("Comp wins")    