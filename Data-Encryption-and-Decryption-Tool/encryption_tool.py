import os
import base64

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption
)

def generate_aes_key():
    return AESGCM.generate_key(bit_length=256)


def aes_encrypt(message, key):
    aes = AESGCM(key)

    nonce = os.urandom(12)

    encrypted_data = aes.encrypt(
        nonce,
        message.encode(),
        None
    )

    result = nonce + encrypted_data

    return base64.b64encode(result).decode()


def aes_decrypt(encrypted_message, key):
    try:
        data = base64.b64decode(encrypted_message)

        nonce = data[:12]
        encrypted_data = data[12:]

        aes = AESGCM(key)

        decrypted_data = aes.decrypt(
            nonce,
            encrypted_data,
            None
        )

        return decrypted_data.decode()

    except Exception:
        return "Decryption failed."

def generate_rsa_keys():

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key

def rsa_encrypt(message, public_key):

    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.b64encode(encrypted).decode()

def rsa_decrypt(encrypted_message, private_key):

    try:

        encrypted = base64.b64decode(encrypted_message)

        decrypted = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()
                ),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return decrypted.decode()

    except Exception:
        return "Decryption failed."

print("=" * 50)
print("       DATA ENCRYPTION AND DECRYPTION TOOL")
print("=" * 50)

print("\nSelect Encryption Algorithm")
print("1. AES")
print("2. RSA")

choice = input("\nEnter your choice (1/2): ")

message = input("\nEnter a test message: ")

if choice == "1":

    print("\nGenerating AES-256 key...")

    aes_key = generate_aes_key()

    encrypted_message = aes_encrypt(
        message,
        aes_key
    )

    print("\nEncrypted Message:")
    print(encrypted_message)

    decrypted_message = aes_decrypt(
        encrypted_message,
        aes_key
    )

    print("\nDecrypted Message:")
    print(decrypted_message)

elif choice == "2":

    print("\nGenerating RSA-2048 key pair...")

    private_key, public_key = generate_rsa_keys()

    encrypted_message = rsa_encrypt(
        message,
        public_key
    )

    print("\nEncrypted Message:")
    print(encrypted_message)

    decrypted_message = rsa_decrypt(
        encrypted_message,
        private_key
    )

    print("\nDecrypted Message:")
    print(decrypted_message)


else:

    print("\nInvalid choice.")