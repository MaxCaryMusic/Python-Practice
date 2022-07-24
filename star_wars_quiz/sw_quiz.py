
print("I'd like to play a game...")

playing = input("Do you want to play? (y/n) ").lower()
if playing != "y":
    print("coward...")
    quit()

print("excellent...")
score = 0

answer = input("Who is Luke Skywalker's Father? ").lower()
if answer in ["anakin skywalker", "anakin", "vader", "darth vader"]:
    print("point, house skywalker!")
    score += 1
else:
    print("Uncultured swine!")

answer = input("What is baby Yoda's real name? ").lower()
if answer in ["grogu", "yodito"]:
    print("This is the way...")
    score += 1
else:
    print("This is not the way...")

answer = input("what is Princess Leia's home planet? ").lower()
if answer == "alderaan":
    print("The force is strong with this one...")
    score += 1
else:
    print("I find your lack of faith disturbing...")

answer = input("Who was the original template for the clone troopers? ").lower()
if answer == "jango fett":
    print("he was just a simple man, making his way in the galaxy...")
    score += 1
else:
    print("disapointing...")

answer = input("Who was Qui-Gon Jin's padawan apprentice? ").lower()
if answer in ["obi wan", "obi-wan", "obi-wan kenobi", "obiwan", "obi wan kenobi", "obiwan kenobi", "kenobi"]:
    print("impressive...most impressive...")
    score += 1
else:
    print("You clearly don't have the high ground...")

print("calculating your score...")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("you scored " + str(score) + " out of 5")
print("which means you're " + str(score * 20) + "% cultured in modern cinema")