#InitialKey: "This key is used" (16 bytes)
#ModifiedKey: "Dhis key is used" (16 bytes)
#Initialization Vector (IV): "This is the IV12" (16 bytes)
#Text: "first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb" (80 bytes)
#The 1,3 and 5 blocks in the above text are same

from Crypto.Cipher import AES

# Encryption
aes_enc = AES.new('This key is used',AES.MODE_OFB,'This is the IV12')
block_text="first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb"
#Converted to ciphertext
cipher_text = aes_enc.encrypt(block_text)
#Converted to hex
encoded_cipher=cipher_text.encode('hex')
print('encrypted message:')
print(encoded_cipher)

print('')

# Decryption using original key
aes_dec = AES.new('This key is used', AES.MODE_OFB,'This is the IV12')
#Convert to plaintext using original key
plain_text = aes_dec.decrypt(cipher_text)
print('decrypted message:') 
print(plain_text)

# Decryption using new key
aes_dec_new = AES.new('Dhis key is used', AES.MODE_OFB,'This is the IV12')
#Convert to plaintext using new key
plain_text_new = aes_dec_new.decrypt(cipher_text)
print('decrypted message with new key:') 
print(plain_text_new)
