%define name	cvsgraph
%define version	1.6.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Create graphs of branches and revisions for files in a CVS repository
License:	GPL
Group:		System/Servers
Source:		http://www.akhphd.au.dk/~bertho/cvsgraph/release/%{name}-%{version}.tar.bz2
URL:		http://www.akhphd.au.dk/~bertho/cvsgraph
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
%configure
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_mandir}/{man1,man5}
install -m 755 %{name} %{buildroot}%{_bindir}
install -m 644 %{name}.conf %{buildroot}%{_sysconfdir}
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1
install -m 644 %{name}.conf.5 %{buildroot}%{_mandir}/man5

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%doc contrib/*.php3
%doc contrib/automatic_documentation
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*

