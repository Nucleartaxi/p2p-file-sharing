# Echo server program 
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
DELIM = "|"
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
        with open(self.working_directory + filename, "wb") as out_file: #reads the file in chunks and sends it chunk by chunk
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
                    chunk = conn.recv(1024)
                    # header = conn.recv(1024).decode().split(" ")
                    header = chunk.decode().split(DELIM) #parses the incoming chunk to read the header 
                    command = header[0] 
                    args = "" 
                    if len(header) > 1:
                        args = header[1]
                    print("header=" + str(header))
                    print("command=" + command + " args=" + args)
                    if command == "CHAT":
                        self.process_chat(conn)
                    elif command == "FILE":
                        self.process_file(conn, args)
                    # while True:
                    #     data = conn.recv(1024)
                    #     if not data: break
                    #     conn.sendall(data)