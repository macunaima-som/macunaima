
import os
here = os.path.dirname(__file__)

import sys
if here not in sys.path:
    sys.path.append(here)

import web

import forall.webapp

urls = (".*", "forall.webapp.WebApp")
application = web.application(urls, globals()).wsgifunc()


