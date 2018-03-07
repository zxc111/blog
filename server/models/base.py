import redis

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from utils.utils import SingletonMeta
from config.config import Config

Base = declarative_base()


class Connection(metaclass=SingletonMeta):

    def __init__(self, env):
        """传入env表示环境"""
        self.env = env

        config = Config(env=self.env)

        print(env)
        print(config.mysql)
        print(config.redis)
        self.engine = create_engine(**config.mysql)
        pool = redis.ConnectionPool(**config.redis)
        self.redis = redis.Redis(connection_pool=pool)


class LoadModule:

    def __init__(self):
        from models.article import Article

        Base.metadata.create_all(bind=Connection().engine)
