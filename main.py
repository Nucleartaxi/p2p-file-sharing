from client import sender
from server import server
from peers import peer_db
from peers import peer_db, peer
from instance import instance
from user_interface import instance_user_interface
from user import user_database, user, login_handler

import threading



class main: #main class
    def __init__(self):
        self.peer_db = peer_db()

    # def demo_UI(self):
    #     db = peer_db()
    def demo_user_loop(self, user):
        # i = instance(self.peer_db.get_peer("Alice")) #construct the instance the UI will control
        ui = instance_user_interface(peers_db=self.peer_db, peer=self.peer_db.get_peer(user)) #construct UI, run as user
        ui.start_user_interface_loop() #start UI loop
    def demo_user_with_login(self):
        user_db = user_database()
        login = login_handler(user_db=user_db) 
        login.login_prompt(self.demo_user_loop) #login prompt that runs demo_user_loop on successful login

        

m = main()
m.demo_user_with_login()