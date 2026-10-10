import random
number=random.randint(1,100)
guess=0
while guess!=number:
    guess=int(input("Enter a number: "))
    if guess<number:
        print("Might be higher")
    elif guess>number:
        print("Might be lower")
print(f"You found it! it's: {number}")