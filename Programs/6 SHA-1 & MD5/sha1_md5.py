import hashlib
# working of SHA1 
# Input string
message = input("Enter the message: ")
# converting to byte
message = message.encode()
# encoding GeeksforGeeks using md5 hash function 
result_sha1 = hashlib.sha1(message)
# printing the equivalent byte value.
print("\nThe byte equivalent of hash is (SHA1): ", end ="")
print(result_sha1.digest())
# printing the equivalent hex value.
print("\nThe hexadecimal equivalent of hash is (SHA1): ", end ="")
print(result_sha1.hexdigest())

# working of MD5 
# Input string
#message = input("Enter the message: ")
# converting to byte
#message = message.encode()
# encoding GeeksforGeeks using md5 hash function 
result_md5 = hashlib.md5(message)
# printing the equivalent byte value.
print("\nThe byte equivalent of hash is (MD5): ", end ="")
print(result_md5.digest())
# printing the equivalent hex value.
print("\nThe hexadecimal equivalent of hash is (MD5): ", end ="")
print(result_md5.hexdigest())