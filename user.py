import bcrypt 
import pyotp
import subprocess
import pickle
import getpass

# https://pyauth.github.io/pyotp/ #easy 2fa will work with google authenticator 

class user:
    def __init__(self, username, password_hash, salt, otp):
        self.username = username
        self.password_hash = password_hash
        self.salt = salt
        self.otp = otp 
    def __repr__(self) -> str:
        return "username: " + self.username + " password_hash: " + str(self.password_hash) + " salt: " + str(self.salt)

class user_database:
    def __init__(self):
        self.users = {}
        self.load_db() #load db on startup
    def save_db(self):
        with open("user_db.pickle", "wb") as f:
            pickle.dump(self.users, f)
    def load_db(self):
        with open("user_db.pickle", "rb") as f:
            self.users = pickle.load(f)
    def add_user(self, username, password):
        #make the password hash
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'), salt) 

        #make the otp
        otp = pyotp.totp.TOTP(pyotp.random_base32())

        #Create the user in the database
        self.users[username] = user(username, hashed_password, salt, otp)

        #create the otp provisioning url and show it 
        otp_uri_for_qrcode = otp.provisioning_uri(name=username, issuer_name='secureapp')
        print(otp_uri_for_qrcode)
        subprocess.run(["qrcode", otp_uri_for_qrcode], shell=True)

        self.save_db() #save our db whenever there is a change 

    def user_login(self) -> str: #returns the user logged in, or None otherwise
        username = input("username: ") 
        if username in self.users.keys():
            password = bytes(getpass.getpass("password: "), 'utf-8') 
            user = self.users[username] 
            # if bcrypt.checkpw(password + user.salt, user.password_hash):
            if bcrypt.hashpw(password, user.salt) == user.password_hash: #check password
                print("Password accepted") 
                otp = input("Enter otp: ")
                if user.otp.verify(otp):
                    print("otp accepted. ")
                    return username
                print("Error: incorrect otp.")
                return None
            print("Error: incorrect password.")
            return None
        print("Error, user does not exist.")
        return None
    
    def __repr__(self):
        result = "" 
        for x in self.users.items():
            result += str(x[1]) + "\n"
        return result
# db = user_database() 
# db.add_user("Alex", "Password") 

# print(db.user_login())
class login_handler:
    def __init__(self, user_db: user_database):
        self.db = user_db
    
    def initialize_db_with_sample_users(self):
        self.db.add_user("Alice", "AlicePassword")
        self.db.add_user("Bob", "BobPassword")
    def login_prompt(self, func): 
        while True:
            print("1. Login\n2. Exit")
            user_input = input() 
            if user_input == "1":
                login = self.db.user_login()
                if not login:
                    print("Login failed.")
                    continue
                else: #accept
                    print("Logging in...")
                    func(login) #call the function with the login
            else:
                return

# l = login_handler()
# l.initialize_db_with_sample_users() #our users are already created
# print(l.db)
# l.login_prompt()