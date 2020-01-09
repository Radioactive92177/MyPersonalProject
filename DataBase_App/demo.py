import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
print("Connection Success")
