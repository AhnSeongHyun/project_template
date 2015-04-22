# -*- coding:utf-8 -*-
__author__ = 'sh.ahn'
import MySQLdb
import functools
import traceback
import sys


class ProjectDB(object):

    cursor = None
    conn = None
    host = None
    user = None
    passwd = None
    db = None
    port = 3306

    def __init__(self, host=None, user=None, passwd=None, db=None, port=3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port

    def exception(func): #try catch exception handler
        @functools.wraps(func)
        def newFunc(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:

                print ("Exception in user code:")
                print ('-'*60)
                traceback.print_exc(file=sys.stdout)
                print ('-'*60)
                raise e


            return result
        return newFunc


    @exception
    def test_connection(self): #example
        result = True
        self.open()
        if not self.conn or not self.cursor:
            result = False
        self.close()
        return result

    @exception
    def open(self):
        self.conn = MySQLdb.connect(host=self.host,
                                    user=self.user,
                                    passwd=self.passwd,
                                    db=self.db,
                                    port=self.port)

        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

    @exception
    def close(self):
        if self.cursor:
            self.cursor.close()
            self.conn.close()