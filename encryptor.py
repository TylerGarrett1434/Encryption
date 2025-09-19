import argparse
from cryptography.fernet import Fernet

# Generate a new key and save to file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved as secret.key")

# Load existing key
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("[-] secret.key not found. Run 'generate-key' first.")
        exit()

# Encrypt a text message
def encrypt_text(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    print(encrypted.decode())

# Decrypt a text message
def decrypt_text(token, key):
    f = Fernet(key)
    decrypted = f.decrypt(token.encode()).decode()
    print(decrypted)

# Encrypt a file
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"[+] File encrypted → {filename}.enc")

# Decrypt a file
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    decrypted = f.decrypt(data)
    output_file = filename.replace(".enc", "")
    with open(output_file, "wb") as file:
        file.write(decrypted)
    print(f"[+] File decrypted → {output_file}")

# CLI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Encryption Tool")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("generate-key")

    enc_text = subparsers.add_parser("encrypt-text")
    enc_text.add_argument("message")

    dec_text = subparsers.add_parser("decrypt-text")
    dec_text.add_argument("token")

    enc_file = subparsers.add_parser("encrypt-file")
    enc_file.add_argument("filename")

    dec_file = subparsers.add_parser("decrypt-file")
    dec_file.add_argument("filename")

    args = parser.parse_args()
    if args.command == "generate-key":
        generate_key()
    else:
        key = load_key()
        if args.command == "encrypt-text":
            encrypt_text(args.message, key)
        elif args.command == "decrypt-text":
            decrypt_text(args.token, key)
        elif args.command == "encrypt-file":
            encrypt_file(args.filename, key)
        elif args.command == "decrypt-file":
            decrypt_file(args.filename, key)
        else:
            parser.print_help()
