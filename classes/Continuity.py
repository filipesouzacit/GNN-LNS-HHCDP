import numpy as np
import json


class Continuity:
    def __init__(self, inst, qttPatient, qttCaregiver):
        self.file = 'data/Instances/Instance_' + inst + '/Continuity.json'
        with open(self.file, 'r') as f:
            data = json.load(f)['fidelity']
            self.continuity = np.zeros((qttPatient, qttCaregiver))
            for idPatient, info in data.items():
                for idCaregiver, score in info.items():
                    self.continuity[int(idPatient), int(idCaregiver)] = score

    def getScore(self, idPatient, idCaregiver):
        return self.continuity[idPatient, idCaregiver]
