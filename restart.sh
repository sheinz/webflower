#!/bin/bash

if [ -x flowersite.pid ];
then
    kill `cat flowersite.pid`
fi

python ./manage.py runfcgi demonize=false socket=/home/ubuntu/virt/django/flowersite/flowersite.sock pidfile=/home/ubuntu/virt/django/flowersite/flowersite.pid umask=000
