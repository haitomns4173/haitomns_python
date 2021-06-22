import mysql.connector

conn = mysql.connector.connect(host="localhost",user="python_program",password="123",database="python_test")

cursor = conn.cursor()

cursor.execute("SELECT * FROM users_data")

myresult = cursor.fetchall()

for x in myresult:
  print(x)


conn.close()