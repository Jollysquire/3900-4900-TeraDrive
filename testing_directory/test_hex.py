from unittest import TestCase
from src.hex import CheckFile

class TestCheckFile(TestCase):

    def test_get_hex(self):

        input = CheckFile.get_hex(self, "./testing_files/test_word_doc.docx")
        output = ('', '.docx')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/test_pdf.pdf")
        output = ('', '.pdf')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/test_excel_sheet.xlsx")
        output = ('', '.xlsx')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/test_powerpoint.pptx")
        output = ('', '.pptx')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/bald-eagle.jpg")
        output = ('', '.jpg')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/bald-eagle-PNG.png")
        output = ('', '.png')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/eagle.gif")
        output = ('', '.gif')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/me-at-the-zoo.mp3")
        output = ('', '.mp3')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/me-at-the-zoo.wav")
        output = ('', '.wav')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/me-at-the-zoo.avi")
        output = ('', '.avi')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/me-at-the-zoo.mp4")
        output = ('', '.mp4')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/me-at-the-zoo.mov")
        output = ('', '.mov')
        self.assertEqual(input, output)

        input = CheckFile.get_hex(self, "./testing_files/me-at-the-zoo.wmv")
        output = ('', '.wmv')
        self.assertEqual(input, output)

    def test_check_data(self):

        input = CheckFile.check_data(self, "504B0304", "docx")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "25504446", "pdf")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "504B0304", "xlsx")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "504B0304", "pptx")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "FFD8", "jpg")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "89504E470D0A1A0A", "png")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "474946383761", "gif")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "494433", "mp3")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "52494646", "wav")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "52494646", "avi")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "66747970", "mp4")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "66747970", "mov")
        self.assertIsNone(input)

        input = CheckFile.check_data(self, "3026B2", "wmv")
        self.assertIsNone(input) 

