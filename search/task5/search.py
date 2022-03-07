import nltk
import math
import os
import sys
import json

nltk.download('punkt')
nltk.download("stopwords")

from nltk.corpus import stopwords

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

#получаем список стоп слов
stop = stopwords.words('english')

def compare_vectors(vector1, vector2):
  file = open("../tokens")
  tokens = file.read().split("\n")
  file.close()
  sum = 0
  suma = 0
  sumb = 0
  for token in tokens:
    sum = sum + vector1[token] * vector2[token]
    suma = suma + vector1[token] * vector1[token]
    sumb = sumb + vector2[token] * vector2[token]
  if (sum == 0 or suma == 0 or sumb == 0):
    return 0
  return sum/(math.sqrt(suma) * math.sqrt(sumb))

def get_vector_from_file(name):
  vector_dict = {}
  file = open("../vectors/" + name)
  vecotor_strings = file.read().split("\n")
  file.close()
  for vecotor_string in vecotor_strings:
    if vecotor_string != "":
      vector_dict[vecotor_string.split(" ")[0]] = float(vecotor_string.split(" ")[1])
  return vector_dict

def search(search_term):
  tokens_set = set()
  dictionary = {}
  vector_dict = {}
  file = open("../tokens")
  tokens = file.read().split("\n")
  file.close()
  for token in tokens:
    dictionary[token] = 0
  search_term = '  '.join([word for word in search_term.split() if word not in (stop)])
  words = search_term.split()
  for word in words:
    current_lemma = WordNetLemmatizer().lemmatize(word)
    tokens_set.add(current_lemma)
    dictionary[word] = dictionary[word] + 1
  for token in tokens:
    vector_dict[token] = 0
  for token in tokens_set:
    vector_dict[token] = dictionary[token] / float(len(words))
  result_dict = {}
  vectors_files = os.listdir("../vectors")
  for name in vectors_files:
    result_dict[name] = compare_vectors(get_vector_from_file(name), vector_dict)
  return result_dict

sys.stdout.write(json.dumps((search(sys.argv[1]))))

