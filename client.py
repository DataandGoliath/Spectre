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
def Connect():
    server=sys.argv[1]
    port=9876
    s=socket.socket()
    s.connect((server,int(port)))
    s.send(SHA256PK)
    a=s.recv(9999)
    if str(a)=="UID Free, assigning":
        print("Public Key assigned to client!")
        s.send("Test!")
        print(str(s.recv(64)))
        s.close()
    elif str(a)=="UID Claimed, pick a new one.":
        print("Public Key exists, regenerating")
        s.close()
        KeyGen()
        Connect()
Connect()
