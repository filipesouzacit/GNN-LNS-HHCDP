import numpy as np


class Location:
    def __init__(self, fileLoc):
        self.fileLoc = fileLoc
        with open(self.fileLoc, 'r') as f:
            lines = f.readlines()
            self.qttLocation = len(lines)-1
            self.location = np.empty(self.qttLocation)
            for line in lines[1:]:
                l = line.split(',')
                self.location[int(l[0])] = int(l[1])

    def getZone(self, IdLoc):
        return self.location[IdLoc]
