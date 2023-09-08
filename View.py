import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from clinicController import clinicController
import re

class clinicManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinic Management System")
        self.root.geometry("1200x800")
        self.root.resizable(width=False, height=False)

        self.clinic = clinicController()
        self.clinic.newPatient()
        self.clinic.newDoctor()

        # GUI components
        self.create_interface()

    def create_interface(self):
        # Create and organize the GUI components
        self.create_top_frame()
        self.create_middle_frame()
        self.create_bottom_frame()

    def create_top_frame(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack()

        # Buttons to display patients and doctors
        btn_show_patients = ttk.Button(top_frame, text="Display Patients", command=self.btnShowPa)
        btn_show_patients.grid(row=0, column=0, pady=30)

        btn_show_doctors = ttk.Button(top_frame, text="Display Doctors", command=self.btnShowDoc)
        btn_show_doctors.grid(row=0, column=1)

        # Labels and listboxes for patients and doctors
        self.label_patient = tk.Label(top_frame, text="PATIENT LIST", font=("Arial", 14, "bold"))
        self.label_patient.grid(row=1, column=0)

        self.label_doctor = tk.Label(top_frame, text="DOCTOR LIST", font=("Arial", 14, "bold"))
        self.label_doctor.grid(row=1, column=1)

        self.listbox_patient = tk.Listbox(top_frame, exportselection=0, selectmode=tk.BROWSE)
        self.listbox_patient.grid(row=2, column=0)

        self.listbox_doctor = tk.Listbox(top_frame, exportselection=0, selectmode=tk.BROWSE, width=30)
        self.listbox_doctor.grid(row=2, column=1)

        # Bind selection events for patients and doctors
        self.listbox_patient.bind("<<ListboxSelect>>", self.patientSelect)
        self.listbox_doctor.bind("<<ListboxSelect>>", self.doctorSelect)

        # Create a frame for consultation and grid it under the top_frame
        second_frame = tk.LabelFrame(top_frame, text="CONSULTATION", font=("Arial", 14, "bold"))
        second_frame.grid(row=0, column=2, ipadx=10, ipady=10, pady=50)

        # Create widgets for consultation input
        date_label = tk.Label(second_frame, text="Date")
        date_label.grid(row=0, column=0, pady=10)
        date_entry = tk.Entry(second_frame)
        date_entry.grid(row=0, column=1)

        remind_label = tk.Label(second_frame, text="dd/mm/yyyy")
        remind_label.grid(row=0, column=2, padx=5)

        reason_label = tk.Label(second_frame, text="Reason")
        reason_label.grid(row=1, column=0, pady=10)
        reason_entry = tk.Entry(second_frame)
        reason_entry.grid(row=1, column=1)

        fee_label = tk.Label(second_frame, text="Fee")
        fee_label.grid(row=2, column=0, pady=10)
        fee_entry = tk.Entry(second_frame)
        fee_entry.grid(row=2, column=1)


    def create_middle_frame(self):
        middle_frame = tk.LabelFrame(self.root)
        middle_frame.pack()

        # Labels and entry fields for selected patient and doctor
        pa_label = tk.Label(middle_frame, text="Selected Patient: ")
        pa_label.grid(row=0, column=0)

        self.selPa_label = tk.Entry(middle_frame, width=30, state="readonly")
        self.selPa_label.grid(row=0, column=1)

        doc_label = tk.Label(middle_frame, text="Selected Doctor: ")
        doc_label.grid(row=1, column=0)

        self.selDoc_label = tk.Entry(middle_frame, width=30, state="readonly")
        self.selDoc_label.grid(row=1, column=1)

        # Buttons to view patient and doctor details, and to assign doctors
        btn_view_patient = tk.Button(middle_frame, text="Patient Info", command=self.viewPatient, width=20, height=2)
        btn_view_patient.grid(row=0, column=2, pady=10)

        btn_view_doctor = tk.Button(middle_frame, text="Doctor Info", command=self.viewDoctor, width=20, height=2)
        btn_view_doctor.grid(row=1, column=2, padx=20, pady=10)

        btn_assign_doctor = tk.Button(middle_frame, text="Assign Doctor", command=self.btnAssignDoc, width=20, height=2)
        btn_assign_doctor.grid(row=2, column=2, pady=10)

        btn_add_consultation = tk.Button(middle_frame, text="Add Consultation", command=self.btnAddConsul, width=20, height=2)
        btn_add_consultation.grid(row=3, column=2, pady=10)

    def create_bottom_frame(self):
        bottom_frame = tk.Label(self.root)
        bottom_frame.pack()

        # Create a frame for search and report
        search_frame = tk.Label(bottom_frame)
        search_frame.grid(row=0, column=0)

        # Search entries and buttons
        search_title = tk.Label(
            search_frame,
            text="Search a Patient/Doctor to see their details\n(First name, Last name or Full name)",
            font=("Arial", 14, "bold"),
        )
        search_title.grid(row=0, column=0)

        search_pa_entry = tk.Entry(search_frame)
        search_pa_entry.grid(row=1, column=0)

        btn_search_pa = tk.Button(search_frame, text="Search Patient", command=self.searchPa)
        btn_search_pa.grid(row=1, column=1)

        search_doc_entry = tk.Entry(search_frame)
        search_doc_entry.grid(row=2, column=0)

        btn_search_doc = tk.Button(search_frame, text="Search Doctor", command=self.searchDoc)
        btn_search_doc.grid(row=2, column=1, sticky="w")

        search_label = tk.Label(
            search_frame, text="Search Result (click to select)", font=("Arial", 14, "bold")
        )
        search_label.grid(row=3, column=0, pady=10)

        self.search_result_box = tk.Listbox(search_frame, width=40, height=8)
        self.search_result_box.grid(row=4, column=0, padx=20)

        self.search_result_box.bind("<<ListboxSelect>>", self.patientSelect)

        # Report and control buttons...
        report_frame = tk.Label(bottom_frame)
        report_frame.grid(row=0, column=1)

        btn_consultation_report = tk.Button(
            report_frame, text="Consultation Report", command=self.consulReport, width=20, height=2
        )
        btn_consultation_report.grid(row=0, column=0, padx=70, pady=40)

        btn_clear_all = tk.Button(
            report_frame, text="Clear All Fields", command=self.clearAll, width=20, height=2
        )
        btn_clear_all.grid(row=1, column=0)

        btn_exit = tk.Button(report_frame, text="Exit", command=self.exitRoot, width=20, height=2)
        btn_exit.grid(row=2, column=0, pady=40)

    def btnShowPa(self):
        for patient in self.clinic.allPatients:
            self.listbox_patient.insert(tk.END, str(patient))

    def btnShowDoc(self):
        for doctor in self.clinic.allDoctors:
            self.listbox_doctor.insert(tk.END, str(doctor))

    def selectPaDoc(self):
        selectedPatient = self.selPa_label.get()
        selectedDoctor = self.selDoc_label.get()

        if not selectedPatient:
            showwarning("Warning", "Please select a patient.")
            return None, None
        if not selectedDoctor:
            showwarning("Warning", "Please select a doctor.")
            return None, None

        selectedPaName = selectedPatient.split(" ", 1)[1]
        selectedDocName = selectedDoctor.split(" ", 4)[1] + " " + selectedDoctor.split(" ", 4)[2]

        return selectedPaName, selectedDocName

    def selPaLabel(self, selected_patient):
        self.selPa_label.config(state="normal")
        self.selPa_label.delete(0, tk.END)
        self.selPa_label.insert(0, selected_patient)
        self.selPa_label.config(state="readonly")

    def patientSelect(self, event):
        selPatientIndex = event.widget.curselection()
        if selPatientIndex:
            selectedPatient = event.widget.get(selPatientIndex)
            print(selectedPatient)
            self.selPaLabel(selectedPatient)
        else:
            self.selPaLabel.config(text="")

    def selDocLabel(self, selected_doctor):
        self.selDoc_label.config(state="normal")
        self.selDoc_label.delete(0, tk.END)
        self.selDoc_label.insert(0, selected_doctor)
        self.selDoc_label.config(state="readonly")

    def doctorSelect(self, event):
        selDocIndex = event.widget.curselection()
        if selDocIndex:
            selectedDoc = event.widget.get(selDocIndex)
            self.selDocLabel(selectedDoc)
        else:
            self.selDocLabel.config(text="")

    def btnAssignDoc(self):
        selectedPaName, selectedDocName = self.selectPaDoc()

        if selectedPaName and selectedDocName:
            self.clinic.assignDoctor(str(selectedPaName), str(selectedDocName))
            showinfo(
                "Message",
                f"Patient {selectedPaName} is Assigned to Doctor {selectedDocName}!",
            )

    def btnAddConsul(self):
        selectedPaName, selectedDocName = self.selectPaDoc()

        if selectedPaName and selectedDocName:
            conDate = self.date_entry.get()
            conReason = self.reason_entry.get()
            conFee = self.fee_entry.get()

            if not conDate or not conReason or not conFee:
                showwarning("Warning", "Please fill in all consultation details.")
                return

            date_pattern = re.compile(r"^\d{2}/\d{2}/\d{4}$")
            if not date_pattern.match(conDate):
                showwarning("Warning", "Please enter the date in dd/mm/yyyy format.")
                return

            try:
                conFee = float(conFee)
            except ValueError:
                showwarning("Warning", "Consultation fee must be a valid number.")
                return

            conFee = "{:.2f}".format(float(conFee))

            self.clinic.bookConsultation(selectedDocName, selectedPaName, conDate, conReason, conFee)
            showinfo("Message", "The new consultation has been added!")

    def searchPa(self):
        query = self.searchPa_entry.get().lower()
        print(query)
        self.searchResultBox.delete(0, tk.END)

        matchingPatients = self.clinic.searchPatients(query)

        for matchingPatient in matchingPatients:
            self.searchResultBox.insert(tk.END, str(matchingPatient))
            self.searchResultBox.bind("<<ListboxSelect>>", self.patientSelect)

        if not matchingPatients:
            self.searchResultBox.insert(tk.END, "No matching patients found")

    def searchDoc(self):
        query = self.searchDoc_entry.get().lower()
        self.searchResultBox.delete(0, tk.END)

        matchingDocs = self.clinic.searchDoctors(query)

        for matchingDoc in matchingDocs:
            self.searchResultBox.insert(tk.END, str(matchingDoc))
            self.searchResultBox.bind("<<ListboxSelect>>", self.doctorSelect)

        if not matchingDocs:
            self.searchResultBox.insert(tk.END, "No matching Doctors found.")

    def viewPatient(self):
        selPatient = self.selPa_label.get()
        print(selPatient)

        if not selPatient:
            showerror("Error", "Choose a patient first!")
        else:
            selPatientName = selPatient.split(" ", 1)[1]
            foundPatient = self.clinic.findPatient(selPatientName)

            if foundPatient is not None:
                assignedDocName = foundPatient.myDoctor
                print(assignedDocName)

                assignedDoc = self.clinic.findDoctor(assignedDocName)

                patient_info = f"Patient Information\n\n\n"
                patient_info += f"Patient: {foundPatient}\n\n"
                patient_info += f"Doctor: \n{assignedDoc}\n\n"
                patient_info += f"Consultations:\n{foundPatient.consulInfo()}\n\n"
                patient_info += f"Total Fees Due: ${foundPatient.totalconFee()}"

                showinfo("Patient Info", patient_info)
            else:
                showerror("Error", "No matching patient found.")

    def viewDoctor(self):
        selDoc = self.selDoc_label.get()

        if not selDoc:
            showerror("Error", "Choose a doctor first!")
        else:
            foundDocName = selDoc.split(" ", 4)[1] + " " + selDoc.split(" ", 4)[2]
            foundDoc = self.clinic.findDoctor(foundDocName)

            if foundDoc is not None:
                doctor_info = f"Doctor Information\n\n\n"
                doctor_info += f"{foundDoc}\n\n"
                doctor_info += f"Patient List\n{foundDoc.aPatient()}\n"
                doctor_info += f"\nConsultations\n{foundDoc.consulInfo()}\n\n"

                showinfo("Doctor Info", doctor_info)
            else:
                showerror("Error", "No matching doctor found.")

    def consulReport(self):
        if self.clinic.allConsultations:
            report_window = tk.Toplevel(self.root)
            report_window.title("Consultation Report")
            report_window.geometry("600x400")
            report_info = ""
            report_info = "\n\n".join(str(aReport) for aReport in self.clinic.allConsultations)
            report_label = tk.Label(report_window, text=report_info)
            report_label.pack()
        else:
            print("no report")
            showwarning("Warning", "No consultation information.")

    def clearAll(self):
        self.listbox_patient.selection_clear(0, tk.END)
        self.listbox_doctor.selection_clear(0, tk.END)
        self.searchResultBox.delete(0, tk.END)

        self.selPa_label.config(state="normal")
        self.selPa_label.delete(0, tk.END)
        self.selPa_label.config(state="readonly")

        self.selDoc_label.config(state="normal")
        self.selDoc_label.delete(0, tk.END)
        self.selDoc_label.config(state="readonly")

        self.date_entry.delete(0, tk.END)
        self.reason_entry.delete(0, tk.END)
        self.fee_entry.delete(0, tk.END)
        self.searchPa_entry.delete(0, tk.END)
        self.searchDoc_entry.delete(0, tk.END)

    def exitRoot(self):
        showinfo("Close", "Thank you for using Clinic Management System!")
        self.root.destroy()



    
if __name__ == "__main__":
    root = tk.Tk()
    app = clinicManagementApp(root)
    root.mainloop()

