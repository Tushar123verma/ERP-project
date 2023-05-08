import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ord.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Order_(po_NO INTEGER PRIMARY KEY AUTOINCREMENT,offerNo INTEGER,podate text,Cname text,addr text,pName text,contact text,email text,project_leader text)')
    con.commit()
create_db()
