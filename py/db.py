import mysql.connector as mysql

class DatabaseConnection(object):
    def __new__(cls, *args, **kwargs):
        conn = mysql.connect(
            host='127.0.0.1',
            database='pocoh',
            user='root',
            password=''
        )
        # print("connected")
        # print(type(conn))
        return conn