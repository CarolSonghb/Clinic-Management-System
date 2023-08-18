from Patient import *
from Doctor import *


class clinicController:
    def __init__(self):
        self.allPatients = []
        self.allDoctors = []

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
    
    def 
