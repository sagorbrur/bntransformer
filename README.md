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
