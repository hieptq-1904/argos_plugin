#!/usr/bin/env python
# coding=utf8
"""
====================================
 :mod:`argoslabs.sqlite_plugin.execution`
====================================
.. moduleauthor:: Hiep Tran <Tranquanghiep2009@gmail.com>
.. note:: ARGOS-LABS License

Description
===========
SQLite Execution Plugin: unittest
"""

################################################################################
import os
import sqlite3
import sys
from alabs.common.util.vvargs import ArgsError
from unittest import TestCase
# noinspection PyProtectedMember
from sqlite_plugin.execution import _main as main


################################################################################
class TU(TestCase):
    """
    TestCase for argoslabs.sqlite_plugin.
    """
    # ==========================================================================
    def setup_db(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS stocks;")
        conn.close()

    # ==========================================================================
    def test0000_init(self):
        self.assertTrue(True)

    # ==========================================================================
    def test0001_failure(self):
        self.setup_db()
        result = main('example.db', "SELECT * FROM stocks")
        self.assertEqual(result, 1)

    # ==========================================================================
    def test0100_success(self):
        self.setup_db()
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
        result = main(
            'example.db',
            "INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)",
            "SELECT * FROM stocks"
        )
        self.assertEqual(result, 0)
        self.assertEqual(len(c.execute("SELECT * FROM stocks").fetchall()), 1)
        conn.close()
