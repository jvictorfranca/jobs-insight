from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobsNames = []
    with open(path) as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs:
            jobsNames.append(job)
    return jobsNames
