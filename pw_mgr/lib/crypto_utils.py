from cryptography.fernet import Fernet


def write_key():
    """
    if key.key exists, load key.key. otherwise, create key.key.
    """
    with open ("key.key", "wb") as key_file:
        key = Fernet.generate_key()
        key_file.write(key)

"""check if key.key exists. if not, create key.key. if yes, open key.key."""
def init_key():
    try:    
        f = open("key.key")
        print("Encryption key detected. Starting program...")
        print("\n")
        f.close()
    except IOError:
        with open ("key.key", "wb") as key_file:
            key = Fernet.generate_key()
            key_file.write(key)
        print("Encryption Key generated successfully!")

"""check for password db, create if not found"""
def check_db():
    try:
        f = open("passwords.txt")
        f.close()
    except IOError:
        open("passwords.txt", "w")
        print("Password DataBase created successfully!")


"""load key.key and encrypt password data"""
def load_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

key = load_key()
fer = Fernet(key)

"""view stored encrypted passwords from db"""
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split("|")
            print("user: ", name)
            print("password: ", fer.decrypt(pwd.encode()).decode() + "\n")
            print("\n")

"""add new password to encrypted db"""
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open ("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    print("Password added successfully!")
    print("\n")