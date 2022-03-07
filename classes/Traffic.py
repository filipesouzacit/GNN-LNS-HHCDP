import numpy as np


class Traffic:
    def __init__(self, fileTraf):
        self.fileTraf = fileTraf
        with open(self.fileTraf, 'r') as f:
            lines = f.readlines()
            self.qttZones = int(lines[0].split(':')[1])
            self.qttSection = int(lines[1].split(':')[1])
            self.traffic = np.empty((self.qttZones, self.qttZones, self.qttSection))
            for line in lines[4:]:
                l = line.split(',')
                self.traffic[int(l[0]), int(l[1]), int(l[2])] = l[3]

    def getTraffic(self, _from, _to, section):
        return self.traffic[_from, _to, section]
