#!/bin/ash

if [ $# = 1 ]
then
    name=$1
    index=${name:1:1}
    let if_index=$index-1
    up_interface_name="eth${if_index}"
    down_interface_name="eth${index}"

# typical values: name=r2 ; index = 2 ; if_index=1 ; up_interface_name=eth1

# There are a few things we must only do the very first time
# we launch this container.
# To memorize the fact that we have already touched its filesystem
# we create a file /etc/DONE and check for its presence the very first time

# If the file does not exist, it is the first execution and the initialization
# steps are taking place, namely the edit of the /etc/network/interfaces file

    if [ ! -f /etc/DONE ] 
    then
        i=$index
	stat_ip_interface="${i}0.${i}0.${i}0.101"
        mac_address="aa:9${i}:9${i}:9${i}:9${i}:9${i}"
	if [ $name = "r1" ]
	    then
	    dyn_ip_interface="192.168.122.100"
	elif [ $name = "r2" ]
	    then
	    dyn_ip_interface="10.10.10.100"
	else
	    echo "ERROR _______ I only know how to configure r1 or r2, Sorry ___________"
        fi

# we configure both interfaces, one with dhcp, the other statically
        /etc/MYBOOT/add_dhcp.sh $up_interface_name $dyn_ip_interface $mac_address $name

        /etc/MYBOOT/add_static.sh $down_interface_name $stat_ip_interface 

     fi
else
    echo "ERROR ______ I need one parameter to configure a router: the router name (r1 or r2)"
fi

# The following instructions are executed every time we start the container
# The very first time they will fail because the interfaces are not configured
# This is why, the very first time, we need to start then stop then start the machines
# to ensure the success of the following commands


# Lauching Iptables on r1 only

if [ $name = "r1" ]
then 
# we provide NATING to the outside world
	    /sbin/iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
# we tell r1 how to reach 20.20.20.0
	    /sbin/route add -net 20.20.20.0 netmask 255.255.255.0 gw 10.10.10.100
fi


# Launching dnsmasq with the r1 or r2 config file 

config="/etc/MYBOOT/${name}_dnsmasq.conf"
/usr/sbin/dnsmasq -C ${config}


# when the router gets its up for eth0 from the DHCP server, it
# overwrites /etc/resolv.conf and forgets that it  itself is a 
# nameserver. We have to remind him that.
# Before telling the information, we need to wait a bit to make sure
# the "overwriting" has been done

sleep 5 

echo " " >> /etc/resolv.conf
echo "nameserver 127.0.0.1" >> /etc/resolv.conf

# and we tell them to try to add the net3.local domain name to non FQDN
echo "search net2.local net3.local" >> /etc/resolv.conf


# tinyproxy
# _________

# We copy the needed config files

cp -f /etc/MYBOOT/TINYPROXY/tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

# We launch the server

tinyproxy




/etc/MYBOOT/default.sh  $name

echo "Configuration of router $name completed"
