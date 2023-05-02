from config import data
import psycopg2

sql = '''
   CREATE PROCEDURE insert_new_users(
    names_list TEXT[],
    phones_list TEXT[],
    OUT incorrect_phones_list TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
    phone_pattern VARCHAR(20) := '^[0-9]{10,12}$'; -- pattern for valid phone numbers
    incorrect_phones VARCHAR(255) := '';
BEGIN
    WHILE i <= array_length(names_list, 1) LOOP
        IF phones_list[i] ~ phone_pattern THEN
            INSERT INTO phonebook(name, phonenumber) VALUES(names_list[i], phones_list[i]);
        ELSE
            incorrect_phones := CONCAT(incorrect_phones, phones_list[i], ',');
        END IF;

        i := i + 1;
    END LOOP;

    incorrect_phones_list := TRIM(BOTH ',' FROM incorrect_phones);
END $$;

'''



conn = psycopg2.connect(**data)

cursor = conn.cursor()

names_list = 'Johnny_Cage, Qairat, Samat'
phones_list = '1234567890,999-888-7777,123'
cursor.execute(f"CALL insert_new_users('{names_list}', '{phones_list}', %s)", ('',))
incorrect_phones_list = cursor.fetchone()[0]
print(f"Incorrect phone numbers: {incorrect_phones_list}")

cursor.close()
conn.commit()
conn.close()