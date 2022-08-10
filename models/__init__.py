#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv

storage = getenv('HBNB_TYPE_STORAGE')
if storage == 'db':
    from models.engine.db_storage import DBStorage
    s = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    s = FileStorage()

s.reload()
