#!usr/bin/env python

# topic.py
# generate a list of important topics in a text

import sys
from operator import itemgetter

class COCA(object):
	def __init__(self,filename):
		self.freq = {}
		self.lemmas = {}
		self.ranks = {}
		with open(filename,"r") as f:
			for line in f:
				fields = line.split()
				if fields[1] != "w1":
					if fields[1] in self.freq:
						self.freq[fields[1]] = self.freq[fields[1]] + float(fields[6])
					else:
						self.freq[fields[1]] = float(fields[6])
					self.lemmas[fields[1]] = fields[2]
					self.ranks[fields[1]] = int(fields[0])


def clean_word(word):
	punctuation = ["!",",",".","?",")","(","&","$","#","@","/","{","}","[","]",":",";"]
	if word.isalpha():
		return word
	else:
		if word in punctuation:
			return None
		else:
			if word[-1] in punctuation:
				return clean_word(word[:-1])
			elif word[0] in punctuation:
				return clean_word(word[1:])
			else:
				return None


#=============================================================================
#                   Class and methods for analyzing text
#=============================================================================

class Text(object):
	def __init__(self,f,coca):
		self.coca = coca
		self.words = []
		for line in f:
			line_raw = line.split()
			for word in line_raw:
				if clean_word(word) == None:
					None
				else:
					self.words.append(clean_word(word))
		self._make_vocab()
		self._make_freq_dict()
		self._common_words()
	def _make_vocab(self):
		self.vocab = []
		for word in self.words:
			if word in self.vocab:
				None
			else:
				self.vocab.append(word)
	def _make_freq_dict(self):
		self.freq = {}
		for word in self.words:
			if word in self.freq.keys():
				self.freq[word] = self.freq[word] + 1
			else:
				self.freq[word] = 1
	def normalize(self):
		markers = ["the","a","an","they","their","and","of","in","to","it","be","that","for","have","are","or","do","have"]
		factors = []
		for marker in markers:
			if marker in self.coca.freq.keys() and marker in self.vocab:
				factor = float(self.freq[marker])/self.coca.freq[marker]
				factors.append(factor)
		return max(factors)
	def _common_words(self):
		shared = []
		for word in self.vocab:
			if word.lower() in self.coca.freq.keys():
				shared.append(word)
		self.shared = shared
	def topics(self):
		topics = []
		x = self.normalize()
		scale_factor = 2
		for word in self.shared:
			if self.freq[word] > self.coca.freq[word.lower()]*x*100:
				topics.append(word)
		return topics
	def _by_rank(self):                                                   # this is not integrated in the topics() method yet
		rank_raw = sorted(self.freq.items(), key = itemgetter(1))
		
		n_rank_raw_dict = {}
		for word in self.shared:
			n_rank_raw_dict[word] = self.coca.ranks[word.lower()]
		n_rank_raw = sorted(n_rank_raw_dict.items(), key = itemgetter(1))

		rank = {}
		n_rank = {}

		weighted = {}
		for i in range(len(rank_raw)):
			rank[rank_raw[i][0]] = i #
		for n in range(len(n_rank_raw)):
			n_rank[n_rank_raw[n][0]] = n

		for word in self.shared:
			weighted[word] = rank[word] - n_rank[word]
		return weighted
	def histogram(self):
		hist_raw = {}
		for word in self.shared:
			hist_raw[word] = float(self.freq[word])/self.coca.freq[word.lower()]
			hist = sorted(hist_raw.items(), key = itemgetter(1))
		return hist

#=============================================================================
#     Run the Topic Index Generator on the files specified at the command line
#=============================================================================

corpus_info = COCA("COCA/100k_all_b028.txt")

for filename in sys.argv[1:]:
	with open(filename,"r") as f:
		text = Text(f,corpus_info)
		print text.topics()
		text._by_rank()