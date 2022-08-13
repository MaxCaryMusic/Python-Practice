"""password manager utilizing fernet encryption for stored passwords and hashing for master password"""
from lib.crypto_utils import check_db, view, add, init_key
from lib.hash_utils import create_master_password, check_master_password, init_master_password


def main():
  
    print("Welcome to Max's Password Manager!")
    print("\n")
    fer = init_key()
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
            view(fer)
            input("Press enter to return to main menu...")
        elif mode == "add":
            print("\n")
            add(fer)
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
