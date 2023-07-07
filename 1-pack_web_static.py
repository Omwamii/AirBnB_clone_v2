#!/usr/bin/python3
""" Fabric module to create a tgz archive of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ creates a tgz archive of web_static
    """
    # create versions directory if not existing
    local("mkdir -p versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    tar_file = "web_static_{}.tgz".format(timestamp)
    target_path = "versions/{}".format(tar_file)
    # unpack file web_static contents to tar file
    result = local("tar -czvf {} web_static".format(target_path))

    if result.succeeded:
        return target_path
    else:
        return None
