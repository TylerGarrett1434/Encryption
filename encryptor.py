pip install cryptography
from cryptography.fernet import Fernet

def generate_key():
    key=Fernet.generate.key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret_key", "rb").read()

def encrypt_message(message,key):
    f=Fernet(key)
    encrypted=f.encrypt(message.encode())
    return encrypted

def encrypt_file(filename, key):
    f=Fernet(key)
    with open(filename,"rb") as file:
        data=file.read()
    encrypted=f.encrypt(date)
    file.write(encrypted)

def decrypt_message(encrypted,key):
    f=Fernet(key)
    decrypted=f.decrypt(encrypted).decode()
    return decrypted

def decrypt_file(filename, key):
    f=Fernet(key)
    with open(filename, "rb") as file:
        data=file.read()
    decrypted=f.decrypt(data)
    with open(filename.replace(".enc", ""),"wb") as file:
        file.write(decrypted)




if _name_="_main_":
key=load_key()
msg="Brains Before Brawn"
encrypted=encrypt_message(msg,key)
print("Encrypted:", encrypted)


decrypted=decrypt_message(encrypted, key)
print("Decrypted:", decrypted)
