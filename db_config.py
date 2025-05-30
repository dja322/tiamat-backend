# -*- coding: utf-8 -*-

# MySQL Connector/Python - MySQL driver written in Python.
# Copyright (c) 2009, 2013, Oracle and/or its affiliates. All rights reserved.

# MySQL Connector/Python is licensed under the terms of the GPLv2
# <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>, like most
# MySQL Connectors. There are special exceptions to the terms and
# conditions of the GPLv2 as it is applied to this software, see the
# FOSS License Exception
# <http://www.mysql.com/about/legal/licensing/foss-exception.html>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    """Configure me so examples work"""

    HOST = os.getenv("MYSQL_HOST")      # fill with your host address
    DATABASE = 'tiamat_db'  # fill with your database
    USER = os.getenv("MYSQL_USER")      # fill with your username
    PASSWORD = os.getenv("MYSQL_PASSWORD")  # fill with your user's password
    PORT = 3306

    CHARSET = 'utf8'
    UNICODE = True
    WARNINGS = True
    CONNECT_TIMEOUT = 10  # Increase the connection timeout to 10 seconds

    @classmethod
    def dbinfo(cls):
        return {
            'host': cls.HOST,
            'database': cls.DATABASE,
            'user': cls.USER,
            'password': cls.PASSWORD,
            'charset': cls.CHARSET,
            'use_unicode': cls.UNICODE,
            'get_warnings': cls.WARNINGS,
            'port': cls.PORT,
            'connect_timeout': cls.CONNECT_TIMEOUT,
        }
