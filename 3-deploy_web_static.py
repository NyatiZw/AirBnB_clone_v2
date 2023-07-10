#!/usr/bin/python3
"""
Fabric script methods:
    do_pack: packs web_static/ files into .tgz archive
    do_deploy: deploys archive to webservers
    deploy: do_packs && do_deploys
usage:
    fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
from fabric.api import local, env, put, run
from datetime import datetime
from os.path import exists

env.host = ['54.157.189.169', '54.157.141.240']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'


def do_pack():
    """Generate a tgz archive file"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None

def do_deploy(archive_path):
    """Distribute an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        releases_path = "/data/web_static/releases/"
        tmp_path = "/tmp/{}".format(archive_name)

        put(archive_path, tmp_path)
        run('mkdir -p {}{}/'.format(releases_path, folder_name))
        run('tar -xzf {} -C {}{}/'.format(tmp_path, releases_path, folder_name))
        run('rm {}'.format(tmp_path))
        run('mv {}{}/web_static/* {}{}/'.format(releases_path, folder_name,
            releases_path, folder_name))
        run('rm -rf {}{}/web_static'.format(releases_path, folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(release_path, folder_name))
        return True
    except Exception:
        return False

def deploy():
    """¢reate and distribute an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
