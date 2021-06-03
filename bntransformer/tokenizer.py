
from transformers import AutoTokenizer

class BanglaTokenizer:
    def __init__(self, model_path=None):
        if not model_path:
            model_path = "sagorsarker/bangla-bert-base"
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

    def tokenize(self, text):
        tokens = self.tokenizer.tokenize(text)
        return tokens

    def encode(self, text):
        encode_ids = self.tokenizer.encode(text, add_special_tokens=True)
        return encode_ids

    def decode(self, encode_id_list):
        decode_text = self.tokenizer.decode(encode_id_list)
        return decode_text
