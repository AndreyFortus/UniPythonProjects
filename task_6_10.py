import sqlite3
import csv

conn = sqlite3.connect('imdb.db')

# create ratings
conn.execute('''CREATE TABLE IF NOT EXISTS ratings
             (id INTEGER PRIMARY KEY,
             title VARCHAR(20),
             year INT,
             rating FLOAT)''')

with open('imdb.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip title
    for row in reader:
        conn.execute("INSERT INTO ratings (title, year, rating) VALUES (?, ?, ?)",
                     (row[1], int(row[2]), float(row[3])))

# save changes in DB
conn.commit()

print("Усі записи у таблиці ratings:")
result = conn.execute("SELECT * FROM ratings ORDER BY title")
for row in result:
    print(row)

print("\nЗаписи у таблиці ratings з ретингом більшим за 8.70:")
result = conn.execute("SELECT * FROM ratings WHERE rating > 8.70")
for row in result:
    print(row)

conn.close()
