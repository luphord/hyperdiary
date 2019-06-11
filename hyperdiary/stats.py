import yaml
from sys import argv
from argparse import ArgumentParser
from collections import OrderedDict

from .diary import find_tags, find_ids, iter_entries, load_all

def stats(args):
    if args.file:
      with open(args.file) as f:
        y = yaml.load(f, Loader=yaml.SafeLoader)
    else:
      y = load_all()

    output = OrderedDict()
    output['# Days'] = len(y)
    output['# Entries'] = sum(len(v) for v in y.values())
    output['# Taggings'] = sum(len(find_tags(l)) for d, l, t in iter_entries(y))
    output['# Identification'] = sum(len(find_ids(l)) for d, l, t in iter_entries(y))

    for key, val in output.items():
      print('{:.<20}{:.>5}'.format(key, val))
