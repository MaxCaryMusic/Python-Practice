"""password manager utilizing fernet encryption for stored passwords and hashing for master password"""
from lib.crypto_utils import init_key
from lib.crypto_utils import check_db
from lib.crypto_utils import view
from lib.crypto_utils import add
from lib.hash_utils import create_master_password
from lib.hash_utils import check_master_password
from lib.hash_utils import init_master_password


def main():
  
    print("Welcome to Max's Password Manager!")
    print("\n")
    
    init_master_password()

    check_db()


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
