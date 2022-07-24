import random


user_wins = 0
computer_wins = 0
draw = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type Rock, Paper, or Scissors or Q to quit: ").lower()
    if user_input == "q":
        print("weakling...")
        break

    if user_input not in options:
        print("next time try Rock, Paper, or Scissors")
        continue

    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, scissors is 2
    computer_input = options[random_number]
    print("You chose " + user_input + "!")
    print("Computer chose " + computer_input + "!")

    if user_input == "rock" and computer_input == "scissors":
        print("you win!")
        user_wins += 1

    elif user_input == "paper" and computer_input == "rock":
        print("you win!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_input == "paper":
        print("you win!")
        user_wins += 1

    elif user_input == computer_input:
        print("draw!")
        draw += 1

    else:
        print("you lose!")
        computer_wins += 1

print("you have " + str(user_wins) + " wins")
print("computer has " + str(computer_wins) + " wins")
print("there have been " + str(draw) + " draws")

print("Goodbye!")