import bcrypt
pepper = "P3pp3R".encode()



"""master password is created, hashed, and stored in master_password.txt"""
def create_master_password():
    mstrpwd = input("Create Master Password: ").encode() + pepper
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(mstrpwd, salt)
    with open("master_password.txt", "w") as f:
        f.write(hashed.decode())

"""authenticate master password attempt against stored hash"""
def check_master_password():
        pwattempt = input("Master Password: ")
        if bcrypt.checkpw(pwattempt.encode() + pepper, open("master_password.txt", "r").read().encode()):
            print("Master Password correct!")
            return True
        else:
            print("Master Password incorrect!")
            exit()

"""check for master password file, create if not found"""
def init_master_password():
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