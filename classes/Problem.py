from classes.Caregiver import Caregiver
from classes.Continuity import Continuity
from classes.Distance import Distance
from classes.Location import Location
from classes.Patient import Patient
from classes.Traffic import Traffic


class Problem:
    def __init__(self, instance):
        self.distance = Distance('data/DistanceSpeedDuration.txt')
        self.location = Location('data/Location.txt')
        self.traffic = Traffic('data/Traffic_Indexes.txt')
        self.patient = Patient(instance)
        self.caregiver = Caregiver(instance)
        self.continuity = Continuity(instance, self.patient.qttPatient, self.caregiver.qttCaregiver)
