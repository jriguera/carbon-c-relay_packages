# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$rpmscript = <<"SCRIPT"
echo I am provisioning ... $@
yum -y install rpmlint rpmdevtools redhat-rpm-config rpm-build git
cp -a /vagrant /tmp
cd /tmp/vagrant
make rpmbuild
cp rpm/RPMS/x86_64/carbon-c-relay*.rpm /vagrant
rpm -i rpm/RPMS/x86_64/carbon-c-relay*.rpm
/etc/init.d/carbon-c-relay start
SCRIPT

$debscript = <<"SCRIPT"
echo I am provisioning ... $@
apt-get update
apt-get install -y build-essential devscripts fakeroot dh-make automake git vim
apt-get install -y pkg-config libssl-dev
cp -a /vagrant /tmp
cd /tmp/vagrant
export DEBEMAIL="$1"
export DEBFULLNAME="$2"
make debuild
cd /tmp/ && dpkg -i carbon-c-relay*.deb
cp /tmp/carbon-c-relay*.deb /vagrant
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.  

  config.vm.define :centos do |centos|
      # Every Vagrant virtual environment requires a box to build off of.
      centos.vm.box = "nrel/CentOS-6.5-x86_64"

      # Create a forwarded port mapping which allows access to a specific port
      # within the machine from a port on the host machine. In the example below,
      # accessing "localhost:8080" will access port 80 on the guest machine.
      # centos.vm.network "forwarded_port", guest: 80, host: 8080

      # Create a private network, which allows host-only access to the machine
      # using a specific IP.
      # centos.vm.network "private_network", ip: "192.168.33.10"

      # Create a public network, which generally matched to bridged network.
      # Bridged networks make the machine appear as another physical device on
      # your network.
      # centos.vm.network "public_network"

      # Enable provisioning with shell
      centos.vm.provision "shell" do |s|
        s.inline = $rpmscript
      end
  end

  config.vm.define :ubuntu do |ubuntu|
      # Every Vagrant virtual environment requires a box to build off of.
      ubuntu.vm.box = "ubuntu/trusty64"

      # Create a forwarded port mapping which allows access to a specific port
      # within the machine from a port on the host machine. In the example below,
      # accessing "localhost:8080" will access port 80 on the guest machine.
      # ubuntu.vm.network "forwarded_port", guest: 80, host: 8080

      # Create a private network, which allows host-only access to the machine
      # using a specific IP.
      # ubuntu.vm.network "private_network", ip: "192.168.33.10"

      # Create a public network, which generally matched to bridged network.
      # Bridged networks make the machine appear as another physical device on
      # your network.
      # ubuntu.vm.network "public_network"

      # Enable provisioning with shell
      ubuntu.vm.provision "shell" do |s|
        s.inline = $debscript
        s.args   = "#{ENV['DEBEMAIL']}, #{ENV['DEBFULLNAME']}"
      end
  end

end
