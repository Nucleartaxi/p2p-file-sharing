# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
class sender: #handles sending data 
    def __init__(self) -> None:
        self.socket = None
        pass
    def send_str_data(self, str_data): #sends string data to the server
        self.socket.sendall(str_data.encode('utf-8'))
        # data = self.socket.recv(1024)
        # print('Received', repr(data))
    def connect(self, host, port, header):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.sendall(header.encode('utf-8'))
    def chat_connect(self, host, port):
        self.connect(host, port, "CHAT")
    def file_connect(self, host, port, filename):
        self.connect(host, port, "FILE" + " " + filename)
    def disconnect(self):
        self.socket.close()
    def send_file(self, filename):
        with open(filename, "rb") as in_file: #reads the file in chunks and sends it chunk by chunk
            while True:
                chunk = in_file.read(1024)
                if chunk == b"":
                    break
                self.socket.sendall(chunk)