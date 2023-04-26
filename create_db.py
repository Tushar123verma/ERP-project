import sqlite3
def create_db():
    con=sqlite3.connect(database=r'erp.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,usertype text,aadhar text,pan text,address text)')
    con.commit()
create_db()