import sqlite3
from flask import flash
import feedparser
import hashlib
from dateutil import parser as date_parser
def Hash(plaintext):
    return hashlib.sha256(bytes(plaintext, 'utf-8')).hexdigest()
def addUser(username,password):
    conn = sqlite3.connect('pwd.db')
    c= conn.cursor()
    c.execute(""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users' """)
    if c.fetchone()[0]!=    1 : 
        flag=1
        c.execute("""CREATE TABLE Users (id INTEGER,username TEXT,password TEXT)""")
        c.execute("INSERT INTO Users VALUES (:id, :username,:password)",{'id':1,'username':'admin','password':Hash('admin')})
    else:
        flag=0
        c.execute("INSERT INTO Users VALUES (:id, :username,:password)",{'id':0, 'username':username,'password':Hash(password)})
    conn.commit()
    conn.close()
    return flag

def validateUser(username,password):
    print("inside validation")
    conn = sqlite3.connect('pwd.db')
    c = conn.cursor()
    c.execute(" SELECT * FROM Users WHERE username = (:username) AND password = (:password)",{'username':username,'password':Hash(password)})
    result=c.fetchall()
    print(result)
    if len(result)==0 :
        flash("Incorrect Password  !")
        return -1
    conn.commit()
    conn.close()
    return result[0][0]