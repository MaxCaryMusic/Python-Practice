import os
from cryptography.fernet import Fernet

"""load key.key and encrypt password data"""
def load_key():
    with open("key.key", "rb") as key_file:
        print("Encryption key detected. Starting program...")
        return Fernet(key_file.read())

def create_key():
    with open("key.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())
        print("Encryption Key generated successfully!")


"""check if key.key exists. if not, create key.key. if yes, open key.key."""
def init_key():
    if not os.path.exists("./key.key"):
        create_key()

    return load_key()

    
"""check for password db, create if not found"""
def check_db():
    try:
        f = open("passwords.txt")
        f.close()
    except IOError:
        open("passwords.txt", "w")
        print("Password DataBase created successfully!")


"""view stored encrypted passwords from db"""
def view(fer):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split("|")
            print("user: ", name)
            print("password: ", fer.decrypt(pwd.encode()).decode() + "\n")
            print("\n")

"""add new password to encrypted db"""
def add(fer):
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open ("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        print("Password added successfully!\n")