# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
class sender: #handles sending data 
    def __init__(self) -> None:
        self.socket = None
        pass
    def send_data(self, str_data): #sends string data to the server
        self.socket.sendall(str_data.encode('utf-8'))
        data = self.socket.recv(1024)
        print('Received', repr(data))
    def connect(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        self.socket = s
    def disconnect(self):
        self.socket.close()