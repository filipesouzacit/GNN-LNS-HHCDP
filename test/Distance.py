from classes.Distance import Distance
dist = Distance('data/DistanceSpeedDuration.txt')

assert(dist.getDistance(0, 1) == 7.595)
assert(dist.getSpeed(0, 1) == 0.614151)
assert(dist.getDuration(0, 1) == 12.3667)
assert(sum(dist.getAll3(0, 1)) == sum([7.595, 0.614151, 12.3667]))

