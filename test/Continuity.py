from classes.Continuity import Continuity
dist = Continuity('01', 40, 5)

assert(dist.getScore(8, 2) == 4)
assert(dist.getScore(9, 2) == 0)
assert(dist.getScore(10, 1) == 3)
