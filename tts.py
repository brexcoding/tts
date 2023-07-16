# importing the modules
import PyPDF2
import pyttsx3
from PyPDF2 import PdfReader

reader = PdfReader("Answer.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

