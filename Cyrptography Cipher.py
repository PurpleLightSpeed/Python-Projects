import string

# Function to encrypt a message using Caesar cipher
# Message is the string to be encrypted, key is the number of positions to shift each letter
def caesar_encrypt(message, key):

    # Normalize the key to be within the range of 0-25
    shift= key % 26
    # Create a translation table for the Caesar cipher
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    # Convert the message to lowercase and translate it using the cipher
    encrypted_message = message.lower().translate(cipher)

    return encrypted_message

def caesar_decrypt(encrypted_message, key):

    shift = 26 - (key % 26)  # Reverse the shift for decryption
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    # Decrypt the message by translating it back using the cipher
    message = encrypted_message.translate(cipher)
    return message

message = input("Enter the message to encrypt: ")
key = int(input("Enter the key (shift value): "))

encrypted_message = caesar_encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")

# This code provides a simple implementation of the Caesar cipher for encryption and decryption.
# It uses a translation table to shift letters by a specified key value.
# The user can input a message and a key, and the program will output the encrypted and decrypted messages.
# Note: This implementation only works with lowercase letters and ignores non-letter characters.
