import PyPDF2
import Matching


def segment_and_output(audio_file, pptx_file):
    slide_to_sent_mapped = Matching.match(audio_file, pptx_file)
    print(slide_to_sent_mapped)


if name == "__main__":
    # how get input??
    segment_and_output("./my_env/chaining.wav", "./my_env/garbage_collection.pptx")
