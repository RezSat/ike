from flask import Flask, request, url_for, render_template
from flask_markdown import Markdown

from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from deep_translator import GoogleTranslator

from config import google_api_key
from subject import Prompts, LocalVectorStore
from file_finder import *

app = Flask(__name__)
Markdown(app)

subj = {
	0: "history",
	1: "science",
	2: "business",
	3: "geography",
	4: "entrepreneurship",
	5: "civic",
	6: "ict",
	7: "mathematics"

}
vector_store = LocalVectorStore()
prompt = Prompts()

def english2sinhala(text):
    translator = GoogleTranslator(source='en', target='si')
    text = translator.translate(text)
    return text

def sinhala2enlgish(text):
    translator = GoogleTranslator(source='si', target='en')
    text = translator.translate(text)
    return text


def load_embeddings(subject):
	new_db = FAISS.load_local(os.path.join(CWD, DATASETS, VECTOR_STORE, subject), vector_store.embeddings, allow_dangerous_deserialization=True)
	return new_db

def get_answer(q, subject):
	pr = getattr(prompt, subject)
	model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5, google_api_key=google_api_key)
	chain = load_qa_chain(model, chain_type='stuff', prompt=pr())
	docs = load_embeddings(subject).similarity_search(q)
	response = chain.invoke(
		{"input_documents": docs, "question": q},
		return_only_outputs=True
		)
	return response['output_text']

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/<lang>/subject')
def subject(lang):
	return render_template(f"{lang}_subject.html")

@app.route('/<lang>/<subject>/ask')
def ask(lang, subject):
	return render_template(f"{lang}_ask.html", subject=subject)

@app.route('/<lang>/answer', methods=['POST'])
def answer(lang):
	if request.method == "POST":
		question = request.form['question']
		subject = request.form['subject']

	if lang=='si':
		question_m = sinhala2enlgish(question)
		answer = english2sinhala(get_answer(question_m, subject))
	else:
		answer = get_answer(question, subject)

	return render_template(f"{lang}_answer.html", question=question, answer=answer, subject=subject)

if __name__ == '__main__':
	saved = open('saved', 'r').read()
	if 'FALSE' in saved:
		vector_store.history() 
		vector_store.science()
		vector_store.business()
		vector_store.geography()
		vector_store.entrepreneurship()
		vector_store.civic()
		vector_store.ict()
		vector_store.mathematics()
		with open('saved', 'w') as f:
			f.write("TRUE")
			f.close()

	app.run(debug=True)