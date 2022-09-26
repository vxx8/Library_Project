def welcome_screen():
    options = '''
    Welcome to the Zeiss Library, please choose from one of the following options:
    1. Login
    2. Registration
    3. Exit
    '''
    choice = input(options)
    return choice


def check_username():
    username = input("Enter a username")
    return username

def registration():
    username = check_username()   
    password_1 = input("Enter your password: ")
    password_2 = input("Re-enter your password: ")
    if password_1 == password_2:
        password = password_1
        print("passwords match")
    else:
        print("passwords do not match, please re-enter your password")
        registration():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = first_name + last_name
    email = input("Enter your email address: ")
    contact_number = int(input("Enter your contact number: "))


def registration_success():
    print("Account created successfully, please login to continue")


def user_console():
    options = '''
    1. Current rentals and dues
    2. Account details
    3. Exit
    '''
    choice = input(options)
    return choice


#def user_account_details():
    print(registration.username)
    print(registration.full_name)
    print(registration.email)
    print(registration.contact_number)
    options = '''
    1. Change password
    2. Change email
    3. Change contact number
    4. Exit'''
    pass


def admin_console():
    options = '''
    1. Rent book
    2. Return book
    3. Check user details
    4. Check book details
    5. Exit
    '''
    choice = input(options)
    return choice


def exit():
    print("You have exited successfully")


def invalid_selection():
    print("You have selected an invalid option, please try again")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password")


def login_success():
    print("Login success!")


def invalid_username():
    print("The username entered is invalid, please try again")

def unavailable_username():
    print("The username selected is already in use, please enter another username")

def available_username():
    print("Username available, please proceed")


def invalid_password():
    print("The password you have entered in invalid, please try again")


def invalid_credentials():
    print("The credentials entered are invalid, please try again")    