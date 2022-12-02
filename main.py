from client import sender
import user_interface

from server import server
import threading

test_server = server(working_directory="./server/")
thread = threading.Thread(target=test_server.start_server, args=(), daemon=True)
thread.start()
print("Thread started")

user_interface.main_user_interface_loop() 