

import web
import forall.webapp

urls = (".*", "forall.webapp.WebApp")
application = web.application(urls, globals()).wsgifunc()


