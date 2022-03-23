from src.sorting import sort_by
import pytest


@pytest.fixture
def mockedJobs():
    return [
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2020-07-25",
        },
        {
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2020-04-27",
        },
        {
            "min_salary": 2500,
            "max_salary": 5000,
            "date_posted": "2019-04-25",
        },
        {
            "max_salary": 2005,
            "date_posted": "2020-04-26",
        },
        {
            "max_salary": 2001,
            "date_posted": "2020-04-23",
        },
        {
            "min_salary": 900,
            "date_posted": "2020-04-25",
        },
        {
            "min_salary": 950,
            "max_salary": 1800,
        },
    ]


jobs_sorted_by_min = [
        {
            "min_salary": 900,
            "date_posted": "2020-04-25",
        },
        {
            "min_salary": 950,
            "max_salary": 1800,
        },
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2020-07-25",
        },
        {
            "min_salary": 2500,
            "max_salary": 5000,
            "date_posted": "2019-04-25",
        },
        {
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2020-04-27",
        },
        {
            "max_salary": 2005,
            "date_posted": "2020-04-26",
        },
        {
            "max_salary": 2001,
            "date_posted": "2020-04-23",
        },
    ]


jobs_sorted_by_max = [
        {
            "min_salary": 2500,
            "max_salary": 5000,
            "date_posted": "2019-04-25",
        },
        {
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2020-04-27",
        },
        {
            "max_salary": 2005,
            "date_posted": "2020-04-26",
        },
        {
            "max_salary": 2001,
            "date_posted": "2020-04-23",
        },
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2020-07-25",
        },
        {
            "min_salary": 950,
            "max_salary": 1800,
        },
        {
            "min_salary": 900,
            "date_posted": "2020-04-25",
        },
    ]

jobs_sorted_by_date = [
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2020-07-25",
        },
        {
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2020-04-27",
        },
        {
            "max_salary": 2005,
            "date_posted": "2020-04-26",
        },
        {
            "min_salary": 900,
            "date_posted": "2020-04-25",
        },
        {
            "max_salary": 2001,
            "date_posted": "2020-04-23",
        },
        {
            "min_salary": 2500,
            "max_salary": 5000,
            "date_posted": "2019-04-25",
        },
        {
            "min_salary": 950,
            "max_salary": 1800,
        },
    ]


def test_sort_by_criteria(mockedJobs):
    sort_by(mockedJobs, "min_salary")
    assert mockedJobs == jobs_sorted_by_min
    sort_by(mockedJobs, "max_salary")
    assert mockedJobs == jobs_sorted_by_max
    sort_by(mockedJobs, "date_posted")
    assert mockedJobs == jobs_sorted_by_date

