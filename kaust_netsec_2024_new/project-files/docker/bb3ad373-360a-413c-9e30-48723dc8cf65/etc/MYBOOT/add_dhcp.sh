
#!/bin/ash


if [ $# = 4 ]
then
    interface_name=$1
    dyn_ip_interface=$2
    mac_address=$3
    name=$4

# typical values: interface_name=eth1 ; dyn_ip_interface=10.10.10.100 or undefined ; mac_address=aa:11:11:11:11:11 ; name=c21

    echo " " >> /etc/network/interfaces
    echo "auto ${interface_name} " >> /etc/network/interfaces
    echo "iface ${interface_name} inet dhcp" >> /etc/network/interfaces
    echo "          hwaddress ether ${mac_address} " >> /etc/network/interfaces
    echo "          hostname ${name}" >> /etc/network/interfaces
    if [ $dyn_ip_interface != "undefined" ]
	then 
	echo "          udhcpc_opts -r ${dyn_ip_interface}" >> /etc/network/interfaces
    fi

else
	echo "ERROR ===== I need 4 arguments: an interface name (eg eth0), an IP address and a MAC address and an interface name (eg c21)"

fi

