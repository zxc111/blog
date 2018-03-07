# coding: utf-8
import time
import json

from uuid import uuid4

_missing = object()


class SingletonMeta(type):
    """单例的__metaclass__

    用来实现单例，不知道是否线程安全
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


class cached_property(property):
    """重写property，添加一个缓存机制，使用了_missing后，对None值也可以缓存

    设计思路：
    缓存的值写在"_{}".format(attribute_name)里面，
    所有缓存都标记在"_cached_properties"里面。
    想过设计更统一的东东，比如所有缓存的值都写在一个attribute里面，不过似乎写setter的时候会坑
    切忌：除了setter之外，其他代码尽力不要设置"_{}".format(attribute_name)里的值，否则代码会相当confused
    """
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = obj.__dict__.get("_{}".format(self.fget.__name__), _missing)  # 手动在__dict__里面查找
        if value is _missing:
            value = super(cached_property, self).__get__(obj, objtype)  # 找不到就获取值
            obj.__dict__["_{}".format(self.fget.__name__)] = value  # 写入数据
            self._addCachedProperties(obj)
        return value

    def __set__(self, obj, value):
        super(cached_property, self).__set__(obj, value)  # 调用父类的方法
        self._addCachedProperties(obj)

    def __delete__(self, obj):
        super(cached_property, self).__delete__(obj)
        self._delCachedProperties(obj)

    def _addCachedProperties(self, obj):
        """在类的缓存set里面标记一下"""
        try:
            obj._cached_properties.add(self.fget.__name__)
        except AttributeError:
            obj._cached_properties = {self.fget.__name__}

    def _delCachedProperties(self, obj):
        """把类的单个缓存清理掉"""
        if self.fget.__name__ in obj.__dict__:  # 安全做法，囧
            del obj.__dict__["_{}".format(self.fget.__name__)]
            obj._cached_properties.remove(self.fget.__name__)

    @classmethod
    def delCachedProperties(cls, obj):
        """批量obj清除缓存的方法"""
        if hasattr(obj, "_cached_properties"):
            for item in obj._cached_properties.copy():
                del obj.__dict__["_{}".format(item)]
                obj._cached_properties.remove(item)
