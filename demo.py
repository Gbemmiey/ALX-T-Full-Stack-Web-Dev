import psycopg2

connection = psycopg2.connect(database="demo", user="postgres", password="deft_dev")
cursor = connection.cursor()
