# Authority: SounOS.org

Summary: PushService for push.parse.com
Name: ipush
Version: 0.0.2
Release: 2%{?dist}
License: BSD
Group: System Environment/Libraries
URL: https://github.com/sounos/ipush

Source: http://code.google.com/p/sbase/download/%{name}-%{version}.tar.gz
Packager: SounOS <SounOS@gmail.com>
Vendor: SounOS
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevbase >= 0.0.18
Requires: libevbase >= 0.0.18

%description
PushService for push.parse.com

%prep
%setup

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
[ "`grep ipush /etc/passwd`" ] || /usr/sbin/useradd -M -s /sbin/nologin ipush && echo ''
/sbin/chkconfig --add ipushd && /sbin/chkconfig --level 345 ipushd on || echo ''

%preun
[ "`pstree|grep ipushd|wc -l`" -gt "0" ] && /sbin/service ipushd stop || echo ''
/sbin/chkconfig --del ipush
[ "`grep ipush /etc/passwd`" ]  && /usr/sbin/userdel ipush || echo ''

%files
%defattr(-, root, root, 0755)
%{_sbindir}/*
%{_bindir}/*
%{_sysconfdir}/rc.d/*
%config(noreplace) %{_sysconfdir}/*.ini

%changelog
* Tue Oct  8 2013 13:37:50 CST SounOS <SounOS@gmail.com>
- added configure.in
