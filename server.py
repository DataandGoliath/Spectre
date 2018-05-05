import socket
import random as r
import sys
while True:
    s=socket.socket()
    try:
        s.bind(("0.0.0.0",9876))
    except:
        sys.exit(1)
    try:
        s.listen(5)
        c,a=s.accept()
        a=c.recv(64)
        PUBSHA=str(a)
        c.send("UID Free, assigning")
        print(str(c.recv(64)))
        c.send("Close")
    except:
        pass
