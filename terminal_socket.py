#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/sc/.spyder2/.temp.py
"""

# TEST OF PI C 884K004 communication via TCP/IP

import time
import socket
import sys
WAIT_TIME_UNIT=0.01
host="192.168.3.211"
port=101



print "connected"
"""while True:
    userstr = sys.stdin.readline()
    if userstr.startswith('exit'):
        break
    #command=userstr.strip('\n\r')
    command=userstr.strip('\n\r')+'\n\r'##userstr+chr(13)
    print "sending:", command
    s.write(command+chr(13)+chr(10))
    #time.sleep(1)
    buf = s.read(10000)
    print "answer:", buf

s.close()
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
last_comm_timeout = False
print "Connecting to Host", host, ", Port", port
try:
    sock.setblocking(1)
except:
    pass
try:
    sock.connect((host, port))
except Exception as e:
    print "Exception occured while connecting"
    print e.__class__
    print e
    connected = False
else:
    print "Success."
    connected = True
    sock.setblocking(0)
print connected
while True:
   userstr = sys.stdin.readline()
   if userstr.startswith('exit'):
       break
   command=userstr.strip('\n\r')
   print "sending:", command
   sock.send(command+'\r')
   time.sleep(0.1)
   resp = sock.recv(4096)
   print "answer:", resp
sock.close()

    
def communicate(self, command, timeout=2.0):
    # send command
    with self.commlock:
        #print "communicate called"
        try:
            self.sock.send(command)
        except socket.error:
            self.connected = False
        # get an answer
        resp = ""
        try:
            resp += self.sock.recv(10000)
        except socket.error:
            pass
        tstart = time.time()
        tend = tstart
        # really wait (block!) until end-of-line character is reached
        while( (len(resp)==0 or resp[-1]!='\n') and tend-tstart<timeout):
            #print "Delay!"
            try:
                resp += self.sock.recv(10000)
            except socket.error:
                pass
            time.sleep(WAIT_TIME_UNIT)
            tend = time.time()
        self.last_comm_timeout = (tend-tstart>=timeout)
        #print resp
        return resp
