'''
NLP
====

-- NLP (Natural language provess )
--- it is also a part fo AI

nlp -- it teaches machines to understan text

raw text -> Text prepoorcessing --> tokenization --> clean text --> AI/ML / GEN-AI Model

1. Text preprocessing

-- raw -- invalid characters, different fonts, messy, extra spaces, uppercase letters

Raw text --> "Welcome to Aimore  
  :O) TECHNOLOGIES"
  
Preprocessed text --> "welcome to aimore technologies"

2. Tokenization

-- break the text into smaller pices called tokens
-- word or even sentence

word tokenization:
====================
text =  "welcome to aimore technologies"
tokens = text.split()
print(tokens)

sentence tokenization:
========================

text =  "welcome to aimore technologies. Gen AI is the future"
sentence = text.split(".")
print(sentence)


3. cleaning text data

-- remove unwanted and noisy data fromt eh text  

text = "Welcoem to Aimore TECHNOLOGIES"
text = text.lower()
print(text)

-- remove puncatuation


import re
import string

text = "Hello!! Welcome to Aimore :) TECHNOLOGIES"

text = text.lower()
text = re.sub(r'[^\x00-\x7F]+','', text)
print(text)
text = text.translate(str.maketrans('','',string.punctuation))
print(text)
text = re.sub(r'\s+', ' ', text).strip()
print(text)


common mistakes:
=============

-- removing stopwords weithut thing
-- over-cleaning 
-- mixing preprocessing logic across files
==============================================


-- Punkt used break text into senteces and words

-- helps NLTK -- natural language kit understand that ther are n numbe of sentences 


'''

import PyPDF2
import nltk
nltk.download('punkt') 
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

files = [               r'D:\lenin\Practise_SF\B28\nlp\Employee_Attendance_Policy.pdf',r'D:\lenin\Practise_SF\B28\nlp\Employee_Conduct_Policy.pdf',
r'D:\lenin\Practise_SF\B28\nlp\HR_Policy_Document.pdf',
r'D:\lenin\Practise_SF\B28\nlp\IT_Security_Policy.pdf']

print(files)


documents = []

for file in files:
    reader = PyPDF2.PdfReader(file)
    text =""
    for page in reader.pages:
        text+=page.extract_text()
    documents.append(text)

print("Documents Loaded:", len(documents))

query = input("User question: ")

query_tokens = word_tokenize(query)

print("Query tokens:", query_tokens)
