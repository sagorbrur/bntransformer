# Contributing to bntransformer

To contribute you can follow these steps below

* Do implementation of any of the state of the art transformer(Bert, xlnet, gpt2, roberta etc) in bengali.
* Do tokenizer, pretraining, finetuning script using that bengali transformer model.
* update `README.md` to provide API access, how people use it.

## Example

Let us consider, we did a bengali `bert` model with bengali `vocab` file.

So, what we can do here, 

* provide a pretraining script with our `bengali bert` model `vocab` and `config` file. 
* provide tokenizer using `bengali bert` model `vocab` file. 
* provide fine-tuning approach using our `bengali bert` pretraining model, config and vocab file. 

All we want to do building bengali transformer repository like [transformers](https://github.com/huggingface/transformers)

## Code and Details

* clone https://github.com/USER_NAME/bntransformer.git to your local directory.
* [bntransformer/bntransformer](https://github.com/sagorbrur/bntransformer/tree/master/bntransformer) is the main directory for script.
* do write your script according to your bengali transformer
* send PR to us. 

Thanks and Happy Contributing
