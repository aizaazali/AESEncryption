#InitialKey: "This key is used" (16 bytes)
#Initialization Vector (IV): "This is the IV12" (16 bytes)
#Text: "first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb" (80 bytes)
#The 1,3 and 5 blocks in the above text are same

from Crypto.Cipher import AES

# Encryption
aes_enc = AES.new('This key is used',AES.MODE_OFB,'This is the IV12')
block_text="first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb"
#Convert to cipher text
cipher_text = aes_enc.encrypt(block_text)
#Convert to hex format
encoded_cipher=cipher_text.encode('hex')
print('encrypted message:')
print(encoded_cipher)

print('')

# Decryption
aes_dec = AES.new('This key is used', AES.MODE_OFB,'This is the IV12')
#Convert to plaintext
plain_text = aes_dec.decrypt(cipher_text)
print('decrypted message:') 
print(plain_text)

# Decryption after modifying firstbit of second block of ciphertext
cipher_text_new='2bfa77a98058f7c3dc7080a9165e24814617e791c67e93fae7ff1ccf5a185f2fc1910d8bc93019ddd4e1b9a30e314d408294f89ffd045b6d31b8850869b75f024b5953a23841e38af913772ebfd8fe76'
#Decode hex format
decoded_cipher=cipher_text_new.decode('hex')
#Convert to plaintext
plain_text_new = aes_dec.decrypt(decoded_cipher)
print('new decrypted message:') 
print(plain_text_new)
