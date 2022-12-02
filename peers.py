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
        self.add_peer("Alice", "localhost", 50007)
    def __repr__(self):
        result = "" 
        for x in self.db.items():
            result += str(x[1]) + "\n"
        return result

# db = peer_db()
# db.initialize_db_with_sample_peers()
# print(db)
