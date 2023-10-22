
# Imports the Google Cloud client library
import io
import re
import KeywordExtract
import SlidesScrape
from google.oauth2 import service_account
from google.cloud import speech
import gensim.downloader as api


def extract_notes(audio_file) -> speech.RecognizeResponse:
    transcription_keyword_dict = dict()
    client_file = './my_env/hacktx2023-402718-c351f35febef.json'
    credentials = service_account.Credentials.from_service_account_file(client_file)
    delimiter_pattern = r'[.!?]'
    
    
    with io.open(audio_file, 'rb') as f:
        content = f.read()
    # Instantiates a client
    client = speech.SpeechClient(credentials=credentials)

    # The name of the audio file to transcribe

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        sample_rate_hertz = 44100,
        audio_channel_count = 2,
        enable_automatic_punctuation=True
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript
    
    keywords_list = re.split(delimiter_pattern, transcript)
    for sent in keywords_list:
        if (len(sent) > 0):
            filtered_words = KeywordExtract.get_keywords(sent)
            transcription_keyword_dict[sent] = filtered_words
    return transcription_keyword_dict
        
if __name__ == "__main__":
    audio_file = "./my_env/long.wav"
    pptx_file = "./my_env/garbage_collection.pptx"
    transcription_keyword_dict = extract_notes(audio_file)
    body_text, slide_dict, title_dict = SlidesScrape.extract_notes_from_slides(pptx_file)
    
    
    