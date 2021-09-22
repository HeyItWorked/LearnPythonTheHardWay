import web
urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')


class Index(object):
    def GET(self):
        greeting = "Hello World"
        # render.index because it's invoking index.html, this can be render. any html file
        return render.index(greeting=greeting)


if __name__ == "__main__":
    app.run()

"""
import web is possible by placing file near the folder your wish to import but that folder
needs to have an empty __init__.py file
"""
