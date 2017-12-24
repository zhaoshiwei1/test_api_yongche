# -*- coding: UTF-8 -*-
# add to git remote
import web
import sys

from db_utility import db_action
from utility import utility
reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'start',
    '/new_api_i', 'add_api_start',
    '/new_api_ii', 'add_api_submit',
    '/show_tc', 'show_test_case',
    '/del_tc', 'delete_test_case',
    '/view_tc', 'view_test_case'
)

app = web.application(urls, globals())


class start:

    def GET(self):
        d_a = db_action()
        result = d_a.get_all_api_list()
        render = web.template.render('templates/')
        return render.index(result)

    def POST(self):
        d_a = db_action()
        input_set = web.input()
        if input_set.has_key("del_api_btn"):
            d_a.delete_api_by_id(input_set["del_api_btn"])
        return self.GET()


class add_api_start:

    def GET(self):
        form = web.form.Form(
            web.form.Textbox('API_MODULE', web.form.notnull, description="接口模块："),
            web.form.Textbox('API_NAME', web.form.notnull, description="接口名称："),
            web.form.Textbox('API_URL', web.form.notnull, description="接口地址："),
            web.form.Dropdown('API_METHOD', description="接口HTTP方法：", args=["GET", "POST"]),
            web.form.Textbox('API_PARAM_NUM', web.form.notnull, description="接口参数数目："),
            web.form.Button("CONTINUE")
        )
        render = web.template.render('templates/')
        return render.add_api_page(form)

    def POST(self):
        d_a = db_action()
        uti = utility()
        api_dic = {}
        input_set = web.input()
        if input_set.has_key("CONTINUE"):
            para_num = input_set["API_PARAM_NUM"]
            api_dic["API_METHOD"] = input_set["API_METHOD"]
            api_dic["API_URL"] = input_set["API_URL"]
            api_dic["API_PARAM_NUM"] = para_num
            api_dic["API_NAME"] = input_set["API_NAME"]
            api_dic["API_MODULE"] = input_set["API_MODULE"]
            form_string = uti.make_text_form(api_dic["API_PARAM_NUM"])
            API_string = api_dic["API_MODULE"] + " : " + api_dic["API_NAME"] + " : " + api_dic["API_URL"]
            API_ID = d_a.get_max_id()
            d_a.new_api_general(api_dic, API_ID)
            render = web.template.render('templates/')
            return render.add_api_page_submit(API_ID, API_string, form_string)


class add_api_submit:

    def GET(self):
        return web.seeother('/')

    def POST(self):
        d_a = db_action()
        input_set = web.input()
        if input_set.has_key("submit_api_btn"):
            API_ID = input_set.pop("submit_api_btn")
            value_list = input_set.values()
            d_a.update_param_by_id(API_ID, value_list)
            return web.seeother('/')


class show_test_case:

    def GET(self):
        category_dic = {}
        d_a = db_action()
        uti = utility()
        result = d_a.get_all_api_list()
        for item in result[1]:
            category_string = ""
            category_string += item[1] + """ : """
            category_string += item[2] + """ : """
            category_string += item[3]
            category_dic[item[0]] = category_string
        render = web.template.render('templates/')
        return render.test_case_i(uti.make_category_form(category_dic, 0))

    def POST(self):
        input_set = web.input()
        if input_set["category_id"] == "NULL":
            return web.seeother('/show_tc')
        else:
            api_id = input_set["category_id"]
            category_id_fake = int(api_id) + 1
            category_dic = {}
            d_a = db_action()
            tc_body = d_a.get_tc_list_by_api_id(api_id)
            uti = utility()
            result = d_a.get_all_api_list()
            for item in result[1]:
                category_string = ""
                category_string += item[1] + """ : """
                category_string += item[2] + """ : """
                category_string += item[3]
                category_dic[item[0]] = category_string
            render = web.template.render('templates/')
            return render.test_case_ii(uti.make_category_form(category_dic, category_id_fake), tc_body)


class delete_test_case:

    def GET(self):
        return web.seeother('/show_tc')

    def POST(self):
        input_set = web.input()
        if input_set.has_key("del_tc_btn"):
            tc_id = input_set["del_tc_btn"]
            d_a = db_action()
            d_a.delete_tc_by_id(tc_id)
        return self.GET()


class view_test_case:

    def POST(self):
        input_set = web.input()
        if input_set.has_key("v_tc_details"):
            tc_id = input_set["v_tc_details"]
            d_a = db_action()
            details_string = d_a.get_tc_details_by_id(tc_id)
            if len(details_string[0]) == len(details_string[1]):
                render = web.template.render('templates/')
                return render.test_case_iii(details_string)
            else:
                return "Error Code: NOT DEFINED"

if __name__ == "__main__":
        app.run()