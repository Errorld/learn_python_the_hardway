#!/usr/bin/env python
#!encoding: utf-8
#########################################################################
# File Name: bin/app.py
# Author: Errorld
# Mail: errorld@outlook.com
# Created Time: Fri 20 Nov 2015 11:52:03 AM CST
#########################################################################

import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()
