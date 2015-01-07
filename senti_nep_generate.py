
'''
@Author Amit Joshi
'''

import MySQLdb

db = MySQLdb.connect("localhost","root","3","SentiWordNetNep" )
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

sql_nep_mean = "SELECT * FROM `nep_mean` WHERE word = '%s'" % (key)
sql_eng_senti = "SELECT * FROM `senti_eng` WHERE SynsetTerms = '%s'" % (key)
# cursor.execute(sql)
# data = cursor.fetchone()
# print data

try:
    # cursor.execute(sql_nep_mean)
    if cursor.execute(sql_nep_mean) == 0:
        print "NOT FOUND!!! NEPALI MEANING"
    else:
        data_nep = cursor.fetchone()
        # print "NEPALI:::  ", data_nep[1]
except:
    print "ERROR_1"#, cursor.execute(sql).IntegrityError

try:
    # cursor.execute(sql_eng_senti)
    if cursor.execute(sql_eng_senti) == 0:
        print "NOT FOUND!!! ENGLISH SENTI"
        data_eng = [None]*5
    else:
        data_eng = cursor.fetchone()
        # print "ENG_SENTI:::  ", data_eng
except:
    print "ERROR_2"#, cursor.execute(sql).IntegrityError

# params = [data_eng[0], data_eng[1], data_eng[2], data_eng[3], data_nep[1]]

if data_nep[0] == data_eng[4]:
    sql3 = "INSERT INTO nepali_senti(POS, ID, PosScore, NegScore, SynsetTerms) VALUES('%s', '%s', '%s', '%s', '%s');" % \
        (data_eng[0], data_eng[1], float(data_eng[2]), float(data_eng[3]), data_nep[2])

    cursor.execute(sql3)
    db.commit()
else:
    print "baD one"
    db.rollback()


db.close()