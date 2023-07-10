#!/usr/bin/python3
""" web server distribution"""
from fabric.api import *
import os.path


env.user = 'ubuntu'
env.hosts = ["100.26.237.41", "54.157.189.169"]
env.key.filename = "~/id_rsa"



def do_deploy(archive_path):
    """distributes archive file to web_servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        #Extract archive name and directory
        archive_file = os.path.basename(archive_path)
        directory_name = archive_file.split('.')[0]

        #Upload the archive to the /tmo/ directory on the server
        put(archive_path, "/tmp/{}".format(archive_file))

        #Create the release directory and extract the archve contents
        sudo ("mkdir -p /data/web_static/releases/{}/".format/directory_name))
        sudo ("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                .format(archive_file, directory_name))

        #Remove the archive file
        sudo ("rm /tmp/{}".format(archive_file))

        #Move the contents from the extracted directory to the release directory
        sudo ("mv /data/web_static/releases/{}/web_static/* "
              "/data/web_static/releases/{}/".format(directory_name, directory_name))

        #Remove the empty web_static dirctory
        sudo ("rm -rf /data/web_static/releases/{}/web_static".format(directory_name))

        #Update the symbolic link
        sudo ("rm -rf /data/web_static/current")
        sudo ("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                .format(directory_name))

        return True
    except Exception as e:
        return False
