if __name__ == '__main__':
 
    # Both the persons will be agreed upon the
    # public keys G and P
    # A prime number P is taken
    P = int(input("Enter first Prime Number P: "))
    # A primitive root G is taken
    G = int(input("Enter Second Prime Number G: "))
    # Alice will choose the private key a
    a = int(input("Enter private key a for Alice: "))
    # Bob will choose the private key b
    b = int(input("Enter private key b for Bob: "))

    print()
    print('The Value of P is :%d'%(P))
    print('The Value of G is :%d'%(G))

    print('The Private Key a for Alice is :%d'%(a))
    # gets the generated key
    x = int(pow(G,a,P)) 
     
    print('The Private Key b for Bob is :%d'%(b))
    # gets the generated key
    y = int(pow(G,b,P)) 
      
    # Secret key for Alice
    ka = int(pow(y,a,P))
     
    # Secret key for Bob
    kb = int(pow(x,b,P))
     
    print('Secret key for the Alice is : %d'%(ka))
    print('Secret Key for the Bob is : %d'%(kb))

"""
Input:
Enter first Prime Number P: 23
Enter Second Prime Number G: 7
Enter private key a for Alice: 2
Enter private key b for Bob: 1
"""