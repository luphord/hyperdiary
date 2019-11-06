from datetime import date
from .diary import Diary


def view(diary: Diary, dt: date) -> None:
    print(dt)
    for line in diary[dt].lines:
        print('- ' + str(line))
