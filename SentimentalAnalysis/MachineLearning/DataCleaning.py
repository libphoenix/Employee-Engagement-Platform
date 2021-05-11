import pandas as pd
import re 
import string
# import nltk

# nltk.download('stopwords')
# from nltk.corpus import stopwords
# stop = set(stopwords.words("english"))


def remove_url_punctuation_stopwords(text):
    try:
        url = re.compile(r"[https|http]+://[a-z A-Z 0-9 .]*.[a-z]*")
        text = url.sub(r"",text)

        translator = str.maketrans("","",string.punctuation)
        text = text.translate(translator)

        # filtered_words = [word.lower() for word in text.split() if word.lower() not in stop]
        # text = " ".join(filtered_words)

        return text
    except:
        print(str(text))


def clean_and_load(file_path, data_type):
    data_store = pd.read_csv(file_path,dtype = data_type)
    data_store['clean_text'] = data_store['clean_text'].fillna("clean text")
    data_store['category'] = data_store['category'].fillna(0)
    data_store['clean_text'] = data_store.clean_text.map(remove_url_punctuation_stopwords)
    return data_store