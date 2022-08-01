#password manager utilizing fernet encryption for stored passwords and hashing for master password
from cryptography.fernet import Fernet

def write_key():
    """
    if key.key exists, load key.key. otherwise, create key.key.
    """
    with open ("key.key", "wb") as key_file:
        key = Fernet.generate_key()
        key_file.write(key)

#password manager utilizing fernet encryption for stored passwords and hashing for master password
def main():
    import bcrypt

    try: 
        f = open("key.key")
        print("Encryption key detected. Starting program...")
        print("\n")
        f.close()
    except IOError:
        write_key()
        print("Encryption Key generated successfully!")

        
    print("Welcome to Max's Password Manager!")
    print("\n")
    pepper = "P3pp3R".encode()

    
    def create_master_password():
        mstrpwd = input("Create Master Password: ").encode() + pepper
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(mstrpwd, salt)
        with open("master_password.txt", "w") as f:
            f.write(hashed.decode())
            
    def check_master_password():
        pwattempt = input("Master Password: ")
        if bcrypt.checkpw(pwattempt.encode() + pepper, open("master_password.txt", "r").read().encode()):
            print("Master Password correct!")
            return True
        else:
            print("Master Password incorrect!")
            exit()   #exit program if master password is incorrect

    #create master_password.txt if it doesn't exist already
    try:
        f = open("master_password.txt", "r")
        print("Welcome back!")
        f.close()
        check_master_password()
    except IOError:
        print("Master password not found. Creating master password...")
        open("master_password.txt", "w")
        create_master_password()
        print("Master Password created successfully! \n")
        print("re-enter master password to sign-in")
        check_master_password()

    #after master password is authenticated, prompt user to add or view stored encrypted passwords
    try:
        f = open("passwords.txt", "r")
        f.close()
    except IOError:
        open("passwords.txt", "w")
        print("Password DataBase created successfully!")

    def load_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

    key = load_key()
    fer = Fernet(key)

    def view():
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                name, pwd = data.split("|")
                print("user: ", name)
                print("password: ", fer.decrypt(pwd.encode()).decode() + "\n")
                print("\n")

    def add():
        name = input("Account Name: ")
        pwd = input("Password: ")

        with open ("passwords.txt", "a") as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        print("Password added successfully!")
        print("\n")

    while True:
        print("\n")
        mode = input("Add a new password, view existing passwords, change master password, or quit? (add/view/change/q): ").lower()  
        if mode == "q":
            print("\n")
            print("Goodbye!")
            break
        if mode == "view":
            print("\n")
            view()
            input("Press enter to return to main menu...")
        elif mode == "add":
            print("\n")
            add()
        elif mode == "change":
            check_master_password()
            print("\n")
            print("Changing master password...")
            print("\n")
            create_master_password()
            print("Master password changed successfully!")
        else:
            print("Invalid input")
            continue
if __name__ == "__main__":
    main()
