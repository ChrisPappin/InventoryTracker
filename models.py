import sqlite3 as sql
from os import path
import csv

ROOT = path.dirname(path.relpath((__file__)))

def createItem(name, amount):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into items (name, amount) values(?,?)', (name, amount))
    con.commit()
    con.close()

def getItems():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from items')
    items = cur.fetchall()
    return items

def deleteItem(id):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('delete from items where id=?', (id,))
    con.commit()
    con.close()

def editItem(name, amount): 
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('update items set amount=? where name=?', (amount, name))
    con.commit()
    con.close()

def getOneItem(id):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from items where id=?', (id,))
    item = cur.fetchall()
    return item

def createCSV():
    
    #GET all data from db
    items = getItems()

    with open('outputs\Inventory.csv', 'w') as myEmptyCSV:
        writer = csv.writer(myEmptyCSV)

        for item in items:
            writer.writerow(item)

