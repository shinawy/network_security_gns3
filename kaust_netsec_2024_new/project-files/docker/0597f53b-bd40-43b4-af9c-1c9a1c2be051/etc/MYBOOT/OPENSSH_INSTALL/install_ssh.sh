#!/bin/sh
apk add openrc --no-cache
apk add openssh --no-cache
rc-update add sshd
rc-status
touch /run/openrc/softlevel
adduser -D test_ssh
echo "test_ssh:test_ssh" | chpasswd
/etc/init.d/sshd restart
