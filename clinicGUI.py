import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from clinicController import *
import re

clinic = clinicController()
clinic.newPatient()
clinic.newDoctor()

root = tk.Tk()
root.title("Clinic Management System")
root.geometry("1200x800")
root.resizable(width=False, height=False)

######################
# function part
######################
# button to display a list of patients
def btnShowPa():
    for patient in clinic.allPatients:
        listbox_patient.insert(tk.END, str(patient))

# button to display a list of doctors
def btnShowDoc():
    for doctor in clinic.allDoctors:
        listbox_doctor.insert(tk.END, str(doctor))

def selectPaDoc():
    #get selected patient
    selPatientIndex = listbox_patient.curselection()
    #get selected doctor
    selDocIndex = listbox_doctor.curselection()

    if not selPatientIndex:
        showwarning("Warning", "Please select a patient.")
        return None, None

    if not selDocIndex:
        showwarning("Warning", "Please select a doctor.")
        return None, None

    selectedPatient = listbox_patient.get(selPatientIndex)
    # only pass the name, not the ID number
    selectedPaName = selectedPatient.split(" ", 1)[1]
    selectedDoc = listbox_doctor.get(selDocIndex)
    print(selectedDoc)
    # split selectedDoc into 5 parts
    # then retrieve first name and last name, and combine them
    selectedDocName = selectedDoc.split(" ", 4)[1] + " " + selectedDoc.split(" ", 4)[2]
    print(selectedDocName)

    return selectedPaName, selectedDocName

def selPaLabel(selected_patient):
    selPa_label.config(state='normal')
    selPa_label.delete(0, tk.END)
    selPa_label.insert(0, selected_patient)
    selPa_label.config(state='readonly')

def patientSelect(event):
    selPatientIndex = event.widget.curselection()
    if selPatientIndex:
        selectedPatient = event.widget.get(selPatientIndex)
        print(selectedPatient)
        selPaLabel(selectedPatient)
    else:
        selPaLabel.config(text="")

def selDocLabel(selected_doctor):
    selDoc_label.config(state='normal')
    selDoc_label.delete(0, tk.END)
    selDoc_label.insert(0, selected_doctor)
    selDoc_label.config(state='readonly')

def doctorSelect(event):
    #get selected doctor
    selDocIndex = event.widget.curselection()
    if selDocIndex:
        selectedDoc = event.widget.get(selDocIndex)
        selDocLabel(selectedDoc)
    else:
        selDocLabel.config(text="")

# button to assign a patient to a doctor, and vice versa
def btnAssignDoc():
    selectedPaName, selectedDocName = selectPaDoc()

    if selectedPaName and selectedDocName:  # Check if both values are not None
        clinic.assignDoctor(str(selectedPaName), str(selectedDocName))
        showinfo("Message", f"Patient {selectedPaName} is Assigned to Doctor {selectedDocName}!")

def btnAddConsul():
    selectedPaName, selectedDocName = selectPaDoc()

    if selectedPaName and selectedDocName:
        conDate = date_entry.get()
        conReason = reason_entry.get()
        conFee = fee_entry.get()

        if not conDate or not conReason or not conFee:
            showwarning("Warning", "Please fill in all consultation details.")
            return 
        
        # Validate conDate format using regex
        date_pattern = re.compile(r"^\d{2}/\d{2}/\d{4}$")
        if not date_pattern.match(conDate):
            showwarning("Warning", "Please enter the date in dd/mm/yyyy format.")
            return
        
        # check if conFee is a float number
        try:
            conFee = float(conFee)
        except ValueError:
            showwarning("Warning", "Consultation fee must be a valid number.")
            return
        
        # format conFee with two decimal places
        conFee = "{:.2f}".format(float(conFee))

        clinic.bookConsultation(selectedDocName, selectedPaName, conDate, conReason, conFee)
        showinfo("Message", "The new consultation has been added!")

def searchPa():
    # Get the search query from the entry widget
    query = searchPa_entry.get().lower()
    print(query)

    # Clear previous search results
    searchResultBox.delete(0, tk.END)

    # List to store matching patients
    matchingPatients = []

    for patient in clinic.allPatients:
        if query in patient.patientFName.lower() or query in patient.patientLName.lower() or query in patient.patientFullName.lower(): 
            matchingPatients.append(patient)
            print(patient)

    # Display search results in the box
    for matchingPatient in matchingPatients:
        searchResultBox.insert(tk.END, str(matchingPatient))
        searchResultBox.bind("<<ListboxSelect>>", patientSelect)


    if not matchingPatients:
        searchResultBox.insert(tk.END, "No matching patients found")
        

