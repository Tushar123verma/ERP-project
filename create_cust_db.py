import sqlite3
def create_db2():
    con=sqlite3.connect(database=r'custmr1.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS customer(org_name text,name text,email text,contact text,address text,project text)')
    con.commit()
create_db2()