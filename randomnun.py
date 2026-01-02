import random
num=random.randint(1,20)
usernum=int(input("Enter a number between 1 and 20"))
if num==usernum:
    print("you guessed it right")
else:
    print("You guessed it wrong")
    print(f"Computer guessed num is {num}")
