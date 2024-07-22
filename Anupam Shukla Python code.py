               #HOSPITAL MANAGEMENT SYSTEM

class Patient:
    # patient constructor
    def __init__(self, patient_id, name, age, gender, disease, doctor_id=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.doctor_id = doctor_id

    def __str__(self):
        return f"Patient [ID={self.patient_id}, Name={self.name}, Age={self.age}, Gender={self.gender}, Disease={self.disease}, Doctor ID={self.doctor_id}]"


class Doctor:
    #doctor constructor
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor [ID={self.doctor_id}, Name={self.name}, Specialization={self.specialization}]"


class HospitalManagementSystem:
    #hospital managemnt system constructor
    def __init__(self):
        self.patients = {}
        self.doctors = {}

    # Patient Management
    def add_patient(self, patient):
        if patient.patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient.patient_id} already exists.")
        self.patients[patient.patient_id] = patient

    def update_patient(self, patient_id, **kwargs):
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        for key, value in kwargs.items():
            setattr(self.patients[patient_id], key, value)

    def delete_patient(self, patient_id):
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        del self.patients[patient_id]

    # Doctor Assignment
    def add_doctor(self, doctor):
        if doctor.doctor_id in self.doctors:
            raise ValueError(f"Doctor with ID {doctor.doctor_id} already exists.")
        self.doctors[doctor.doctor_id] = doctor

    def assign_doctor_to_patient(self, patient_id, doctor_id):
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        if doctor_id not in self.doctors:
            raise ValueError(f"Doctor with ID {doctor_id} does not exist.")
        self.patients[patient_id].doctor_id = doctor_id

    # Reporting
    def get_patients_by_doctor(self, doctor_id):
        if doctor_id not in self.doctors:
            raise ValueError(f"Doctor with ID {doctor_id} does not exist.")
        return [patient for patient in self.patients.values() if patient.doctor_id == doctor_id]

    def __str__(self):
        return f"HospitalManagementSystem with {len(self.patients)} patients and {len(self.doctors)} doctors."


def main():
    system = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Update Patient")
        print("3. Delete Patient")
        print("4. Add Doctor")
        print("5. Assign Doctor to Patient")
        print("6. Generate Report by Doctor")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = int(input("Enter Patient ID: "))
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            gender = input("Enter Patient Gender: ")
            disease = input("Enter Patient Disease: ")
            try:
                system.add_patient(Patient(patient_id, name, age, gender, disease))
                print("Patient added successfully.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            patient_id = int(input("Enter Patient ID to Update: "))
            name = input("Enter New Name (leave blank to keep current): ")
            age = input("Enter New Age (leave blank to keep current): ")
            gender = input("Enter New Gender (leave blank to keep current): ")
            disease = input("Enter New Disease (leave blank to keep current): ")
            update_data = {}
            if name:
                update_data['name'] = name
            if age:
                update_data['age'] = int(age)
            if gender:
                update_data['gender'] = gender
            if disease:
                update_data['disease'] = disease
            try:
                system.update_patient(patient_id, **update_data)
                print("Patient updated successfully.")
            except ValueError as e:
                print(e)

        elif choice == '3':
            patient_id = int(input("Enter Patient ID to Delete: "))
            try:
                system.delete_patient(patient_id)
                print("Patient deleted successfully.")
            except ValueError as e:
                print(e)

        elif choice == '4':
            doctor_id = int(input("Enter Doctor ID: "))
            name = input("Enter Doctor Name: ")
            specialization = input("Enter Doctor Specialization: ")
            try:
                system.add_doctor(Doctor(doctor_id, name, specialization))
                print("Doctor added successfully.")
            except ValueError as e:
                print(e)

        elif choice == '5':
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            try:
                system.assign_doctor_to_patient(patient_id, doctor_id)
                print("Doctor assigned to patient successfully.")
            except ValueError as e:
                print(e)

        elif choice == '6':
            doctor_id = int(input("Enter Doctor ID: "))
            try:
                patients = system.get_patients_by_doctor(doctor_id)
                if not patients:
                    print("No patients assigned to this doctor.")
                else:
                    print(f"Patients assigned to Doctor ID {doctor_id}:")
                    for patient in patients:
                        print(patient)
            except ValueError as e:
                print(e)

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
