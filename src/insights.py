from src.jobs import read


def get_unique_job_types(path):
    jobTypes = []
    allJobs = read(path)
    for job in allJobs:

        if job['job_type'] not in jobTypes:
            jobTypes.append(job['job_type'])

    return jobTypes


def filter_by_job_type(jobs, job_type):
    filteredJobs = [
        job
        for job in jobs if job['job_type'] == job_type
    ]

    return filteredJobs


def get_unique_industries(path):
    industries = []
    allJobs = read(path)
    for job in allJobs:

        if job['industry'] not in industries and len(job['industry']) > 0:
            industries.append(job['industry'])

    return industries


def filter_by_industry(jobs, industry):
    filteredJobs = [
        job
        for job in jobs if job['industry'] == industry
    ]

    return filteredJobs


def get_max_salary(path):
    maxSalary = []
    allJobs = read(path)
    allSalaries = [
        int(job['max_salary'])
        for job in allJobs if job['max_salary'].isdigit()
    ]
    maxSalary = max(allSalaries)

    return maxSalary


def get_min_salary(path):
    minSalary = []
    allJobs = read(path)
    allSalaries = [
        int(job['min_salary'])
        for job in allJobs if job['min_salary'].isdigit()
    ]
    minSalary = min(allSalaries)

    return minSalary


def validateNumber(number):
    return not isinstance(number, int) or number < 0


def matches_salary_range(job, salary):

    if 'max_salary' not in job.keys() or 'min_salary' not in job.keys():
        raise ValueError
    elif validateNumber(job['max_salary']) or validateNumber(
            job['min_salary']):
        raise ValueError
    elif not isinstance(salary, int):
        raise ValueError
    elif job['max_salary'] < job['min_salary']:
        raise ValueError
    else:
        return job['max_salary'] >= salary >= job['min_salary']


def does_match_salary_range(job, salary):

    if 'max_salary' not in job.keys() or 'min_salary' not in job.keys():
        return False
    elif validateNumber(job['max_salary']) or validateNumber(
            job['min_salary']):
        return False
    elif not isinstance(salary, int):
        return False
    elif job['max_salary'] < job['min_salary']:
        return False
    else:
        return True


def filter_by_salary_range(jobs, salary):
    validJobs = [
        job
        for job in jobs if does_match_salary_range(job, salary)
    ]
    filteredJobs = [
        job
        for job in validJobs if
        job['max_salary'] >= salary >= job['min_salary']
    ]

    return filteredJobs
