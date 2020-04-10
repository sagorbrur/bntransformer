
from transformers import BertModel, BertTokenizer
#import torch

class Tokenizer(object):
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

    def tokenize(self, text):
        tokens = self.tokenizer.tokenize(text)

        return tokens

    def encode(self, text):
        encode_ids = self.tokenizer.encode(text, add_special_tokens=True)
        return encode_ids

    def decode(self, encode_id_list):
        decode_text = self.tokenizer.decode(encode_id_list)
        return decode_text
