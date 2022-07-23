import random


random_generator = random.randint(1, 10)
print(random_generator)


lives = 5
game_on = True

while game_on:

    guess = input("choose a number between 1 and 10 ")

    if lives == 0:
        print(f"bad luck you have {lives} lives ")
        game_on = False
        play_game = input("play again y/n")
        if play_game == "y":
            game_on = True
            random_generator = random.randint(1, 10)
        else:
            break
    elif int(guess) > random_generator:
        print("To high")
        print(f"you have {lives} lives left")
        lives -= 1
    elif int(guess) < random_generator:
        print("To low")
        lives -= 1
        print(f"you have {lives} lives left")
    else:
        print("you guessed correct")

        game_on = False
        play_game = input("play again y/n ")

        if play_game == "y":
            game_on = True
            random_generator = random.randint(0, 10)
        else:
            break


