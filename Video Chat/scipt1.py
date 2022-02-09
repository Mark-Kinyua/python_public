from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

# Lets make Zoom.

receiving = StreamingServer('192.168.0.14', 9999) # ip, portNumber
sending = StreamingServer('192.168.0.14', 9999) # ip, portNumber

t1 = threading.Thread(target=receiving.start_server)
t1.start()

time.sleep(2)

t2 = threading.Thread(target=sending.start_stream)
t2.start

while input("") =! "STOP":
    continue


receiving.stop_server()
sending.stop_stream()

# PUT CODE ON BOTH MACHINES AND SWAP IP ADDRESSES
