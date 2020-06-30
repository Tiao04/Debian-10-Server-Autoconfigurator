import os
import time

print("Update and Upgrade system:")
os.system('apt-get update')
print("Network configuration file:")
f = open("/etc/network/interfaces", "w")
f.write('# deb cdrom:[Debian GNU/Linux 10.0.0 _Buster_ - Official amd64 NETINST 20190706-10:23]/ buster main\n\n# deb cdrom:[Debian GNU/Linux 10.0.0 _Buster_ - Official amd64 NETINST 20190706-10:23]/ buster main\n\ndeb http://deb.debian.org/debian/ buster main contrib non-free\ndeb-src http://deb.debian.org/debian/ buster main contrib non-free\n\ndeb http://security.debian.org/debian-security buster/updates main\ndeb-src http://security.debian.org/debian-security buster/updates main\n\n# buster-updates, previously known as \'volatile\'\ndeb http://deb.debian.org/debian/ buster-updates main contrib non-free\ndeb-src http://deb.debian.org/debian/ buster-updates main contrib non-free')
f.close()
f = open("/etc/network/interfaces", "r")
print(f.read())
f.close()
time.sleep(1)
os.system('apt-get update')
os.system('apt-get upgrade')
time.sleep(1)
print('Installing net-tools:')
os.system('apt-get install net-tools')
os.system('apt-get update')
time.sleep(1)
os.system('ip addr')
time.sleep(1)
netin = input('Principal network interface (ex. eth0): ')
addr = input('Address (ex. 192.168.0.42): ')
net = input('Network (ex. 192.168.0.0): ')
netmask = input('Netmask (ex. 255.255.255.0): ')
broadcast = input('Broadcast (ex. 192.168.0.255): ')
gateway = input('Gateway (ex. 192.168.0.1): ')

nettext = "# This file describes the network interfaces available on your system\n# and how to activate them. For more information, see interfaces(5).\n\nsource /etc/network/interfaces.d/*\n\n# The loopback network interface\nauto lo\niface lo inet loopback\n\nauto " + netin + "\niface " + netin + " inet static\n    address " + addr + "\n    network " + net + "\n    netmask " + netmask + "\n    broadcast " + broadcast + "\n    gateway " + gateway

time.sleep(1)

print("Network configuration file:")
f = open("/etc/network/interfaces", "w")
f.write(nettext)
f.close()

f = open("/etc/network/interfaces", "r")
print(f.read())
f.close()



os.system('apt install openssh-server')
sshPort = input('SSH port[22]: ')
if (sshPort.length == 0): 
    sshPort = 22
os.system('apt-get -y install ufw')
os.system('ufw default deny incoming')
os.system('ufw default allow outgoing')

