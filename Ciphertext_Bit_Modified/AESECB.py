#InitialKey: "This key is used" (16 bytes)
#Text: "first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb" (80 bytes)
#The 1,3 and 5 blocks in the above text are same

from Crypto.Cipher import AES

# Encryption
aes_enc = AES.new('This key is used',AES.MODE_ECB)
block_text="first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb"
#Convert to cipher text
cipher_text = aes_enc.encrypt(block_text)
#Convert to hex format
encoded_cipher=cipher_text.encode('hex')
print('encrypted message:')
print(encoded_cipher)

print('')

# Decryption
aes_dec = AES.new('This key is used', AES.MODE_ECB)
#Convert to plaintext
plain_text = aes_dec.decrypt(cipher_text)
print('decrypted message:') 
print(plain_text)

#Decryption after changing one bit of 2nd ciphertext block
aes_dec_new = AES.new('This key is used', AES.MODE_ECB)
cipher_text_new='600a6e8066ab090007aa11eec076a0dda0f7a22622c0ed276a342e69224b9178600a6e8066ab090007aa11eec076a0ddd281b4e264fd2b5ec448e06889144ae4600a6e8066ab090007aa11eec076a0dd'
#Decode hex format
decoded_cipher=cipher_text_new.decode('hex')
#Convert to plaintext
plain_text_new = aes_dec_new.decrypt(decoded_cipher)
print('new decrypted message:') 
print(plain_text_new)
