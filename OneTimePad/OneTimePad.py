import random 

#generate random key length of message
def generateKey(length):
    return bytes([random.randint(0,255) for _ in range(length)])

#encrypt each character
def encrypt(message, key):
    encrypted = b''
    for i in range(len(message)):
        encrypted_byte = message[i] ^ key[i]
        encrypted += bytes([encrypted_byte])
    return encrypted

def decrypt(encrypted_message, key):
    decrypted = b''
    for i in range(len(encrypted_message)):
        decrypted_byte = encrypted_message[i] ^ key[i]
        decrypted += bytes([decrypted_byte])
    return decrypted

def main():
    message = "message to be encrypted" #add message here
    message_bytes = message.encode('utf-8')
    key = generateKey(len(message_bytes)) #key function above
    
    encrypted_message = encrypt(message_bytes, key)
    decrypted_message = decrypt(encrypted_message, key)
    
    print("plaintext: ", message)
    print("encrypted: ", encrypted_message)
    print("decrypted: ", decrypted_message.decode('utf-8'))
    