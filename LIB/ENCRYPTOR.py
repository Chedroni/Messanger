class ENCRYPTOR:
    def __init__(self):
        pass

    def encrypt_data(self, data: bytes, public_key: [int, int] = None) -> bytes:
        encrypted_data: bytes = b''

        for d in data:
            encrypted_data += d ^ 2

        return encrypted_data

    def decrypt_data(self, data: bytes, private_key: [int, int] = None) -> bytes:
        decrypted_data: bytes = b''

        for d in data:
            decrypted_data += d ^ 2

        return decrypted_data
