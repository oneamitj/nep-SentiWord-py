# -*- coding: utf-8 -*-


'''
@Author Amit Joshi
'''

import MySQLdb

db = MySQLdb.connect("localhost","root","3", "meaning_list" )
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

sql_nep_mean = "SELECT * FROM `nep_mean`"# WHERE word = 'man'"#" WHERE word = '%s'" % (key)

cursor.execute(sql_nep_mean)
data_nep = cursor.fetchall()

for row in data_nep:
	clean_eng_senti = "SELECT * FROM `clean_eng_senti` WHERE SynsetTerms = '%s'" % (row[0])
	
	if cursor.execute(clean_eng_senti) != 0:
		data_eng = cursor.fetchall()

		# print len(data_eng)
		for search_list in data_eng:
			for i in range(1,len(search_list)):
				if row[i] == " " or row[i] == "" :
					break
				try:
					sqlIns = "INSERT INTO clean_nep_senti(POS, ID, PosScore, NegScore, SynsetTerms) VALUES('%s', '%s', '%s', '%s', '%s')" % \
					(search_list[0], search_list[1], float(search_list[2]), float(search_list[3]), row[i])
					
					# print sqlIns
					cursor.execute(sqlIns)
					db.commit()
				except:
				    print "INSERTATION ERROR", row[0] #, cursor.execute(sql).IntegrityError
				    # db.rollback()
	else:
		print "NO", row[0]
db.close()


# राम राम्रो मान्छे हो


'''

INSERTATION ERROR abut
INSERTATION ERROR abysm
INSERTATION ERROR abysm
INSERTATION ERROR abysm
INSERTATION ERROR abyss
INSERTATION ERROR accede
INSERTATION ERROR accelerate
INSERTATION ERROR accelerate
INSERTATION ERROR accelerate
INSERTATION ERROR accelerative
INSERTATION ERROR accelerative
INSERTATION ERROR accelerative
INSERTATION ERROR accelerator
INSERTATION ERROR accent
INSERTATION ERROR accent
INSERTATION ERROR accent
INSERTATION ERROR accented
INSERTATION ERROR accentuate
INSERTATION ERROR accentuate
INSERTATION ERROR accentuate
INSERTATION ERROR acceptability
INSERTATION ERROR acceptability
INSERTATION ERROR accepted
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accessory
INSERTATION ERROR accidence
INSERTATION ERROR accidentally
INSERTATION ERROR acclamation
INSERTATION ERROR acclamation
INSERTATION ERROR acclamation
INSERTATION ERROR acclamation
INSERTATION ERROR acclimatize
INSERTATION ERROR acclimatize
INSERTATION ERROR acclimatize
INSERTATION ERROR acclimatize
INSERTATION ERROR acclivity
INSERTATION ERROR acclivity
INSERTATION ERROR acclivity
INSERTATION ERROR accolade
INSERTATION ERROR accompaniment
INSERTATION ERROR accompaniment
INSERTATION ERROR accompaniment
INSERTATION ERROR accompaniment
INSERTATION ERROR accompanist
INSERTATION ERROR accompanist
INSERTATION ERROR accomplice
INSERTATION ERROR accomplice
INSERTATION ERROR accomplice
INSERTATION ERROR accomplice
INSERTATION ERROR accomplice
INSERTATION ERROR accomplice
INSERTATION ERROR accomplish
INSERTATION ERROR accomplish
INSERTATION ERROR accomplished
INSERTATION ERROR accomplished
INSERTATION ERROR accordance
INSERTATION ERROR accordance
INSERTATION ERROR accordion
INSERTATION ERROR accordion
INSERTATION ERROR accost
INSERTATION ERROR accost
INSERTATION ERROR accost
INSERTATION ERROR accost
INSERTATION ERROR accost
INSERTATION ERROR accoucheur
INSERTATION ERROR accountability
INSERTATION ERROR accountability
INSERTATION ERROR accountant
INSERTATION ERROR accountant
INSERTATION ERROR accountant
INSERTATION ERROR accountant
INSERTATION ERROR accoutrement
INSERTATION ERROR accoutrement
INSERTATION ERROR accoutrement
INSERTATION ERROR accumulated
INSERTATION ERROR accumulated
INSERTATION ERROR accumulated
INSERTATION ERROR accursed
INSERTATION ERROR accursed
INSERTATION ERROR accursed
INSERTATION ERROR accursed
INSERTATION ERROR accursed
INSERTATION ERROR accusation
INSERTATION ERROR accusation
INSERTATION ERROR accusation
INSERTATION ERROR accusation
INSERTATION ERROR accusation
INSERTATION ERROR accusation
INSERTATION ERROR accusation
INSERTATION ERROR accusation
INSERTATION ERROR accusative
INSERTATION ERROR accusative
INSERTATION ERROR accustom
INSERTATION ERROR accustom
INSERTATION ERROR acerbic
INSERTATION ERROR acerbic
INSERTATION ERROR acerbic
INSERTATION ERROR acetylene
INSERTATION ERROR acetylene
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR ache
INSERTATION ERROR achieve
INSERTATION ERROR achieve
INSERTATION ERROR achievement
INSERTATION ERROR achromatic
INSERTATION ERROR achromatic
INSERTATION ERROR acidify
INSERTATION ERROR acidify
INSERTATION ERROR acknowledgement
INSERTATION ERROR acknowledgement
INSERTATION ERROR acknowledgement
INSERTATION ERROR acknowledgement
INSERTATION ERROR acknowledgement
INSERTATION ERROR acme
INSERTATION ERROR acme
INSERTATION ERROR acme'''