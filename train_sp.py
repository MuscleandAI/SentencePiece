import sentencepiece as spm
spm.SentencePieceTrainer.train(input='train.txt', model_prefix='bpe_test', input_format = 'text',
                               vocab_size=8000, character_coverage=0.9995, model_type='bpe')
