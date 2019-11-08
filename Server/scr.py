# FETCH USER HISTORY FROM BROWING DATA STORED IN SQL

# -------------------IMPORTS---------------------
# IMPORT FOR DATABASE READING AND CONNECTIVITY
import sqlite3, os
from datetime import datetime, timedelta

# ------------DATABASE CONNECTIVITY--------------
# DATABASE CONNECTIVITY
history_db = os.path.join('History')

c = sqlite3.connect(history_db)
cursor = c.cursor()

# -------------DATA PRE-PROCESSING---------------
# SELECTING REQUIRED TUPLES FROM THE RELATION
table=[]
epoch = datetime(1601, 1, 1)
for row in (cursor.execute('select url, title, visit_count, last_visit_time from urls')):
    row = list(row)
    url_time = epoch + timedelta(microseconds=row[3])
    row[3] = url_time
    table.append(row)

# SELECTING TUPLES WITH SEARCH RELATED TO LAPTOPS
data = []
for i in table:
    if 'laptop' in i[1] or 'Laptop' in i[1]:
        if 'Graphics' in i[1]:
            data.append(i[1])

# FILTER ONLY SHOPPING HISTORY FROM OBTAINED RESULT
for i in data:
    temp = i.split(' ')
    if temp[0] == 'Amazon.in:':
        lappy_user_likes = temp[2]+' '+temp[3]
    else:
        lappy_user_likes = temp[0]+' '+temp[1]
