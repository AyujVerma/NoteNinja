import Transcription
import gensim.downloader as api
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from gensim.test.utils import common_texts
import pickle 
import numpy as np
import os
import spacy

WINDOW_SIZE = 2

def map_sentences_to_slides(index, transcription_keyword_dict, slide_vector, wv, slide_to_sentence, slide_key):
    sentence_list = list()
    transcription_key_list = list(transcription_keyword_dict.keys())
    index_moved = False
    do_chaining = False
    prev = None
    vector_list = list()
    for i in range(index[0] - WINDOW_SIZE, index[0] + WINDOW_SIZE):
        if (i < 0 or i >= len(transcription_keyword_dict)):
            continue
        else:
            keyword_list = transcription_keyword_dict[transcription_key_list[i]]
            note_vector = [wv.get_vector(word.lower()) for word in keyword_list if wv.__contains__(word.lower())]
            max_chain_similiarity = -1
            text_similarity = wv.n_similarity(slide_vector, note_vector)
            if (do_chaining):
                for vector in vector_list:
                    max_chain_similiarity = max(max_chain_similiarity, wv.n_similarity(vector, note_vector))
            if text_similarity > .2 or max_chain_similiarity > .35:
                sentence_list.append(transcription_key_list[i])
                index[0] = index[0] + 1
                do_chaining = True
                vector_list.append(note_vector)
            else:
                break
    return sentence_list

def preprocess_transcription_dict(transcription_keyword_dict, slide_dict):
    all_slide_words = set()
    keys_to_remove = list()
    for key in slide_dict:
        for word in slide_dict[key]:
            set.add(word)
    for key in transcription_keyword_dict:
        remove = True
        for word in transcription_keyword_dict[key]:
            if word in all_slide_words:
                remove = False
                break
        if remove is True:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        transcription_keyword_dict.remove(key)

def match(audio_file, pptx_file):
    transcription_keyword_dict, transcript = Transcription.extract_notes(audio_file)
    body_text, slide_dict, title_dict, ppt_sents = Transcription.SlidesScrape.extract_notes_from_slides(pptx_file)
    nlp = spacy.load('en_core_web_sm')
    lemmatized_transcript = []
    for sentence in nlp(transcript + ppt_sents).sents:
        lemmatized_sentence = []
        for token in sentence:
            if token.orth_.isalnum():
                lemmatized_sentence.append(token.orth_.lower())
                if (token.orth_.lower() != token.lemma_.lower()):
                    lemmatized_sentence.append(token.lemma_.lower())
        lemmatized_transcript.append(lemmatized_sentence) 
    model = Word2Vec(sentences=common_texts, vector_size=100,window=5, min_count=1, workers=4)
    model.build_vocab(lemmatized_transcript, update=True)
    model.train(lemmatized_transcript, total_examples=model.corpus_count, epochs=10)
    wv = model.wv
    slide_to_sentence = dict()
    index = list()
    index.append(0)
    for slide_key in slide_dict:
        slide_to_sentence[slide_key] = list()
        slide_vector = [wv.get_vector(word.lower()) for word in slide_dict[slide_key] if wv.__contains__(word.lower())]
        prev_index = index[0]
        sentence_list = map_sentences_to_slides(index, transcription_keyword_dict, slide_vector, wv, slide_to_sentence, slide_key)
        while (prev_index == index[0] and index[0] < len(transcription_keyword_dict)):
            index[0] = index[0] + 1
            prev_index = index[0]
            sentence_list = map_sentences_to_slides(index, transcription_keyword_dict, slide_vector, wv, slide_to_sentence, slide_key)
        slide_to_sentence[slide_key] = sentence_list
    
    # for key in slide_to_sentence.keys():
    #     print(key + ": " + str(slide_to_sentence[key]))
    return slide_to_sentence, body_text, title_dict     
            
            
    

# if __name__ == "__main__":
#     match("./my_env/chaining.wav", "./my_env/garbage_collection.pptx")