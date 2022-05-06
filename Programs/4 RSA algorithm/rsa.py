from decimal import Decimal

def gcd (a, b):
  temp = 0
  while (1):
    temp = a%b
    if temp == 0:
      return b
    a = b
    b = temp
#input variables
p = int(input("Enter p: "))
q = int(input("Enter q: "))
message = int(input("Enter message: "))
#calculate n
n = p*q
#calculate totient
phi = (p-1)*(q-1)
#calculate e
for e in range(2,phi):
    if gcd(e,phi)==1:
        break

for i in range(1,10):
    x = 1 + i*phi
    if x%e == 0:
        d = int(x/e)
        break

local_cipher = Decimal(0)
local_cipher = pow(message,e)
cipher_text = local_cipher%n

decrypt_t = Decimal(0)
decrypt_t = pow(cipher_text,d)
decrypted_text = decrypt_t%n

print('\nn = '+str(n))
print('e = '+str(e))
print('message = '+str(message))
print('phi = '+str(phi))
print('d = '+str(d))
print('\ncipher text = '+str(cipher_text))
print('decrypted text = '+str(decrypted_text))

"""
Input: 
Enter p: 11
Enter q: 3
Enter message: 12
"""