import numpy as np


class Distance:
    def __init__(self, fileDist):
        self.fileDist = fileDist
        with open(self.fileDist, 'r') as f:
            lines = f.readlines()
            self.qttLocation = int(lines[0].split(' ')[2])
            self.distance = np.empty((self.qttLocation, self.qttLocation, 3))
            for line in lines[3:]:
                l = line.split(',')
                self.distance[int(l[0]), int(l[1]), :] = l[2:5]

    def getDistance(self, _from, _to):
        return self.distance[_from, _to, 0]

    def getSpeed(self, _from, _to):
        return self.distance[_from, _to, 1]

    def getDuration(self, _from, _to):
        return self.distance[_from, _to, 2]

    def getAll3(self, _from, _to):
        return self.distance[_from, _to, :]
