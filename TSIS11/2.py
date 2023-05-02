from config import data
import psycopg2

name = input()
surname = input()
phonenumber = input()

sql = '''
    CREATE OR REPLACE FUNCTION inserting_new_users(i_name VARCHAR, i_surname VARCHAR, i_phonenumber VARCHAR)
    RETURNS VOID
    AS $$
    BEGIN
        IF EXISTS (SELECT * FROM phonebook WHERE name = i_name) THEN 
            UPDATE phonebook SET phonenumber = i_phonenumber WHERE name = i_name;
        ELSE
            INSERT INTO phonebook VALUES (i_name, i_surname, i_phonenumber);
        END IF;
    END;
    $$ 
    LANGUAGE plpgsql;
'''



conn = psycopg2.connect(**data)

cursor = conn.cursor()

cursor.execute(sql)
cursor.execute('SELECT inserting_new_users(%s, %s, %s)', (name, surname, phonenumber))
cursor.close()
conn.commit()
conn.close()