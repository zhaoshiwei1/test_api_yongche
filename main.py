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
    '/new_api_i', 'add_api_start'
)

app = web.application(urls, globals())


class start:
    d_a = db_action()

    def GET(self):
        result = self.d_a.get_all_api_list()
        render = web.template.render('templates/')
        return render.index(result)

    def POST(self):
        input_set = web.input()
        if input_set.has_key("del_api_btn"):
            self.d_a.delete_api_by_id(input_set["del_api_btn"])
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
            form_string = uti.make_textbox_form(api_dic["API_PARAM_NUM"])
            API_string = api_dic["API_MODULE"] + " : " + api_dic["API_NAME"] + " : " + api_dic["API_URL"]
            render = web.template.render('templates/')
            return render.add_api_page_submit(API_string, form_string)


if __name__ == "__main__":
        app.run()