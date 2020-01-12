import MySQLdb


class DbConnection:
    def __init__(self, name_of_db):
        self.name_of_db = name_of_db
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                            user="root",         # your username
                            passwd="",  # your password
                            db=self.name_of_db)        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        cur = db.cursor()
    
    def delete_db(self):
        cur.execute("DROP DATABASE %s", self.name_of_db)
        db.close()
        # Use all the SQL you like
        # cur.execute("SELECT * FROM YOUR_TABLE_NAME")

        # # print all the first cell of all the rows
        # for row in cur.fetchall():
        #     print row[0]

        # db.close()