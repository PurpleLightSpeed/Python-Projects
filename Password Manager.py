# Gives us the funtionality to encrypt a string and hide it!
import hashlib
import getpass


#password manager empty dictionary to store the key value pairs of the username and password
password_manager = {}

#Ask the user if they want to create an account
def create_account ():
    username = input ("Enter your desired username: ")
    # Using getpass library hids the password from the user or anyone looking at the screen
    password = getpass.getpass("Enter your desired password: ")
    # Its going to take the password and use the hashlib library to hash the password with sha256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    #Its then going to store the username and hashed password in the password manager dictionary as a key value pair
    password_manager[username] = hashed_password
    print("Account created successfully!")

#Ask the user if they want to login
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

#Ask if the username and hased password match the key value pairs in the password manager dictionary
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

#The is the main menu for the user
def main():
    #A while looops default statement is True, until a break statement is used
    while True:
        #Will prompt the user to choose an option 1, 2, or 0
        choice = input("Enter 1 to create an account, 2 to login and 0 to exit: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

#This is a way for you to import the python script and import it into another python script as a library without needing to reorder functions
if __name__ == "__main__":
    main()
#Know as a python idiom
