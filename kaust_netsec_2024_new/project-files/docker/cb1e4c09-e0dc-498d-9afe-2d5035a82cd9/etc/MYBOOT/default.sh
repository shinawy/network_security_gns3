#!/bin/ash

if [ $# = 1 ]
then

# GNS3, when setting the name of a machine, does not modify /etc/hostname
# We have to do it ourselves
 	cat /proc/sys/kernel/hostname > /etc/hostname


# We need to add the list of statically assigned IP addresses, with their names
# Because GNS3 overwrites the /etc/hosts files when starting a container the first time.
# We only need to do this once though. If not, we'll keep adding lines to that file
# everytime we launch the container, therefore the test for the file we will create

	if  [ ! -f /etc/DONE ]
	then 
		touch /etc/DONE
		cat /etc/other_hosts >> /etc/hosts
	fi

else
	echo "ERROR +++++ I need one argument, the interface name, instead of ${#} "
fi
 
