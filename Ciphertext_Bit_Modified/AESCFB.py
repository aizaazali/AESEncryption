#InitialKey: "This key is used" (16 bytes)
#Initialization Vector (IV): "This is the IV12" (16 bytes)
#Text: "first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb" (80 bytes)
#The 1,3 and 5 blocks in the above text are same

from Crypto.Cipher import AES

# Encryption
aes_enc = AES.new('This key is used',AES.MODE_CFB,'This is the IV12')
block_text="first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb"
#Convert to cipher text
cipher_text = aes_enc.encrypt(block_text)
#Convert to hex format
encoded_cipher=cipher_text.encode('hex')
print('encrypted message:')
print(encoded_cipher)

print('')

# Decryption
aes_dec = AES.new('This key is used', AES.MODE_CFB,'This is the IV12')
#Convert to plaintext
plain_text = aes_dec.decrypt(cipher_text)
print('decrypted message:')
print(plain_text)

# Decryption after modifying firstbit of second block of ciphertext
cipher_text_new='2b0d24158d4e13ccba39fa1001b6f686959ac2c7c54ef8701a9022fe56191e668cff3b40d6e37bd5c079b153ed050b5086f87c1d2b63e57638d16e85cee01a649a80fe090178d079dc745cae4cc1137a'
#Decode hex format
decoded_cipher=cipher_text_new.decode('hex')
#Convert to plaintext
plain_text_new = aes_dec.decrypt(decoded_cipher)
print('new decrypted message:') 
print(plain_text_new)
