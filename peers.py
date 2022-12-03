import pickle


class peer:
    def __init__(self, name, ip, port):
        self.name = name 
        self.ip = ip 
        self.port = port
    def __repr__(self):
        return "Name: " + self.name + " ip: " + self.ip + " port: " + str(self.port)

class peer_db:
    def __init__(self):
        self.db = {}
        self.load_db()
        self.initialize_db_with_sample_peers()
    def add_peer(self, name, ip, port):
        self.db[name] = peer(name, ip, port)
        self.save_db()
    def get_peer(self, name): #returns the peer by name, None if peer does not exist
        return self.db.get(name, None)
    def print_peers(self): #prints all peers
        print(self)
    def save_db(self):
        with open("peer_db.pickle", "wb") as f:
            pickle.dump(self.db, f)
    def load_db(self):
        with open("peer_db.pickle", "rb") as f:
            self.db = pickle.load(f)
    def initialize_db_with_sample_peers(self):
        self.add_peer("Alice", "localhost", 50007) #who we are for the demo
        self.add_peer("Bob", "localhost", 50010)
        self.add_peer("Charlie", "localhost", 50011)
        self.add_peer("Dave", "localhost", 50070)
        self.add_peer("Eve", "localhost", 50071)
        self.add_peer("Frank", "localhost", 50072)
        self.add_peer("Grace", "localhost", 50083)
        self.add_peer("Heidi", "localhost", 50085)
        self.add_peer("Ivan", "localhost", 50099)
        self.add_peer("Judy", "localhost", 50111)
    def __repr__(self):
        result = "" 
        for x in self.db.items():
            result += str(x[1]) + "\n"
        return result

# db = peer_db()
# db.initialize_db_with_sample_peers()
# print(db)
