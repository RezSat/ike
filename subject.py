from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os

from file_finder import *
from config import *

class Prompts:

	def history(self):
		prompt_template = """
	        You are a history teacher with expertise on Sri Lankan history and G.C.E. O/L related history. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers\nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

	def geography(self):
		prompt_template = """
	        You are a geography teacher with expertise on geography and G.C.E. O/L related geography syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

	def business(self):
		prompt_template = """
	        You are a business and accounting teacher with expertise on business and accounting and G.C.E. O/L related business and accounting syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

	def civic(self):
		prompt_template = """
	        You are a civic / citizenship education teacher with expertise on civic and G.C.E. O/L related civic syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

	def ict(self):
		prompt_template = """
	        You are a ICT teacher with expertise on Information & Communication Technology and G.C.E. O/L related Information & Communication Technology syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

	def science(self):
		prompt_template = """
	        You are a science teacher with expertise on science and G.C.E. O/L related science syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

	def entrepreneurship(self):
		prompt_template = """
	        You are a entrepreneurship teacher with expertise on entrepreneurship and G.C.E. O/L related entrepreneurship syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

	def health(self):
		prompt_template = """
	        You are a health teacher with expertise on health science and G.C.E. O/L related health science syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])


	def mathematics(self):
		prompt_template = """
	        You are a mathematics teacher with expertise on mathematics and G.C.E. O/L related mathematics syllabus. Use the context given to help the student find answers for his/her questions or explanations or whatever they asked. Answer with precise and clear information. Since its mathematics the given context might not hold an direct answer therefore use whatever means necessary to give an accurate answer with nice step by step explanations. Just don't talk about diagrams and figures, DO NOT MENTION digram numbers and figure numbers  \nIf you can't find an exact match, try your best to find an answer by looking for synonyms, related terms, or concepts within the context. Just think this as a conversation between a teacher and a student, help the children to get the knowledge is your task. If you really have no way of helping them just say "Sorry We couldn’t find any answers for your question. Please try another question or re-phrase the question again." \n\n
	        Context:\n {context}?\n
	        Student:\n{question}\n
	        Teacher:
		"""
		return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

class LocalVectorStore:

	def __init__(self):
		self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)
		self.subj = {
			0: "history",
			1: "science",
			2: "business",
			3: "geography",
			4: "entrepreneurship",
			5: "civic",
			6: "ict",
			7: "mathematics",
			8: "health"
		}

	def save(self, i, text_chunks):
		vector_store = FAISS.from_texts(texts=text_chunks, embedding=self.embeddings)
		vector_store.save_local(os.path.join(CWD, DATASETS, VECTOR_STORE, self.subj[i]))
		print(f"[+] Saved {self.subj[i]} successfully")

	def history(self):
		full_text = read_files(HISTORY_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=0, text_chunks=chunks)

	def science(self):
		full_text = read_files(SCIENCE_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=1, text_chunks=chunks)

	def business(self):
		full_text = read_files(BUSINESS_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=2, text_chunks=chunks)

	def geography(self):
		full_text = read_files(GEOGRAPHY_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=3, text_chunks=chunks)

	def entrepreneurship(self):
		full_text = read_files(ENTREPRENEURSHIP_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=4, text_chunks=chunks)

	def civic(self):
		full_text = read_files(CIVIC_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=5, text_chunks=chunks)

	def ict(self):
		full_text = read_files(ICT_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=6, text_chunks=chunks)

	def mathematics(self):
		full_text = read_files(MATH_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=7, text_chunks=chunks)

	def health(self):
		full_text = read_files(HEALTH_TXT)
		text_splitter = RecursiveCharacterTextSplitter(
		    chunk_size=10000,
		    chunk_overlap=200
		)
		chunks = text_splitter.split_text(full_text)
		self.save(i=8, text_chunks=chunks)


