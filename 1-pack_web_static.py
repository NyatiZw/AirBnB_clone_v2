#!/usr/bin/python3
"""
Fabric script to generate tgz archive from the contents of web_static
"""

from datetime import datetime
from fabric.api import local
from os import isdir


def do_pack():
    """ Generate a tgz archive from the contents of a folder """
    try:
        if isdir("versions") is False:
            local("mkdir versions")

        #Generate th file name with the current timestamp
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(current_time)
        archive_path = "versions/{}".format(file_name)

        # Compress the web_static folder into the archive
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
