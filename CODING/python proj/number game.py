import random

top_number = input("Type a number: ")

if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("please type a number larger than 0!")
        quit()
else:
    print("please type a number text time")
    quit()

random_number = random.randint(0, top_number)
guesses = 0

while True:
    guesses += 1
    guess = input("make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please type a number text time")
        continue

    if guess == random_number:
        print("correct")
        break
    elif guess > random_number:
            print ("you were above the number")
    else:
            print ("you were below the number")

print("you have done it", guesses, "guesses!")