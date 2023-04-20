import pytesseract
from PyPDF2 import PdfReader
import re
import json

# Open the PDF file
pdf_file = open('sample.pdf', 'rb')
pdf_reader = PdfReader(pdf_file)

# Extract text from PDF
pages = len(pdf_reader.pages)
text = ""
for i in range(pages):
    page = pdf_reader.pages[i]
    text += page.extract_text()

# Use OCR to recognize dates
dates = []
ocr_text = pytesseract.image_to_string(text)
matches = re.findall(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}', ocr_text)
for match in matches:
    dates.append(match)

# Output dates in JSON format
output = {"dates": dates}
json_output = json.dumps(output)
print(json_output)
