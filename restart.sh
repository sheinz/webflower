#!/bin/bash

# Replace these three settings.
PROJDIR="/home/ubuntu/virt/django/flowersite"
PIDFILE="$PROJDIR/flowersite.pid"
SOCKET="$PROJDIR/flowersite.sock"

pushd $PROJDIR

if [ -f $PIDFILE ]; then
    echo "Stopping fastcgi server..."
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

echo "Starting fastcgi server..."
python ./manage.py runfcgi daemonize=true socket=$SOCKET pidfile=$PIDFILE umask=000

popd
