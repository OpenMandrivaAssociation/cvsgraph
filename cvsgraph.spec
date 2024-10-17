
Name:		cvsgraph
Version:	1.7.0
Release:	5
Summary:	Create graphs of branches and revisions for files in a CVS repository
License:	GPL
Group:		System/Servers
Source:		http://www.akhphd.au.dk/~bertho/cvsgraph/release/%{name}-%{version}.tar.gz
URL:		https://www.akhphd.au.dk/~bertho/cvsgraph
BuildRequires:	libgd-devel
BuildRequires:	flex
BuildRequires:	bison

%description
CvsGraph is a utility to make a graphical representation of all revisions
and branches of a file in a CVS/RCS repository. It has been inspired by
the 'graph' option in WinCVS, but I could not find a stand-alone version
of this graph code. So, it was time to write one.

%prep
%setup -q
chmod 755 contrib/automatic_documentation/*.sh

%build
%configure2_5x
%make

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_mandir}/{man1,man5}
install -m 755 %{name} %{buildroot}%{_bindir}
install -m 644 %{name}.conf %{buildroot}%{_sysconfdir}
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1
install -m 644 %{name}.conf.5 %{buildroot}%{_mandir}/man5

%clean

%files
%doc ChangeLog COPYING AUTHORS NEWS README INSTALL
%doc contrib/*.php
%doc contrib/automatic_documentation
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*



