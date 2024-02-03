import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test('"abc\t"','abc,<EOF>',101))
        self.assertTrue(TestLexer.test("1234567",'1234567,<EOF>',102))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    