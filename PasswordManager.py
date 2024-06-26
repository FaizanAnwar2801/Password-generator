import random
import json
import string

class PasswordManager:
    def __init__(self):
        self.passwords = []
    
    # Function to generate random passwords

    def generate_password(self, length="", level=""): 
        
        characters = string.ascii_letters + string.digits + string.punctuation
        if level == "low":
            length = 6
        elif level == "medium":
            length = 10
        elif level == "high":
            length = 14
        password = "".join(random.choice(characters) for i in range(length))
        return password
    
    # Function to store password in a file named as passwords.json 
    
    def store_password(self, service, username, password):
        entry = {
            "service": service,
            "username": username,
            "password": password
        }
        self.passwords.append(entry)
        with open("passwords.json", "w") as f:
            json.dump(self.passwords, f)
    
    # Function to retrive and return username and password from stored in the file "passwords.json"  

    def retrieve_password(self, service):

        with open("passwords.json", "r") as f:
            data = json.load(f)
        for entry in data:
            if entry["service"] == service:
                return entry["username"], entry["password"]
        return None
