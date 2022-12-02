from client import sender
from peers import peer_db, peer


class main_user_interface_loop():
    def __init__(self, peers_db):
        self.peer_db = peers_db
        self.main_user_interface_loop()
    def request_peer(self) -> peer:

        print("Request from which peer?")
        self.peer_db.print_peers()

    def main_user_interface_loop(self):
        while True:
            print("""
                1. Send file mode 
                2. Request file mode
                3. Exit
            """)
            action = int(input(": "))
            if action == 1: #send file mode 
                print("Enter filename to send")
                filename = input()
                send = sender() 
                send.file_connect('localhost', 50007, filename)
                # send.send_file(filename)
                send.disconnect()
                print("File sent")
            elif action == 2: #request file mode
                print("Enter filename to request") 
                filename = input() 
                print("Enter ip to request from") 
                ip = input() 
                print("Enter port to request from") 
                port = input() 
                send = sender() 
                send.request_connect('localhost', 50007, filename)
                send.disconnect()
            elif action == 3: #exit mode
                exit()