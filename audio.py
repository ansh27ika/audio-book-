import pyttsx3
import PyPDF2
from tkinter.filedialog import *

resume = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(resume)
pages = pdfreader.numPages

for num in range(0,pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()