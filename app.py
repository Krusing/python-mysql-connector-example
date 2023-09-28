import mysql.connector

cnx = mysql.connector.connect(user='root', password='password',host='127.0.0.1',database='mydb')

cursor = cnx.cursor()

try:
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    print("Table names:")
    for table in tables:
        print(table[0])

except mysql.connector.Error as err:
    print("Error on fetching table names: ", err)

finally:
    cursor.close()
    cnx.close()
    