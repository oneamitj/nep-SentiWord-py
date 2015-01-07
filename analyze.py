# -*- coding: utf-8 -*-

'''
@Author Amit Joshi
'''


import MySQLdb
import Queue
import os
import sys, re

reload(sys)
sys.setdefaultencoding('utf8') 

# def main(sentence):
def main():
	# sentence = "अठारौं सार्क शिखर सम्मेलन संघारमै आइपुग्दा सरकारको तयारी भने अझै सुस्त गतिमै छ ।"
	# sentence = 'सरकारले आयोजकका हैसियतले त्यसको तयारी अलि अगाडि सुरु गरिसक्नुपथ्र्यो ।'
	# sentence = 'राम खराब मान्छे होइन'
	sentence = 'राम राम्रो मान्छे हो'
	# sentence = 'लाडो खा'
	# sentence = 'को का की रो रा री नो ना नी लाई संग जानेलाई'
	# sentence = 'धेरै'
	sentence = sentence.replace(",", "").replace("‘", "").replace("'", "").replace("(", "").replace(")", "").replace("/", " ")
	
	Q = Queue.Queue()
	QScore = Queue.Queue()

	inputFile = open('NCG/input', 'w')
	inputFile.write(sentence)
	inputFile.close()

	parse(sentence, Q)

	lookUp(Q, QScore)

	negWord = 0
	posWord = 0
	print sentence
	print
	print 'Word\t\tSentiment'
	while(not QScore.empty()):
		popValue = QScore.get()
		print popValue[0], '\t', numberType(popValue[1])

		if popValue[1]<0:
			negWord += 1
		elif popValue[1]>0:
			posWord += 1

	# print posWord, negWord
	print
	'''
	if negWord == posWord == 0:
		print "No Sentiment"
		print "Neutral Sentence\n"
		return 0
	elif negWord % 2 == 0:
		print "Positive Sentence\n"
		return 1
	elif negWord % 2 == 1:
		print "Negative Sentence\n"
		return -1
'''

def numberType(num):
	if num < 0:
		return 'Negative'
	elif num > 0:
		return 'Positive'
	elif num == 0:
		return 'Neutral'


def lookUp(Q, QScore):
	db = MySQLdb.connect("localhost","root","3", "meaning_list" )
	cursor = db.cursor()
	cursor.execute("SET NAMES utf8")

	while(not Q.empty()):
		word = Q.get()
		print word[0], '\t', word[1]
		cmdSQL = "SELECT * FROM single_word_nep WHERE SynsetTerms = '%s' AND POS = '%s'" % (word[0], word[1])

		if cursor.execute(cmdSQL) == 0:
			cmdSQL = cmdSQL = "SELECT * FROM single_word_nep WHERE SynsetTerms = '%s'" % word[0]
			cursor.execute(cmdSQL)
		
		sentiScore = cursor.fetchall()
		# print sentiScore

		if len(sentiScore)==0:
			continue
		
		posScore = []
		negScore = []
		for eachData in sentiScore:
			posScore.append(eachData[2])
			negScore.append(eachData[3])

		# print word[0], max(posScore), max(negScore)
		if max(posScore) == max(negScore):
			score = 0
		elif max(posScore) > max(negScore):
			score = max(posScore)
		else:
			score = -1*max(negScore)
		# print score
		
		QScore.put((word[0], score))

	db.close()
	print

def parse(sentence, Q):
	os.system("./NCG/run.sh")
	exceptions = ["/PLAI", "/PKO", "/PLE", "/POP", "/YF", '/CD', '/OD', '/ALPH', '/SYM']

	noun = ['/NN','/NNP', '/PP', '/PP$', '/PPR', '/DM', '/DUM']
	verb = ['/VBF', '/VBX', '/VBI', '/VBNE', '/VBKO', '/VBO']
	adj = ['/JJ', '/JJM', '/JJD']
	adverb = ['/RBM', '/RBO']

	nipatFile = open('NCG/res/PopTokenizer/popList', 'r')
	nipatList = nipatFile.read().split('\r\n')
	# print nipatList[5]

	outputFile = open('NCG/output', 'r')
	ncgOutput = outputFile.read().split()

	for val in ncgOutput:
		posNCG = val.encode('ascii', 'ignore')
		word = val.replace(posNCG, '')

		# print word, posNCG
		try:
			noun.index(posNCG)
			pos = 'n'
		except:
			try:
				verb.index(posNCG)
				pos =  'v'
			except:
				try:
					adj.index(posNCG)
					pos =  'a'
				except:
					try:
						adverb.index(posNCG)
						pos =  'r'
					except:
						continue

		# print word, '\t', pos
		# print
		Q.put((word, pos))

	return Q



if __name__ == '__main__':
	main()

	# sentenceFile = open('editorial.txt', 'r')
	# count_positive = 0
	# count_negative = 0
	# count_neutral = 0

	# for sentence in sentenceFile:
	# 	sentiment = main(sentence)

	# 	if sentiment == 0:
	# 		count_neutral += 1
	# 	elif sentiment == 1:
	# 		count_positive += 1
	# 	elif sentiment == 0:
	# 		count_negative += 1

	# 	print "\n------------------------------------------------------------------------\n"

	# print "Neutral Sentences = %d" % count_neutral
	# print "Positive Sentences = %d" % count_positive
	# print "Negative Sentences = %d" % count_negative
	# print "\n\n\t\tCOMPLETED\n\n"
