import nltk
from nltk import word_tokenize, sent_tokenize
# 引入文本
with open("CNN_news.txt", "r") as fp:
    text = fp.read()

# 這會拿來下載一些必要的data  
# nltk.download('omw-1.4')

# 斷句
sentences = sent_tokenize(text)
# print(sentences)

# 斷詞
tokens = word_tokenize(text)
# print(tokens)

# 依照頻率高低把出現過的英文字詞都列出來
from nltk.probability import FreqDist
fdli = FreqDist(tokens)
# 把前10個常出現的東東印出
# for x in fdli.most_common(10):
#     print(x)

# 下載英文的停用詞
from nltk.corpus import stopwords
# print(stopwords.words('english'))


# 做POS
from nltk import pos_tag
pos = [pos_tag(tokens)]
# print(pos)

# 去除字尾(stemming)
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmer.stem('writing')

# lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
# 參數裡面放(需還原的單字, 單字的詞性)
# print(lemmatizer.lemmatize("went", pos = "v"))

# 搜尋字詞
# 文本.concordance("target")
text.concordance("me")
