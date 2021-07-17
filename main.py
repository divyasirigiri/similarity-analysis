from logging import debug
from flask import Flask, render_template, request
import spacy
nlp = spacy.load('en_core_web_sm')

app1 = Flask(__name__)

@app1.route('/')
def hello():
    return render_template('base.html')

@app1.route('/define',methods = ['POST'])
def define():
    ip_word = request.form.get('ip-word')
    ip_word1 = request.form.get('ip-word1')
    doc = nlp(ip_word)
    doc_1 = nlp(ip_word1)

    res = doc.similarity(doc_1)

    return render_template('base.html',translated_text=f'\n the similarity score between the text "{(ip_word)}"  and {(ip_word1)} is :  {res} ')

if __name__=='__main__':
    app1.run(debug=True)
