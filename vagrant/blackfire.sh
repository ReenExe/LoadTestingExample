#!/usr/bin/env bash

# blackfire.io
# http://habrahabr.ru/post/242167/
wget -O - https://packagecloud.io/gpg.key | sudo apt-key add -
echo "deb http://packages.blackfire.io/debian any main" | sudo tee /etc/apt/sources.list.d/blackfire.list
sudo apt-get update
sudo apt-get install -y blackfire-php blackfire-agent

# blackfire-agent -register