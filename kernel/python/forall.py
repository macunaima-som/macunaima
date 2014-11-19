

import web

urls = ("/.*", "hello")
application = web.application(urls, globals()).wsgifunc()

class hello:
    def GET(self):
        return 'Hello, world!'



#import web
#import forall.webapp


#urls = ("/", "forall.webapp.WebApp")

#app = web.application(urls, globals())


#if __name__ == "__main__":
#    app.run()
