from classes.Caregiver import Caregiver
dist = Caregiver('01')

assert(dist.getCaregiver(0)["max_work_time_week"] == 2103)
assert(dist.getCaregiver(2)["min_work_time_week"] == 129)
assert(dist.getCaregiver(4)["location"] == 103)
