from Crypto.Cipher import DES
import os

def pad_data(data):
    """Pad the data to ensure it's a multiple of 8 bytes."""
    length = len(data)
    padding_length = 8 - (length % 8)
    return data + b'\0' * padding_length

def encrypt_data(key, data):
    """Encrypt the given data using DES."""
    des = DES.new(key, DES.MODE_ECB)
    padded_data = pad_data(data)
    return des.encrypt(padded_data)

def decrypt_data(key, data):
    """Decrypt the given data using DES."""
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(data)

def main():
    # Get the key from the user
    key = input("Enter the DES key (8 bytes): ").encode()

    # Check if the key is valid (8 bytes)
    if len(key) != 8:
        print("Invalid key length. Please enter an 8-byte key.")
        return

    filename = input("Enter the filename (plain.txt or cipher.txt): ")

    if filename.endswith('.txt'):
        # Read the file content
        with open(filename, 'rb') as file:
            data = file.read()

        # Determine whether to encrypt or decrypt
        action = input("Do you want to encrypt (E) or decrypt (D)? ").upper()

        if action == 'E':
            # Encrypt the data
            encrypted_data = encrypt_data(key, data)
            output_filename = filename.replace('.txt', '_encrypted.txt')
            with open(output_filename, 'wb') as out_file:
                out_file.write(encrypted_data)
            print(f"Encrypted data saved to {output_filename}")
        elif action == 'D':
            # Decrypt the data
            decrypted_data = decrypt_data(key, data)
            output_filename = filename.replace('.txt', '_decrypted.txt')
            with open(output_filename, 'wb') as out_file:
                out_file.write(decrypted_data)
            print(f"Decrypted data saved to {output_filename}")
        else:
            print("Invalid action selected.")
    else:
        print("Please enter a .txt file.")

if __name__ == "__main__":
    main()
