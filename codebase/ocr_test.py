import pdfplumber
import os

pdf_path = r"C:\Users\visl2441\workspace\OCR_PRAC\codebase\masterdocs\polycab1.pdf"
text = ""

print("Running from:", os.getcwd()) #prints cur working dir
print("PDF exists:", os.path.exists(pdf_path)) #checks if pdf exists at that location

#file opened - read -automatically closed after use
with pdfplumber.open(pdf_path) as pdf:
    #processs pages 1 by 1 
    for page in pdf.pages:  
        page_text=page.extract_text() #visible text is extracted
        text+=page_text +"\n"

print(text)