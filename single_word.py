# -*- coding: utf-8 -*-
import MySQLdb


'''
@Author Amit Joshi
'''

db = MySQLdb.connect("localhost","root","3","meaning_list" )
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

select_sql = "SELECT * FROM `single_word_nep`"# WHERE word = 'man'"#" WHERE word = '%s'" % (key)

cursor.execute(select_sql)
data_all = cursor.fetchall()

idn = 0
for row in data_all:
	# count = len(row[4].split())
	# if count == 1:
	word = row[4]
	idn = idn + 1
	skip = ['(', ')', '0','1','2','3','4','5','6','7','8','9']
	for x in skip:
		word = word.replace(x, '')
	
	# print str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(word) + "\t" + str(idn)
	if word[:3] == 'ु' or word[:3] == 'ू':
		word = word[3:]

	if word[-3:] == 'ि':
		word = word[:(len(word)-3)]
		word = word + 'ी'
		# print word

	try:
		sqlIns = "INSERT INTO single_word_nep(POS, ID, PosScore, NegScore, SynsetTerms, SNO) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % \
		(row[0], row[1], row[2], row[3], word, idn)
		
		# print sqlIns
		# cursor.execute(sqlIns)
		# db.commit()
		print sqlIns
	except:
	    print "INSERTATION ERROR", row[0] #, cursor.execute(sql).IntegrityError
	    # db.rollback()
else:
	# print "NO", row[0]
	pass
db.close()

# row = '(मिल्काउ75नु)'
# skip = ['0','1','2','3','4','5','6','7','8','9']
# for x in ['0','1','2','3','4','5','6','7','8','9']:

# word = row.replace('(', '')
# word = word.replace(')', '')
# word = word.replace('0', '')
# word = word.replace('1', '')
# word = word.replace('2', '')
# word = word.replace('3', '')
# word = word.replace('4', '')
# word = word.replace('5', '')
# word = word.replace('6', '')
# word = word.replace('7', '')
# word = word.replace('8', '')
# word = word.replace('9', '')
# print word

# मतिस73मता
# 'ु'  \xe0\xa5\x81		\u0941
# 'ू'  \xe0\xa5\x82		\u0942
# a = "ुआसुक्त"
# print a
# if a[:3] == 'ू' or a[:3] == 'ु':
# 	print a[3:]
