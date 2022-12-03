from client import sender
from server import server
from peers import peer
import threading
import sys


class instance: #an instance of the p2p program instance
    def __init__(self, peer: peer):
        self.peer = peer #who are we

        self.sender = sender() 
        self.sender.working_directory = "./" + self.peer.name + "/" #working directory is name of this peer 

        self.server = server(working_directory="./")
        self.server.working_directory = "./" + self.peer.name + "/" #working directory is the name of this peer 
        self.start_server()

    def start_server(self): #start the server
        thread = threading.Thread(target=self.server.start_server, args=(self.peer.ip, self.peer.port), daemon=True) 
        thread.start()
        print("Started server thread for user " + self.peer.name)
    
    def send_file(self, filename: str, peer: peer): #send file to the specified peer
        self.sender.file_connect(peer.ip, peer.port, filename)
        self.sender.disconnect()
    def request_file(self, filename: str, peer: peer):
        self.sender.request_connect(peer.ip, peer.port, filename)
        self.sender.disconnect()
    def __repr__(self) -> str:
        return str(self.peer)


if __name__ == '__main__':
    args = sys.argv[1:]
    p = peer(args[0], args[1], args[2]) #name ip port
    instance(p)
