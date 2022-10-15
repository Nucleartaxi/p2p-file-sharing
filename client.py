# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
class sender: #handles sending data 
    def __init__(self) -> None:
        pass
    def send_data(self, str_data): #sends string data to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(str_data.encode('utf-8'))
            data = s.recv(1024)
            print('Received', repr(data))