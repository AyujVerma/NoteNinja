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

# def segment_and_output(audio_file, pptx_file):
    
    for entry in slides_text:
        if entry[0] is not None: #image
            image = entry[0]
            openImage = Image.open(BytesIO(image))
            openImage = openImage.convert('RGB')
            packet = BytesIO()
            img_holder = canvas.Canvas(packet)
            openImage = openImage.resize((200, 200))
            openImage.save('temp.jpeg')
            img_holder.drawImage('temp.jpeg', X_CENTER, Y_CENTER)
            img_holder.save()
            packet2 = BytesIO()
            text_holder = canvas.Canvas(packet2)
            text_holder.drawString(x, y, entry[1])
            for note in mappings[entry[1]]:
                wrapped = wrap_string(note)
                if len(wrapped) == 0:
                    y -= INCREMENT
                    text_holder.drawString(x + INCREMENT, y, "No notes")
                else:
                    for str in wrapped:
                        y -= INCREMENT
                        text_holder.drawString(x + INCREMENT, y, str)
            text_holder.save()
            packet2.seek(0)
            overlay = PdfReader(packet)
            overlay2 = PdfReader(packet2)
            merger = PdfMerger()
            merger.append(overlay.pages[0])
            merger.append(overlay2.pages[0])
            pdf_writer.add_page(merger)
        else:
            packet = BytesIO()
            text_holder = canvas.Canvas(packet)
            text_holder.drawString(x, y, entry[1])
            for note in mappings[entry[1]]:
                wrapped = wrap_string(note)
                if len(wrapped) == 0:
                    y -= INCREMENT
                    text_holder.drawString(x + INCREMENT, y, "No notes")
                else:
                    for str in wrapped:
                        y -= INCREMENT
                        text_holder.drawString(x + INCREMENT, y, str)
            text_holder.save()
            packet.seek(0)
            overlay = PdfReader(packet)
            pdf_writer.add_page(overlay.pages[0])
    
            
def segment_and_output2(audio_file, pptx_file):
    mappings, slide_text = Matching.match(audio_file, pptx_file)
    
    x = 25
    y = 800
    numPages = 1
    
    c = canvas.Canvas('output.pdf')
    append = "0"
    for entry in slide_text:
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
            c.setFont('Times-Bold', 14)
            wrapped = wrap_string(entry[1], True)
            if len(wrapped) == 0:
                    c.drawString(x, y, "No notes")
            else:
                for str in wrapped:
                    y -= Y_INCREMENT
                    if y < 50:
                        c.showPage()
                        y = 800
                    c.drawString(x, y, str)
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
    print(numPages)
    c.save()
            

if __name__ == "__main__":
    # how get input??
    segment_and_output2("./my_env/chaining.wav", "./my_env/garbage_collection.pptx")
