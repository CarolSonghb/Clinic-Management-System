class Consultation:
    def __init__(self, date, doctor, patient):
        self.__myCDate = date
        self.__myCDoctor = doctor
        self.__myCPatient = patient
        self.__myCReason = "None"
        self.__myFee = None
    
    @property
    def consulDate(self):
        return self.__myCDate
    
    @property
    def consulDoctor(self):
        return self.__myCDoctor
    
    @property
    def consulPatient(self):
        return self.__myCPatient
    
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
        return "Date: " + self.consulDate + "Doctor: " + self.consulDoctor + "Patient: " + self.consulPatient + "Reason: " + self.consulReason + "Fee: " + self.consulFee
