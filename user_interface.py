from client import sender
from peers import peer_db, peer


class main_user_interface_loop():
    def __init__(self, peers_db):
        self.peer_db = peers_db
        self.main_user_interface_loop()
    def request_peer(self) -> peer:

        print("Request from which peer?")
        self.peer_db.print_peers()
        input_peer = input(": ")
        return self.peer_db.get_peer(input_peer)

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

                peer = self.request_peer() 
                if peer == None:
                    print("Error, could not find peer.")
                    continue

                send = sender() 
                send.file_connect(peer.ip, peer.port, filename)
                send.disconnect()
                print("File sent")
            elif action == 2: #request file mode
                print("Enter filename to request") 
                filename = input() 

                peer = self.request_peer() 
                if peer == None:
                    print("Error, could not find peer.")
                    continue

                send = sender() 
                send.request_connect(peer.ip, peer.port, filename)
                send.disconnect()
                print("File received")
            elif action == 3: #exit mode
                exit()