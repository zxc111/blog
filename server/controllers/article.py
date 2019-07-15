from base_controller import BaseController
from models.article import Article
import json
import logging


class ArticleList(BaseController):
    urls = r"/article/list/?"

    def get(self):
        page = int(self.get_argument("page", 1))
        page_size = int(self.get_argument("page_size", 10))
        if page_size > 10 or page_size < 1:
            page_size = 10
        page -= 1
        count = self.session.query(Article).count()
        articles = (self.session
                .query(Article)
                .order_by(Article.id.asc())
                .offset(page*page_size)
                .limit(page_size)
                .all())
        self.write(
                dict(
                    data=dict(
                        articles=[i.dict for i in articles],
                        total=count,
                        ),
                    status=0
                    )
                )


class ArticleCreate(BaseController):
    urls = r"/article/new/?"

    def get(self):
        self.write("123")
        pass

    def post(self):
        try:
            body = json.loads(self.request.body)
        except Exception as e:
            logging.error(e, exc_info=True)
            self.write({"status": 1})
            return
        title = body.get("title", "")
        content = body.get("content", "")
        new_article = Article(
                title=title,
                content=content,
                )
        self.save(new_article)
        self.write({"status": 0})




class ArticleUpdate(BaseController):
    urls = r"/article/([0-9]+)/update/?"

    def post(self, aid):
        pass


class ArticleDelete(BaseController):
    urls = r"/article/([0-9]+)/delete/?"

    def post(self):
        pass

class ArticleDetail(BaseController):
    urls = r"/article/([0-9]+)/?"

    def get(self, aid):
        # import pdb; pdb.set_trace()
        article = (self.session.query(Article)
                .filter(Article.id == aid)
                .first()
                )
        self.write(dict(
            status=0,
            article=article.dict,
            ))
        
    def post(self, aid):
        body = self.request.body
        if body == "":
            self.write({"status": 1})
            return
        body = json.loads(body)

        (self.session
        .query(Article)
        .filter(Article.id == aid)
        .update(
            body
            )
        )
        res = self.commit()
        if res:

            self.write({"status": 0})
        else:
            self.write({"status": 1})
