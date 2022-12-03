from client import sender
from server import server
from peers import peer_db
from peers import peer_db, peer
from instance import instance
from user_interface import instance_user_interface

import threading



class main: #main class
    def __init__(self):
        self.peer_db = peer_db()

    # def demo_UI(self):
    #     db = peer_db()
    def demo_user_loop_no_login(self):
        i = instance(self.peer_db.get_peer("Alice")) #construct the instance the UI will control
        ui = instance_user_interface(peers_db=self.peer_db, instance=i) #construct UI, run as Alice
        ui.start_user_interface_loop() #start UI loop
        

m = main()
m.demo_user_loop_no_login()