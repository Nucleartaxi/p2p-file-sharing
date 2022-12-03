from instance import instance 
from peers import peer_db, peer
from user import user_database, login_handler
from user_interface import instance_user_interface

class complete_demo:
    def __init__(self):
        self.peer_db = peer_db()
        self.instances = []
        self.initialize_instances()

    def demo_user_loop(self, user):
        print("Starting Main UI loop") 
        ui = instance_user_interface(peers_db=self.peer_db, peer=self.peer_db.get_peer(user)) #construct UI, run as user
        ui.start_user_interface_loop() #start UI loop, demo will be run as Alice

    def handle_login(self):
        user_db = user_database()
        login = login_handler(user_db=user_db) 
        login.login_prompt(self.demo_user_loop) #login prompt that runs demo_user_loop on successful login

    def start(self):
        print("Starting login prompt") 
        self.handle_login()
    
    def create_test_file(self, name): #creates test files in each directory 
        with open("./" + name + "/" + name + ".txt", "w") as f:
            f.write(name)


    def initialize_instances(self): #initializes the other instances in the network
        for key in self.peer_db.db.keys():
            if key != "Alice": #we are Alice so we want to skip creating an Alice instance for now, it is created for the UI
                self.instances.append(instance(self.peer_db.get_peer(key))) #create and append each instance 
                self.create_test_file(key)
        # print(self.instances)


if __name__ == '__main__':
    demo = complete_demo()
    demo.start()