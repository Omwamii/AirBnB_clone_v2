#!/usr/bin/python3
""" Fabric module to create a tgz archive of web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ creates a tgz archive of web_static
    """
    # create versions directory if not existing
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        tar_file = "web_static_{}.tgz".format(timestamp)
        target_path = "versions/{}".format(tar_file)
        # unpack file web_static contents to tar file
        local("tar -czvf {} web_static".format(target_path))
        print("web_static packed: {} -> \
                {}Bytes".format(target_path, os.path.getsize(target_path)))
        return target_path
    except Exception:
        return None
