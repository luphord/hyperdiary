from typing import List

MONTHS_EN = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November',
             'December']


class Localization:
    def __init__(self, months: List[str]=MONTHS_EN) -> None:
        self.months = months

    def get_month(self, i: int) -> str:
        '''Get the localized name of month i (zero-based index)
           >>> l = Localization()
           >>> l.get_month(0)
           'January'
           >>> l.get_month(11)
           'December'
           >>> l.get_month(12)
           Traceback (most recent call last):
           ...
           AssertionError
        '''
        assert i >= 0
        assert i < 12
        return self.months[i]
