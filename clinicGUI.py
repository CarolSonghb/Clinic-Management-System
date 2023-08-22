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
    selectedDocName = selectedDoc.split(" ", 1)[1]

    return selectedPaName, selectedDocName

def selPaLabel(selected_patient):
    selPa_label.config(text=f"{selected_patient}")

def patientSelect(event):
    selPatientIndex = listbox_patient.curselection()
    if selPatientIndex:
        selectedPatient = listbox_patient.get(selPatientIndex)
        selPaLabel(selectedPatient)
    else:
        selPaLabel.config(text="")

def selDocLabel(selected_doctor):
    selDoc_label.config(text=f"{selected_doctor}")

def doctorSelect(event):
    #get selected doctor
    selDocIndex = listbox_doctor.curselection()
    if selDocIndex:
        selectedDoc = listbox_doctor.get(selDocIndex)
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

    # Hide previous search results
    for widget in searchResultFrame.winfo_children():
        widget.destroy()

    # List to store matching patients
    matchingPatients = []

    for patient in clinic.allPatients:
        if query in patient.patientFullName.lower(): 
            matchingPatients.append(patient)

    # Display search results in the frame
    for i, matchingPatient in enumerate(matchingPatients, start=1):
        result_label = tk.Label(searchResultFrame, text=str(matchingPatient))
        result_label.grid(row=i, column=0, padx=10, pady=5)
        doctor_label = tk.Label(searchResultFrame, text=f"Doctor: {matchingPatient.myDoctor}")
        doctor_label.grid(row=i+1, column=0)
        consul_label = tk.Label(searchResultFrame, text="Consultations")
        consul_label.grid(row=i+2, column=0)
        consul_info = tk.Label(searchResultFrame, text=str(matchingPatient.consulInfo()))
        consul_info.grid(row=i+3, column=0)
        fee_label = tk.Label(searchResultFrame, text=f"Total Fees Due: ${matchingPatient.totalconFee()}")
        fee_label.grid(row=i+4, column=0)


    if not matchingPatients:
        no_result_label = tk.Label(searchResultFrame, text="No matching patients found.")
        no_result_label.grid(row=1, column=0, padx=10, pady=5)

def searchDoc():
    # Get the search query from the entry widget
    query = searchDoc_entry.get().lower()

    # Hide previous search results
    for widget in searchResultFrame.winfo_children():
        widget.destroy()

    # List to store matching patients
    matchingDocs = []

    for doctor in clinic.allDoctors:
        if query in doctor.docFullName.lower(): 
            matchingDocs.append(doctor)

    # Display search results in the frame
    for i, matchingDoc in enumerate(matchingDocs, start=1):
        result_label = tk.Label(searchResultFrame, text=str(matchingDoc))
        result_label.grid(row=i, column=0, padx=10, pady=5)
        pa_label = tk.Label(searchResultFrame, text="Patient List")
        pa_label.grid(row=i+1, column=0)
        paList_label = tk.Label(searchResultFrame, text=str(matchingDoc.aPatient()))
        paList_label.grid(row=i+2, column=0)
        consul_label = tk.Label(searchResultFrame, text="Consultations")
        consul_label.grid(row=i+3, column=0)
        consul_info = tk.Label(searchResultFrame, text=str(matchingDoc.consulInfo()))
        consul_info.grid(row=i+4, column=0)



    if not matchingDocs:
        no_result_label = tk.Label(searchResultFrame, text="No matching Doctors found.")
        no_result_label.grid(row=1, column=0, padx=10, pady=5)
    

#############################
# interface part
#############################
# create a frame located at the top of the window
topframe = tk.Frame(root)
topframe.pack()

# set the frame to place patient and doctor list widget
first_frame = tk.Label(topframe)
first_frame.grid(row=0, column=0, padx=50, pady=20)

# Create and grid the button
buttonPatients = ttk.Button(first_frame, text="Display Patients", command=btnShowPa)
buttonPatients.grid(row=0, column=0)

# Create and grid the label for patient list
label_patient = tk.Label(
    first_frame, text="PATIENT LIST", font=("Arial", 14, "bold")
)
label_patient.grid(row=1, column=0)

# Create and grid the listbox for patients
listbox_patient = tk.Listbox(first_frame, exportselection=0, selectmode=tk.BROWSE)
listbox_patient.grid(row=2, column=0)
#bind the patient selection function to the listbox
listbox_patient.bind("<<ListboxSelect>>", patientSelect)

# Create and grid the button
buttonDoc = ttk.Button(first_frame, text="Display Doctors", command=btnShowDoc)
buttonDoc.grid(row=0, column=1)  

# Create and grid the label for doctor list
label_doctor = tk.Label(
    first_frame, text="DOCTOR LIST", font=("Arial", 14, "bold")
)
label_doctor.grid(row=1, column=1)

# Create and grid the listbox for doctors
listbox_doctor = tk.Listbox(first_frame, exportselection=0, selectmode=tk.BROWSE)
listbox_doctor.config(width=30)
listbox_doctor.grid(row=2, column=1)
#bind the patient selection function to the listbox
listbox_doctor.bind("<<ListboxSelect>>", doctorSelect)

pa_label = tk.Label(first_frame, text="Selected Patient: ")
pa_label.grid(row=3, column = 0)
# Create a label widget to display selected patient's name
selPa_label = tk.Label(first_frame, text="")
selPa_label.grid(row=3, column=1)

doc_label = tk.Label(first_frame, text="Selected Doctor: ")
doc_label.grid(row=4, column = 0)

# Create a label widget to display selected doctor's name
selDoc_label = tk.Label(first_frame, text="")
selDoc_label.grid(row=4, column=1)

# set padding for widgets in the first frame
for widget in first_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Create a frame for consultation and grid it on top right side of the window
second_frame = tk.LabelFrame(topframe, text="CONSULTATION", font=("Arial", 14, "bold"))
second_frame.grid(row=0, column=1, padx=50, ipadx=10, ipady=10)

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

buttonAssignDoc = tk.Button(middleFrame, text="Assign Doctor", command=btnAssignDoc, width=20, height=2)
buttonAssignDoc.grid(row=0, column=0, padx=100, pady=20)

buttonAddCons = tk.Button(middleFrame, text="Add Consultation", command=btnAddConsul, width=20, height=2)
buttonAddCons.grid(row=0, column=1, padx=100)

middleFrame2 = tk.Label(root)
middleFrame2.pack()

searchFrame = tk.Label(middleFrame2)
searchFrame.grid(row=0, column=0)

searchTitle = tk.Label(searchFrame, text="Search a Patient/Doctor to see their details", font=("Arial", 14, "bold"))
searchTitle.grid(row=0, column=0)

searchPa_entry=tk.Entry(searchFrame)
searchPa_entry.grid(row=1, column=0)


button_searchPa = tk.Button(searchFrame, text="Search Patient", command=searchPa)
button_searchPa.grid(row=1, column=1)

searchDoc_entry=tk.Entry(searchFrame)
searchDoc_entry.grid(row=2, column=0)
button_searchDoc = tk.Button(searchFrame, text="Search Doctor", command=searchDoc)
button_searchDoc.grid(row=2, column=1)

searchReminder = tk.Label(searchFrame, text="Please type in full name to search")
searchReminder.grid(row=3, column=0)

searchLabel = tk.Label(searchFrame, text="Search results displayed below...")
searchLabel.grid(row=4, column=0)
# Create a frame to display search results
searchResultFrame = tk.LabelFrame(searchFrame)
searchResultFrame.grid(row=5, column=0)



root.mainloop()
