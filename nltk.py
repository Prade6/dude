from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ex = "This is an example showing stop words"

stop_words = set(stopwords.words("english"))

words = word_tokenize(ex)

filtered_sent = []




"""for w in words:
	if w not in stop_words:
		filtered_sent.appene(w)
"""


# one liner instead of the above commented out for loop________________

filtered_sent = [w for w in words if not w in stop_words]



print(filtered_sent)