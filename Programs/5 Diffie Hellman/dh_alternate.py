#implementation of Diffie Hellman key exchange algorithm
#function to calculate
def cal(a,b,P):
    if (b == 1):
        return a
    else:
        return ((pow(a, b)) % P)
P = int(input("Enter the prime number :"))
G = int(input("Enter the primitve root for pervious prime number :"))
e=0
if(G>=P):
    print("G can't be greater than P")
    e=1
if(e==0):
    x = int(input("Enter the secret key x:"))
    a = cal(G, x, P)
    print("The number shared is ",a)
    y = int(input("Enter the secret key y:"))
    b = cal(G, y, P)
    print("The number shared is ",b)
    #a and b are exchanged and the following values are calculated
    k1 = cal(b, x, P)
    k2 = cal(a, y, P)
    print("The value of K1 is :", k1)
    print("The value of K2 is :", k2)

"""
Input:
Enter the prime number :23
Enter the primitve root for pervious prime number :9
Enter the secret key x:4
The number shared is  6
Enter the secret key y:7
The number shared is  4
The value of K1 is : 3
The value of K2 is : 3
"""