# bntransformer
[![Build Status](https://travis-ci.org/sagorbrur/bntransformer.svg?branch=master)](https://travis-ci.org/sagorbrur/bntransformer)
[![PyPI version](https://img.shields.io/pypi/v/bntransformer)](https://pypi.org/project/bntransformer/)

`bntransformer` build with [transformers](https://github.com/huggingface/transformers) for different transformer based inference task for Bengali language.



## Installation
```
pip install bntransformer

or

pip install -U bntransformer
```

## Dependency
- **pytorch(1.6+)**

## Usage
### Usage Notes
- All below task are using default model for Bengali tokenization, question answering, name entity recognition, translation, text generation. You can find default model link [here](#Default-Inference-Models). 

- You can pass your own trained **local transformers model** or **huggingface model hub model**. All you need to pass that model while calling the base class.

- **Example:** while calling `BanglaQA` class you can simple use default model for inference as `bnqa = BanglaQA()` or you can pass another model like `bnqa = BanglaQA("another_model")`
- You can find an example colab notebook under [examples](examples/)

### Tokenization

```py
from bntransformer import BanglaTokenizer

bntokenizer = BanglaTokenizer() 
# you can pass custom model path or other bengali huggingface model path
# example: bntokenizer = BanglaTokenizer("bert-base-multilingual-uncased")
# default it takes "sagorsarker/bangla-bert-base"
text = "আমি বাংলায় গান গাই ।"
tokens = bntokenizer.tokenize(text)
print(tokens)
# outputs: ['আমি', 'বাংলা', '##য', 'গান', 'গাই', '।']
encode_ids = bntokenizer.encode(text)
print(encode_ids)
decode_text = bntokenizer.decode(encode_ids)
print(decode_text)

```

### Bangla Question Answering
```py
from bntransformer import BanglaQA

bnqa = BanglaQA()
# you can pass custom QA model path or other bengali huggingface QA model path
# default it takes "sagorsarker/mbert-bengali-tydiqa-qa"
context = "সূর্য সেন ১৮৯৪ সালের ২২ মার্চ চট্টগ্রামের রাউজান থানার নোয়াপাড়ায় অর্থনৈতিক ভাবে অস্বচ্ছল পরিবারে জন্মগ্রহণ করেন। তাঁর পিতার নাম রাজমনি সেন এবং মাতার নাম শশী বালা সেন। রাজমনি সেনের দুই ছেলে আর চার মেয়ে। সূর্য সেন তাঁদের পরিবারের চতুর্থ সন্তান। দুই ছেলের নাম সূর্য ও কমল। চার মেয়ের নাম বরদাসুন্দরী, সাবিত্রী, ভানুমতী ও প্রমিলা। শৈশবে পিতা মাতাকে হারানো সূর্য সেন কাকা গৌরমনি সেনের কাছে মানুষ হয়েছেন। সূর্য সেন ছেলেবেলা থেকেই খুব মনোযোগী ভাল ছাত্র ছিলেন এবং ধর্মভাবাপন্ন গম্ভীর প্রকৃতির ছিলেন।"
question = "মাস্টারদা সূর্যকুমার সেনের বাবার নাম কী ছিল ?"

answers = bnqa.find_answer(context, question)
print(answers)
# output: {'score': 0.8070710301399231, 'start': 131, 'end': 141, 'answer': 'রাজমনি সেন'}

```

### Bangla NER
```py
from bntransformer import BanglaNER

bnner = BanglaNER()
# you can pass custom NER model path or other bengali huggingface NER model path
# default it takes "neuropark/sahajBERT-NER"
sentence = "আমি জাহিদ হাসান এবং আমি ঢাকায় বাস করি ।"
output = bnner.ner_tag(sentence)
print(output)

```

### Bangla Mask Generation
```py
from bntransformer import BanglaMaskGeneration

bnunmasker = BanglaMaskGeneration()
# you can pass custom mask generation model path or other bengali huggingface model path
# default it takes "sagorsarker/bangla-bert-base"
sentence = "আমি জাহিদ হাসান এবং আমি [MASK] বাস করি । "
output = bnunmasker.generate_mask(sentence)
print(output)
```

### Bangla To English Translation
```py
from bntransformer import BanglaTranslation

bntrans = BanglaTranslation()
# you can pass custom translation model path or other bengali huggingface translation model path
# default it takes "Helsinki-NLP/opus-mt-bn-en"
bn_sentence = "আমার নাম জাহিদ, আমি ঢাকায় বাস করি।"
output = bntrans.bn2en(bn_sentence)
print(output)
# output: My name is Zahid, I live in Dhaka.

```

### Bangla Text Generation
```py
from bntransformer import BanglaTextGeneration

bntrans = BanglaTextGeneration()
# you can pass custom text generation model path or other bengali huggingface Bengali text gen model path
# default it takes "flax-community/gpt2-bengali"
input_text = "আমি রতন এবং আমি"
output = bntrans.generate_text(input_text)
print(output)
```

## Default Inference Models
- [Question Answering](https://huggingface.co/sagorsarker/mbert-bengali-tydiqa-qa)
- [Name Entity Recognition](https://huggingface.co/neuropark/sahajBERT-NER)
- [Mask Generation](https://huggingface.co/sagorsarker/bangla-bert-base)
- [Translation](https://huggingface.co/Helsinki-NLP/opus-mt-bn-en)
- [Text Generation](https://huggingface.co/flax-community/gpt2-bengali)

NB: Or you can use custom model local model path or other huggingface model path while calling the base class

