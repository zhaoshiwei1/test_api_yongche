# -*- coding: UTF-8 -*-
# add to git remote
import web
import sys

from db_utility import db_action

reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'start'
)

app = web.application(urls, globals())


class start:

    def GET(self):
        d_a = db_action()
        result = d_a.get_all_api_list()
        print result[1][0][0]
        render = web.template.render('templates/')
        return render.index(result)

    def POST(self):
        return self.GET()

if __name__ == "__main__":
        app.run()