#!/usr/bin/python

import sqlite3, music


'''
@Author Amit Joshi
'''


conn = sqlite3.connect('Data.db')
conn.text_factory = str
db = conn.cursor()
#db.execute('create table PATTERN (pattern text,tag text,count int)')

def learn(song_name,tag):
	for pattern in music.throw_pattern('Music/'+song_name):
		pattern = list(pattern)
		pattern[0] = '_'.join(pattern[0])
	
		db.execute('select count from PATTERN where pattern=? and tag=?', (pattern[0], tag))
		existing_count = db.fetchone()
		
		if existing_count:
			db.execute('update PATTERN set count=? where pattern=? and tag=?', (existing_count[0] + pattern[1], pattern[0], tag))
		else:
			db.execute('insert into PATTERN (pattern, tag, count) values (?,?,?)', (pattern[0], tag, pattern[1]))


def classify(song_name):

	positive_count = 0.0
	negative_count = 0.0
	for pattern in music.throw_pattern('Music/'+song_name):
		
		db.execute('select count from PATTERN where pattern=? and tag=?', ('_'.join(pattern[0]),'p'))
		existing_positive = db.fetchone()
		if existing_positive:
			positive_count += existing_positive[0]
		
		db.execute('select count from PATTERN where pattern=? and tag=?', ('_'.join(pattern[0]),'n'))
		existing_negative = db.fetchone()
		if existing_negative:
			negative_count += existing_negative[0]

	print float(positive_count/(positive_count+negative_count))

'''print 'start\n'
for a in open('a.csv').readlines():
	aa = a.split('\t')
	print aa
	learn(aa[0],aa[1].strip())
'''
classify('spacebound.wav')

conn.commit()
conn.close()

