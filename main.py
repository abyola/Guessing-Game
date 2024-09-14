import random

number=random.randint(1,100)
attempt =1
guess=int(input("Guess the number: "))
while(True):
    if(guess>number):
        guess=int(input("Try again! This is too high: "))
        attempt+=1

    elif(guess<number):
        guess=int(input("Try again! This is too low: "))
        attempt+=1

    else:
        print(f"You Guessed right! You guessed it right in {attempt} attempts")
        break
