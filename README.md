# Bengali Transformer
[![Build Status](https://travis-ci.org/sagorbrur/bntransformer.svg?branch=master)](https://travis-ci.org/sagorbrur/bntransformer)

Bengali Transformer for natural language processing using state of the art transformer(language model)

Thanks to huggingface [transformers](https://github.com/huggingface/transformers)

## Installation
```
pip install bntransformer
```

## Tokenizer
### Bert Multilingual Tokenizer

  ```py
  from bntransformer.bnbert import Tokenizer

  tokenizer = Tokenizer()
  tokens = tokenizer.tokenize('আমি ভাত খাই।')
  print(tokens)
  # output: ['আ', '##মি', 'ভ', '##াত', 'খা', '##ই', '।']
  ```

  Encode Ids from text

  ```py
  from bntransformer.bnbert import Tokenizer

  tokenizer = Tokenizer()
  encode_ids = tokenizer.encode('আমি ভাত খাই।')
  print(encode_ids)
  # output: [101, 938, 37376, 971, 43004, 80501, 14998, 920, 102]
  ```
    
   Decode Ids from text
   
   ```py
   from bntransformer.bnbert import Tokenizer

   tokenizer = Tokenizer()
   decode_text = tokenizer.decode([101, 938, 37376, 971, 43004, 80501, 14998, 920, 102])
   print(decode_text)
   # output: [CLS] আমি ভাত খাই । [SEP]
   
   ```
    


