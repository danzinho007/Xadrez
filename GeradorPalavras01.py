from nltk.corpus import stopwords

stop_words = stopwords.words('portuguese')
print(stop_words[:1000])

stop_words = stopwords.words('english')
print(stop_words[:1000])

stop_words = stopwords.words('spanish')
print(stop_words[:1000])

# japonês não funciona
stop_words = stopwords.words('japanese')
print(stop_words[:1000])
