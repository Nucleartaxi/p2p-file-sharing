from peers import peer_db
from peers import peer_db
from user_interface import instance_user_interface
from user import user_database, login_handler




class main: #main class
    def __init__(self):
        self.peer_db = peer_db()
    
    def select_demo(self):
        while True:
            print("Which demo to run?\n0. Exit\n1. Login demo\n2. main loop no login (for testing)\n3. Mininet 10 peers demo")
            selection = str(input())
            if selection == "0":
                exit() 
            elif selection == "1":
                self.demo_user_with_login()
            elif selection == "2":
                self.demo_user_loop()
            elif selection == "3":
                pass

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
m.select_demo()

# db = user_database()
# db.initialize_db_with_sample_users()
