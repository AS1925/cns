from Crypto.Cipher import DES
key=b'secret_k'
msg=b'Hello123'
cipher=DES.new(key,DES.MODE_ECB)
ct=cipher.encrypt(msg)
pt=cipher.decrypt(ct)
print("Cipher text:",ct)
print("decrypted:",pt)
import string

letters = string.ascii_letters
key = 4

text = input("Enter text: ")

# Encrypt
cipher = ''.join(
    letters[(letters.index(c)+key) % len(letters)] if c in letters else c
    for c in text
)

# Decrypt
plain = ''.join(
    letters[(letters.index(c)-key) % len(letters)] if c in letters else c
    for c in cipher
)

print("Cipher Text:", cipher)
print("Recovered Text:", plain)
