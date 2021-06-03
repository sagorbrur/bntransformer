# BNTRANSFORMERS
[![Build Status](https://travis-ci.org/sagorbrur/bntransformer.svg?branch=master)](https://travis-ci.org/sagorbrur/bntransformer)
[![PyPI version](https://img.shields.io/pypi/v/bntransformer)](https://pypi.org/project/bntransformer/)

`bntransformer` build with [transformers](https://github.com/huggingface/transformers) for different transformer based inference task for Bengali language.



## Installation
```
pip install bntransformer

or

pip install -U bntransformer
```

## Usage

### Tokenization

```py
from bntransformer import BanglaTokenizer

bntokenizer = BanglaTokenizer() 
# you can custom model path or other bengali huggingface model path
# default it takes "sagorsarker/bangla-bert-base"
text = "আমি বাংলায় গান গাই ।"
tokens = bntokenizer.tokenize(text)
print(tokens)
# outputs: ['আমি', 'বাংলা', '##য', 'গান', 'গাই', '।']

```

### Bangla Question Answering
```py
from bntransformer import BanglaQA

bnqa = BanglaQA()
# you can custom model path or other bengali huggingface model path
# default it takes "sagorsarker/mbert-bengali-tydiqa-qa"
context = "সূর্য সেন ১৮৯৪ সালের ২২ মার্চ চট্টগ্রামের রাউজান থানার নোয়াপাড়ায় অর্থনৈতিক ভাবে অস্বচ্ছল পরিবারে জন্মগ্রহণ করেন। তাঁর পিতার নাম রাজমনি সেন এবং মাতার নাম শশী বালা সেন। রাজমনি সেনের দুই ছেলে আর চার মেয়ে। সূর্য সেন তাঁদের পরিবারের চতুর্থ সন্তান। দুই ছেলের নাম সূর্য ও কমল। চার মেয়ের নাম বরদাসুন্দরী, সাবিত্রী, ভানুমতী ও প্রমিলা। শৈশবে পিতা মাতাকে হারানো সূর্য সেন কাকা গৌরমনি সেনের কাছে মানুষ হয়েছেন। সূর্য সেন ছেলেবেলা থেকেই খুব মনোযোগী ভাল ছাত্র ছিলেন এবং ধর্মভাবাপন্ন গম্ভীর প্রকৃতির ছিলেন।"
question = "মাস্টারদা সূর্যকুমার সেনের বাবার নাম কী ছিল ?"

answers = bnqa.find_answer(context, question)
print(answer)
# output: {'score': 0.8070710301399231, 'start': 131, 'end': 141, 'answer': 'রাজমনি সেন'}

```

### Bangla NER
```py
from bntransformer import BanglaNER

bnner = BanglaNER()
# you can custom model path or other bengali huggingface model path
# default it takes "neuropark/sahajBERT-NER"
sentence = "আমি জাহিদ হাসান এবং আমি ঢাকায় বাস করি ।"
output = bnner.ner_tag(sentence)
print(output)

```

### Bangla Mask Generation
```py
from bntransformer import BanglaMaskGeneration

bnunmasker = BanglaMaskGeneration()
# you can custom model path or other bengali huggingface model path
# default it takes "sagorsarker/bangla-bert-base"
sentence = "আমি জাহিদ হাসান এবং আমি [MASK] বাস করি । "
output = bnunmasker.generate_mask(sentence)
print(output)
```

### Bangla To English Translation
```py
from bntransformer import BanglaTranslation

bntrans = BanglaTranslation()
# you can custom model path or other bengali huggingface model path
# default it takes "Helsinki-NLP/opus-mt-bn-en"
bn_sentence = "আমার নাম জাহিদ, আমি ঢাকায় বাস করি।"
output = bntrans.bn2en(bn_sentence)
print(output)
# output: My name is Zahid, I live in Dhaka.

```


