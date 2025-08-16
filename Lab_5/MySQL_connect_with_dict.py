import mysql.connector
dbConfig = {
'user': "Le Hoang Tam",  
'password': "Tamle90066@",  
'host': '127.0.0.1',
}
# unpack dictionary credentials
conn = mysql.connector.connect(**dbConfig)  
print(conn)

