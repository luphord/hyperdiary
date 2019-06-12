from .diary import Diary
from datetime import date, timedelta

def view(date):
    entries = Diary.discover_and_load().entries
    print(date)
    for line in entries[date]:
        print('- ' + str(line))
