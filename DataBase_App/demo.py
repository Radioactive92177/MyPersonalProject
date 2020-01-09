import psycopg2


def create():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE DEMO_Table(Name text, Age text, Address text);''')
    print("Table Created")
    conn.commit()
    conn.close()


def insert_data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="6502", host="localhost")
    cur = conn.cursor()
    cur.execute('''INSERT INTO demo_table(name, age, address) VALUES ('John',25,'NY');''')
    print("Data Inserted")
    conn.commit()
    conn.close()


insert_data()
