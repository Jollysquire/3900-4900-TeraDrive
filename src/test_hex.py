import unittest
from hex import CheckFile


class TestCheckFile(unittest.TestCase):

    def test_get_hex(self):
        
        input = CheckFile.get_hex(self, './testing_dir/test.avi')
        output = ('', '.avi')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.doc')
        output = ('', '.doc')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.flv')
        output = ('', '.flv')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.pdf')
        output = ('', '.pdf')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.png')
        output = ('', '.png')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.wmv')
        output = ('', '.wmv')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.xls')
        output = ('', '.xls')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.rar')
        output = ('', '.rar')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.zip')
        output = ('', '.zip')
        self.assertEqual(input, output)
        
        input = CheckFile.get_hex(self, './testing_dir/test.zip')
        output = ('', '.rar')
        self.assertNotEqual(input, output)

        input = CheckFile.get_hex(self, './testing_dir/test.rar')
        output = ('', '.zip')
        self.assertNotEqual(input, output)
    
    def test_check_data(self):        
        input = CheckFile.check_data(self, '89504E470D0A1A0A', 'png')
        self.assertIsNone(input)
        
        input = CheckFile.check_data(self, '504B0304', 'docx')
        self.assertIsNone(input)
        
        input = CheckFile.check_data(self, '52494646', 'wav')
        self.assertIsNone(input)
        
        input = CheckFile.check_data(self, '52617221A0700', 'rar')
        self.assertIsNone(input)


if __name__ == '__main__':
    unittest.main()