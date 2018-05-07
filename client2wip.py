import random
import math
import string
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto import Random
def KeyGen():
    global SHA256PK
    global privatekey
    global publickey
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    N=random.randint(1000,99999)
    code=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(N))
#code = 'nooneknows'
    key = RSA.generate(4096)
    privatekey = key.exportKey(passphrase=code, pkcs=8)
    publickey = key.publickey().exportKey()
#    print("PUBLIC KEY:\n"+str(publickey))
#    print("\n\nPRIVATE KEY:\n"+str(privatekey))
    h=SHA256.new()
    h.update(publickey)
    SHA256PK=h.hexdigest()
#    global SHA256PK
#    global publickey
#    global privatekey
#    print("\n\nPUBLIC KEY SHA256 HASH:\n"+SHA256PK())
KeyGen()
print("PUBLIC KEY:\n"+str(publickey))
print("\nPRIVATE KEY:\n"+str(privatekey))
print("\nUSERID:\n"+str(SHA256PK))
#Connect to server!
import socket
import sys
import time as t
global s
s=socket.socket()
def Signup():
    global UID
    global server
    global port
    global spk
    server=sys.argv[1]
    port=9876
    KeyGen()
    s.connect((server,int(port)))
    s.send("CHECK "+SHA256PK)
    valid=s.recv(len("INVALID"))
    if str(valid)=="VALID":
        KeyGen()
    elif str(valid)=="INVALID":
        s.send("REQUEST "+SHA256PK)
        good=s.recv(len("NOT ASSIGNED"))
        if good=="ASSIGNED":
            UID=SHA256PK
            s.send("REQUESTING SERVER PUBLIC KEY")
            spk=str(s.recv(9000))
            Login()
        elif good=="NOT ASSIGNED":
            print("ERROR IN ASSIGNMENT.")
            sys.exit(1)
            
def Login():
    global server
    global port
    global UID
    global spk
    server=sys.argv[1]
    port=9876
    s.connect((server,int(port)))
    s.send("LOGIN "+UID)
    accepted=s.recv(len("LOGIN ACCEPTED"))
    if accepted=="LOGIN ACCEPTED":
        print("Login accepted! (yay!)")
    elif accepted=="LOGIN DENIED":
        print("Welp something went wrong :(")
