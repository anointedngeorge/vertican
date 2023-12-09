import random
import string

def generateUniqueId():
    # Generate 6 random numbers
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
    # Generate 3 random capital alphabets
    random_alphabets = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    # Combine numbers and alphabets with a hyphen
    unique_id = f"{random_numbers}-{random_alphabets}"
    return unique_id


def generateUniqueOrderId():
    # Generate 6 random numbers
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
    # Generate 3 random capital alphabets
    random_alphabets = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
    # Combine numbers and alphabets with a hyphen
    unique_id = f"{random_numbers}-{random_alphabets}"
    return unique_id