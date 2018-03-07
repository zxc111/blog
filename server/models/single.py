# coding: utf8
import time


class SingletonMeta(type):
    """单例的__metaclass__

    Usage:
        >>> class YouClass(object):
        ...     __metaclass__ = SingletonMeta
        ...
        >>> YouClass() is YouClass()
        True
    """
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
