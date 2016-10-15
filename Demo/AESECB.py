#Key: "This key is used"
#Text: (contains 5 blocks) "first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb"

from Crypto.Cipher import AES

# Encryption
aes_enc = AES.new('This key is used',AES.MODE_ECB)

block_text="first block1 ecbsecond block ecbfirst block1 ecbfourth block ecbfirst block1 ecb"
#Converted to ciphertext
cipher_text = aes_enc.encrypt(block_text)
#Converted to hex format
encoded_cipher=cipher_text.encode('hex')
print('encrypted message:')
print(encoded_cipher)

print('')

# Decryption
aes_dec = AES.new('This key is used', AES.MODE_ECB)
#Converted to plaintext
plain_text = aes_dec.decrypt(cipher_text)
print('decrypted message:') 
print(plain_text)
