#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
import time
import functools
import tornado.gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from dmd.dmdweb import WebBase

class TaskNew(WebBase):
    _thread_pool = ThreadPoolExecutor(5)
    def prepare(self):
        pass
    def on_finish(self):
        super(TaskNew, self).on_finish()

    def get(self):
        self.render("task.html")
        # task_items = [
        #     {"id":1,"name":"deepin-auto-build","createtime":"2017","state":"success","resultinfo":"info"},
        #     {"id":2,"name":"deepin-auto-build","createtime":"2017","state":"success","resultinfo":"info"}
        # ]
        # self.render("task.html", tasklist=task_items)
        pass
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        tornado.ioloop.IOLoop.instance().add_callback(functools.partial(self.call_mkiso,"abc"))
        self.render("task.html")

    @tornado.concurrent.run_on_executor(executor='_thread_pool')
    def call_mkiso(self,data):
        time.sleep(5)
        print("over!")
        pass
    pass

class TaskInfo(WebBase):
    pass
