import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer
ps = PorterStemmer()
sentence = "Stemming reduces words to their root form"
tokenizer = TreebankWordTokenizer()
words = tokenizer.tokenize(sentence)
for word in words:
    stemmed_word = ps.stem(word)
    print(word, ":", stemmed_word)