import unittest
import main

from ast import arg
import os
import sys
import datetime
import argparse
from pathlib import Path
import logging
from os.path import getsize
from hex import CheckFile
from src.main import DirToArray


class TestMain(unittest.TestCase):
    
    def test_DirToArray(self):
        self.assertTrue(main.DirToArray())
        pass
    
    def test_make_HTML(self):
        pass
    
    def test_main(self):
        self.assertTrue(main.main, )
        pass

if __name__ == '__main__':
    unittest.main()