ls
ls /
ls /dat
ls /data/
touch /data/gns3_python_scripts/hello.txt
echo "hello world" > /data/gns3_python_scripts/hello.txt 
ls
ls /data/gns3_python_scripts/hello.txt 
cat /data/gns3_python_scripts/hello.txt 
vi /etc/hosts/
cat /etc/hosts
vi /etc/hosts
nano /etc/host
ls
ls /etc/
nano /etc/hosts
cat /etc/hosts
nano /etc/hosts
cat /etc/hosts
ls /data/gns3_python_scripts/
cat /data/gns3_python_scripts/
cat /data/gns3_python_scripts/hello.txt 
cat /etc/hosts
nano /etc/hosts
cat /etc/hosts
cat /etc/resolf.conf
cat /etc/resolv.conf 
nano /etc/resolv.conf 
nano /etc/network/interfaces
apk add iptables
apt add iptables
apt install iptables
rc-service networking restart
ping www.google.com
ifconfig
ping www.google.com
apt install iptables
ping c3
curl http://www.multipath-tcp.org
sysctl net.mptcp.mptcp_enabled
cat /etc/os-release 
uname -r
cat /etc/hosts
ping c3
cat /etc/hosts
iptables --v
apt install iptables
cat /etc/network/interfaces
cat /etc/resolv.conf 
cat /etc/hosts
ls
cat /etc/hostss
cat /etc/hosts
ping c3
iperf3 c3
ls
ping c3
iperf3 -c c3
iperf3 -s
uname -r
apt install linux-image-5.15.0-mptcp
apt install linux-image-6.9.0-mptcp
wget https://github.com/multipath-tcp/mptcp_net-next/tree/export
apt install wget
curl https://github.com/multipath-tcp/mptcp_net-next/tree/export
ls
curl -LO https://github.com/multipath-tcp/mptcp_net-next/tree/export
ls
cd export
nano /etc/sysctl.conf
sudo sysctl -p
sysctl -p
uname -a
>ournalctl -k | grep -i mptcp
journalctl -k | grep -i mptcp
sysctl net.mptcp
uname -a
curl -LO https://bintray.com/cpaasch/deb/mptcp/v0.94.5
ls
rm -r ournalctl 
cd v0.94.5 
xz
tar
tar -v
tar -xvf v0.94.5 
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.5/linux-mptcp_v0.94.5_20190604201236_all.deb
ls
apt update
dpkg -i linux-mptcp_v0.94.5_20190604201236_all.deb 
apt-get install -f
apt show git
apt show mptcp
mkdir mptcp_pkg
cd mptcp_pkg
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.5/linux-headers-4.14.123.mptcp_20190604201236_amd64.deb
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.5/linux-image-4.14.123.mptcp_20190604201236_amd64.deb
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.5/linux-libc-dev_20190604201236_amd64.deb
apt update
dpkg -i linux*.deb
apt-get install -f
reboot
uname -a
uname -r
nano /etc/sysctl.conf
sysctl -p
cd mptcp_pkg/
ls
dpkg -i linux*.deb
lsb_release -a
cat /etc/os-release 
uname -r
uname -mrs
dpkg --list | grep linux-image
ls -l /lib/modules/
sudo find /boot/ -iname "vmlinuz*"
find /boot/ -iname "vmlinuz*"
update-initramfs -c -k 4.14.123
apt install update-initramfs
uname ~
apt install initramfs-tools
update-initramfs -c -k 4.14.123
update-grub
which grub-install
which grub2-install
apt-get update
apt-get install grub-pc
awk -F\' '/menuentry / {print $2}' /boot/grub/grub.cfg
cat /boot/grub/unicode.pf2 
ls
ls /etc
ls /etc/default/
ls
ls /etc/default/grub/
ls /etc/default/grub.d/
uname -r
cat /etc/default/grub.d/init-select.cfg 
cat /etc/default/grub
nano /etc/default/grub
dpkg --list | grep linux-image
ls /data/gns3_python_scripts/
nano /data/gns3_python_scripts/enable_mptcp.sh
cp /data/gns3_python_scripts/enable_mptcp.sh .
ls
chmod +x enable_mptcp.sh 
./enable_mptcp.sh 
ls
ls mptcp_deb/
cat enable_mptcp.sh 
cd mptcp_deb/
ls
curl -LO https://github.com/multipath-tcp/mptcp/releases/download/v0.94.6/linux-headers-4.14.127.mptcp_20190618035815_amd64.deb
ls
apt-get install ca-certificates
apt-get install -y ca-certificates
cd ..
ls
nano enable_mptcp.sh 
./enable_mptcp.sh 
dpkg --list | grep linux-image
rm /data/gns3_python_scripts/enable_mptcp.sh 
cp enable_mptcp.sh /data/gns3_python_scripts/
cat enable_mptcp.sh 
clear
cat /etc/default/grub
apt install -y grub-pc
cat /etc/default/grub
nano /etc/default/grub
uname -r
nano /etc/default/grub
update-grub
apt install grub-install
apt-get install linux-mptcp
update-grub
ls /boot/grub/
./enable_mptcp.sh 
ls
dpkg --list | grep linux-image
grub-mkconfig | grep -iE "menuentry 'Ubuntu, with Linux" | awk '{print i++ " : "$1, $2, $3, $4, $5, $6, $7}'
apt install grub
fdisk -l 
apt show grub
uname -r
cat /data/gns3_python_scripts/enable_mptcp.sh 
nano /data/gns3_python_scripts/enable_mptcp.sh 
dpkg --list | grep linux-image
cat ./enable_mptcp.sh 
rm enable_mptcp.sh 
rm -r mptcp_deb/
cp /data/gns3_python_scripts/enable_mptcp.sh .
./enable_mptcp.sh 
cp /data/gns3_python_scripts/enable_mptcp.sh .
dpkg --list | grep linux-image
cat /etc/default/grub
nano /etc/default/grub
grub-update
update-grub
update-grub2
reboot
uname -r
systemctl reboot
apt install systemd-sysv
reboot
uname -r 
dpkg --list | grep linux-image
ls /boot/
ls /boot/grub/
ls /boot/vmlinuz-4.14.127.mptcp 
cat /etc/default/grub
cat $GRUB_CONFIG
grub-reboot 1
grub2-mkconfig -o /boot/grub2/grub.cfg
grub-mkconfig -o /boot/grub2/grub.cfg
