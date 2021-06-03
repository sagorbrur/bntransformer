import unittest
from bntransformer.tokenizer import BanglaTokenizer

class TestTokenizer(unittest.TestCase):
    
    def test_tokenizer(self):
        tokenizer = BanglaTokenizer()
        tokens = tokenizer.tokenize('আমি ভাত খাই।')
        self.assertEqual(tokens, ['আমি', 'বাংলা', '##য', 'গান', 'গাই', '।']) 

if __name__ == '__main__':
    unittest.main()
