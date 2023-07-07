#!/usr/bin/python3
""" Fabric script to distribute archive to the servers
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os
env.hosts = ['54.84.24.93', '34.224.95.244']


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


def do_deploy(archive_path):
    """ distributes archive to the servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        _, tar_file = os.path.split(archive_path)
        _, tar_dir = os.path.splitext(tar_file)
        put(archive_path, '/tmp/')
        dir_name = '/data/web_static/releases/{}/'.format(tar_dir)
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(tar_file, dir_name))
        run('rm /tmp/{}'.format(tar_file))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(tar_dir))
        run('rm -rf /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(dir_name))

        return True
    except:
        return False
