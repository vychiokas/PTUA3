import datetime


def calculate_holidays(starting_date: datetime.date) -> float:
    today = datetime.date.today()
    return round(
        (today.year - starting_date.year) * 12
        + (today.month - starting_date.month) * 1.6,
        1,
    )


date = datetime.date(2023, 1, 1)
print(calculate_holidays(date))
