from collections import OrderedDict
from typing import Dict, List
from .diary import find_tags, find_ids, iter_entries, DayEntry


def stats(entries: List[DayEntry]) -> Dict[str, int]:
    output = OrderedDict()  # type: Dict[str, int]
    output['# Days'] = len(entries)
    output['# Entries'] = sum(len(entry.lines) for entry in entries)
    output['# Taggings'] = sum(len(list(find_tags(l)))
                               for d, l in iter_entries(entries))
    output['# Identification'] = sum(len(list(find_ids(l)))
                                     for d, l in iter_entries(entries))

    for key, val in output.items():
        print('{:.<20}{:.>5}'.format(key, val))

    return output
