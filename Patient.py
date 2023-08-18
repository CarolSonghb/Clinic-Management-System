class Patient:
    nextID = 1000

    def __init__(self, paFirstname, paLastname):
        self.__patientID = Patient.nextID
        self.__patientFName = paFirstname
        self.__patientLName = paLastname
        self.__doctorList = []
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
        return self.__patientFName + " " + self.patientLName

    @patientFullName.setter
    def patientFullName(self, full_name):
        names = full_name.split()
        self.__patientFName = names[0]
        self.__patientLName = names[-1]

    def __str__(self):
        return str(self.patientID) + " " + self.patientFullName
