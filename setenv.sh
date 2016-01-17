#!/usr/bin/env bash
apt-get install -y libjpeg-dev  libpng12-dev git-core git redis-server python-setuptools python-dev
easy_install pip
pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv nile
workon nile
pip install -r requirements.txt
