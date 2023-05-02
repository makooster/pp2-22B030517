from config import data
import psycopg2

sql = '''
  CREATE OR REPLACE FUNCTION get_data_with_pagination(table_name text, limit_value integer, offset_value integer, OUT name text, OUT email text)
AS $$
DECLARE
  row record;
  query text;
BEGIN
  query := 'SELECT name, email FROM ' || table_name || ' LIMIT ' || limit_value || ' OFFSET ' || offset_value;
  FOR row IN EXECUTE query LOOP
    name := row.name;
    surname := row.surname;
    phonenumber := row.phonenumber;
    RETURN NEXT;
  END LOOP;
END;
$$ LANGUAGE plpgsql;
'''



conn = psycopg2.connect(**data)

cursor = conn.cursor()

cursor.execute(sql)
cursor.execute('SELECT get_data_with_pagination(%s, %s, %s)', ('phonebook', 3, 2))
cursor.close()
conn.commit()
conn.close()