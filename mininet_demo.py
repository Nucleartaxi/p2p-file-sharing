from instance import instance 
from peers import peer_db, peer 


class mininet_demo:
    def __init__(self):
        self.peer_db = peer_db()
    def start(self):
        instances = self.setup_instances()
        [print(x) for x in instances]

    def setup_instances(self):
        result = [] 
        peers = ["Bob"]
        for name in peers:
            result.append(instance(self.peer_db.get_peer(name)))
        return result