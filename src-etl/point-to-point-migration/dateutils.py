import datetime

DATE_FORMAT = r"%Y%m%d"


def today():
    return datetime.date.today().strftime(DATE_FORMAT)


def yesterday():
    return (datetime.date.today() + datetime.timedelta(days=-1)).strftime(DATE_FORMAT)


def all_dates_since_last_month(end_date_not_inclusive: str):
    end_date_not_inclusive = datetime.datetime.strptime(end_date_not_inclusive, DATE_FORMAT).date()
    to_add = end_date_not_inclusive + datetime.timedelta(days=-30)
    res = []
    while True:
        res.append(to_add.strftime(DATE_FORMAT))
        to_add += datetime.timedelta(days=1)
        if to_add == end_date_not_inclusive:
            break
    return res


def from_date_to_date(begin_date: str, end_date: str):
    end_date_not_inclusive = datetime.datetime.strptime(end_date, DATE_FORMAT).date()
    to_add = datetime.datetime.strptime(begin_date, DATE_FORMAT).date()
    res = []
    while True:
        to_add += datetime.timedelta(days=1)
        res.append(to_add.strftime(DATE_FORMAT))
        if to_add == end_date_not_inclusive:
            break
    return res
