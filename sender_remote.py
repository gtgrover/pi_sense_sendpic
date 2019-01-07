#!/usr/bin/env python
#Socket client example in python
import socket   #for sockets
import sys
import importlib

# GET THE PICTURE MODULE TO LOAD, FROM THE COMMAND LINE
if len(sys.argv) > 1:
    module="."+sys.argv[1]
else:
    module=".arraise"

# GET THE IMAGE, USE IMPORT MODULES TO LOAD A PICTURE AS A PY MODULE
svar=importlib.import_module(module,"pictures")
message = svar.image
print message

#create an AF_INET, STREAM socket (TCP)
try:
   #create an AF_INET, STREAM socket (TCP)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
   print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
   sys.exit();
print 'Socket Created'


#print 'Ip address of ' + host + ' is ' + remote_ip
remote_ip = '10.1.10.100'
port = 8675

#Connect to remote server
try:
   s.connect((remote_ip , port))
except socket.error, msg:
   print 'Failed to connect socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
   sys.exit();
print 'Socket Connected to ip ' + remote_ip


#Send picture data to remote server
try :
    #Send the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()

# NO EXITS, Everything worked
print 'Message send successfully'
print "message:",message
