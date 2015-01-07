import MySQLdb
import os


'''
@Author Amit Joshi
'''

db = MySQLdb.connect("localhost","root","3","SentiWordNetNep" )
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

# key = raw_input('word::')
key = 'ache'#key.lower()


ra_eng_senti = "SELECT * FROM `ra_eng_senti`"# where SynsetTerms = '%s'" % ("shock-absorbent#1")
cursor.execute(ra_eng_senti)
# data = cursor.fetchall()
data = cursor.fetchall()

for row in data:
    wordArr = row[4].split()
    # print
    for word in wordArr:
        word = word.replace("'","\\'")
        cmd = 'echo %s | grep -i -o "^[.0-9]*[a-z\'._-/0-9]*"' % word
        # print cmd
        clean_word = os.popen(cmd).read().strip()
        # gloss = row[5].replace("'","\\'")
        sqlIns = 'INSERT INTO clean_eng_senti(POS, ID, PosScore, NegScore, SynsetTerms, Gloss) VALUES("%s", "%s", "%s", "%s", "%s", "%s")' % \
                    (row[0], row[1], row[2], row[3], clean_word, row[5])
        # print sqlIns, "\n"
        try:
            cursor.execute(sqlIns)
            db.commit()
        except:
            print "\n\tERRORR\t", word
            print sqlIns

db.close()