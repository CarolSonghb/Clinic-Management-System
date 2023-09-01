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
