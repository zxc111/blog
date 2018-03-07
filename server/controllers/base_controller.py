# coding: utf8

import traceback
import logging
import json

from tornado.web import RequestHandler
from tornado.log import access_log
from sqlalchemy.orm import sessionmaker

from models.base import Connection as Conn
from utils.utils import cached_property


class BaseController(RequestHandler):
    conn = Conn().engine.connect()
    redis = Conn().redis

    def on_finish(self):
        # 完成时清空sql session
        self.session.rollback()

    @cached_property
    def session(self):
        Session = sessionmaker(bind=Conn().engine, autoflush=False)
        Session.configure(bind=Conn().engine)
        return Session()

    def write_error(self, status_code, **kwargs):
        # 先输出发过来的参数
        logging.warning(self.request.arguments)
        if 'exc_info' in kwargs:
            exception = kwargs['exc_info'][1]
            logging.error("\n".join(traceback.format_exception(*kwargs["exc_info"])))
            self.write(
                dict(
                    error_code=1,
                    msg="内部错误",
                )
            )
        else:
            self.write(
                dict(
                    error_code=1,
                    msg="未知错误",
                )
            )

    def prepare(self):
        pass

    def save(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
        except Exception as e:
            logging.error(e, exc_info=True)
            self.session.rollback()
