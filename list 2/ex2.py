from datetime import date


class Patient:
    """
    Represents a patient.

    Attributes:
        name (str): Name of the patient
        dob (str or date): Patient's date of birth.
        patient_id (int): Unique patient identifier.
        diagnosis (str): Name of the diagnosis.
        admitted (bool): A status indicating whether the patient is currently admitted.
    """

    def __init__(self, name, dob, patient_id, diagnosis, admitted):
        """
        A constructor which creates a patient.

        Args:
            name (str): Name of the patient.
            dob (str or date): Patient's date of birth.
            patient_id (int): Unique patient identifier.
            diagnosis (str): Name of the diagnosis.
            admitted (bool): A status indicating whether the patient is currently admitted.

        Raises:
            TypeError: If name is not a string. If dob is not a string or date. If patient_id is not an int. If diagnosis is not a string. If admitted is not a boolean.
        """

        if not isinstance(name, str):
            raise TypeError("'Name' must be a string.")
        if not isinstance(dob, (str, date)):
            raise TypeError("'Date of birth' must be a string or date.")
        if not isinstance(patient_id, int):
            raise TypeError("'Patient ID' must be an integer.")
        if not isinstance(diagnosis, str):
            raise TypeError("'Diagnosis' must be a string.")
        if not isinstance(admitted, bool):
            raise TypeError("'Admitted' must be a boolean.")

        self.name = name
        self.dob = dob
        self.patient_id = patient_id
        self.diagnosis = diagnosis
        self.admitted = admitted


    def admit(self):
        """
        Admits the patient to the hospital.
        """
        self.admitted = True
        
    def discharge(self):
        """
        Discharges the patient from the hospital.
        """
        self.admitted = False
        
    def __str__(self):
        """
        Returns formatted information about the patient.
        """
        return f"Patient: \n-Name: {self.name} \n-Date of birth: {self.dob} \n-ID: {self.patient_id} \n-Diagnosis: {self.diagnosis} \n-Admitted?: {self.admitted}"
        