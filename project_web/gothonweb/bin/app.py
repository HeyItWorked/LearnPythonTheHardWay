import web
import sys
sys.path.append(
    '/Users/lamnguyen/Downloads/the hard way/project_web/gothonweb/bin/webpy-0.61')

urls = (
    '/', 'index'
)

app = web.application(urls, globals())


class index:
    def GET(self):
        greeting = "Hello World"
        return greeting


if __name__ == "__main__":
    app.run()
