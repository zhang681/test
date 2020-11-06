import sqlite3
import random

conn = sqlite3.connect('testQueLib.db')
cursor = conn.cursor()
def Update(n,name1):
    if(n==1):
        cursor.execute("update users set number=number+1,true=true+1 where name='"+str(name1)+"'")
    else:
        cursor.execute("update users set number=number+1 where name='" + str(name1)+"'")
    conn.commit()

def select():
    return cursor.execute("SELECT * from QUESTIONS where id="+str(random.randint(1,16)))
def check(name1):
    ff=cursor.execute("SELECT * from users where name='"+str(name1)+"'")
    return ff
def add(name1):
    c=cursor.execute("INSERT INTO users(name,number,true) values('"+name1+"',0,0)")
    conn.commit()
    # print(c)
    return c
# cursor.execute("INSERT INTO users(name,number,true) values('12345',0,0)")
# cursor.close()
# conn.commit()
# conn.close()