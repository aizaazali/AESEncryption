#InitialKey: "This key is used" (16 bytes)
#Initialization Vector (IV): "This is the IV12" (16 bytes)
#Text: "first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb" (80 bytes)
#The 1,3 and 5 blocks in the above text are same

from Crypto.Cipher import AES

# Encryption
aes_enc = AES.new('This key is used',AES.MODE_CBC,'This is the IV12')

block_text="first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb"
#Convert to cipher text
cipher_text = aes_enc.encrypt(block_text)
#Convert to hex format
encoded_cipher=cipher_text.encode('hex')
print('encrypted message:')
print(encoded_cipher)

print('')

# Decryption
aes_dec = AES.new('This key is used', AES.MODE_CBC,'This is the IV12')
#Convert to plaintext
plain_text = aes_dec.decrypt(cipher_text)
print('decrypted message:') 
print(plain_text)

# Decryption after modifying firstbit of second block of ciphertext
cipher_text_new='3a0cb825e1fb99f5f12d1c4c2e2b3cab12f094233b296035a76832e4e1303936ce5de6faa4460b0ca767191177ec155e6d5e7130e2a60564ed2f79494c4d1176e03e4cbc9913a084653a9b6a9febefce'
#Decode to hex
decoded_cipher=cipher_text_new.decode('hex')
#Convert to plaintext
plain_text_new = aes_dec.decrypt(decoded_cipher)
print('new decrypted message:') 
print(plain_text_new)
