mkdir -p mptcp_deb
cd mptcp_deb
apt-get install -y grub-pc ca-certificates
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.6/linux-headers-4.14.127.mptcp_20190618035815_amd64.deb
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.6/linux-image-4.14.127.mptcp_20190618035815_amd64.deb
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.6/linux-libc-dev_20190618035815_amd64.deb
dpkg -i linux*.deb
apt-get install -f
dpkg --list | grep linux-image
