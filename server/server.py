# coding: utf8

import logging
import tornado.ioloop

from tornado import ioloop
from tornado.options import options
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.log import access_log

from utils.controller_loader import ControllerLoader
from models.base import Connection, LoadModule


class Application(Application):
    def __init__(self):
        handlers = ControllerLoader().discover(
            "controllers",
            urls_py="urls.ini"
        )
        if options.config == "dev":
            debug = True
        else:
            debug = False

        settings = dict(
            cookie_secret="temp",
            xsrf_cookies=True,
            debug=debug,
        )
        super(Application, self).__init__(handlers, **settings)

    def log_request(self, handler):
        """Writes a completed HTTP request to the logs.
        OVERLAY origin log_request
        """
        if "log_function" in self.settings:
            self.settings["log_function"](handler)
            return
        if handler.get_status() < 400:
            log_method = access_log.info
        elif handler.get_status() < 500:
            log_method = access_log.warning
        else:
            log_method = access_log.error
        request_time = 1000.0 * handler.request.request_time()
        source = handler.request.headers.get("source", "unknow")
        origin_ip = handler.request.headers.get("origin_ip", "unknow")

        log_method(
            "%d %s %.2fms %s %s",
            handler.get_status(),
            handler._request_summary(),
            request_time,
            source,
            origin_ip
        )


if __name__ == "__main__":
    options.define(name="config", default="dev")
    options.define(name="port", default="22345")
    options.define(name="process", default=1)
    options.define(name="name", default="default")

    options.parse_command_line()
    Connection(env=options.config)
    LoadModule()

    APP = Application()

    logging.info("Starting API Server...")
    logging.info("Listening on port: %s" % options.port)

    SERVER = HTTPServer(APP, xheaders=True)
    SERVER.bind(int(options.port))
    SERVER.start(num_processes=options.process)
    ioloop.IOLoop.instance().start()
