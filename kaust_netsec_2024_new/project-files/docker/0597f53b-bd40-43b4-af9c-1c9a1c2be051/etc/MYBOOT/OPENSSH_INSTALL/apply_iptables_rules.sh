#!/bin/ash


echo "This script must be run on the r2 router in the topo2 topology"
echo "It will block all traffic between the networks net2 and net3"
echo "but it will let the c3 machine initiate an ssh connection with server s2"
echo " "
echo "c3 is expected to have the IP address: 20.20.20.89"
echo "s2 is expected to have the IP address: 10.10.10.54"
echo " "
echo "If not, change the rules accordingly"


iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

iptables -A FORWARD -s 20.20.20.89 -d 10.10.10.54 -i eth2 -o eth1 -p tcp --dport 22 -j ACCEPT

iptables -A FORWARD -s 10.10.10.54 -d 20.20.20.89 -i eth1 -o eth2 -m state --state NEW,ESTABLISHED -p tcp --sport 22 -j ACCEPT


