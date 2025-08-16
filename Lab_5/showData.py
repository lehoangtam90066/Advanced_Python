import mysql.connector 
import MySQL_connect_with_dict as guiConf 

GUIDB = 'GuiDB' 
 
# unpack dictionary credentials  
conn = mysql.connector.connect(**guiConf.dbConfig) 
 
cursor = conn.cursor() 

cursor.execute("SHOW DATABASES") 
print(cursor.fetchall()) 
 
conn.close() 