from instance import instance 
from peers import peer_db, peer 

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info


# It would be nice if we didn't have to do this:
# pylint: disable=arguments-differ

class SingleSwitchTopo( Topo ):
    "Single switch connected to n hosts."
    def build( self, n=2):
        switch = self.addSwitch('s1')
        for h in range(n):
            # Each host gets 50%/n of system CPU
            # 10 Mbps, 5ms delay, no packet loss
            # self.addLink(host, switch, bw=10, delay='5ms', loss=0, use_htb=True)
            # Each host gets 50%/n of system CPU
            # host = self.addHost('h%s' % (h + 1),
            #                     cpu=.5 / n)
            host = self.addHost("h%s" % (h+1), cpu=.5 / n)
            # 10 Mbps, 5ms delay, no packet loss
            self.addLink(host, switch, bw=10, delay='5ms', loss=0, use_htb=True)

class MyTopo(Topo):
    def build(self, peers):
        switch = self.addSwitch('s1') 
        i = 1 
        for peer in peers:
            host = self.addHost("h%s" % (i))
            self.addLink(host, switch, bw=10, delay='5ms', loss=0, use_htb=True)
            host.cmd("python3 ./instance.py " + peer.name + " " + peer.ip + " " + peer.port)


def perfTest():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo( n=4 )
    net = Mininet( topo=topo,
                   host=CPULimitedHost, link=TCLink,
                   autoStaticArp=True )
    # net.get('h1').setIP('192.168.1.1')
    [print(net.get('h' + str(x)).IP()) for x in range(1, 5)]
    net.start()
    info( "Dumping host connections\n" )
    dumpNodeConnections(net.hosts)
    info( "Testing bandwidth between h1 and h4\n" )
    h1, h4 = net.getNodeByName('h1', 'h4')
    # net.iperf( ( h1, h4 ), l4Type='UDP' )
    net.pingAll()
    net.stop()


class mininet_demo:
    def __init__(self):
        self.peer_db = peer_db()
    def start(self):
        instances = self.setup_instances()
        [print(x) for x in instances]
        #give you a user to mess around with as an option 
    def setup_mininet(self):
        pass

    def setup_peers(self):
        result = [] 
        peers = ["Bob"]
        for name in peers:
            result.append(self.peer_db.get_peer(name))
        return result

    def testMyTopo(self):
        "Create network and run simple performance test"
        topo = MyTopo(self.setup_peers()) #creates topo with peers
        net = Mininet( topo=topo,
                    host=CPULimitedHost, link=TCLink,
                    autoStaticArp=True )
        # net.get('h1').setIP('192.168.1.1')
        # [print(net.get('h' + str(x)).IP()) for x in range(1, 5)]
        net.start()
        info( "Dumping host connections\n" )
        dumpNodeConnections(net.hosts)
        info( "Testing bandwidth between h1 and h4\n" )
        # h1, h4 = net.getNodeByName('h1', 'h4')
        # net.iperf( ( h1, h4 ), l4Type='UDP' )
        net.pingAll()
        net.stop()

if __name__ == '__main__':
    perfTest()