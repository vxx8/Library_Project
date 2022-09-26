from re import T
import mysql.connector
from mysql.connector import Error


class db:

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost', database='library', user='root', password='password')
            self.cursor = self.connection.cursor(buffered=True)
        except Error as e:
            print(e)

    
    def execute_query(self, query):
        try:
            self.cursor = self.connection.cursor(buffered=True)
            self.cursor.execute(query)
        except Error as e:
            print(e)
        #self.cursor.close()

    def check_exists(self):
        try:
            self.cursor.rowcount()
        except Error as e:
            print(e)

    def fetch_rows(self):
        try:
            self.cursor.fetchall()
        except Error as e:
            print(e)

    def commit(self):
        self.connection.commit()

mysql = db()

class user:

    def __init__(self, username, password, first_name, last_name, email, contact_number):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact_number = contact_number

    def check_user(self, username): 
        
        check_user = f"select username from user_info where username='{self.username}'"
        mysql.execute_query(check_user)
        if mysql.check_exists() != 0:
            return False
        else:
            return True


    def create_account(self, username, password, first_name, last_name, email, contact_number):
        query = f"insert into user_info (first_name, last_name, email, username, password, contact_number) values ('{self.first_name}', '{self.last_name}', '{self.email}', '{self.username}', '{self.password}', '{self.contact_number}')"
        mysql.execute_query(query)
        mysql.commit()


    def login(self, username, password):
        mysql.execute_query(f"select * from user_info where username = '{self.username}' and password = '{self.password}'")
        a = mysql.check_exists()
        if a != 0
            return True
        else:
            return False
            
        
    def current_status(self):
        query = "SELECT book1, book1_rentdate, book2, book2_rentdate, book2, book3_rentdate, fines FROM user_info"
        mysql.execute_query(query)
        rows = mysql.fetch_rows()
        for x in rows
            print(x)

    def rent_book(self, username, isbn):
        self.isbn = isbn
        check_user = f"select username from user_info where username ='{username}'"
        mysql.execute_query(check_user)
        if mysql.check_exists() != 0: 
            check_book = f"select * from books where isbn = '{isbn}'"
            mysql.execute_query(check_book)
            if mysql.check_exists() != 0:
                check_qty = f"select * from books where isbn='{isbn}' and Copies_available > 0"
                mysql.execute_query(check_qty)
                if mysql.check_exists() != 0:
                    new_qty = f"update books set Copies_available = Copies_available-1 where isbn = '{isbn}'"
                    mysql.execute_query(new_qty)
                    mysql.commit()
                else:
                    print("All copies are currently rented")
            else:
                print("Book not found, please check your entry and try again")
        else:
            print("Invalid user credentials, please check and re-enter the username")

    
    def return_book(self, username, isbn):
       check_user = f"select username from user_info where username = '{username}'"
        mysql.execute_query(check_user)
        if mysql.check_exists() != 0: 
            check_book = f"select * from books where isbn = '{isbn}'"
            mysql.execute_query(check_book) 
            if mysql.check_exists() != 0:
               new_qty = f"update books set Copies_available = Copies_available+1 where isbn = '{isbn}'"
               mysql.execute_query(new_qty)
               mysql.commit()

    def check_fines(self, username)


    def account_details(self):
        query = f"select first_name, last_name, username, email, contact_number from user_info where username='{self.username}'"
        mysql.execute_query(query)
        rows = mysql.fetch_rows()
        for x in rows:
            print(x)

    
                

        

    