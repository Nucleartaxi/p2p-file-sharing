from client import sender

from server import server
import threading

test_server = server(working_directory="./server/")
thread = threading.Thread(target=test_server.start_server, args=(), daemon=True)
thread.start()
print("Thread started")

while True:
    # print("""
    #     1. Request file 
    #     2. Seed files 
    # """)
    print("""
        1. Chat mode 
        2. File mode 
        3. Exit
    """)
    action = int(input(": "))
    # if action == 1:
    #     file_to_request = input("enter file to request: ") #gets the file the user wants to request from the network
    #     send = sender() #initializes a sender object so we can establish a connection to the server
    #     send.connect('localhost', 50007)
    #     send.send_data(file_to_request) #sends the file we want to request to the other program on the network 
    #     send.disconnect()
    # else:
    #     print("Invalid input. Please try again.") 
    if action == 1: #chat mode
        print("Type messages and press enter to send them, or type EXIT to exit")
        send = sender() 
        send.chat_connect('localhost', 50007) 
        while True:
            user_input = input()
            if user_input == "EXIT":
                break
            send.send_str_data(user_input)
        send.disconnect()
    elif action == 2: #file mode 
        print("Enter filename to send")
        filename = input()
        send = sender() 
        send.file_connect('localhost', 50007, filename)
        send.send_file(filename)
        send.disconnect()
        print("File sent")
    elif action == 3: #exit mode
        exit()
