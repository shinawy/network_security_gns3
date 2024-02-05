#!/bin/ash

if [ $# = 1 ]
then
    name=$1 
    id=${name:1:2}
    index=${name:1:1}
    let if_index=$index-1
    interface_name="eth${if_index}"
    i=$index

# typical values: name=c21 ; index = 2 ; if_index=1 ; interface_name=eth1

    dyn_ip_interface="undefined"

    mac_address="aa:${id}:${id}:${id}:${id}:${id}"


# There are a few things we must only do the very first time
# we launch this container.
# To memorize the fact that we have already touched its filesystem
# we create a file /etc/DONE and check for its presence the very first time

# If the file does not exist, it is the first execution and the initialization
# steps are taking place, namely the edit of the /etc/network/interfaces file

    if [ ! -f /etc/DONE ] 
    then
	/etc/MYBOOT/add_dhcp.sh $interface_name $dyn_ip_interface $mac_address $name
    fi

# Configuration of the clients in the net1.local network


# There is a risk of a race condition here when a large amount of containers are 
# starting at the same time. If the two routers r1 and r2 do not start before the clients
# the clients dhcp clients will only obtain the information for the resolv.conf file after
# having executed the code here below. As a net result, the routes may not be added
# because the interfaces won't be up and the config could be overwritten
# This is why we will spend a couple of seconds waiting before continuing

sleep 5 


    if [ $index = 1 ]    
	then
# they need to be given the default route to both networks
# 20.20.20.0 and 10.10.10.0 
# A default gateway must be provided to them
# The gw IP is known because requested statically to the dhcpd server

	route add -net 10.10.10.0 netmask 255.255.255.0 gw 192.168.122.100
	route add -net 20.20.20.0 netmask 255.255.255.0 gw 192.168.122.100


# They must also been told that 10.10.10.101 is the DNS server to find machines in these networks
# If this modif has not already been done and locked in.

	if [ ! -f /etc/DONE ]
	    then
            echo "nameserver 10.10.10.101" >> /etc/resolv.conf

# They must be given the chance to simply give the short name and add the FQDN by themselves
	    echo "search net2.local net3.local " >> /etc/resolv.conf
	fi
    fi



# Configuration of the clients in the net2.local network

    if [ $index = 2 ]
	    then

# clients in net2.local need to be given the default route to 20.20.20.0
	    route add -net 20.20.20.0 netmask 255.255.255.0 gw 10.10.10.100
# they know how to find a DNS server thanks to the DHCP server they have talked to
# for the same reason they know their default gw
# they also know to search for net2.local, thanks to the dhcpd server but
# they ignore the existence of net3.local, let us help them with that fqdn
# since only one "search" command is taken into account per resolv.conf (the last one)
# we must add net2.local anyway despite the fact that it will already appear in the file
# Unless if these changes have already been made and locked in

	if [ ! -f /etc/DONE ]
	    then
	    echo "search net2.local net3.local" >> /etc/resolv.conf
	fi
    fi

# Configuration of the clients in the net3.local network

    if [ $index = 3 ]
	    then


# they know how to find a DNS server thanks to the DHCP server they have talked to
# for the same reason they know their default gw
# they also know to search for net3.local, thanks to the dhcpd server but
# they ignore the existence of net2.local, let us help them with that fqdn
# since only one "search" command is taken into account per resolv.conf (the last one)
# we must add net3.local anyway despite the fact that it will already appear in the file
# Unless if these changes have been made already and locked in

	if [ ! -f /etc/DONE ]
	    then
	    echo "search net2.local net3.local" >> /etc/resolv.conf
	fi
    fi

# This last one is tricky ...
# the resolver will add to the hostname given the domain names found in the search command
# it will perform one resolution after another
# it will move to the next domain name as soon as he gets a negative reply for the previous one
# "no such name"  or a successfull resolution
# if for whatever reason the resolution hangs for a given domain name (eg its server name is down)
# then the resolution dies without having tried all options
# In particular,in our case, if we try to resolve "c11", the resolver will first try to resolve 
# c11.net2.local by talking, eg to 10.10.10.101. Let us assume this server is up and running
# It is responsible for net2.local and will respond negatively.
# The resolver will thus try to resolve c11.net3.local by, eg, sending a request again to
# 10.10.10.101 which will forward that request to the DNS it knows is responsible for net3.local,
# namely 10.10.10.100. If that server is down, no response comes and the resolution dies ...
# To prevent this, we can use the "ndots:X" option which says that for any name given to the resolver
# that contains at least X dots, then no domain name from the search list should be added.
# In other words, in the previous scenario, by specifying the "options ndots:1" we could simply 
# resolve "c11." successfully because no suffix will be added and 10.10.10.101 will forward the request
# to the DNS 192.168.122.1 which will provide an answer ....
# An additional benefit is that when trying to resolve "c21.net2.local", a single query will be made and
# no spurious request such as "c21.net2.local.net3.local" will be made 

# Unless if that change has already been made and locked in

if [ ! -f /etc/DONE ]
then
    echo "options ndots:1" >> /etc/resolv.conf
fi


# This is all good and nice but, in fact, useless because in the Alpine Linux docker that we are using
# by default, the option "ndots:1" seems to be active by default and trying to change it in the resolv.conf
# does not seem to have any effect (in other words, it is not supported ...)  :-) 



echo "launching the default configuration now"
/etc/MYBOOT/default.sh $name

else
    echo "I need one paramater: the hostname"
fi



echo "DONE"
