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

Initialize the src git submodule by typing:

```
git submodule init
git submodule update
```

and then just type `vagrant up` to create a vm and automatically run all 
scripts, when finished the packages will appear in `build` folder. You 
can have a look at Vagrantfile to see the build process.

If you want to build it in your computer, just type `make`. If you want 
to build a debian package, just run `make debuild` (you will need to 
define DEBEMAIL and DEBFULLNAME as environment variables). Other targets 
are 'make distclean' to delete all binary files and `make install` to 
install the program in `/usr/local` (conf and binary files)


To build a specific version, for example 'v1.11':

```
# git checkout by tag 
pushd src && git checkout tags/v1.11 && popd
# bump the version for debian and rpm spec
make newrelease
# and now, vagrant up again, for example to get an ubuntu package
vagrant up ubuntu
```

Now, to check the process on the vm, just type: `vagrant ssh ubuntu` 
(it should be installed and running). Once finished with the review, 
just type `vagrant destroy` to destroy the vm(s).


For Debian, you can define these variables to create the packages:
```
export DEBEMAIL
export DEBFULLNAME
```


Docker
------

You can build the docker container by typing `docker build -t carbon-c-relay .`, 
it will take the configuration defined in `config/`. After that you can 
run it with `docker run -i -t carbon-c-relay`.


Author
------
José Riguera López  <jriguera@gmail.com>