def searchDoc():
    # Get the search query from the entry widget
    query = searchDoc_entry.get().lower()

     # Clear previous search results
    searchResultBox.delete(0, tk.END)

    # List to store matching patients
    matchingDocs = []

    for doctor in clinic.allDoctors:
        if query in doctor.docFullName.lower() or query in doctor.docFName.lower() or query in doctor.docFName.lower(): 
            matchingDocs.append(doctor)

    # Display search results in the frame
    for matchingDoc in matchingDocs:
        searchResultBox.insert(tk.END, str(matchingDoc))
        searchResultBox.bind("<<ListboxSelect>>", doctorSelect)

    if not matchingDocs:
        searchResultBox.insert(tk.END, "No matching Doctors found.")


def viewPatient():
    selPatient = selPa_label.get()
    print(selPatient)
    
    if not selPatient:
        showerror("Error", "Choose a patient first!")
    else:
        foundPatient = None
        
        for patient in clinic.allPatients:
            if selPatient == str(patient):
                foundPatient = patient
                print(foundPatient)
                break
        
        if foundPatient is not None:
            patient_info = f"Patient Information\n\n\n"
            patient_info += f"Patient: {foundPatient}\n\n"
            patient_info += f"Doctor: {foundPatient.myDoctor}\n\n"
            patient_info += f"Consultations:\n{foundPatient.consulInfo()}\n\n"
            patient_info += f"Total Fees Due: ${foundPatient.totalconFee()}"
            
            showinfo("Patient Info", patient_info)
        else:
            showerror("Error", "No matching patient found.")

def viewDoctor():
    selDoc = selDoc_label.get()

    if not selDoc:
        showerror("Error", "Choose a doctor first!")
    else:
        foundDoc = None

        for doctor in clinic.allDoctors:
            if selDoc == str(doctor):
                foundDoc = doctor
                break
        if foundDoc is not None:
            doctor_info = f"Doctor Information\n\n\n"
            doctor_info += f"{foundDoc}\n\n"
            doctor_info += f"Patient List\n{foundDoc.aPatient()}\n"
            doctor_info += f"\nConsultations\n{foundDoc.consulInfo()}\n\n"
            
            showinfo("Doctor Info", doctor_info)
        else:
            showerror("Error", "No matching doctor found.")

def consulReport():
    report_window = tk.Toplevel(root)
    report_window.title("Consultation Report")
    report_window.geometry("600x400")
    report_info = ""

    if clinic.allConsultations:
        report_info = "\n\n".join(str(aReport) for aReport in clinic.allConsultations)
        report_label = tk.Label(report_window, text=report_info)
        report_label.pack()
    else:
        print("no report")
        showwarning("Warning", "No consultation has been added.")
    
def exitRoot():
    showinfo("Close", "Thank you for using Clinic Management System!")
    root.destroy()

    




    

#############################
# interface part
#############################
# create a frame located at the top of the window
topframe = tk.Frame(root)
topframe.pack()

# set the frame to place patient and doctor list widget
first_frame = tk.Label(topframe)
first_frame.grid(row=0, column=1, padx=50, pady=20)

button_frame = tk.Label(topframe)
button_frame.grid(row=0, column=0)

# Create and grid the button
buttonPatients = ttk.Button(button_frame, text="Display Patients", command=btnShowPa)
buttonPatients.grid(row=0, column=0)

space = tk.Label(button_frame, text="")
space.grid(row=1, column=0)

# Create and grid the label for patient list
label_patient = tk.Label(
    first_frame, text="PATIENT LIST", font=("Arial", 14, "bold")
)
label_patient.grid(row=0, column=0)

# Create and grid the listbox for patients
listbox_patient = tk.Listbox(first_frame, exportselection=0, selectmode=tk.BROWSE)
listbox_patient.grid(row=1, column=0)
#bind the patient selection function to the listbox
listbox_patient.bind("<<ListboxSelect>>", patientSelect)

# Create and grid the button
buttonDoc = ttk.Button(button_frame, text="Display Doctors", command=btnShowDoc)
buttonDoc.grid(row=2, column=0)  

# Create and grid the label for doctor list
label_doctor = tk.Label(
    first_frame, text="DOCTOR LIST", font=("Arial", 14, "bold")
)
label_doctor.grid(row=0, column=1)

# Create and grid the listbox for doctors
listbox_doctor = tk.Listbox(first_frame, exportselection=0, selectmode=tk.BROWSE)
listbox_doctor.config(width=30)
listbox_doctor.grid(row=1, column=1)
#bind the patient selection function to the listbox
listbox_doctor.bind("<<ListboxSelect>>", doctorSelect)

