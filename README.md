About carbon-c-relay
====================

Carbon-like graphite line mode relay made by Fabian Groffen.

Project homepage: https://github.com/grobian/carbon-c-relay 


About carbon-c-relay_packages
=============================

This is a project to build Debian, Centos packages and Docker containers
with carbon-c-relay. 


Building
--------
Just type `vagrant up` to create a vm and run all scripts, when finished 
a deb package will appear. You can have a look at Vagrantfile to see the 
build process.

If you want to build it in your computer, just type `make`. If you want 
to build a debian package, just run `make debuild` (you will need to 
define DEBEMAIL and DEBFULLNAME as environment variables). Other targets 
are 'make distclean' to delete all binary files and `make install` to 
install the program in `/usr/local` (conf and binary files)


Docker
------

You can build the docker container by typing `docker build -t carbon-c-relay .`, 
it will take the configuration defined in `config/`. After that you can 
run it with `docker run -i -t carbon-c-relay`.


Author
------
Jose Riguera
