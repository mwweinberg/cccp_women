#python3

import sqlite3

#open the db
db = sqlite3.connect('china1')

# Get a cursor object
cursor = db.cursor()

#input variables to fill the db
name = input("Name: ")
province = input("Province: ")
city = input("City: ")
rank = input("Rank: ")
title = input("Title: ")


#inserts into the tabled called "members".  Looks for columns (name, provice, city).  Inserts the value associated with the variables from above.
cursor.execute("INSERT INTO members(name, province, city) VALUES(?, ?, ?)", (name, province, city))

#same thing,  just in the titles table.
cursor.execute("INSERT INTO positions(rank_indiv, title) VALUES(?, ?)", (rank, title))

#writes it to the db
db.commit()
