#Random Dice Role Function
import random
# Provides an array of string constants for letters, digits, and punctuation
import string
def generate_password(length: int = 16):
    #concatenate letters, digits, and punctuation
    alphabets = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabets) for i in range(length))
    return password

password = generate_password()
print(f"Generated Password: {password}")
