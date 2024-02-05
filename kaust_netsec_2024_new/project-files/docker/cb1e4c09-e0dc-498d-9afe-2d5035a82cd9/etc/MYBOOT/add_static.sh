#!/bin/ash

if [ $# = 2 ]
then
    interface_name=$1
    stat_ip_interface=$2

    echo " " >> /etc/network/interfaces
    echo "auto ${interface_name} " >> /etc/network/interfaces
    echo "iface ${interface_name} inet static" >> /etc/network/interfaces
    echo "          address ${stat_ip_interface}" >> /etc/network/interfaces
    echo "          netmask 255.255.255.0" >> /etc/network/interfaces

else
	echo "ERROR ---- I need 2 arguments: an interface name (r11 or r21) and an IP address"

fi





echo "DONE configuring $interface for $name"
