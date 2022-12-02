from client import sender
from server import server
from peers import peer_db
from peers import peer
import user_interface

import threading

test_server = server(working_directory="./server/")
thread = threading.Thread(target=test_server.start_server, args=(), daemon=True)
thread.start()
print("Thread started")


def demo_UI():
    db = peer_db()
    user_interface.main_user_interface_loop(db) 

demo_UI()