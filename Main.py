import string
import random

savedPasswords = list()

#The random password is being generated depending on the length, and the characters that it could contain.
def setPassword(passwordLength, characters):
    #I make use of the list, so that I can build the string character by character.
    listPassword = list()

    #For each character in the password, a random character is being chosen, from the list "character"
    for i in range(0, passwordLength):
        listPassword.append(random.choice(characters))

    #The list is being turned into a string
    password = ''.join(listPassword)

    print("The password generated was: " + password)
    return password

def generatePassword(passwordLength, specialCharacters, passwordLower, passwordUpper, charactersToOmmit):

    #The characters list is the list which contains all the possible characters that the password could contain.
    characters = list()

    #Checks whether the password is set to be uppercase, lower case, or default case, and modifies / creates the
    #"characters" list accordingly
    if passwordLower == True:
        characters = list(string.ascii_lowercase)
    elif passwordUpper == True:
        characters = list(string.ascii_uppercase)
    else:
        characters = list(string.ascii_letters)

    #Adds each special character entered by the user into the "characters" list.
    for i in specialCharacters:
        characters.append(i)

    #Removes any characters which are in the "characters" list, which were entered by the user to ommit.
    for i in charactersToOmmit:
        if characters.__contains__(i):
            characters.remove(i)

    password = setPassword(passwordLength, characters)
    passwordConfirmed = False

    while passwordConfirmed == False:
        print("---------------------------------------------")
        print("Enter 1. = Regenerate password")
        print("Enter 2. = Confirm password.")
        choice = int(input("Enter your choice (1 - 2): "))

        if choice == 1:
            password = setPassword(passwordLength, characters)
        elif choice == 2:
            passwordConfirmed = True
            savedPasswords.append(password)


#Displays the user's current password preferences.
def passwordPreferences(passwordLength, specialCharacters, passwordLower, passwordUpper, charactersToOmmit):
    print("\n------------------------------------------------------------------")

    #Displays the password length
    print("Password Length: " + str(passwordLength))

    #Displays the characters which are to be ommitted from the password.
    if len(charactersToOmmit) > 0:
        print("characters to be ommitted: ", end = "")
        for i in charactersToOmmit:
            print("'" + i + "' , ", end = "")
        print()

    #Displays how the password is to be capitalised.
    if passwordLower == True:
        print("The password is set to lowercase characters only!")
    elif passwordUpper == True:
        print("The password is set to uppercase characters only!")
    else:
        print("The password has default capitalisation!")

    #Displays the special characters which could (possible) be included in the password.
    if len(specialCharacters) > 0:
        print("Special characters to be (possibly) included in the password: ", end = "")
        for i in specialCharacters:
            print("'" + i + "' , ", end = "")
        print()


def setPasswordLength():
    passwordLength = int(input("\nPlease enter the length of your password: "))
    return passwordLength

def passwordMenu():

    passwordLength = setPasswordLength()
    specialCharacters = list()
    passwordLower = False
    passwordUpper = False
    charactersToOmmit = list()
    passwordGenerated = False

    while passwordGenerated == False:

        print("\n------------------------------------------------------------------")

        print("1. = Change password length")
        print("2. = Add special character")
        print("3. = Ommit character from password")
        print("4. = Reset characters to ommit from password")
        print("5. = Set password to only uppercase")
        print("6. = Set password to only lowercase")
        print("7. = Set password to default capitalisation (mixed)")
        print("8. = Show current password preferences")
        print("9. = Generate password")

        choice = int(input("Please enter your choice (1 - 9): "))
        ##Sets the password length
        if choice == 1:
            passwordLength = setPasswordLength()
        #Adds a desired special character to the list of possible characters.
        elif choice == 2:
            specialCharacters.append(
                input("\nPlease enter the special character you want to (possibly) be included in the password: "))
        #Adds a character which is to be omitted from the password.
        elif choice == 3:
            charactersToOmmit.append(input("\nPlease enter the character you want to ommit from the password: "))
        #Clears characters which are to be omitted from the password.
        elif choice == 4:
            charactersToOmmit.clear()
        #Sets the password to uppercase.
        elif choice == 5:
            passwordUpper = True
            passwordLower = False
        #Sets the password to lowercase.
        elif choice == 6:
            passwordLower = True
            passwordUpper = False
        #Sets the password to mixed (default) capitalisation.
        elif choice == 7:
            passwordLower = False
            passwordUpper = False
        #Displays all user password preferences.
        elif choice == 8:
            passwordPreferences(passwordLength, specialCharacters, passwordLower, passwordUpper, charactersToOmmit)
        #Generates the password
        elif choice == 9:
            passwordGenerated = True
            generatePassword(passwordLength, specialCharacters, passwordLower, passwordUpper, charactersToOmmit)


def menu():
    while True:
        print("------------------------------------------------------------------")

        menuChoice = int(input("1. = Create a password\n2. = Look at saved passwords\n3. = Quit\nPlease enter your choice. (1 - 3): "))
        #User is asked to enter password length, and then the password menu is displayed to the user.
        if menuChoice == 1:
            passwordMenu()
        #The saved passwords are displayed to the user (If any are already existing).
        elif menuChoice == 2:
            if len(savedPasswords) > 0:
                print("Saved passwords:")
                for i in savedPasswords:
                    print("> " + i)
            else:
                print("You havent created any passwords yet!")
        #The program closes.
        elif menuChoice == 3:
            print("You quit!")
            break

menu()