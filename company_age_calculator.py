import datetime


def calculate_company_age():
    foundation_year = datetime.datetime(year=1920, month=1, day=21)
    today = datetime.date.today()
    company_age = today.year - foundation_year.year
    return company_age
