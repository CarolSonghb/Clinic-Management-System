import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from clinicController import *
from datetime import datetime

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
        
        clinic.bookConsultation(selectedDocName, selectedPaName, conDate, conReason, conFee)
        showinfo("Message", "The new consultation has been added!")


    

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

searchPa_entry=tk.Entry(middleFrame2)
searchPa_entry.grid(row=0, column=0)
button_searchPa = tk.Button(middleFrame2, text="Search Patient")
button_searchPa.grid(row=0, column=1)

searchDoc_entry=tk.Entry(middleFrame2)
searchDoc_entry.grid(row=1, column=0)
button_searchDoc = tk.Button(middleFrame2, text="Search Doctor")
button_searchDoc.grid(row=1, column=1)







root.mainloop()
