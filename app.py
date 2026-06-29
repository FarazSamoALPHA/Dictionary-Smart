import streamlit as st
import pandas as pd
# import numpy as np
import nltk
import textblob
# from textblob.wordnet import Synset
from textblob import Word
from textblob import TextBlob

# title
st.title('Spell Checker Tool')

# app  fuction
spellc= st.text_input('spell suggestion')
l = Word(spellc)

sc= l.spellcheck()
st.write(f'this is your correct spell:  {sc}')

#correct
corr= st.text_input('write text correction')
k = TextBlob(corr)
c= k.correct()
st.write(f'this is your correct spell:{c}')

#file upload
file = st.file_uploader('upload file here',type=['csv','docx'])
if file:
    df1 =pd.read_csv(file)
    f = TextBlob('df1')
    ff = f.correct()
    st.write(f'this is your correct spell:{ff}')
