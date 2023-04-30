from config import data
import psycopg2
import csv


db = psycopg2.connect(**data)
cursor = db.cursor()

with open('text.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        sql = "INSERT INTO phonebook (name, surname, phonenumber) VALUES (%s, %s, %s)"
        cursor.execute(sql, row)

db.commit()
cursor.close()
db.close()