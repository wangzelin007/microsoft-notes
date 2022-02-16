https://stackoverflow.com/questions/13965823/resource-corpora-wordnet-not-found-on-heroku
https://stackoverflow.com/questions/25534214/nltk-wordnet-lemmatizer-shouldnt-it-lemmatize-all-inflections-of-a-word
https://stackoverflow.com/questions/3753021/using-nltk-and-wordnet-how-do-i-convert-simple-tense-verb-into-its-present-pas
```python
nltk.stem.WordNetLemmatizer().lemmatize('loving', 'v')

from nltk.stem.wordnet import WordNetLemmatizer
words = ['gave','went','going','dating']
for word in words:
    print(word+"-->"+WordNetLemmatizer().lemmatize(word,'v'))
```