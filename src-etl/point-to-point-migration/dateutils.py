import datetime

DATE_FORMAT = r"%Y%m%d"


def today():
    return datetime.date.today().strftime(DATE_FORMAT)


def yesterday():
    return (datetime.date.today() + datetime.timedelta(days=-1)).strftime(DATE_FORMAT)


def all_days_since_last_month(end_date: str):
    end_date = datetime.datetime.strptime(end_date, DATE_FORMAT).date()
    to_add = end_date + datetime.timedelta(days=-30)
    res = []
    while True:
        res.append(to_add.strftime(DATE_FORMAT))
        to_add += datetime.timedelta(days=1)
        if to_add == end_date:
            break
    return res
