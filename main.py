# -*- coding: UTF-8 -*-

import web
import sys

reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'start'
)

app = web.application(urls, globals())


class start:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, description='Post title: '),

        web.form.Textbox('content', web.form.notnull, description='Post content: '),

        web.form.Button('Post entry'),
    )
    a = ['1', '2', '3']

    def GET(self):
        form = self.form
        render = web.template.render('templates/')
        return render.index(form)

    def POST(self):
        get_input = web.input()
        print get_input
        form = self.form
        render = web.template.render('templates/')
        return render.index(form)

if __name__ == "__main__":
        app.run()