#!/usr/bin/env bash
# script to setup server for web_static
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<h1>It works!</h1>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

printf %s "
server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /error.html;
    location /error {
             root /etc/nginx/html;
             internal;
     }
    location /hbnb_static {
             alias /data/web_static/current/;
     }
}
" > /etc/nginx/sites-enabled/default
sudo service nginx restart
