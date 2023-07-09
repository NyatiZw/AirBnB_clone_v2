from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generate a .tgz archive from the contents of a folder"""
    try:
        # Create the versions folder
        if not os.path.exist("versions"):
            os.makedirs("versions")

        #Generate th file name with the current timestamp
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(current_time)
        archive_path = "versions/{}".format(file_name)

        # Compress the web_static folder into the archive
        local("tar -czvf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None
