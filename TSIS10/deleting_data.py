from config import data
import psycopg2

sql = '''
    DELETE 
    FROM phonebook
    WHERE name = %s
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

cursor.execute(sql, ('Makoster',))

cursor.close()
db.commit()
db.close()