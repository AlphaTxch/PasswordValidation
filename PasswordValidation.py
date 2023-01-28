# Password Validation System
# 27/01/2023
# JM

def password_check(data):
    SpecialCharacters = ["$", "@", "#", "%","~","{}", "!"]
    boolean = True

    if len(data) < 6:
        print("- Length should be at least 6") # checks password length is smaller than 6
        boolean = False

    if len(data) > 25:
        print("- Length should be not be greater than 25") # makes sure password length isnt higher than 25 
        boolean = False

    if not any(char.isdigit() for char in data):
        print("- Password should have at least one number") # checks if there is a numerical data in the input 
        boolean = False

    if not any(char.isupper() for char in data):
        print("- Password should have at least one uppercase letter") # checks if there is a uppercase character in the input
        boolean = False

    if not any(char.islower() for char in data):
        print("- Password should have at least one lowercase letter") # checks if there is a lower character in the input 
        boolean = False

    if not any(char in SpecialCharacters for char in data): # checks if any data from the input matches the given data set 
        print("- Password needs a special symbol") 
        boolean = False

    if boolean:
        return boolean

def main():
    attempts = 0
    while True:
        print("Type 'Q' to exit.")
        data = input("Enter your password: ")
        attempts += 1 #adds one for every time it goes through a loop in the var 
        if data.upper() == "Q":
            print("Exiting the code.")
            break
        elif (password_check(data)):
            print("Password is valid")
            break
        else:
            print("Invalid Password, try again.")
    print(f"Total attempts taken:" ,attempts) # only prints when a valid password is ran 

if __name__ == "__main__":
    main()
