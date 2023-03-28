import random

top_of_range = input("Type a number from 1-10: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please type a number above zero next time")
        quit()
    if top_of_range >10:
        print("Please type a number below ten next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

print(random_number)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if top_of_range <= 0:
            print("Please type a number above zero next time")
            quit()
        if top_of_range > 10:
            print("Please type a number below ten next time")
            quit()
    else:
        print("Please type a number next time")
        quit()
        continue

    if user_guess == random_number:
        print("Well done m8! you got it in", guesses, "tries")
        break
    elif user_guess > random_number:
        print("You're above the number bruv")
    else:
        print("You're below the number bruv")



