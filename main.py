from client import sender


while True:
    print("""
        1. Request file 
        2. Seed files 
    """)
    action = int(input(": "))
    if action == 1:
        file_to_request = input("enter file to request: ") #gets the file the user wants to request from the network
        send = sender() #initializes a sender object so we can establish a connection to the server
        send.send_data(file_to_request) #sends the file we want to request to the other program on the network 
    else:
        print("Invalid input. Please try again.") 