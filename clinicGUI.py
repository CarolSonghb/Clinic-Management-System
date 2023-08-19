import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from clinicController import *

clinic = clinicController()
clinic.newPatient()
clinic.newDoctor()

root = tk.Tk()
root.title("Clinic Management System")
root.geometry("1000x600")
root.resizable(width=False, height=False)


def btnShowPa():
    for patient in clinic.allPatients:
        listbox_patient.insert(tk.END, str(patient))


def btnShowDoc():
    for doctor in clinic.allDoctors:
        listbox_doctor.insert(tk.END, str(doctor))

def btnAssignDoc():
    #get selected patient
    selPatientIndex = listbox_patient.curselection()
    selectedPatient = listbox_patient.get(selPatientIndex)
    # only pass the name, not the ID number
    selectedPaName = selectedPatient.split(" ", 1)[1]

    #get selected doctor
    selDocIndex = listbox_doctor.curselection()
    selectedDoc = listbox_doctor.get(selDocIndex)
    selectedDocName = selectedDoc.split(" ", 1)[1]

    clinic.assignDoctor(str(selectedPaName), str(selectedDocName))



# set the frame to place patient and doctor list widget
lefttop_frame = tk.Frame(root)
lefttop_frame.grid(row=0, column=0, padx=5, pady=5)

# add the widgets for Patient List
frm_patientCreate = tk.Frame(lefttop_frame, relief=tk.FLAT, borderwidth=3)
# Pack the frame into the window
frm_patientCreate.pack(padx=5, pady=5, side=tk.LEFT)

# Create and pack the label for patient list
label_patient = tk.Label(
    frm_patientCreate, text="PATIENT LIST", font=("Arial", 14, "bold")
)
label_patient.pack()

# Create and pack the listbox for patients
listbox_patient = tk.Listbox(frm_patientCreate, exportselection=0, selectmode=tk.BROWSE)
listbox_patient.pack(fill="x", padx=20, pady=5, side=tk.TOP)

# Create and pack the "Show Patients" button
button = ttk.Button(frm_patientCreate, text="Display Patients", command=btnShowPa)
button.pack(fill="x", padx=5, pady=5, side=tk.TOP)  # Place it under the listbox

# add the widgets for Doctor List
frm_doctorCreate = tk.Frame(lefttop_frame, relief=tk.FLAT, borderwidth=3)
frm_doctorCreate.pack(padx=5, pady=5, side=tk.LEFT)

# Create and pack the label for doctor list
label_doctor = tk.Label(
    frm_doctorCreate, text="DOCTOR LIST", font=("Arial", 14, "bold")
)
label_doctor.pack()

# Create and pack the listbox for doctors
listbox_doctor = tk.Listbox(frm_doctorCreate, exportselection=0, selectmode=tk.BROWSE)
listbox_doctor.pack(fill="x", padx=20, pady=5, side=tk.TOP)

# Create and pack the "Show Doctors" button
button = ttk.Button(frm_doctorCreate, text="Display Doctors", command=btnShowDoc)
button.pack(fill="x", padx=5, pady=5, side=tk.TOP)  # Place it under the listbox

button = ttk.Button(lefttop_frame, text="Assign Doctor", command=btnAssignDoc)
button.pack(fill="x", padx=5, pady=5, side=tk.TOP)


root.mainloop()
