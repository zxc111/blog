from tornado.web import UIModule


class Header(UIModule):
    def render(self, ):
        return self.render_string("header.html")


class Footer(UIModule):
    def render(self, ):
        return self.render_string("footer.html")
