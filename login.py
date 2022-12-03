import bcrypt 
import pyotp

# password = b'my_password' 
# salt = bcrypt.gensalt() 
# hashed = bcrypt.hashpw(password, salt)


# otp = pyotp.totp.TOTP(pyotp.random_base32(length=32, chars="test"))
# s = otp.provisioning_uri(name='alexander.shirk@wsu.edu', issuer_name='secureapp')
# print(s)


def login(): 
    username = input("Enter your username: ")
    password = bytes(input("Enter your password: "), 'utf-8')
    if bcrypt.hashpw(password, salt) == hashed:
        print("Success!")
    else:
        print("Error: invalid password")

def login_loop():
    while True:
        print("""
        1. Login
        """)
        action = int(input(": ")) 
        if action == 1:
            login()

login_loop()