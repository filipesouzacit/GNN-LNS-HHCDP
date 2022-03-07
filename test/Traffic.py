from classes.Traffic import Traffic
dist = Traffic('../data/Traffic_Indexes.txt')

assert(dist.getTraffic(0, 3, 13) == 0.9)
assert(dist.getTraffic(7, 5, 268) == 1)
assert(dist.getTraffic(11, 12, 14) == 0.85)
