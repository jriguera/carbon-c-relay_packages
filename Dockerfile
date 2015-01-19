# carbon-c-relay
#
# VERSION  0.1.0
#
# Use phusion/baseimage as base image.
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
#
FROM phusion/baseimage:0.9.15
MAINTAINER Jose Riguera <jriguera@gmail.com>

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

# Delete ssh_gen_keys
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Update
RUN apt-get update

# install package or download it from releases
# ADD *.deb /tmp/
# Latest release: https://github.com/jriguera/carbon-c-relay_packages/releases/latest
ADD https://github.com/jriguera/carbon-c-relay_packages/releases/download/0.37/carbon-c-relay_0.37_amd64.deb /tmp/

# Install
RUN dpkg -i /tmp/*.deb
ADD config/*.conf /etc/carbon/

# runinit
RUN mkdir /etc/service/carbon-c-relay
RUN sh -c 'echo "#!/bin/sh\n. /etc/default/carbon-c-relay\nexec /sbin/setuser carbon /usr/sbin/carbon-c-relay \$OPTS" > /etc/service/carbon-c-relay/run'
RUN chmod 0755 /etc/service/carbon-c-relay/run

EXPOSE 2003

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
