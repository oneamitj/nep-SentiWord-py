# -*- coding: utf-8 -*-


'''
@Author Amit Joshi
'''

def checker(file_name):
	i = 0
	f = open(file_name, 'r')
	word_list = open('word_dict.txt', 'r')
	word_list = word_list.read().split()
	for line in f:
		for word in line.split():
			word = word.replace(",‘'", "")
			word = word.replace("‘", "")
			word = word.replace("'", "")
			try:
				word_list.index(word)
				i+=1
				print line,
				break
			except:
				pass


checker('sentences.csv')