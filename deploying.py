import streamlit as st
from spacy import displacy

st.title("NER prediction")

sent = st.text_area("Enter any sentence","Google is capturing users' data without consent.")

import spacy
nlp = spacy.load("model")
doc = nlp(sent)
ents = [(ent.text,ent.label_) for ent in nlp(sent).ents]

st.write("Your output will be displayed here!")

out_html = displacy.render(doc,style="ent")
st.components.v1.html(out_html)