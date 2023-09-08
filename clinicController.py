from Models import *


class clinicController:
    def __init__(self):
        self.allPatients = []
        self.allDoctors = []
        self.allConsultations = []

    def newPatient(self):
        patientFile = open("Patient.txt", "r")
        for line in patientFile:
            data = line.strip().split(",")
            paFirstname = data[0]
            paLastname = data[1]
            aPatient = Patient(paFirstname, paLastname)
            self.allPatients.append(aPatient)

    def newDoctor(self):
        doctorFile = open("Doctor.txt", "r")
        for line in doctorFile:
            data = line.strip().split(",")
            docFirstname = data[0]
            docLastname = data[1]
            docSpecialty = data[2]
            aDoctor = Doctor(docFirstname, docLastname, docSpecialty)
            self.allDoctors.append(aDoctor)

    def findPatient(self, patientFullName):
        for aPatient in self.allPatients:
            if aPatient.patientFullName == patientFullName:
                return aPatient
        return None

    def findDoctor(self, docFullName):
        for aDoctor in self.allDoctors:
            if aDoctor.docFullName == docFullName:
                return aDoctor
        return None
    
    def assignDoctor(self, paName, docName):
        aPatient = self.findPatient(paName)
        aDoctor = self.findDoctor(docName)
        pDoctor = aPatient.myDoctor
        if aPatient.myDoctor is None :
            aPatient.myDoctor = aDoctor.docFullName
        else:
            prevDotocr = self.findDoctor(pDoctor)
            prevDotocr.removePatient(aPatient)
            aPatient.myDoctor = aDoctor.docFullName
        aDoctor.addPatient(aPatient)
        print(f"Patient {aPatient} is Assigned to Dcotor {aDoctor}!")

    def bookConsultation(self, conDoc, conPa, conDate, conReason, conFee):
        aPatient = self.findPatient(conPa)
        aDoctor = self.findDoctor(conDoc)

        if aPatient and aDoctor:
            newConsultation = Consultation(aDoctor.docFullName, aPatient.patientFullName)
            newConsultation.consulDate = conDate
            newConsultation.consulReason = conReason
            newConsultation.consulFee = conFee

            aPatient.consulList.append(newConsultation)
            aDoctor.consulList.append(newConsultation)
            self.allConsultations.append(newConsultation)

            print(newConsultation)
        else:
            print("Error: Patient or doctor not found!")
    
    def searchPatients(self, query):
        # Logic to search patients based on the query
        matchingPatients = []

        for patient in self.allPatients:
            if (
                query in patient.patientFName.lower()
                or query in patient.patientLName.lower()
                or query in patient.patientFullName.lower()
            ):
                matchingPatients.append(patient)

        return matchingPatients
    
    def searchDoctors(self, query):
        # Logic to search doctors based on the query
        matchingDoctors = []

        for doctor in self.allDoctors:
            if (
                query in doctor.docFullName.lower()
                or query in doctor.docFName.lower()
                or query in doctor.docLName.lower()
            ):
                matchingDoctors.append(doctor)

        return matchingDoctors
    
    def getPatientInfo(self, patientFullName):
        aPatient = self.findPatient(patientFullName)
        # Get the assigned doctor for the patient
        assignedDocName = aPatient.myDoctor

        # Find the corresponding doctor object
        assignedDoc = self.findDoctor(assignedDocName)

        patient_info = f"Patient Information\n\n\n"
        patient_info += f"Patient: {aPatient}\n\n"
        patient_info += f"Doctor: \n{assignedDoc}\n\n"
        patient_info += f"Consultations:\n{aPatient.consulInfo()}\n\n"
        patient_info += f"Total Fees Due: ${aPatient.totalconFee()}"
        return patient_info
    
    def getDocInfo(self, doctorFullName):
        aDoctor = self.findDoctor(doctorFullName)
        doctor_info = f"Doctor Information\n\n\n"
        doctor_info += f"{aDoctor}\n\n"
        doctor_info += f"Patient List\n{aDoctor.aPatient()}\n"
        doctor_info += f"\nConsultations\n{aDoctor.consulInfo()}\n\n"
        return doctor_info
    
    def consulReport(self):
        # calculate the sum of all consultation fees
        total_fee = 0
        for consultation in self.allConsultations:
            total_fee += float(consultation.consulFee)
        report_info = ""
        report_info = "\n\n".join(str(aReport) for aReport in self.allConsultations)
        
        return f"{report_info} \n\n Total Fees: ${str(total_fee)}"
    
    

