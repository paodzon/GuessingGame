#Made by P0W7 Paolo Dizon

import random

print("\t\t\t\t\tGuessing Game Challenge")
print("If your guess is more than 10 away from the answer, I'll tell you you're too far")
print("If your guess is within 10 of my number, I'll tell you you're close")
print("-------------------------------------------------------------------------------")
value = random.randint(1,100)
tries = 1

while True:
    try:
        guess = int(input("Please Enter a number from 1 to 100 only: "))
        xrange = value - guess

        if value == guess:
            print('CONGRATULATIONS YOU HAVE GUESS THE NUMBER CORRECTLY')
            print(f"With a total of {tries} tries")
            break
        elif guess < 1 or guess > 100:
            print("OUT OF BOUNDS")
        elif tries == 1:
            if abs(xrange) <= 10:
                print("Your first guess is close")
            else:
                print("Your first guess is too far!")
        else:
            if abs(xrange) <= 10:
                print("Your Guess is CLOSE!")
            else:
                print("MEH TOO FAR")
        tries += 1
    except ValueError:
        pass


