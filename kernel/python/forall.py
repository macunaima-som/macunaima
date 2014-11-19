

import web

urls = ("/.*", "hello")

class hello:
    def GET(self):
        return 'Hello, world!'

application = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
    application.run()


#import web
#import forall.webapp


#urls = ("/", "forall.webapp.WebApp")

#app = web.application(urls, globals())


#if __name__ == "__main__":
#    app.run()
