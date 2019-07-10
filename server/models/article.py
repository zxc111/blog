# coding: utf-8

import time

from sqlalchemy import (
    Column, String,
    Integer, Text
)

from models.base import Base


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    title = Column(String(64), )
    content = Column(Text)
    created_at = Column(Integer, default=time.time, index=True)
    updated_at = Column(Integer, default=time.time, index=True)
    owner = Column(Integer)

    @property
    def dict(self):
        return dict(
                id=self.id,
                title=self.title,
                content=self.content,
                created_at=self.created_at,
                updated_at=self.updated_at,
                )
