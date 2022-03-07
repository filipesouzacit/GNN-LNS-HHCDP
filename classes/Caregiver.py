import numpy as np
import json


class Caregiver:
    def __init__(self, inst):
        self.file = 'data/Instances/Instance_' + inst + '/Caregiver.json'
        with open(self.file, 'r') as f:
            data = json.load(f)
            self.qttCaregiver = len(data)
            self.caregiver = [0] * self.qttCaregiver
            for idCaregiver, info in data.items():
                self.caregiver[int(idCaregiver)] = info

    def getCaregiver(self, idCaregiver):
        return self.caregiver[idCaregiver]
