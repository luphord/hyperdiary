#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from pathlib import Path

from hyperdiary import parser, Diary


def in_test_folder(relative_path):
    return Path(__file__).parent / relative_path


class TestHyperdiary(unittest.TestCase):

    def test_command_line_interface(self):
        self.assertEqual('check', parser.parse_args(['check']).subcommand)
    
    def test_loading_of_entries(self):
        diary = Diary.discover(in_test_folder('src'))
        diary.load_entries()
        self.assertGreaterEqual(len(diary.entries), 3)
