# Bengali Transformer
Bengali Transformer for natural language processing using state of the art transformer(language model)

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
