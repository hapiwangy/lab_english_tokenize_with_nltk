from nltk.corpus import wordnet as wn
# 找出同義詞集合
wn.synsets('motorcar')
# 一個詞也可能對應到多個synset
wn.synsets('trunk')

# 找出同義詞
# 前面的參數放從哪個同義詞集合裡面尋找
wn.synset('car.n.01').lemma_names()
# 使用definiton可以尋找特定集合的定義
wn.synset('car.n.01').definition()