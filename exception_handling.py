import traceback as tb
file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        for line in file_in:
            line = line.rstrip()
            print(line)
except FileNotFoundError as err:   # 'catch' in Java
    print(err, err.errno, err.args)
    # tb.print_exc()

data = [1, 2, 3, 4]
try:
    value = data[19]
except (IndexError, KeyError) as err:
    print(err)
except Exception as err:
    print(err)
else:
    print(value)

values = 5, 9, 0, 15, "22", "wombat", 45
factor = 99

for value in values:
    try:
        result = factor / int(value)
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print("Invalid data!! Bad vendor!")
    else:
        print(result)

import pymysql
conn = None

try:
    conn = pymysql.connect(host='dbserver', db='mydb', user='john', password='l0lz')
except pymysql.OperationalError as err:
    print(err)
    print("WE are doomed!")
    exit()
else:
    cursor = conn.cursor()
    cursor.execute('select * from customers')
    for row in cursor.fetchall():
        print(row)
finally:
    if conn:
        conn.close()
    print("cleaning up")