import numpy as np
import json


class Patient:
    def __init__(self, inst):
        self.file = 'data/Instances/Instance_' + inst + '/Patient.json'
        with open(self.file, 'r') as f:
            data = json.load(f)
            self.qttPatient = len(data)
            self.patient = [0] * self.qttPatient
            for idPatient, info in data.items():
                self.patient[int(idPatient)] = info

    def getPatient(self, idPatient):
        return self.patient[idPatient]
