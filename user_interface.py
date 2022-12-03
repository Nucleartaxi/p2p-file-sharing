import os
from client import sender
from peers import peer_db, peer
from instance import instance


class instance_user_interface():
    def __init__(self, peers_db: peer_db, peer: peer):
        self.peer_db = peers_db
        self.peer = peer
        self.instance = instance(peer) #who are we running this user interface as? 

    def request_peer(self) -> peer: #helper for the user interface to prompt peers from the user.
        print("Which peer?")
        self.peer_db.print_peers()
        input_peer = input(":")
        return self.peer_db.get_peer(input_peer)
    
    def prompt_for_file(self) -> str:
        print("Enter filename") 
        filename = input()
        if not os.path.isfile(self.instance.sender.working_directory + filename): #if file doesn't exist in sender's directory
            return None 
        return filename

    def send_file_prompt(self): #user prompt for sending files
        #get the filename from user input
        filename = self.prompt_for_file()
        if filename == None:
            print("Error, could not find file")
            return

        peer = self.request_peer() 
        if peer == None:
            print("Error, could not find peer.")
            return

        self.instance.send_file(filename, peer)
        print("File " + filename + " sent")

    def request_file_prompt(self): #user prompt for requesting files
        print("Enter filename to request") 
        filename = input() 

        peer = self.request_peer() 
        if peer == None:
            print("Error, could not find peer.")
            return 
        
        self.instance.request_file(filename, peer)
        print("File " + filename + " received")
        
    def start_user_interface_loop(self): #user interface loop
        while True:
            print("""
                1. Send file mode 
                2. Request file mode
                3. Exit
            """)
            action = int(input(": "))
            if action == 1: #send file mode 
                self.send_file_prompt()
            elif action == 2: #request file mode
                self.request_file_prompt()
            elif action == 3: #exit mode
                exit()

    # def main_user_interface_loop(self):
    #     while True:
    #         print("""
    #             1. Send file mode 
    #             2. Request file mode
    #             3. Exit
    #         """)
    #         action = int(input(": "))
    #         if action == 1: #send file mode 
    #             print("Enter filename to send")
    #             filename = input()

    #             peer = self.request_peer() 
    #             if peer == None:
    #                 print("Error, could not find peer.")
    #                 continue

    #             send = sender() 
    #             send.file_connect(peer.ip, peer.port, filename)
    #             send.disconnect()
    #             print("File sent")
    #         elif action == 2: #request file mode
    #             print("Enter filename to request") 
    #             filename = input() 

    #             peer = self.request_peer() 
    #             if peer == None:
    #                 print("Error, could not find peer.")
    #                 continue

    #             send = sender() 
    #             send.request_connect(peer.ip, peer.port, filename)
    #             send.disconnect()
    #             print("File received")
    #         elif action == 3: #exit mode
    #             exit()