%define name	cvsgraph
%define version	1.7.0
%define release	5

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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%doc ChangeLog COPYING AUTHORS NEWS README INSTALL
%doc contrib/*.php
%doc contrib/automatic_documentation
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-4mdv2011.0
+ Revision: 617484
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.7.0-3mdv2010.0
+ Revision: 425533
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.7.0-2mdv2009.0
+ Revision: 266546
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.0-1mdv2009.0
+ Revision: 210895
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.1-2mdv2008.1
+ Revision: 132417
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cvsgraph


* Mon Jul 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.1-1mdv2007.0
- New version 1.6.1

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-1mdk
- New release 1.6.0

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.2-2mdk
- move configuration file in %%{_sysconfdir} 
- %%mkrel
- fix documentation scripts perms

* Thu Jun 16 2005 Lenny Cartier <lenny@mandriva.com> 1.5.2-1mdk
- 1.5.2

* Tue Oct 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5.1-1mdk
- 1.5.1

* Mon Aug 16 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5.0-1mdk
- 1.5.0

* Wed May 26 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.4.0-3mdk
- rebuild
- rpmbuildupdate aware

* Fri Apr 25 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.4.0-2mdk
- fixed buildrequires (Stefan van der Eijk <stefan@eijk.nu>)

* Sat Mar 22 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.4.0-1mdk
- first mdk release, with a spec stolen from Jason Corley <jason.corley@borland.com>
