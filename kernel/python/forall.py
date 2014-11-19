

import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

if __name__ == "__main__":
    app.run()


#import web
#import forall.webapp


#urls = ("/", "forall.webapp.WebApp")

#app = web.application(urls, globals())


#if __name__ == "__main__":
#    app.run()
