import sentencepiece as spm
sp_bpe = spm.SentencePieceProcessor() 
sp_bpe.load('bpe_test.model')
print('*** BPE ***')
# print(sp_bpe.encode_as_pieces('The excellence of a translation can only be judged by noting'))
# print(len(sp_bpe.encode_as_pieces('The excellence of a translation can only be judged by noting')))
print(sp_bpe.encode_as_pieces('山东能源集团是能源行业领军者，云鼎科技股份有限公司是其2级子公司。'))
print(len(sp_bpe.encode_as_pieces('山东能源集团是能源行业领军者，云鼎科技股份有限公司是其2级子公司。')))