from cryptography.fernet import Fernet

# Keeping secrets safe!
class PasswordManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password).decode()

if __name__ == "__main__":
    manager = PasswordManager()
    secret = "MySuperSecretPassword123"
    
    encrypted = manager.encrypt_password(secret)
    print(f"Locked: {encrypted}")
    
    decrypted = manager.decrypt_password(encrypted)
    print(f"Unlocked: {decrypted}")
    print("\nBuddy, in a real app, save the 'self.key' securely!")
