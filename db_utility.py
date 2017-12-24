# -*- coding: UTF-8 -*-
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

    def get_tc_list_by_api_id(self,api_id):
        # rec = self.db.cu.execute("SELECT * FR0M TC_COMMON WHERE API_ID = " +"\'" + api_id +"\'")
        rec = self.db.cu.execute("SELECT TC_ID, API_ID, TC_NAME, TC_PARAMS from TC_COMMON WHERE API_ID = " + api_id)
        col_name_list = [tuple[0] for tuple in rec.description ]
        tc_body = []
        tc_body.append(col_name_list)
        tc_body.append(self.db.cu.fetchall())
        return tc_body

    def delete_tc_by_id(self, tc_id):
        self.db.cu.execute("DELETE FROM TC_COMMON WHERE TC_ID = " + tc_id)
        self.db.conn.commit()
        self.db.conn.close()

    def get_tc_details_by_id(self, tc_id):
        tc_details = []
        titles = []
        values = []
        self.db.cu.execute("SELECT API_MODULE, API_NAME, API_URL, API_METHOD FROM API_COMMON WHERE API_ID = "
                           "(SELECT API_ID FROM TC_COMMON WHERE TC_ID = " + tc_id + ")")
        reuslt_1 = self.db.cu.fetchall()
        titles.append("接口模块： ")
        values.append(reuslt_1[0][0])
        titles.append("接口名称： ")
        values.append(reuslt_1[0][1])
        titles.append("接口URL: ")
        values.append(reuslt_1[0][2])
        titles.append("接口方法： ")
        values.append(reuslt_1[0][3])
        self.db.cu.execute("SELECT TC_NAME, TC_PARAMS FROM TC_COMMON WHERE TC_ID = " + tc_id)
        result_set = self.db.cu.fetchall()
        titles.append("测试用例名称： ")
        values.append(result_set[0][0])
        param_string_list = result_set[0][1].split("[#]")
        for item in param_string_list:
            param = item.split("(#)")
            titles.append(param[0])
            values.append(param[1])
        tc_details.append(titles)
        tc_details.append(values)
        return tc_details
