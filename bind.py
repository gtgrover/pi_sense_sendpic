import socket
import sys
from sense_hat import SenseHat
from time import sleep
import array
import ast

sense = SenseHat()
sense.set_rotation(270)

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8675 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    screen = conn.recv(4096)

    if not screen:
        print "screen bad"
        break

    screen_data = ast.literal_eval(screen)
    print "SCREEN:", screen_data

    screen_data_len = len(screen_data)
    print screen_data_len

    if screen_data_len = 64:
        sense.set_pixels(screen_data)

    data = "one"
    reply = data

    #sense.show_message(str(data))

    print "REPLYING WITH:"
    print reply

    conn.sendall(reply)

conn.close()
s.close()
