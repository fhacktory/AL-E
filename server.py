import sys
sys.path.insert(0, "./lib")
import Leap, socket

class Server(object):
    def __init__(self):
        super(Server, self).__init__()
        print 'Bonjour Server'
        self.sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((socket.gethostname(), 8081))
        self.sock.listen(1)
        self.clients = []
        self.nb_client = 0

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        for client in self.clients:
            client.sendall(msg)

    def run(self):
        while 1:
            #accept connections from outside
            print 'waiting for a connection'
            (client, address) = self.sock.accept()
            self.clients.append(client)
            self.nb_client += 1
            #now do something with the clientsocket
            #in this case, we'll pretend this is a threaded server
            self.send('Hello\n')

    def __del__(self):
        self.sock.close()

class MyListener(Server, Leap.Listener):
    def __init__(self# , *args, **kwargs
    ):
        super(MyListener, self).__init__(# *args, **kwargs
        )
        self.controller = Leap.Controller()
        self.controller.add_listener(self)

    def find_direction(self, position):
        if position.x > 90: # right
            return 'right'
        elif position.x < -90: # left
            return 'left'
        elif position.z < -90: # forward
            return 'forward'
        elif position.z > 90: # backward
            return 'backward'
        else:
            return 'undefined' # undefined

    def on_connect(self, controller):
        print 'Connected'

    def on_frame(self, controller):
        frame = controller.frame()
        fingers = frame.fingers.extended()
        hand = frame.hands[0]
        if hand.is_valid and len(fingers) == 5:
            direction = self.find_direction(hand.palm_position)
            print str(direction)
            self.send(str(direction) + '\n')
        if hand.is_valid and len(fingers) == 2:
            seld.send('ok');

    def __del__(self):
        self.controller.remove_listener(self)
        super(MyListener, self).__del__()

def main():
    listener = MyListener()

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        listener.run()
    except KeyboardInterrupt:
        pass
    finally:
        print 'bye'
        # Remove the sample listener when done

if __name__ == "__main__":
    main()
