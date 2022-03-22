from src.jobs import read


def get_unique_job_types(path):
    jobTypes = []
    allJobs = read(path)
    for job in allJobs:

        if job['job_title'] not in jobTypes:
            jobTypes.append(job['job_title'])

    return jobTypes


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    industries = []
    allJobs = read(path)
    for job in allJobs:

        if job['industry'] not in industries and len(job['industry']) > 0:
            industries.append(job['industry'])

    return industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
