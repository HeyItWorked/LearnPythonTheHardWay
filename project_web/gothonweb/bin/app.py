import web
urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting=greeting)


if __name__ == "__main__":
    app.run()

"""
import web is possible by placing file near the folder your wish to import but that folder
needs to have an empty __init__.py file
"""
