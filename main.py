from cryptography.fernet import Fernet                  # pip install cryptography

key = Fernet.generate_key()     ## key generation
with open('private.key', 'wb') as filekey:              # string the key in a file
    filekey.write(key)

with open('private.key', 'rb') as filekey:              # opening the key
    key = filekey.read()

fernet = Fernet(key)                                    # using the generated key
with open('example-data.csv', 'rb') as file:                     # opening the original file to encrypt
    original = file.read()

encrypted = fernet.encrypt(original)                    # encrypting the file
with open('example-data-encrypted.csv', 'wb') as encrypted_file: # opening the file in write mode and
    encrypted_file.write(encrypted)                     # writing the encrypted data

fernet = Fernet(key)                                    # using the key
with open('example-data-encrypted.csv', 'rb') as enc_file:       # opening the encrypted file
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)                   # decrypting the file
with open('example-data-decrypted.csv', 'wb') as dec_file:       # opening the file in write mode and
    dec_file.write(decrypted)                           # writing the decrypted data