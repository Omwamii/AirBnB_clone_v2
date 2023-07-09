#!/usr/bin/python3
""" Fabric script to create and distribute archive to servers
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os
env.hosts = ['54.84.24.93', '34.224.95.244']


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
    except Exception:
        return None


def do_deploy(archive_path):
    """ distributes archive to the servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        _, tar_file = os.path.split(archive_path)
        tar_dir, _ = os.path.splitext(tar_file)
        put(archive_path, '/tmp/')
        dir_name = '/data/web_static/releases/{}/'.format(tar_dir)
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(tar_file, dir_name))
        run('rm /tmp/{}'.format(tar_file))
        run('mv /data/web_static/releases/{}/web_static/* \
                {}'.format(tar_dir, dir_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(tar_dir))
        run('rm -rf /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(dir_name))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """ perform full deployment of archives to server
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
