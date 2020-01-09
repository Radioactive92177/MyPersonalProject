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
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    address = input("Enter Address: ")

    query = '''INSERT INTO demo_table(name, age, address) VALUES (%s,%s,%s);'''
    cur.execute(query, (name, age, address))
    print("Data Inserted")
    conn.commit()
    conn.close()

insert_data()
