from config import data
import psycopg2
pattern = input()
sql = f'''
    CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern text)
    RETURNS SETOF phonebook AS 
    $$
    BEGIN
        RETURN QUERY SELECT * FROM phonebook WHERE name LIKE '%' || pattern || '%'
        OR surname LIKE '%' || pattern || '%'
        OR phonenumber LIKE '%' || pattern || '%';
    END;
$$ LANGUAGE plpgsql;
'''


conn = psycopg2.connect(**data)

cursor = conn.cursor()

cursor.execute(sql)
cursor.execute('SELECT get_records_by_pattern (%s)',(f'{pattern}',))
print(cursor.fetchall())
cursor.close()
conn.commit()
conn.close()