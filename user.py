import bcrypt 
import pyotp

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
    def add_user(self, username, password):
        #make the password hash
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'), salt) 

        #make the otp
        otp = pyotp.totp.TOTP(pyotp.random_base32())

        #Create the user in the database
        self.users[username] = user(username, hashed_password, salt, otp)

        #create the otp provisioning url and show it 
        s = otp.provisioning_uri(name='alexander.shirk@wsu.edu', issuer_name='secureapp')
        print(s)

    def user_login(self) -> bool:
        username = input("username: ") 
        if username in self.users.keys():
            password = bytes(input("password: "), 'utf-8') 
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
db = user_database() 
db.add_user("Alex", "Password") 

print(db.user_login())