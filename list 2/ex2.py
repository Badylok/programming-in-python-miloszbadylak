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


# Tests for patient


def test_patient():
    """
    Tests the Patient class by validating type checks in the constructor and verifying the admit and discharge methods.
    """

    try:
        Patient(123, "12 feb 2006", 1001, "Diabetes", True)
        assert False
    except TypeError:
        pass

    try:
        Patient("Miłosz", 2006, 1001, "Diabetes", True)
        assert False
    except TypeError:
        pass

    try:
        Patient("Miłosz", "12 feb 2006", "1001", "Diabetes", True)
        assert False
    except TypeError:
        pass

    try:
        Patient("Miłosz", "12 feb 2006", 1001, 1004, True)
        assert False
    except TypeError:
        pass

    try:
        Patient("Miłosz", "12 feb 2006", 1001, "Diabetes", "Tak")
        assert False
    except TypeError:
        pass

    testPatient = Patient("Miłosz", "12.02.2006", 4747, "Diabetes", False)

    testPatient.admit()
    assert testPatient.admitted == True

    testPatient.discharge()
    assert testPatient.admitted == False

    print("\nAll tests for patient passed.")


# Hospital


class Hospital:
    """
    Represents a hospital.

    Attributes:
        name (str): Name of the hospital

    Raises:
        TypeError: If 'name' is not a string.
    """

    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("'name' must be a string.")
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        """
        Asings the patient to the hospital.
        """
        self.patients.append(patient)

    def discharge_patient(self, id):
        """
        Discharges the patient from the hostipal by their id.
        """
        for patient in self.patients:
            if patient.patient_id == id:
                patient.discharge()

    def get_patient_list(self):
        """
        Returns a list of id's of patients admitted to the hospital.
        """
        admitted_ids = []

        for patient in self.patients:
            if patient.admitted == True:
                admitted_ids.append(patient.patient_id)

        return admitted_ids


# Tests for hospital


def test_hospital():
    """
    Tests the Hospital class functions.
    """

    try:
        Hospital(123)
        assert False
    except TypeError:
        pass

    new_hospital = Hospital("Szpital Kliniczny")
    new_patient = Patient("Miłosz", "12.02.2006", 1111, "Diabetes", False)
    new_patient2 = Patient("Jakub", "12.02.2016", 2222, "Cancer", False)

    new_hospital.add_patient(new_patient)
    new_hospital.add_patient(new_patient2)

    print("\nBefore admitting: \n", new_hospital.get_patient_list())
    assert new_hospital.get_patient_list() == []

    new_patient.admit()
    new_patient2.admit()
    print("\nAfter admitting both patients: \n", new_hospital.get_patient_list())
    assert new_hospital.get_patient_list() == [1111, 2222]

    new_hospital.discharge_patient(new_patient.patient_id)
    print("\nAfter discharging first patient: \n", new_hospital.get_patient_list())
    assert new_hospital.get_patient_list() == [2222]

    print("\nAll tests for Hospital passed.")


test_patient()
test_hospital()
