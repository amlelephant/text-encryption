from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def make_salt():
    return get_random_bytes(32)

def encrypt(password, salt, message):
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(message, AES.block_size))
    return cipher.iv + ciphered_data  # Include IV in the output

def decrypt(encrypted, password, salt):
    key = PBKDF2(password, salt, dkLen=32)
    iv = encrypted[:AES.block_size]  # Extract the IV from the encrypted data
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    deciphered_data = unpad(cipher.decrypt(
        encrypted[AES.block_size:]), AES.block_size)
    return deciphered_data

if __name__ == "__main__":
    
    salt = b'\x7f\xf5\x86)\xfd\xd5\x96P;\xe9\x1e\x9c\x16\x9c\x93\x8f0\xabF\x97\xdb\x1a5+\xe7\xaa\x0b\x9e\xd3g8\xc6'
    password = "password"
    message = b"secret"

    encrypted = encrypt(password, salt, message)
    print(encrypted)

    decrypted = decrypt(encrypted, password, salt)
    print(decrypted)
