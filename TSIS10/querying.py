from config import data
import psycopg2

sql = '''
    SELECT *
    FROM phonebook
    WHERE surname = ' KingOfCalc'
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

cursor.execute(sql)

print(cursor.fetchall())
cursor.close()
db.commit()
db.close()