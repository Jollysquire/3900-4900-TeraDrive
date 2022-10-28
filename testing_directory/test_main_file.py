import unittest
from unittest import TestCase
import src.main


from ast import arg
import os
import sys
from pathlib import Path
import logging
from os.path import getsize
from src.hex import CheckFile
from src.main import DirToArray

class TestMain(TestCase):

    def test_dir_to_array(self):
        self.assertTrue(src.mainmain.DirToArray())

    def test_make_HTML(self):
        self.assertTrue(src.main.make_HTML())
        
        pass

    def test_main(self):
        self.assertTrue(src.main.main())

        pass

if __name__ == '__main__':
    unittest.main()