'''def encryptDecrypt(inpString):
    xorKey='H'
    length=len(inpString)
    for i in range(length):
        inpString=(inpString[:i]+chr(ord(inpString[i])^ord(xorKey))+inpString[i+1:]);
        print(inpString[i],end=' ')
    return inpString
if __name__=='__main__':
    sampleString="Hello World"
    print("encrypted String:", end='')
    sampleString=encryptDecrypt(sampleString)
    print("\n")
    print("decrypted String:",end='')
    encryptDecrypt(sampleString)'''
from Crypto.Cipher import DES
def pad(text):
    while len(text)%8!=0:
        text+=b' '
    return text
def encrypt(key,plaintext):
    cipher=DES.new(key,DES.MODE_ECB)
    padded_text=pad(plaintext)
    ciphertext=cipher.encrypt(padded_text)
    return ciphertext
def decrypt(key,ciphertext):
    cipher=DES.new(key,DES.MODE_ECB)
    padded_text=cipher.decrypt(ciphertext)
    plaintext=padded_text.rstrip(b' ')
    return plaintext
key=b'secretke'
plaintext=b'This is a secret message'
ciphertext=encrypt(key,plaintext)
decrypted_text=decrypt(key,ciphertext)
print('Plaintext:',plaintext)
print('Ciphertext:',ciphertext)
print('Decrypted text:',decrypted_text)
                   
        
