# audio-book
An audiobook is a recording or voice-over of a book or other work being read out loud.
You do not need to buy a subscription for an audiobook if you have a pdf format of the book. 
you will know how to develop a basic audiobook in just 7 lines of python code.
## Installation:
we will require two libraries to develop an audiobook.
1. pyttsx3
2. PyPDF2 
### libraries from PyPl,
1.pip install PyPDF2
2.pip install pyttsx3
## Play the Audiobook:
Extract the text from the pdf file page by page using the PyPDF2 implementation. Loop through each page,
by reading the text and feeding it to the pyttsx3 speaker engine. It will read out loud the text from the pdf page.
Loop the process for every page in the pdf file and stop the pyttsx3 speaker engine as last.
