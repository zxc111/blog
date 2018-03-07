from base_controller import BaseController
from models.article import Article


class ArticleList(BaseController):
    urls = r"/article/list/?"

    def get(self):
        self.render("article_list.html")
        pass


class ArticleCreate(BaseController):
    urls = r"/article/new/?"

    def get(self):
        pass

    def post(self):
        pass


class ArticleUpdate(BaseController):
    urls = r"/article/([0-9]+)/update/?"

    def post(self, aid):
        pass


class ArticleDelete(BaseController):
    urls = r"/article/([0-9]+)/delete/?"

    def post(self):
        pass
