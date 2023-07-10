#!/usr/bin/env bash
#Script that sets up web servers for deployment of web_static

if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi

# Create directories for web_static
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "Hello, web_static!" | sudo tee /data/web_static/releases/test/index.html

#Remove existing symbolic link if it exists
sudo rm -rf /data/web_static/current

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#Update Nginx configuratipn to serve the content of /data/web_static/current/
sudo -i '/^\s*server_name\s/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/; \n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
