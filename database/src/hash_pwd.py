from lib.json_helper import read_json,write_json
import hashlib
import json
import random
import string
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    # # Load the user data from the JSON file
    # users = read_json("database/data/users.json")
    # # Update each user with a new password
    # for user in users:
    #     user['password'] = generate_password()
    #     print(f"Generated new password for {user['username']}: {user['password']}")
    # # Save the updated user data to a new JSON file
    # output_file = 'database/data/users_with_passwords.json'
    # write_json(output_file, users)
    # print(f"Updated user data with passwords saved to {output_file}")
    users_pwd = read_json("database/data/users_with_passwords.json")
    for user in users_pwd:
        user['password_hash'] = hash_password(user['password'])
        print(f"Hashed password for {user['username']}: {user['password']}: {user['password_hash']}")
    output_file = 'database/data/users_with_hashed_passwords.json'
    write_json(output_file, users_pwd)