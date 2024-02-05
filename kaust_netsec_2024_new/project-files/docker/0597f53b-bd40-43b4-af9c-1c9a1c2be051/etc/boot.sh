#!/bin/ash

echo "Ready to launch the requested services"
echo "I accept the following ones:"
echo "dnsmasq nginx sshd postfix iptables"
echo "..........................................."

while [ $# -gt 0 ]
	do
		case $1 in 
		dnsmasq)
			/usr/sbin/dnsmasq
			echo "_______   dnsmasq launched"
			;;
		nginx)
			echo "I should launch NGINX"
			;;
		sshd)
			echo "I should launch SSHD"
			;;
		postfix)
			echo "I should launch Postfix"
			;;
		iptables)
			iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
			echo "I should launch iptables"
			;;
		*)
			echo "Argument NOT recognised"
			;;
		esac
	shift
	done

echo "Done with the arguments."
cat /etc/other_hosts >> /etc/hosts
echo "Launching a new shell to maintain the container alive"
/bin/ash
echo "This line will only be printed when the container will die"

