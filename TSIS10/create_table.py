from config import data
import psycopg2
 
name = input("Enter your name, please:")
surname = input("Enter your surname, please:")
phonenumber = input("Enter your phonenumber, please:")

# sql = '''
#     CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR,
#     level INT DEFAULT 1
#     )
# '''
# sql = '''
#     CREATE TABLE user_score(
#     id SERIAL PRIMARY KEY,
#     user_id INT NOT NULL,
#     level INT NOT NULL,
#     score INT DEFAULT 0,
#     FOREIGN KEY (user_id) REFERENCES users(id)
#     )
# '''
sql = f'''
    INSERT INTO 
    phonebook (name, surname, phonenumber)
    VALUES ('{name}', '{surname}', '{phonenumber}') 
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

cursor.execute(sql)

cursor.close()
db.commit()
db.close()