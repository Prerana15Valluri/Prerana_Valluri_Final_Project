import csv
from datetime import datetime

def log_usage(username, role, action, status):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('Usage_Statistics.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, role, action, timestamp, status])

