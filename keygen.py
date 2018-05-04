import random
import math
import string
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
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
print("PUBLIC KEY:\n"+str(publickey))
print("\n\nPRIVATE KEY:\n"+str(privatekey))
h=SHA256.new()
h.update(publickey)
print("\n\nPUBLIC KEY SHA256 HASH:\n"+h.hexdigest())
#Only 22 lines? Wow. "Encryption is easy!" --No one, ever
