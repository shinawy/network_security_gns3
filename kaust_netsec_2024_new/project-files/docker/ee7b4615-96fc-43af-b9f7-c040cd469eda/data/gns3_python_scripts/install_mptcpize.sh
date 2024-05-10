mkdir -p mptcpize_pkg
cd mptcpize_pkg
apt update
apt install libmptcpwrap0
curl -LO http://archive.ubuntu.com/ubuntu/pool/universe/m/mptcpd/mptcpize_0.9-1_amd64.deb
dpkg -i mptcpize*.deb
