from random import randint
N = 23
G = 9
print('The Value of P is :%d'%(N))
print('The Value of G is :%d'%(G))
a = 4
print('The Private Key a for Alice is :%d'%(a))

x = int(pow(G,a,N))
b = 3
print('The Private Key b for Bob is :%d'%(b))
y = int(pow(G,b,N))
# Secret key for Alice
k1 = int(pow(y,a,N))
# Secret key for Bob
k2 = int(pow(x,b,N))
print('Secret key for the Alice is : %d'%(k1))
print('Secret Key for the Bob is : %d'%(k2))
if(k1==k2):
    print("Key Exchange Successful")
else:
    print("Key Exchange Unsuccessful")
