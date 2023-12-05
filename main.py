def text_to_binary(text):
    binary_result = ''
    for char in text:
        # Convert each character in the text to its binary representation
        binary_result += format(ord(char), '08b') + ' '
    return binary_result

def vigenere_encrypt(plaintext, key):
    encrypted_text = ''
    key_index = 0

    for char in plaintext:
        # XOR operation on the binary representation of characters
        encrypted_char = chr(ord(char) ^ ord(key[key_index]))
        encrypted_text += encrypted_char

        # Move to the next key character
        key_index = (key_index + 1) % len(key)

        # Output the encryption process for each character
        print(f"Encrypting '{char}' with '{key[key_index]}': "
              f"{format(ord(char), '08b')} XOR {format(ord(key[key_index]), '08b')} = "
              f"{format(ord(encrypted_char), '08b')} ('{encrypted_char}')")

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ''
    key_index = 0

    for char in ciphertext:
        # XOR operation on the binary representation of characters
        decrypted_char = chr(ord(char) ^ ord(key[key_index]))
        decrypted_text += decrypted_char

        # Move to the next key character
        key_index = (key_index + 1) % len(key)

        # Output the decryption process for each character
        print(f"Decrypting '{char}' with '{key[key_index]}': "
              f"{format(ord(char), '08b')} XOR {format(ord(key[key_index]), '08b')} = "
              f"{format(ord(decrypted_char), '08b')} ('{decrypted_char}')")

    return decrypted_text

if __name__ == "__main__":
    # Input plaintext and key from the user
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    # Check if the key is empty
    if not key:
        print("Key cannot be empty.")
    else:
        # Encryption
        print("\nEncryption Process:")
        encrypted_text = vigenere_encrypt(plaintext, key)
        print("\nEncrypted Text:", encrypted_text)
        print("Binary:", text_to_binary(encrypted_text))

        # Decryption
        print("\nDecryption Process:")
        decrypted_text = vigenere_decrypt(encrypted_text, key)
        print("\nDecrypted Text:", decrypted_text)
        print("Binary:", text_to_binary(decrypted_text))
