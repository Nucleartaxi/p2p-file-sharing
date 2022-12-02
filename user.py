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
        

    def user_login(self) -> bool:
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
                    return True
                print("Error: incorrect otp.")
                return False
            print("Error: incorrect password.")
            return False
        print("Error, user does not exist.")
        return False
# db = user_database() 
# db.add_user("Alex", "Password") 

# print(db.user_login())
class login_handler:
    def __init__(self):
        self.db = user_database()
    
    def initialize_db_with_sample_users(self):
        self.db.add_user("Alice", "AlicePassword")
        self.db.add_user("Bob", "BobPassword")
    def login_prompt(self): 
        while True:
            print("1. Login\n2. Exit")
            user_input = input() 
            if user_input == "1":
                if not self.db.user_login():
                    print("Login failed.")
                    continue
                else: #accept
                    print("Logging in...")
                    break
            else:
                exit()

l = login_handler()
# l.initialize_db_with_sample_users() #our users are already created
l.login_prompt()