#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2017-04-06
@author: Heysion Yuan
@copyright: 2017, Heysion Yuan <heysions@gmail.com>
@license: GPLv3
'''
from dmd.dmdweb import WebBase

class TaskNew(WebBase):
    def prepare(self):
        pass
    def on_finish(self):
        super(TaskList, self).on_finish()

    def get(self):
        self.render("task.html")
        # task_items = [
        #     {"id":1,"name":"deepin-auto-build","createtime":"2017","state":"success","resultinfo":"info"},
        #     {"id":2,"name":"deepin-auto-build","createtime":"2017","state":"success","resultinfo":"info"}
        # ]
        # self.render("task.html", tasklist=task_items)
        pass
    def post(self):
        self.render("task.html")
    pass

class TaskInfo(WebBase):
    pass
