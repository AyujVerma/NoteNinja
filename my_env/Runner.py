import pptx.parts.image
from pptx import Presentation
import Matching
from reportlab.pdfgen import canvas
from PIL import Image
from io import BytesIO
import random

WRAP_LIMIT_SMALL = 100
WRAP_LIMIT_LARGE = 80
Y_INCREMENT = 35
X_INCREMENT = 30
X_SMALL_INCREMENT = 15
X_CENTER = 200
Y_CENTER = 500


def wrap_string(string, is_big):
    strs = []
    length = WRAP_LIMIT_LARGE if is_big else WRAP_LIMIT_SMALL
    while(len(string) > 0):
        curr = string[:length]
        string = string [length:]
        strs.append(curr)
    return strs
            
def segment_and_output(audio_file, pptx_file):
    mappings, slide_text, title_dict = Matching.match(audio_file, pptx_file)
    
    x = 25
    y = 800
    numPages = 1
    
    c = canvas.Canvas('output.pdf')
    append = "0"
    for key in title_dict:
        title = key
        c.setFont('Times-Bold', 15)
        wrapped = wrap_string(key, True)
        if len(wrapped) == 0:
            c.drawString(x, y, "No notes")
        else:
            for str in wrapped:
                if y < 50:
                    c.showPage()
                    y = 800
                c.drawString(x, y, str)
        if y < 50:
            c.showPage()
            y = 800
        for entry in title_dict[key]:
            if entry[0] is not None: #image
                image = entry[0]
                openImage = Image.open(BytesIO(image))
                openImage = openImage.convert('RGB')
                file_name = "temp" + append + ".jpeg"
                openImage.save(file_name)
                y -= 225
                if y < 50:
                    c.showPage()
                    y = 600
                c.drawImage(file_name, X_CENTER - 20, y, width=200, height=200)
                y -= 25
                if y < 50:
                    c.showPage()
                    y = 800
                append += "0"
                c.setFont('Times-Roman', 11)
                wrapped = wrap_string(entry[1], False)
                if len(wrapped) == 0:
                    c.drawString(x + X_INCREMENT, y, "No notes")
                else:
                    for str in wrapped:
                        y -= Y_INCREMENT
                        if y < 50:
                            c.showPage()
                            y = 800
                        c.drawString(x + X_INCREMENT, y, str)
                y -= Y_INCREMENT
                if y < 50:
                    c.showPage()
                    y = 800
            else:
                c.setFont('Times-Bold', 13)
                wrapped = wrap_string(entry[1], True)
                if len(wrapped) == 0:
                        c.drawString(x, y, "No notes")
                else:
                    for str in wrapped:
                        y -= Y_INCREMENT
                        if y < 50:
                            c.showPage()
                            y = 800
                        c.drawString(x + X_SMALL_INCREMENT, y, str)
                c.setFont('Times-Roman', 11)
                put_sub_text = False
                for note in mappings[entry[1]]:
                    put_sub_text = True
                    wrapped = wrap_string(note, False)
                    if len(wrapped) == 0:
                        c.drawString(x + X_INCREMENT, y, "No notes")
                    else:
                        for str in wrapped:
                            y -= Y_INCREMENT
                            if y < 50:
                                c.showPage()
                                y = 800
                            c.drawString(x + X_INCREMENT, y, str)
                if (put_sub_text):
                    y -= Y_INCREMENT
                    if y < 50:
                        c.showPage()
                        y = 800
    c.save()
            

def runner(audio, ppt):
    # how get input??
    
    segment_and_output("./my_env/chaining.wav", "./my_env/garbage_collection.pptx")

runner(None, None)