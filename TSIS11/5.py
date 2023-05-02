from config import data
import psycopg2

name = input()
phonenumber = input()

sql = '''
   CREATE OR REPLACE FUNCTION delete_user_data(username text, phone text)
RETURNS void AS $$
BEGIN
    IF username IS NOT NULL THEN
        DELETE FROM phonebook WHERE username = username;
    ELSEIF phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = phone;
    ELSE
        RAISE EXCEPTION 'Either username or phone must be provided.';
    END IF;
END;
$$ LANGUAGE plpgsql;
'''



conn = psycopg2.connect(**data)

cursor = conn.cursor()

cursor.execute(sql)
cursor.execute('SELECT delete_user_data(%s, %s)', (name,phonenumber))
cursor.close()
conn.commit()
conn.close()