#!/usr/bin/env bash
# configuration
config="
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        location / {
        try_files \$uri \$uri/ =404;
        }
        location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
        try_files \$uri \$uri /hbnb_static/index.html;
        }
}
"
sudo apt-get update
sudo apt-get install nginx -y
sudo chmod 666 /etc/nginx/sites-available/default
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo $'<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo echo -e "$config" > /etc/nginx/sites-available/default
sudo service nginx restart