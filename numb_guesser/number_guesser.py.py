import random

top_of_range = input("give me a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("that's not a valid number. must be greater than 0")
        quit()
else:
    print("next time try a number")
    quit()

random_number = random.randint(0, top_of_range)
tries = 0

while True:
    tries += 1
    guess = input("guess a number between 0 and " + str(top_of_range) + ": ")

    if guess.isdigit():
        guess = int(guess)

        if guess < 0 or guess > top_of_range:
            print("that's not a valid number. must be between 0 and " + str(top_of_range))
            continue

        if guess == random_number:
            print("you got it!")
            break
        elif guess > random_number:
            print("too high")
        else:
            print("too low")
    else:
        print("next time try a number")
        continue


print("you guessed it in " + str(tries) + " tries")