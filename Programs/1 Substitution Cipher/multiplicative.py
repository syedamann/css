#Multiplicative Cipher
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Multiplicative_encrypt(Plaintext, key):
    outText = []
    cryptText = []
    for eachLetter in Plaintext:
        if eachLetter in character:
            # index letters 
            index = character.index(eachLetter)
            # C = (P * K) mod 26
            crypting = (index * key) % 26
            cryptText.append(crypting)
            newLetter = character[crypting]
            outText.append(newLetter)
    return outText

def modInverse(key, numchar) :
  for x in range(1, numchar) :
    if ((key * x) % numchar == 1) :
      return x
  return 1

def Multiplicative_decrypt(plaintext, key):
  outText = []
  decryptText = []
  for eachLetter in plaintext:
    if eachLetter in character:
      # index letters
      index = character.index(eachLetter)
      # C = (P * K^-1) mod 26
      decrypt = (index * modInverse(key, 26)) % 26
      decryptText.append(decrypt)
      newLetter = character[decrypt]
      outText.append(newLetter)
  return outText

text = input ('Type text to encrypt: ')
plaintext = str(text.lower())
num = input('Type key between 0-25: ')
key = int(num)
ciphertext = Multiplicative_encrypt(plaintext, key)
print('Ciphertext:' , ciphertext) 
print('Decrypt Text:' ,*Multiplicative_decrypt(ciphertext, key))