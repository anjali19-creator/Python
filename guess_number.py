import random
random_num=random.randint(1,100)
print("welcome to the number guessing game!!")
print("Guess the number between 1 to 100")
turn=0
while True:
    guess=int(input("Guess a number:"))
    turn+=1
    if guess>random_num:
        print("choose a lower number")
    elif guess<random_num:
        print("choose a higher number")
    else:
        print(f"CONGRATULATION!!\nyou guessed it right in {turn} turns")
        break