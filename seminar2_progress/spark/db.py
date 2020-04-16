import sqlite3
from sqlite3 import Error
from random import randint

def create_conn(db_file):
     try:
         conn = sqlite3.connect(db_file)
     except Error as e:
         print(e)
     finally:
         conn.close()

conn = sqlite3.connect('db\\sqlite\\db\\pythonsqlite.db')

c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")


def create_tables(c):
    try:

        c.execute('CREATE TABLE IF NOT EXISTS LOGIN'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'email text, '
                  'pswd text)');

        c.execute('CREATE TABLE IF NOT EXISTS STUD_INFO'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'fname text, '
                  'lname text, '
                  'sem_id integer, '
                  'FOREIGN KEY(id) REFERENCES LOGIN(id) ON DELETE CASCADE)');

        c.execute('CREATE TABLE IF NOT EXISTS GPA_DETAILS'
                  '(id integer, '
                  'sem1 real, '
                  'sem2 real, '
                  'sem3 real, '
                  'sem4 real, '
                  'sem5 real, '
                  'sem6 real, '
                  'sem7 real, '
                  'sem8 real, '
                  'FOREIGN KEY(id) REFERENCES STUD_INFO(id) ON DELETE CASCADE)');

    except Error as e:
        print(e)


create_tables(c)
conn.commit()


def populate(c):
    try:
        # id, email, pswd


        LOGIN_INFO = [(1, '15001001015', 'harsh123'),
                       (2, '15001001058', 'vikas123')]

        c.executemany('INSERT INTO LOGIN VALUES (?,?,?)', LOGIN_INFO)

        # id, fname, lname, sem_id


        STUD_DETAILS = [(1, 'Harsh', 'Pandey', 6),
                         (2, 'Vikas', 'Sangwan', 7)]

        c.executemany('INSERT INTO STUD_INFO VALUES (?,?,?,?)', STUD_DETAILS)

        # id, sem(1 to 8)


        GPA_DETAILS = [(1, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 7.6 , 8.1 , 0.0),
                       (2, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 8.9 , 8.3 , 0.0)
                       ]

        c.executemany('INSERT INTO GPA_DETAILS VALUES (?,?,?,?,?,?,?,?,?)', GPA_DETAILS);

    except Error as e:
        print(e)


populate(c)
conn.commit()
