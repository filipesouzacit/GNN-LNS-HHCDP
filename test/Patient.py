from classes.Patient import Patient
dist = Patient('01')

assert (dist.getPatient(4)['location'] == 119)

assert (dist.getPatient(13)['service_duration'] == 43)
