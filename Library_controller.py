import Library_view
import Library_model
import logging

def start():
    choice = None
    while choice != '3':
        choice = Library_view.welcome_screen()
        logging.info(f"Choice selected by user is: {choice}")
        if choice == '1':
            username, password = Library_view.login()
            logging.info(f"username entered is: {username}, password is {password}")
            login = Library_model.user.login(username, password)
            while login == False:
                logging.info(f"Incorrect credentials entered, username: {username}, password: {password}")
                Library_view.invalid_credentials()
                username, password = Library_view.login()
                login = Library_model.user.login(username, password) 
            Library_view.login_success()
            logging.info(f"Successful login with username: {username}")
        elif choice == '2':
            username = Library_view.check_username()
            logging.info(f"username selected is {username}")
            user_check = Library_model.user.check_user(username)
            while user_check == False:
                logging.info(f"Unavailable username selected -> {username}")
                Library_view.unavailable_username()
                username = Library_view.check_username()
                user_check = Library_model.user.check_user(username)
            Library_view.available_username()
            logging.info(f"New username created: {username}")
            username, password_1, password_2, first_name, last_name, email, contact_number = Library_view.registration()
            user_details = Library_model.user.create_account(username, password, first_name, last_name, email, contact_number)