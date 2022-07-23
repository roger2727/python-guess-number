

import random


random_generator=random.randint(0, 10)

print(random_generator)
game_on=True
while game_on == True:
    
    guess = input("choose a number between 1 and 10 ")

    if int(guess) > random_generator:
        print("To high")
    elif int(guess) < random_generator:
        print("To low")
    else: 
        print("you guessed correct")
        game_on = False
        

