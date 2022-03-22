from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobNames = []
    with open(path) as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs:
            jobNames.append(job)
    return jobNames
