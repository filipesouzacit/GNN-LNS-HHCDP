from classes.Location import Location
dist = Location('data/Location.txt')

assert(dist.getZone(10) == 7)
assert(dist.getZone(6) == 4)
assert(dist.getZone(36) == 6)
