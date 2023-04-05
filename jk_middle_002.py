
from pdfminer.high_level import extract_text
text = extract_text('sample01.pdf')

f = open('myfile.txt', 'w', encoding='UTF-8')

f.write(text)

f.close()