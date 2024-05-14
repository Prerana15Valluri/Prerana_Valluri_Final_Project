import csv
from tkinter import messagebox, simpledialog


class Patient:
    def __init__(self, patient_id, visit_id, visit_time, visit_department, race, gender, ethnicity, age, zip_code,
                 insurance, chief_complaint, note_id, note_type):
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
                row['Race'], row['Gender'], row['Ethnicity'], row['Age'], row['Zip_code'],
                row['Insurance'], row['Chief_complaint'], row['Note_ID'], row['Note_type']
            )
            patients.append(patient)
    return patients


def write_patient_information_file(patients, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Patient_ID', 'Visit_ID', 'Visit_time', 'Visit_department', 'Race', 'Gender', 'Ethnicity', 'Age',
             'Zip_code', 'Insurance', 'Chief_complaint', 'Note_ID', 'Note_type'])
        for patient in patients:
            writer.writerow([patient.patient_id, patient.visit_id, patient.visit_time, patient.visit_department,
                             patient.race, patient.gender, patient.ethnicity, patient.age, patient.zip_code,
                             patient.insurance, patient.chief_complaint, patient.note_id, patient.note_type])


def retrieve_patient(patient_id):
    patients = read_patient_information_file("Project_patient_information.csv")
    for patient in patients:
        if patient.patient_id == patient_id:
            messagebox.showinfo("Retrieve Patient", f"Patient ID: {patient_id}\n"
                                                    f"Visit ID: {patient.visit_id}\n"
                                                    f"Visit Time: {patient.visit_time}\n"
                                                    f"Visit Department: {patient.visit_department}\n"
                                                    f"Race: {patient.race}\n"
                                                    f"Gender: {patient.gender}\n"
                                                    f"Ethnicity: {patient.ethnicity}\n"
                                                    f"Age: {patient.age}\n"
                                                    f"Zip Code: {patient.zip_code}\n"
                                                    f"Insurance: {patient.insurance}\n"
                                                    f"Chief Complaint: {patient.chief_complaint}\n"
                                                    f"Note ID: {patient.note_id}\n"
                                                    f"Note Type: {patient.note_type}")
            return
    messagebox.showerror("Error", f"Patient with ID {patient_id} not found.")


def add_patient():
    patient_id = simpledialog.askstring("Add Patient", "Enter Patient ID:")
    if patient_id:
        visit_id = simpledialog.askstring("Add Patient", "Enter Visit ID:")
        visit_time = simpledialog.askstring("Add Patient", "Enter Visit Time:")
        visit_department = simpledialog.askstring("Add Patient", "Enter Visit Department:")
        race = simpledialog.askstring("Add Patient", "Enter Race:")
        gender = simpledialog.askstring("Add Patient", "Enter Gender:")
        ethnicity = simpledialog.askstring("Add Patient", "Enter Ethnicity:")
        age = simpledialog.askinteger("Add Patient", "Enter Age:")
        zip_code = simpledialog.askstring("Add Patient", "Enter Zip Code:")
        insurance = simpledialog.askstring("Add Patient", "Enter Insurance:")
        chief_complaint = simpledialog.askstring("Add Patient", "Enter Chief Complaint:")
        note_id = simpledialog.askstring("Add Patient", "Enter Note ID:")
        note_type = simpledialog.askstring("Add Patient", "Enter Note Type:")

        # Create a new patient object
        new_patient = Patient(patient_id, visit_id, visit_time, visit_department, race, gender, ethnicity, age,
                              zip_code, insurance, chief_complaint, note_id, note_type)

        # Append the new patient to the existing patient list
        patients = read_patient_information_file("Project_patient_information.csv")
        patients.append(new_patient)

        # Write the updated patient list back to the CSV file
        write_patient_information_file(patients, "Project_patient_information.csv")

        messagebox.showinfo("Add Patient", f"Patient with ID: {patient_id} has been added.")


def remove_patient(patient_id):
    patients = read_patient_information_file("Project_patient_information.csv")
    removed = False
    for patient in patients:
        if patient.patient_id == patient_id:
            patients.remove(patient)
            removed = True
            break

    if removed:
        # Write the updated patient list back to the CSV file
        write_patient_information_file(patients, "Project_patient_information.csv")
        messagebox.showinfo("Remove Patient", f"Patient with ID: {patient_id} has been removed.")
    else:
        messagebox.showerror("Error", f"Patient with ID {patient_id} not found.")


def count_visits(date):
    patients = read_patient_information_file("Project_patient_information.csv")
    count = 0
    for patient in patients:
        if patient.visit_time == date:
            count += 1
    messagebox.showinfo("Count Visits", f"Number of visits on {date}: {count}")
