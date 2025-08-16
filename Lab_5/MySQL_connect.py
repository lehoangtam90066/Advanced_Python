# import mysql.connector

# # Thay <adminUser> và <adminPwd> bằng tên người dùng và mật khẩu thực tế
# conn = mysql.connector.connect(
#     user='Le Hoang Tam',  # Tên người dùng của bạn
#     password='Tamle90066@',  # Mật khẩu của bạn
#     host='127.0.0.1'  # Địa chỉ host (localhost)
# )

# print(conn)  # In ra kết nối thành công
# conn.close()  # Đóng kết nối







# import mysql.connector
# import MySQL_connect_with_dict as guiConf
# GUIDB = 'GuiDB'

# # unpack dictionary credentials
# conn = mysql.connector.connect(**guiConf.dbConfig)

# cursor = conn.cursor()
# try:
#     cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(GUIDB))
#     print("Database {} created successfully.".format(GUIDB))
# except mysql.connector.Error as err:  
#     print("Failed to create DB: {}".format(err))
# finally:
#     conn.close()  # Đảm bảo đóng kết nối dù có lỗi hay không




import mysql.connector
from mysql.connector import Error
from pprint import pprint
import sys
import io

# Thiết lập mã hóa đầu ra cho console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    # Kết nối đến cơ sở dữ liệu
    connection = mysql.connector.connect(
        host='127.0.0.1',  # hoặc địa chỉ máy chủ của bạn
        user='Le Hoang Tam',  # tên người dùng MySQL
        password='Tamle90066@',  # mật khẩu MySQL
        database='guidb'  # tên cơ sở dữ liệu
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Tạo bảng Quotations
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Quotations (
            Quote_ID INT AUTO_INCREMENT PRIMARY KEY,
            Quotation VARCHAR(250),  
            Books_Book_ID INT,
            FOREIGN KEY (Books_Book_ID)  
                REFERENCES Books(Book_ID)  
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """
        cursor.execute(create_table_query)

        # Lấy thông tin cột từ bảng Quotations
        cursor.execute("SHOW COLUMNS FROM Quotations")
        quotations_columns = cursor.fetchall()

        # Lấy thông tin cột từ bảng Books
        cursor.execute("SHOW COLUMNS FROM Books")
        books_columns = cursor.fetchall()

        # In kết quả
        print("Thông tin cột từ bảng Quotations:")
        pprint(quotations_columns)

        print("\nThông tin cột từ bảng Books:")
        pprint(books_columns)

except Error as e:
    print("Lỗi:", e)

finally:
    # Đóng kết nối
    if connection.is_connected():
        cursor.close()
        connection.close()










