import csv
import tkinter as tk
from tkinter import messagebox, simpledialog
from user import authenticate_user
from patient import retrieve_patient, add_patient, remove_patient, count_visits

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Patient:
    def __init__(self, patient_id, visit_id, visit_time, visit_department, race, gender, ethnicity, age, zip_code, insurance, chief_complaint, note_id, note_type):
        self.patient_id = patient_id
        self.visit_id = visit_id
        self.visit_time = visit_time
        self.visit_department = visit_department
        self.race = race
        self.gender = gender
        self.ethnicity = ethnicity
        self.age = age
        self.zip_code = zip_code
        self.insurance = insurance
        self.chief_complaint = chief_complaint
        self.note_id = note_id
        self.note_type = note_type

def read_patient_information_file(file_path):
    patients = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patient = Patient(
                row['Patient_ID'], row['Visit_ID'], row['Visit_time'], row['Visit_department'],
                row['Race'], row['Gender'], row['Ethnicity'], int(row['Age']), row['Zip_code'],
                row['Insurance'], row['Chief_complaint'], row['Note_ID'], row['Note_type']
            )
            patients.append(patient)
    return patients

class Dashboard:
    def __init__(self, user):
        self.user = user
        self.root = tk.Tk()
        self.root.title("Dashboard")
        self.root.geometry("600x400")
        self.root.configure(bg="#add8e6")  # Light blue background color

        self.label_welcome = tk.Label(self.root, text=f"Welcome, {self.user.username}!", bg="#add8e6")  # Light blue label background
        self.label_welcome.pack()

        buttons_frame = tk.Frame(self.root, bg="#add8e6")
        buttons_frame.pack(expand=True, fill='both', padx=20, pady=20)

        if self.user.role in ["management"]:
            self.btn_generate_stats = tk.Button(buttons_frame, text="Generate Key Statistics", command=self.generate_statistics, bg="#0077cc", fg="white")  # Blue button with white text
            self.btn_generate_stats.grid(row=0, column=0, padx=10, pady=10)

        if self.user.role in ["admin"]:
            self.btn_count_visits = tk.Button(buttons_frame, text="Count Visits", command=self.count_visits, bg="#0077cc", fg="white")  # Blue button with white text
            self.btn_count_visits.grid(row=0, column=0, padx=10, pady=10)

        if self.user.role in ["clinician", "nurse"]:
            self.btn_retrieve_patient = tk.Button(buttons_frame, text="Retrieve Patient", command=self.retrieve_patient, bg="#0077cc", fg="white")  # Blue button with white text
            self.btn_retrieve_patient.grid(row=0, column=1, padx=10, pady=10)

            self.btn_add_patient = tk.Button(buttons_frame, text="Add Patient", command=self.add_patient, bg="#0077cc", fg="white")  # Blue button with white text
            self.btn_add_patient.grid(row=0, column=0, padx=10, pady=10)

            self.btn_remove_patient = tk.Button(buttons_frame, text="Remove Patient", command=self.remove_patient, bg="#0077cc", fg="white")  # Blue button with white text
            self.btn_remove_patient.grid(row=1, column=0, padx=10, pady=10)

            self.btn_count_visits = tk.Button(buttons_frame, text="Count Visits", command=self.count_visits, bg="#0077cc", fg="white")  # Blue button with white text
            self.btn_count_visits.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.btn_logout = tk.Button(self.root, text="Exit", command=self.log_out, bg="#ff6347", fg="white")  # Red button with white text
        self.btn_logout.pack()

    def generate_statistics(self):
        patients = read_patient_information_file("Project_patient_information.csv")
        race_counts = {}
        gender_counts = {}
        ethnicity_counts = {}
        insurance_counts = {}
        age_sum = 0
        age_count = 0

        for patient in patients:
            race_counts[patient.race] = race_counts.get(patient.race, 0) + 1
            gender_counts[patient.gender] = gender_counts.get(patient.gender, 0) + 1
            ethnicity_counts[patient.ethnicity] = ethnicity_counts.get(patient.ethnicity, 0) + 1
            insurance_counts[patient.insurance] = insurance_counts.get(patient.insurance, 0) + 1
            age_sum += patient.age
            age_count += 1

        average_age = age_sum / age_count if age_count > 0 else 0

        statistics = f"Race Counts: {race_counts}\n" \
                     f"Gender Counts: {gender_counts}\n" \
                     f"Ethnicity Counts: {ethnicity_counts}\n" \
                     f"Insurance Counts: {insurance_counts}\n" \
                     f"Average Age: {average_age:.2f}"

        messagebox.showinfo("Key Statistics", statistics)

    def retrieve_patient(self):
        patient_id = simpledialog.askstring("Retrieve Patient", "Enter Patient ID:")
        if patient_id:
            retrieve_patient(patient_id)

    def add_patient(self):
        add_patient()

    def remove_patient(self):
        patient_id = simpledialog.askstring("Remove Patient", "Enter Patient ID:")
        if patient_id:
            remove_patient(patient_id)

    def count_visits(self):
        date = simpledialog.askstring("Count Visits", "Enter Date (yyyy-mm-dd):")
        if date:
            count_visits(date)

    def log_out(self):
        self.root.destroy()
        root = tk.Tk()
        ui = UI(root)
        root.mainloop()

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinical Data Warehouse")
        self.root.geometry("400x300")

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        self.btn_login = tk.Button(root, text="Login", command=self.login)
        self.btn_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        action = "login"
        user = authenticate_user(username, password, action)
        if user:
            self.root.destroy()
            Dashboard(user)
        else:
            messagebox.showerror("Error", "Invalid username or password")

def main():
    root = tk.Tk()
    ui = UI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
