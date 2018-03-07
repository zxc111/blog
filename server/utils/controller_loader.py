# coding=utf-8
import os
import re
import sys
import traceback
import fnmatch
import logging

from tornado.web import RequestHandler


VALID_MODULE_NAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)


class ControllerLoader(object):
    """用于载入所有需要用的controller

    Reference:
        http://hg.python.org/cpython/file/181ced5bf0be/Lib/unittest/loader.py
    """

    def __init__(self):
        self._top_level_dir = None

    def discover(self, start_dir, pattern="*", top_level_dir=None, urls_py=None):
        if top_level_dir is None:
            top_level_dir = start_dir
        top_level_dir = os.path.abspath(top_level_dir)
        if not top_level_dir in sys.path:
            sys.path.append(top_level_dir)
        self._top_level_dir = top_level_dir

        is_not_importable = False
        if os.path.isdir(os.path.abspath(start_dir)):
            start_dir = os.path.abspath(start_dir)
            if start_dir != top_level_dir:
                is_not_importable = not os.path.isfile(os.path.join(start_dir, '__init__.py'))
        else:
            try:
                __import__(start_dir)
            except ImportError:
                is_not_importable = True
            else:
                the_module = sys.modules[start_dir]
                start_dir = os.path.abspath(os.path.dirname(the_module.__file__))
        if is_not_importable:
            raise ImportError('Start directory is not importable: %r' % start_dir)

        controllers = []
        for _controllers in self._find_controllers(start_dir, pattern):
            controllers.extend(_controllers)

        if urls_py is not None:
            self._print_urls_py(controllers, urls_py)

        return controllers

    @staticmethod
    def _print_urls_py(controllers, urls_py):
        """写一个urls_py，不太健壮的一段代码"""
        with open(urls_py, "w") as f:
            f.write("#encoding=utf-8\n")
            f.write("'''\n")
            f.write("Notice the os.path.insert or os.path.append, and the file may fails. It's just a guide.\n")
            f.write("'''\n")
            for controller in controllers:
                uri, obj = controller
                f.write("from {} import {}\n".format(obj.__module__, obj.__name__))
            f.write("\n\n")
            f.write("urls = [\n")
            for controller in controllers:
                uri, obj = controller
                _realPath = sys.modules[obj.__module__].__file__
                import __main__
                _realPath = os.path.relpath(_realPath, __main__.__file__)
                f.write("    (r'{}', {}),  # @file {}\n".format(uri, obj.__name__, _realPath))
            f.write("]\n")

    def _find_controllers(self, start_dir, pattern):
        """在start_dir目录下根据pattern查找controller类"""
        paths = os.listdir(start_dir)
        for path in paths:
            full_path = os.path.join(start_dir, path)  # 当前目录
            if os.path.isfile(full_path):  # 如果是文件，查找文件中的class载入
                if not VALID_MODULE_NAME.match(path):  # 是否为Python文件
                    continue
                if not self._match_path(path, full_path, pattern):
                    continue
                name = self._get_name_from_path(full_path)
                if name == "__init__":
                    continue
                try:
                    module = self._get_module_from_name(name)
                except Exception:  # 类没有正常import，大概需要logging吧
                    logging.warn("Failed to import controller module: {}\n{}".format(name, traceback.format_exc()))
                else:
                    mod_file = os.path.abspath(getattr(module, '__file__', full_path))
                    realPath = os.path.splitext(os.path.realpath(mod_file))[0]
                    fullPath_noteText = os.path.splitext(os.path.realpath(full_path))[0]
                    if realPath.lower() != fullPath_noteText.lower():
                        module_dir = os.path.dirname(realPath)
                        mod_name = os.path.splitext(os.path.basename(full_path))[0]
                        expected_dir = os.path.dirname(full_path)
                        msg = ("%r module incorrectly imported from %r. Expected %r. "
                               "Is this module globally installed?")
                        raise ImportError(msg % (mod_name, module_dir, expected_dir))
                    yield self.loadControllersFromModule(module)
            elif os.path.isdir(full_path):  # 如果是文件夹，迭代进去
                if not os.path.isfile(os.path.join(full_path, '__init__.py')):  # 不是package，不鸟
                    continue
                for controllers in self._find_controllers(full_path, pattern):
                    yield controllers

    @staticmethod
    def generateControllers(controller):
        if not issubclass(controller, RequestHandler):
            return {}
        urls = controller.__dict__.get("urls", [])  # 保证urls不是继承来的
        if isinstance(urls, str):
            urls = [urls, ]
        if isinstance(urls, list):
            return [(url, controller) for url in urls if isinstance(url, str)]
        return []

    def loadControllersFromModule(self, module):
        """返回一个dict，url: RequestHandler"""
        controllers = []
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, RequestHandler):
                controllers.extend(self.generateControllers(obj))
        return controllers

    @staticmethod
    def _match_path(path, full_path, pattern):
        """判断path是否满足pattern"""
        return fnmatch.fnmatch(path, pattern)

    def _get_name_from_path(self, path):
        """根据path返回对应的包名"""
        path = os.path.splitext(os.path.normpath(path))[0]

        _realPath = os.path.relpath(path, self._top_level_dir)
        assert not os.path.isabs(_realPath), "Path must be within the project"
        assert not _realPath.startswith('..'), "Path must be within the project"

        name = _realPath.replace(os.path.sep, '.')
        return name

    @staticmethod
    def _get_module_from_name(name):
        """根据name(字符串)返回对应包"""
        __import__(name)
        return sys.modules[name]
