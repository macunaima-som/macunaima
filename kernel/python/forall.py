
import web
import forall.webapp


urls = ("/", "forall.webapp.WebApp")

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
