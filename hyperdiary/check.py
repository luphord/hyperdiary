from datetime import date, timedelta
from .diary import Diary

def check():
    entries = Diary.discover_and_load().entries

    current = date(2016,1,5)
    today = date.today()
    one_day = timedelta(days=1)

    number_of_days = 0
    while current < today:
        if not current in entries:
            raise Exception('Missing entry {}'.format(current))
        current += one_day
        number_of_days += 1

    print('OK found {} days'.format(number_of_days))
