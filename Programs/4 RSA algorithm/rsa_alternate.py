import math

print("\n------------RSA------------")
message_str = input("\nEnter the message to be encrypted: ")
message = int(19161)
p = 3
q = 11
e = 7

n = p*q
phi = (p-1)*(q-1)

def encrypt(me):
    en = math.pow(me,e)
    c = int(en % n)
    print("Encrypted Message is: ", c)
    return c

def find_mod_inv(e,n):
    # d*e%phi=1
    for x in range(1,n):
        if((e*x) % phi==1):
            return x
    raise Exception('The modular inverse does not exist.')

def decrypt(c):
    de = math.pow(c,d)
    pt = int(de % n)
    print("Decrypted Message is: ", pt)
    return pt

print("Original Text Message is: ", message_str)
print("Original Message is: ", message)
c = encrypt(message)
d = find_mod_inv(e,n)
print("Public Key: \nn = {} \ne = {}".format(n, e))
print("Private key: \nd = {}".format(d))
pt = decrypt(c)