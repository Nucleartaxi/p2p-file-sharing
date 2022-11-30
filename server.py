# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
class server:
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def process_chat(self, conn): 
        while True:
            data = conn.recv(1024) #receive data
            text = data.decode() #decode bytes into regular string
            print(text) #print chat string to screen
            if not data: break #break if end of data
    def process_file(self, conn, filename):
        with open(self.working_directory + filename, "ab") as out_file: #reads the file in chunks and sends it chunk by chunk
            while True:
                chunk = conn.recv(1024)
                if not chunk: break
                out_file.write(chunk)

    def start_server(self): #starts the server. 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            while True: #server will continue to listen
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    header = conn.recv(1024).decode().split(" ")
                    print("header=" + str(header))
                    if header[0] == "CHAT":
                        self.process_chat(conn)
                    elif header[0] == "FILE":
                        self.process_file(conn, header[1])
                    # while True:
                    #     data = conn.recv(1024)
                    #     if not data: break
                    #     conn.sendall(data)