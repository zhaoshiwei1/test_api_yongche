import os
import sqlite3


class db:

    def __init__(self):
        if os.path.exists("yc_api_test.db3"):
            self.conn = sqlite3.connect("yc_api_test.db3", check_same_thread=False)
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


    def delete_api_by_id(self, id):
        self.db.cu.execute("DELETE FROM API_COMMON WHERE API_ID = " + id)
        self.db.conn.commit()
        self.db.conn.close()

    def new_api_general(self, api_dic, API_ID):
        api_dic["API_ID"] = API_ID
        sql = """
            INSERT INTO API_COMMON (API_ID, API_MODULE, API_NAME, API_URL, API_METHOD, API_PARAM_NUM)
                             VALUES(
        """
        sql += str(api_dic["API_ID"]) + """, """
        sql += """\"""" + api_dic["API_MODULE"] + """\", """
        sql += """\"""" + api_dic["API_NAME"] + """\", """
        sql += """\"""" + api_dic["API_URL"] + """\", """
        sql += """\"""" + api_dic["API_METHOD"] + """\", """
        sql += """\"""" + api_dic["API_PARAM_NUM"] + """\" ) """
        self.db.cu.execute(sql)
        self.db.conn.commit()
        self.db.conn.close()

    def get_max_id(self):
        l = []
        self.db.cu.execute("SELECT DISTINCT API_ID FROM API_COMMON")
        result_set = self.db.cu.fetchall()
        for m in result_set:
            l.append(int(m[0]))
        if len(l) == 0:
            return 0
        else:
            return max(l)+1


    def update_param_by_id(self, id, param_list):
        param_string = ';'.join(param_list)
        sql = """
            UPDATE API_COMMON SET API_PARAMS =
        """
        sql += "\"" + param_string + "\""
        sql += """ WHERE API_ID = """
        sql += id
        self.db.cu.execute(sql)
        self.db.conn.commit()
        self.db.conn.close()
