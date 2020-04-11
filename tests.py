import unittest
from bntransformer.bnbert import Tokenizer

class TestTokenizer(unittest.TestCase):
    
    def test_tokenizer(self):
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize('আমি ভাত খাই।')
        self.assertEqual(tokens, ['আ', '##মি', 'ভ', '##াত', 'খা', '##ই', '।'])    

if __name__ == '__main__':
    unittest.main()
