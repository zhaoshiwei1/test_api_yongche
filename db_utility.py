import os
import sqlite3


class db:

    def __init__(self):
        if os.path.exists("yc_api_test.db3"):
            self.conn = sqlite3.connect("yc_api_test.db3")
            self.cu = self.conn.cursor()
        else:
            print "DataBase File Not Found"


class db_action:

    def __init__(self):
        self.db = db()

    def get_all_api_list(self):
        rec = self.db.cu.execute("SELECT API_ID, API_MODULE, API_NAME, API_URL FROM API_COMMON")
        col_name_list = [tuple[0] for tuple in rec.description ]
        all_information = []
        all_information.append(col_name_list)
        all_information.append(self.db.cu.fetchall())
        return all_information

