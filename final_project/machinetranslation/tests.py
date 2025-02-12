'''
importing modules
'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Love'), 'Aimer')

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Aimer'), 'Love')

unittest.main()