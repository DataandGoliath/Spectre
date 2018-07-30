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
        if c.recv(64) == "SIGNUP":
            a=c.recv(64)
            PUBSHA=str(a)
            c.send("UID Free, assigning")
            f=open("claimeduids.txt","a")
            f.write(PUBSHA)
            f.close()
            print(str(c.recv(64)))
            b=c.recv(64)
            if b=="Requesting Server Public Key":
                s.send("TEST")
        elif c.recv(64) == "LOGIN":
            UID=c.recv(64)
            f=open("claimeduids.txt","r")
            uids=f.read()
            f.close()
            if UID in str(uids):
                c.send("Username Good.")
            else:
                c.send("Username Bad.")
    except:
        pass
