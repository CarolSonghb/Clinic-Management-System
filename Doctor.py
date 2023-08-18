class Doctor:
    nextID = 100

    def __init__(self, docFirstname, docLastname, docSpecialty):
        self.__doctorID = Doctor.nextID
        self.__doctorFName = docFirstname
        self.__doctorLName = docLastname
        self.__doctorSpec = docSpecialty
        self.__patientList = []
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
        return self.__doctorFName + " " + self.__doctorLName

    @docFullName.setter
    def docFullName(self, full_name):
        names = full_name.split()
        self.__doctorFName = names[0]
        self.__doctorLName = names[-1]

    def __str__(self):
        return str(self.doctorID) + " " + self.docFullName
