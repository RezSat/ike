import os
import sys

CWD = os.path.abspath(os.getcwd())
DATASETS = 'datasets'
TEXT = "text"
VECTOR_STORE = "vectors"

BUSINESS_TXT = os.path.join(CWD, DATASETS, TEXT, "business")
CIVIC_TXT = os.path.join(CWD, DATASETS, TEXT, "civic")
#ENGLISH_TXT = os.path.join(CWD, DATASETS, TEXT, "english")
ENTREPRENEURSHIP_TXT = os.path.join(CWD, DATASETS, TEXT, "entrepreneurship")
GEOGRAPHY_TXT = os.path.join(CWD, DATASETS, TEXT, "geography")
HEALTH_TXT = os.path.join(CWD, DATASETS, TEXT, "health")
HISTORY_TXT = os.path.join(CWD, DATASETS, TEXT, "history")
ICT_TXT = os.path.join(CWD, DATASETS, TEXT, "ict")
SCIENCE_TXT = os.path.join(CWD, DATASETS, TEXT, "science")
MATH_TXT = os.path.join(CWD, DATASETS, TEXT, "mathematics")


def read_files(dir):
	text = ""
	for file in os.listdir(dir):
		path = os.path.join(dir, file)
		data = open(path, 'r', encoding='utf8', errors='ignore').read()
		text += data
	return text+"\n\n"

def merge_all():
	text = read_files(BUSINESS_TXT) + read_files(CIVIC_TXT) + read_files(ENGLISH_TXT) + read_files(ENTREPRENEURSHIP_TXT) + read_files(GEOGRAPHY_TXT) + read_files(HEALTH_TXT) + read_files(HISTORY_TXT) + read_files(ICT_TXT) + read_files(SCIENCE_TXT) + read_files(MATH_TXT)
	return text