import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def get_keywords(sentence):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(sentence)
    words = [word.lower() for word in words if word.isalnum()]
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words