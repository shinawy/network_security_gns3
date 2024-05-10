# gateway 
#gateway=r23.net3.local
gateway=20.20.20.101

# initialize ip for eth0
eth0_ip=$(ip -f inet addr show eth0 | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')
eth0_gateway=$gateway
eth0_zero_ip=20.20.20.0

# initialize ip for eth1
eth1_ip=$(ip -f inet addr show eth1 | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')
eth1_gateway=$gateway
eth1_zero_ip=20.20.20.0

# vars
num_of_subflows=2

# This creates two different routing tables, that we use based on the source-address.
  ip rule add from $eth0_ip table 1
  ip rule add from $eth1_ip table 2

  # Configure the two different routing tables
  ip route add $eth0_zero_ip/24 dev eth0 scope link table 1
  # ip route add default via $eth0_gateway dev eth0 table 1

  ip route add $eth1_zero_ip/24 dev eth1 scope link table 2
  # ip route add default via $eth1_gateway dev eth1 table 2

  # default route for the selection process of normal internet-traffic
  ip route add default scope global nexthop via $eth0_gateway dev eth0

# set limits for mptcp 
ip mptcp limits set subflow $num_of_subflows add_addr_accepted $num_of_subflows

# add additional subflows
ip mptcp endpoint add $eth1_ip dev eth0 signal
