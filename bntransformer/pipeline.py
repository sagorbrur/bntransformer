import copy
from bntransformer.utils import entity_map
from transformers import (
    AutoModelForQuestionAnswering, 
    AutoModelForTokenClassification,
    AutoModelWithLMHead,
    AutoTokenizer,
    pipeline,
)

class BanglaQA:
    def __init__(self, model_path=None):
        if not model_path:
            model_path = "sagorsarker/mbert-bengali-tydiqa-qa"
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.nlp = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)

    def find_answer(self, context, question):
        qa_input = {
            'question': question,
            'context': context
        }
        result = self.nlp(qa_input)

        return result

class BanglaNER:
    def __init__(self, model_path=None):
        if not model_path:
            model_path = "neuropark/sahajBERT-NER"
        self.model = AutoModelForTokenClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer, grouped_entities=True)

    def get_updated_ner_results(self, ner_results, entity_maps):
        updated_ner_results = []
        for entity in ner_results:
            entity_group = int(entity['entity_group'])
            word = entity['word']
            start = entity['start']
            end = entity['end']
            score = entity['score']
            if entity_group in entity_maps:
                label = entity_maps[entity_group]
                updated_ner_result = {
                    "entity": label,
                    "score": score,
                    "word": word,
                    "start": start,
                    "end": end
                }
                updated_ner_results.append(updated_ner_result)
        return updated_ner_results
    
    def ner_tag(self, sentence, data_type="wikiann"):
        ner_results = self.nlp(sentence)
        if data_type=="wikiann":
            entity_maps = copy.deepcopy(entity_map)
            updated_ner_results = self.get_updated_ner_results(
                ner_results,
                entity_maps
            )
            return updated_ner_results

        return ner_results

class BanglaMaskGeneration:
    def __init__(self, model_path=None):
        if not model_path:
            model_path = "sagorsarker/bangla-bert-base"
        self.unmasker = pipeline('fill-mask', model=model_path)
    def generate_mask(self, sentence):
        try:
            results = self.unmasker(sentence)
            return results
        except Exception as e:
            print(e)
        return sentence

class BanglaTranslation:
    def __init__(self, model_path=None):
        if not model_path:
            model_path = "Helsinki-NLP/opus-mt-bn-en"
        self.model = AutoModelWithLMHead.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

    def bn2en(self, inputs):
        inputs = self.tokenizer.encode(inputs, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
        final_outputs = self.tokenizer.decode(outputs[0])
        if '<pad>' in final_outputs:
          final_outputs = final_outputs.replace('<pad>', '')
        return final_outputs
        
