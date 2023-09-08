class Patient:

    nextID = 1000
    def __init__(self, paFirstname, paLastname):
        self.__patientID = Patient.nextID
        self.__patientFName = paFirstname
        self.__patientLName = paLastname
        self.__myDoctor = None
        self.__consulList = []
        Patient.nextID += 1

    @property
    def patientID(self):
        return self.__patientID

    @property
    def patientFName(self):
        return self.__patientFName

    @property
    def patientLName(self):
        return self.__patientLName

    @property
    def patientFullName(self):
        return self.patientFName + " " + self.patientLName

    @patientFullName.setter
    def patientFullName(self, full_name):
        names = full_name.split()
        self.__patientFName = names[0]
        self.__patientLName = names[-1]

    @property
    def myDoctor(self):
        return self.__myDoctor
    
    @myDoctor.setter
    def myDoctor(self, newDoctor):
        self.__myDoctor = newDoctor

    @property
    def consulList(self):
        return self.__consulList
    
    def consulInfo(self):
        for aConsultation in self.consulList:
            return aConsultation.consulDoctor + " " + aConsultation.consulDate + " " + aConsultation.consulReason + " $" + aConsultation.consulFee
    
    def totalconFee(self):
        total_fee = 0
        for aConsultation in self.consulList:
            total_fee += float(aConsultation.consulFee)
        return "{:.2f}".format(total_fee)


    def __str__(self):
        return str(self.patientID) + " " + self.patientFullName


class Doctor:

    nextID = 100
    def __init__(self, docFirstname, docLastname, docSpecialty):
        self.__doctorID = Doctor.nextID
        self.__doctorFName = docFirstname
        self.__doctorLName = docLastname
        self.__doctorSpec = docSpecialty
        self.__patientList = []
        self.__consulList = []
        Doctor.nextID += 1

    @property
    def doctorID(self):
        return self.__doctorID

    @property
    def docFName(self):
        return self.__doctorFName

    @property
    def docLName(self):
        return self.__doctorLName

    @property
    def docSpecialty(self):
        return self.__doctorSpec

    @property
    def docFullName(self):
        return self.docFName + " " + self.docLName

    @docFullName.setter
    def docFullName(self, full_name):
        names = full_name.split()
        self.__doctorFName = names[0]
        self.__doctorLName = names[-1]

    @property
    def patientList(self):
        return self.__patientList
    
    def aPatient(self):
        for aPatient in self.patientList:
            return aPatient
    
    def addPatient(self, aPatient):
        self.patientList.append(aPatient)

    def removePatient(self, aPatient):
        self.patientList.remove(aPatient)
    
    @property
    def consulList(self):
        return self.__consulList
    
    def consulInfo(self):
        for aConsultation in self.consulList:
            return aConsultation.consulDate + " " + aConsultation.consulReason + " " + aConsultation.consulPatient + " $" + aConsultation.consulFee

    
    def __str__(self):
        return str(self.doctorID) + " " + self.docFullName + " - " + self.docSpecialty

class Consultation:
    def __init__(self, doctor, patient):
        self.__myCDoctor = doctor
        self.__myCPatient = patient
        self.__myCDate = None
        self.__myCReason = None
        self.__myFee = None
    
    @property
    def consulDoctor(self):
        return self.__myCDoctor
    
    @property
    def consulPatient(self):
        return self.__myCPatient
    
    @property
    def consulDate(self):
        return self.__myCDate
    
    @consulDate.setter
    def consulDate(self, aDate):
        self.__myCDate = aDate

    @property
    def consulReason(self):
        return self.__myCReason
    
    @consulReason.setter
    def consulReason(self, aReason):
        self.__myCReason = aReason

    @property
    def consulFee(self):
        return self.__myFee
    
    @consulFee.setter
    def consulFee(self, newFee):
        self.__myFee = newFee

    def __str__(self):
        return "Date: " + self.consulDate + " Doctor: " + self.consulDoctor + " Patient: " + self.consulPatient + " Reason: " + self.consulReason + " Fee: $" + self.consulFee
    