#Create a frame for consultation and grid it on top right side of the window
second_frame = tk.LabelFrame(topframe, text="CONSULTATION", font=("Arial", 14, "bold"))
second_frame.grid(row=0, column=2, ipadx=10, ipady=10)

# Create lable and entry for consultation date
date_label = tk.Label(second_frame, text="Date")
date_label.grid(row=1, column=0, pady=10, ipadx=20)
date_entry=tk.Entry(second_frame)
date_entry.grid(row=1, column=1)

remind_label = tk.Label(second_frame, text="dd/mm/yyyy")
remind_label.grid(row=0, column=1)

# Create lable and entry for consultation reason
reason_label = tk.Label(second_frame, text="Reason ")
reason_label.grid(row=2, column=0, pady=10)
reason_entry=tk.Entry(second_frame)
reason_entry.grid(row=2, column=1)

# Create lable and entry for consultation fee
fee_label = tk.Label(second_frame, text="Fee ")
fee_label.grid(row=3, column=0, pady=10)
fee_entry=tk.Entry(second_frame)
fee_entry.grid(row=3, column=1)

middleFrame = tk.LabelFrame(root)
middleFrame.pack()

middleLeftFrame = tk.Label(middleFrame)
middleLeftFrame.grid(row=0, column=0)

pa_label = tk.Label(middleLeftFrame, text="Selected Patient: ")
pa_label.grid(row=0, column = 0)
# Create a widget to display selected patient's name
selPa_label = tk.Entry(middleLeftFrame, width=20, state='readonly')
selPa_label.grid(row=0, column=1)

doc_label = tk.Label(middleLeftFrame, text="Selected Doctor: ")
doc_label.grid(row=1, column = 0)

# Create a widget to display selected doctor's name
selDoc_label = tk.Entry(middleLeftFrame, width=30, state='readonly')
selDoc_label.grid(row=1, column=1)

buttonViewPa = tk.Button(middleLeftFrame, text = "Patient Info", command=viewPatient, width=20, height=2)
buttonViewPa.grid(row=0, column=2, pady=10)

buttonViewDoc = tk.Button(middleLeftFrame, text = "Doctor Info", command=viewDoctor, width=20, height=2)
buttonViewDoc.grid(row=1, column=2, padx=20, pady=10)

middleRightFrame = tk.Label(middleFrame)
middleRightFrame.grid(row=0, column=1)

buttonAssignDoc = tk.Button(middleRightFrame, text="Assign Doctor", command=btnAssignDoc, width=20, height=2)
buttonAssignDoc.grid(row=0, column=0, padx=100, pady=10)

buttonAddCons = tk.Button(middleRightFrame, text="Add Consultation", command=btnAddConsul, width=20, height=2)
buttonAddCons.grid(row=1, column=0, padx=100, pady=10)

bottomFrame = tk.Label(root)
bottomFrame.pack()

searchFrame = tk.Label(bottomFrame)
searchFrame.grid(row=0, column=0)

searchTitle = tk.Label(searchFrame, text="Search a Patient/Doctor to see their details", font=("Arial", 14, "bold"))
searchTitle.grid(row=0, column=0, pady=20)

searchPa_entry=tk.Entry(searchFrame)
searchPa_entry.grid(row=1, column=0)


button_searchPa = tk.Button(searchFrame, text="Search Patient", command=searchPa)
button_searchPa.grid(row=1, column=1)

searchDoc_entry=tk.Entry(searchFrame)
searchDoc_entry.grid(row=2, column=0)
button_searchDoc = tk.Button(searchFrame, text="Search Doctor", command=searchDoc)
button_searchDoc.grid(row=2, column=1, sticky="w")

searchLabel = tk.Label(searchFrame, text="Search Result (click to select)", font=("Arial", 14, "bold"))
searchLabel.grid(row=3, column=0, pady=10)

searchResultBox = tk.Listbox(searchFrame)
searchResultBox.config(width=40, height=8)
searchResultBox.grid(row=4, column=0, padx=20)

reportFrame = tk.Label(bottomFrame)
reportFrame.grid(row=0, column=1)

buttonReport = tk.Button(reportFrame, text = "Consultation Report", command=consulReport, width=20, height=2)
buttonReport.grid(row=0, column=0)

buttonExit = tk.Button(reportFrame, text = "Exit", command=exitRoot, width=20, height=2)
buttonExit.grid(row=1, column=0)

root.mainloop()
