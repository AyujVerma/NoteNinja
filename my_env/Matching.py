import Transcription
import gensim.downloader as api
from gensim.models import KeyedVectors
import pickle 
import numpy as np
import os

WINDOW_SIZE = 2


def map_sentences_to_slides(index, transcription_keyword_dict, slide_vector, wv, slide_to_sentence, slide_key):
    sentence_list = list()
    transcription_key_list = list(transcription_keyword_dict.keys())
    index_moved = False
    keep_going = True
    for i in range(index[0] - WINDOW_SIZE, index[0] + WINDOW_SIZE):
        if not keep_going:
            break
        if (i < 0 or i >= len(transcription_keyword_dict)):
            continue
        else:
            keyword_list = transcription_keyword_dict[transcription_key_list[i]]
            note_vector = [wv.get_vector(word) for word in keyword_list if wv.__contains__(word)]
            if wv.n_similarity(slide_vector, note_vector) > .5:
                sentence_list.append(transcription_key_list[i])
                index[0] = index[0] + 1
            else:
                keep_going = False
    return sentence_list


def match(audio_file, pptx_file, embeddings):
    # audio_file = "./my_env/long.wav"
    # pptx_file = "./my_env/garbage_collection.pptx"
    transcription_keyword_dict = Transcription.extract_notes(audio_file)
    body_text, slide_dict, title_dict = Transcription.SlidesScrape.extract_notes_from_slides(pptx_file)
    wv = KeyedVectors.load_word2vec_format('word2vec\\GoogleNews-vectors-negative300.bin', binary=True)
    slide_to_sentence = dict()
    index = list()
    index.append(0)
    for slide_key in slide_dict:
        slide_to_sentence[slide_key] = list()
        slide_vector = [wv.get_vector(word) for word in slide_dict[slide_key] if wv.__contains__(word)]
        prev_index = index[0]
        sentence_list = map_sentences_to_slides(index, transcription_keyword_dict, slide_vector, wv, slide_to_sentence, slide_key)
        while (prev_index == index[0] and index[0] < len(transcription_keyword_dict)):
            index[0] = index[0] + 1
            prev_index = index[0]
            sentence_list = map_sentences_to_slides(index, transcription_keyword_dict, slide_vector, wv, slide_to_sentence, slide_key)
        slide_to_sentence[slide_key] = sentence_list
    for key in slide_to_sentence.keys():
        print(key + ": " + str(slide_to_sentence[key]))
                
            
            
    

if __name__ == "__main__":
    home = os.path.expanduser("~")
    embeddings = np.load(os.path.join(home, '\\Users\\anoop\\hacktx23\\vegetables-google-word2vec\\word2vec.news.negative-sample.300d.npy'))
    with open(os.path.join(home, '\\Users\\anoop\\hacktx23\\vegetables-google-word2vec\\word2vec.news.negative-sample.300d.txt'), encoding='utf8') as fp:
        tokens = [line.strip() for line in fp]
    embeddings[tokens.index('hello')]
    match("./my_env/long.wav", "./my_env/garbage_collection.pptx", embeddings)