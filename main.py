import random

print("Welcome to the guessing game...")
print("I'm thinking a number between 1-100")

random_number=random.randint(1,100)
game_on=True
while game_on:
    difficulitiy=input("Choose a difficulitiy. Type 'easy' or type 'hard': ")

    attempts=0
    if difficulitiy.lower()=="easy":
        attempts=10
    elif difficulitiy.lower()=="hard":
        attempts=5

    while attempts>0:
        print("You have "+str(attempts)+" attempts remaining to guess the number")
        guess=int(input("Guess : "))
        attempts-=1
        if guess==random_number:
            print("You won. Number was : " + str(random_number) + ".")
            break
        elif guess<random_number:
            print("Too low")
            if attempts==0:
                print("You lost. Number was : " + str(random_number) + ".")
        elif guess>random_number:
            print("Too high")
            if attempts==0:
                print("You lost. Number was : " + str(random_number) + ".")

    game_on=False
