%define name     carbon-c-relay
%define version 1.11

Name:            %{name}           
Version:         %{version}
Release:         1%{?dist}
Summary:         Enhanced C implementation of Carbon relay, aggregator and rewriter
Group:           Applications/Communications
License:         Apache 2.0
URL:             https://github.com/grobian/carbon-c-relay
Source0:         %{name}-%{version}.tar.gz
ExcludeArch:     s390 s390x
Requires(post):  chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts

%description
Enhanced C implementation of Carbon relay, aggregator and rewriter
The relay is a simple program that reads its routing information from a file. 
The command line arguments allow to set the location for this file, as well 
as the amount of dispatchers (worker threads) to use for reading the data 
from incoming connections and passing them onto the right destination(s). 
The route file supports two main constructs: clusters and matches. The first 
define groups of hosts data metrics can be sent to, the latter define which 
metrics should be sent to which cluster. 

%prep
rm -rf $RPM_BUILD_DIR/*
cp -a %{_topdir}/../src $RPM_BUILD_DIR/
cp -a %{_topdir}/../config $RPM_BUILD_DIR/
cp -a %{_topdir}/../Makefile $RPM_BUILD_DIR/
make dist DISTDIR=%{_sourcedir} 

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/carbon
install -d $RPM_BUILD_ROOT/usr/sbin
make install PREFIX=$RPM_BUILD_ROOT/usr DESTDIR=$RPM_BUILD_ROOT/etc/carbon
install -m 644 %{_topdir}/carbon-c-relay.conf $RPM_BUILD_ROOT/etc/carbon/carbon-c-relay.conf
install -D -m 644 %{_topdir}/carbon-c-relay.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/carbon-c-relay
install -D -m 755 %{_topdir}/carbon-c-relay.init $RPM_BUILD_ROOT/etc/rc.d/init.d/carbon-c-relay

%clean
rm -rf $RPM_BUILD_ROOT

%post
# This adds the proper /etc/rc*.d links for the script
if [ $1 -eq 1 ]; then
        chkconfig --add carbon-c-relay
        useradd -d /tmp -M -s /bin/false --system -G daemon carbon
fi

%preun
if [ $1 -eq 0 ]; then
	service carbon-c-relay stop >/dev/null 2>&1
   	chkconfig --del carbon-c-relay
fi

%files
%doc $RPM_BUILD_DIR/src/README.md
%{_sbindir}/carbon-c-relay
%attr(755, root, root) /etc/rc.d/init.d/carbon-c-relay
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/carbon/carbon-c-relay.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/sysconfig/carbon-c-relay

%changelog
* Wed Jan 21 2015 Jose Riguera <jriguera@gmail.com>
- %{name} %{version}
