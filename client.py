# Echo client program
import socket

PORT = 50007              # The same port as used by the server
DELIM = "|"
class sender: #handles sending data 
    def __init__(self):
        self.socket = None
        self.working_directory = "./"
        pass
    def send_str_data(self, str_data): #sends string data to the server
        self.socket.sendall(str_data.encode('utf-8'))
        # data = self.socket.recv(1024)
        # print('Received', repr(data))
    def connect(self, host, port, header):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        data = header.encode('utf-8') + bytearray([70] * (1024 - len(header))) #pads the byte array 
        print(data.decode())
        self.socket.sendall(data)
    def chat_connect(self, host, port):
        self.connect(host, port, "CHAT" + DELIM)
    def file_connect(self, host, port, filename):
        self.connect(host, port, "FILE" + DELIM + filename + DELIM)
        self.send_file(filename)
    def request_connect(self, host, port, filename):
        self.connect(host, port, "REQUEST" + DELIM + filename + DELIM)
        self.receive_file(filename)

    def receive_file(self, filename):
        chunk = self.socket.recv(1024)
        if chunk.decode() == "NOFILE":
            print("Error: this peer does not have file " + filename)
            return
        with open(self.working_directory + filename, "wb") as out_file: #reads the file in chunks and sends it chunk by chunk
            while True:
                if not chunk: break
                out_file.write(chunk)
                chunk = self.socket.recv(1024)

    def disconnect(self):
        self.socket.close()
    def send_file(self, filename):
        with open(filename, "rb") as in_file: #reads the file in chunks and sends it chunk by chunk
            while True:
                chunk = in_file.read(1024)
                if chunk == b"":
                    break
                self.socket.sendall(chunk)