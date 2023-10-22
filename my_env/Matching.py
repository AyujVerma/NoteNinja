import Transcription
import gensim.downloader as api
from gensim.models import KeyedVectors
import pickle 
import numpy as np
import os

WINDOW_SIZE = 2


def match(audio_file, pptx_file, embeddings):
    # audio_file = "./my_env/long.wav"
    # pptx_file = "./my_env/garbage_collection.pptx"
    transcription_keyword_dict = Transcription.extract_notes(audio_file)
    body_text, slide_dict, title_dict = Transcription.SlidesScrape.extract_notes_from_slides(pptx_file)
    wv = KeyedVectors.load_word2vec_format('word2vec\\GoogleNews-vectors-negative300.bin', binary=True)
    slide_to_sentence = dict()
    index = 0
    for slide_key in slide_dict:
        slide_to_sentence[slide_key] = list()
        # slide_vector = [embeddings[tokens.index(word)] for word in slide_dict[slide_key][0]]
        slide_vector = list()
        for word in slide_dict[slide_key]:
            if word in tokens:
                slide_vector.append(embeddings[tokens.index(word)])
        transcription_key_list = list(transcription_keyword_dict.keys())
        for i in range(index - WINDOW_SIZE, index + WINDOW_SIZE):
            if (i < 0 or i >= len(transcription_keyword_dict)):
                continue
            else:
                keyword_list = transcription_keyword_dict[transcription_key_list[i]]
                note_vector = list()
                for word in keyword_list:
                    if (word in tokens):
                        note_vector.append(embeddings[tokens.index(word)])
                if wv.n_similarity(slide_vector, note_vector) > .5:
                    print("here")
                    slide_to_sentence[slide_key].append(transcription_key_list[i])
                    index += 1
    print(slide_to_sentence, end="\n")
                
            
            
    

if __name__ == "__main__":
    home = os.path.expanduser("~")
    embeddings = np.load(os.path.join(home, '\\Users\\anoop\\hacktx23\\vegetables-google-word2vec\\word2vec.news.negative-sample.300d.npy'))
    with open(os.path.join(home, '\\Users\\anoop\\hacktx23\\vegetables-google-word2vec\\word2vec.news.negative-sample.300d.txt'), encoding='utf8') as fp:
        tokens = [line.strip() for line in fp]
    embeddings[tokens.index('hello')]
    match("./my_env/long.wav", "./my_env/garbage_collection.pptx", embeddings)