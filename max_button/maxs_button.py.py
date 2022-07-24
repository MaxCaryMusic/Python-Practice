yes = ['yes', 'yeah', 'yup', 'y', 'totally', 'go for it', 'hell yeah']
no = ['no', 'nope', 'n', 'nah', 'naw', 'naww', 'no way', 'no way jose', 'nah foo']
idk = ["i dont know", "i dont't know", "i dunno", "idk"]

print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
while True:
    answer = input("Do you want to press the button? ").lower()
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    if answer in yes:
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        response = input("Are you sure you want to press the button? ").lower()
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        if response in yes:
            print("fine...You can press the button, but only because max says so.")
            print("okay, you pressed it, bye bye!")
            break
        elif response in no:
            print("Probably best to just leave it alone.")
            print("give it time, you'll figure it out.")
            continue
        else:
            print("Are you okay????")
            continue
    elif answer in no:
        print("You can't press the button")
        print("And thats the bottom line")
        print("Cuz Stone Cold said so!")
        
    elif answer == "maybe":
        print("Max will think about it.")
        print("Okay, Max thought about it... NO!!!")
        
    elif answer in idk:
        print("Probably best to just leave it alone.")
        print("give it time, you'll figure it out.")
        
    else:
        print("IDK WTF you're even saying RN")
        print("try again in english?")
        
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("Max has spoken...")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    