print("SSH configuration file:")
f = open("/etc/ssh/sshd_config", "w")
f.write("# This is the sshd server system-wide configuration file.  See\n# sshd_config(5) for more information.\n\n# This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin\n\n# The strategy used for options in the default sshd_config shipped with\n# OpenSSH is to specify options with their default value where\n# possible, but leave them commented.  Uncommented options change a\n# default value.\n\nPort " + sshPort + "\n#AddressFamily any\n#ListenAddress 0.0.0.0\n#ListenAddress ::\n\n# The default requires explicit activation of protocol 1\n#Protocol 2\n\n# HostKey for protocol version 1\n#HostKey /etc/ssh/ssh_host_key\n# HostKeys for protocol version 2\n#HostKey /etc/ssh/ssh_host_rsa_key\n#HostKey /etc/ssh/ssh_host_dsa_key\n#HostKey /etc/ssh/ssh_host_ecdsa_key\n\n# Lifetime and size of ephemeral version 1 server key\n#KeyRegenerationInterval 1h\n#ServerKeyBits 1024\n\n# Logging\n# obsoletes QuietMode and FascistLogging\n#SyslogFacility AUTH\n#LogLevel INFO\n\n# Authentication:\n\n#LoginGraceTime 2m\n#BC# Root only allowed to login from LAN IP ranges listed at end\nPermitRootLogin no\n#PermitRootLogin yes\n#StrictModes yes\n#MaxAuthTries 6\n#MaxSessions 10\n\n#RSAAuthentication yes\n#PubkeyAuthentication yes\n#AuthorizedKeysFile  .ssh/authorized_keys\n\n# For this to work you will also need host keys in /etc/ssh/ssh_known_hosts\n#RhostsRSAAuthentication no\n# similar for protocol version 2\n#HostbasedAuthentication no\n# Change to yes if you don't trust ~/.ssh/known_hosts for\n# RhostsRSAAuthentication and HostbasedAuthentication\n#IgnoreUserKnownHosts no\n# Don't read the user's ~/.rhosts and ~/.shosts files\n#IgnoreRhosts yes\n\n# To disable tunneled clear text passwords, change to no here!\n#BC# Disable password authentication by default (except for LAN IP ranges listed later)\nPasswordAuthentication no\nPermitEmptyPasswords no\n#BC# Have to allow root here because AllowUsers not allowed in Match block.  It will not work though because of PermitRootLogin.\n#BC# This is no longer true as of 6.1.  AllowUsers is now allowed in a Match block.\nAllowUsers kmk root\n\n# Change to no to disable s/key passwords\n#BC# I occasionally use s/key one time passwords generated by a phone app\nChallengeResponseAuthentication yes\n\n# Kerberos options\n#KerberosAuthentication no\n#KerberosOrLocalPasswd yes\n#KerberosTicketCleanup yes\n#KerberosGetAFSToken no\n\n# GSSAPI options\n#GSSAPIAuthentication no\n#GSSAPICleanupCredentials yes\n\n# Set this to 'yes' to enable PAM authentication, account processing, \n# and session processing. If this is enabled, PAM authentication will \n# be allowed through the ChallengeResponseAuthentication and\n# PasswordAuthentication.  Depending on your PAM configuration,\n# PAM authentication via ChallengeResponseAuthentication may bypass\n# the setting of \"PermitRootLogin without-password\".\n# If you just want the PAM account and session checks to run without\n# PAM authentication, then enable this but set PasswordAuthentication\n# and ChallengeResponseAuthentication to 'no'.\n#BC# I would turn this off but I compiled ssh without PAM support so it errors if I set this.\n#UsePAM no\n\n#AllowAgentForwarding yes\n#AllowTcpForwarding yes\n#GatewayPorts no\nX11Forwarding yes\n#X11DisplayOffset 10\n#X11UseLocalhost yes\n#PrintMotd yes\n#PrintLastLog yes\n#TCPKeepAlive yes\n#UseLogin no\n#UsePrivilegeSeparation yes\n#PermitUserEnvironment no\n#Compression delayed\n#ClientAliveInterval 0\n#ClientAliveCountMax 3\n#UseDNS yes\n#PidFile /var/run/sshd.pid\n#MaxStartups 10\n#PermitTunnel no\n#ChrootDirectory none\n\n# no default banner path\n#Banner none\n\n# override default of no subsystems\n#Subsystem	sftp	/usr/lib/misc/sftp-server\nSubsystem	sftp	internal-sftp\n\n# the following are HPN related configuration options\n# tcp receive buffer polling. disable in non autotuning kernels\n#TcpRcvBufPoll yes\n\n# allow the use of the none cipher\n#NoneEnabled no\n\n# disable hpn performance boosts. \n#HPNDisabled no\n\n# buffer size for hpn to non-hpn connections\n#HPNBufferSize 2048\n\n\n# Example of overriding settings on a per-user basis\n#Match User anoncvs\n#	X11Forwarding no\n#	AllowTcpForwarding no\n#	ForceCommand cvs server\n\n#BC# My internal networks\n#BC# Root can log in from here but only with a key and kmk can log in here with a password.\nMatch Address 172.22.100.0/24,172.22.5.0/24,127.0.0.1\n  PermitRootLogin without-password\n  PasswordAuthentication yes")
f.close()


f = open("/etc/ssh/sshd_config", "r")
print(f.read())
f.close()

os.system('ufw allow ' + sshPort)
time.sleep(1)
os.system('systemctl restart sshd')


time.sleep(1)
phpLib = input('Apache2 or Ngnix: ')
if phpLib.lower == 'apache2':
    print('Installing LAMP:')
    os.system('apt-get install apache2')
elif phpLib.lower == 'nginx':
    print('Installing LEMP:')
    os.system('apt-get install nginx-extras')
os.system('apt install mariadb-server')
os.system('mysql_secure_installation')
os.system('systemctl status mariadb')
os.system('mysqladmin version')
os.system('apt-get update')



os.system('apt-get update')
time.sleep(1)
os.system('ufw app info "WWW Full"')
os.system('ufw allow in "WWW Full"')
time.sleep(1)
os.system('ufw enable')
os.system('ufw status')

print('Installing php7.3: ')
if phpLib.lower == 'apache2':
    phpLib = 'libapache2-mod-php7.3'
elif phpLib.lower == 'nginx':
    phpLib = 'php7.3-fpm'


os.system('apt-get -y install php7.3' + phpLib + 'libphp7.3-embed php7.3-bcmath php7.3-bz2 php7.3-cgi php7.3-cli php7.3-common php7.3-curl php7.3-dba php7.3-dev php7.3-enchant php7.3-gb php7.3-gmp php7.3-imap php7.3-interbase php7.3-intl php7.3-json php7.3-ldap php7.3-mbstring php7.3-mysql php7.3-odbc php7.3-opcache php7.3-pgsql php7.3-phpdbg php7.3-pspell php7.3-readline php7.3-recode php7.3-snmp php7.3-soap php7.3-sqlite3 php7.3-sybase php7.3-tidy php7.3-xml php7.3-xmlrpc php7.3-xsl php7.3-zip')
os.system('php -v')
time.sleep(1)
os.system('apt-get update')
os.system('service apache2 restart')


print('Rebooting:')
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
os.system('reboot')