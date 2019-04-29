#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from hyperdiary import main


class TestHyperdiary(unittest.TestCase):

    def test_command_line_interface(self):
        main()
