#!/usr/bin/python3
"""generate a .tgz archive"""

from datetime import datetime
from fabric.api import local
from os.path import isdir, exists, getsize


def do_pack():
    """testing"""
    date = datetime.now().strftime("%y%m%d%H%M%S")
    if isdir("versions") is False:
        local("mkdir versions")
    name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(name))
    s = getsize(name)
    print("web_static packed: {} -> {}Bytes".format(name, s))
    if exists(name):
        return name
    return None