import csv
from Usage_Statistics import log_usage

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

def read_credentials_file(file_path):
    users = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = User(row['username'], row['password'], row['role'])
            users.append(user)
    return users

def authenticate_user(username, password, action):
    users = read_credentials_file("Project_credentials.csv")
    for user in users:
        if user.username == username and user.password == password:
            # Log successful login attempt
            if action == "login":
                log_usage(username, user.role, "Login", "Successful")
            elif action == "add_patient":
                log_usage(username, user.role, "Add Patient", "Successful")
            elif action == "retrieve_patient":
                log_usage(username, user.role, "Retrieve Patient", "Successful")
            elif action == "remove_patient":
                log_usage(username, user.role, "Remove Patient", "Successful")
            elif action == "count_visits":
                log_usage(username, user.role, "Count Visits", "Successful")
            elif action == "generate_statistics":
                log_usage(username, user.role, "Generate Statistics", "Successful")
            return user
    # Log failed login attempt
    log_usage(username, "", "Login", "Failed")
    return None
