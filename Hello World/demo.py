from dotenv import dotenv_values
import psycopg2

config = dotenv_values()

connection = psycopg2.connect(database = config['DB_NAME'], user = config['USER'], password = config['PASSWORD'])

cursor = connection.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS todos (
                   id INTEGER PRIMARY KEY,
                   completed BOOLEAN NOT NULL DEFAULT FALSE); 
                   ''')
cursor.execute('INSERT INTO todos (id, completed)' + 
               'VALUES (2, false);')

connection.commit()

cursor.close()
connection.close()
