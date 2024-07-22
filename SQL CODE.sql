-- Create Doctors Table
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100)
);

-- Create Patients Table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(100),
    doctor_id INT,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Insert dummy data into Doctors Table
INSERT INTO Doctors (doctor_id, name, specialization) VALUES
(1, 'Dr. Mayank Sharma', 'Cardiology'),
(2, 'Dr. Aditya Verma', 'Neurology'),
(3, 'Dr. Anurag Gupta', 'Orthopedics'),
(4, 'Dr. Neha Singh', 'Pediatrics'),
(5, 'Dr. Priya Menon', 'Dermatology'),
(6, 'Dr. Rahul Desai', 'Orthopedics'),
(7, 'Dr. Sneha Patel', 'Cardiology'),
(8, 'Dr. Kiran Rao', 'Neurology'),
(9, 'Dr. Ritu Kapoor', 'Pediatrics'),
(10, 'Dr. Amit Bhardwaj', 'Dermatology');

-- Insert dummy data into Patients Table, including some with no assigned doctor
INSERT INTO Patients (patient_id, name, age, gender, disease, doctor_id) VALUES
(101, 'Aarav Mehta', 30, 'Male', 'Flu', 4),
(102, 'Ananya Roy', 25, 'Female', 'Cold', 2),
(103, 'Vikram Kumar', 40, 'Male', 'Migraine', 3),
(104, 'Sanjana Iyer', 50, 'Female', 'Diabetes', 1),
(105, 'Rohan Das', 45, 'Male', 'Hypertension', NULL), -- No doctor assigned
(106, 'Ishita Bansal', 35, 'Female', 'Asthma', 6),
(107, 'Akshay Nair', 28, 'Male', 'Allergy', 8),
(108, 'Kavya Joshi', 22, 'Female', 'Fracture', 9),
(109, 'Devika Sen', 55, 'Female', 'Arthritis', 5),
(110, 'Aman Sharma', 60, 'Male', 'Heart Disease', 10),
(111, 'Meera Chaudhary', 32, 'Female', 'Back Pain', 3),
(112, 'Nikhil Gupta', 27, 'Male', 'Headache', 2),
(113, 'Preeti Mishra', 38, 'Female', 'Obesity', 1),
(114, 'Arjun Yadav', 20, 'Male', 'Allergy', 5),
(115, 'Rekha Reddy', 48, 'Female', 'Asthma', 6),
(116, 'Vishal Rao', 42, 'Male', 'Hypertension', 7),
(117, 'Sonal Kapoor', 33, 'Female', 'Migraine', 8),
(118, 'Rahul Jain', 25, 'Male', 'Cold', 9),
(119, 'Swati Arora', 29, 'Female', 'Flu', 10),
(120, 'Kabir Khanna', 36, 'Male', 'Diabetes', 4),
(121, 'Sneha Singh', 40, 'Female', 'Allergy', NULL), -- No doctor assigned
(122, 'Amit Mishra', 50, 'Male', 'Diabetes', 1); 


select * from Doctors;
select * from Patients;

-- Problem 1 solution=>to find the total number of patients assigned to each doctor.
SELECT doctor_id, COUNT(*) AS total_patients
FROM Patients
GROUP BY doctor_id;

-- Problem 2 solution=>to find the names of doctors and the total number of patients assigned to them.
SELECT d.name AS doctor_name, COUNT(p.patient_id) AS total_patients
FROM Doctors d
LEFT JOIN Patients p ON d.doctor_id = p.doctor_id
GROUP BY d.doctor_id, d.name;

-- Problem 3 solution=>to find the names of patients who have not been assigned a doctor.
SELECT name AS patient_name
FROM Patients
WHERE doctor_id IS NULL;

-- Problem 4 solution=>to find the specializations of doctors who have more than 10 patients assigned.
SELECT d.specialization
FROM Doctors d
JOIN Patients p ON d.doctor_id = p.doctor_id
GROUP BY d.doctor_id, d.specialization
HAVING COUNT(p.patient_id) > 10;

-- Problem 5 solution=>to find the patient names and their corresponding diseases for patients assigned to a specific doctor.


SELECT p.name AS patient_name, p.disease
FROM Patients p
WHERE p.doctor_id = 1;

SELECT p.name AS patient_name, p.disease
FROM Patients p
WHERE p.doctor_id = 3;


