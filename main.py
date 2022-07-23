

import random


random_generator=random.randint(0, 10)

print(random_generator)
lives = 5
game_on=True
while game_on == True:
    
    guess = input("choose a number between 1 and 10 ")
    if lives == 0:
        print("you ran out of lives")
        game_on =False
        play_game=input("play again y/n")   
    elif int(guess) > random_generator:
        print("To high")
        lives -= 1
    elif int(guess) < random_generator:
        print("To low")
        lives -= 1
    else: 
        print("you guessed correct")
        print(f"lives left{lives}")
        game_on = False
        play_game=input("play again y/n")
        
        if play_game == "y":
             game_on = True
           
            
        
        

