#!/bin/ash

node=`cat /proc/sys/kernel/hostname`

case  ${node::1} in 
	s|S)
	echo "looks like a server to configure"
	/etc/MYBOOT/server.sh $node
	;;
	c|C)
	echo "looks like a client to configure"
	/etc/MYBOOT/client.sh $node
	;;
	r|R)
	echo "looks like a router to configure"
	/etc/MYBOOT/router.sh $node
	;;
	k|K)
	echo "looks like a kali distro to configure"
	/etc/MYBOOT/kali.sh $done
	;;
	t|T)
	echo "looks like a tunnel server to configure"
	/etc/MYBOOT/tunnel.sh $done
	;;
	*)
	echo " SORRY THIS IS NOT A NODE I CAN CONFIGURE"
esac

echo "DONE CONFIGURING THE NODE "

# We launch a shell to make sure this process does not terminate
# If it does, this kills the container it has launched

/bin/ash



