%define name hashcash
%define version 1.22
%define release %mkrel 6

Summary: Hashcash anti-spam / denial-of-service counter-measure tool
Name: %{name}
Version: %{version}
Release: %{release}
License: CPL or choice of public domain/BSD/LGPL/GPL
Group: Networking/Mail
URL: http://www.hashcash.org/
Source: http://www.hashcash.org/binaries/rpms/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: openssl-static-devel >= 0.9.8

%description
Hashcash is a denial-of-service counter measure tool.  It's main current use
is to help hashcash users avoid losing email due to content based and
blacklist based anti-spam systems.

The hashcash tool allows you to create hashcash stamp to attach to emails
you send, and to verify hashcash stamp attached to emails you receive. 
Email senders attach hashcash stamps with the X-Hashcash: header.  Vendors
and authors of anti-spam tools are encouraged to exempt mail sent with
hashcash from their blacklists and content based filtering rules.

A hashcash stamp constitutes a proof-of-work which takes a parameterizable
amount of work to compute for the sender.  The recipient can verify received
stamps efficiently. This package also includes a sha1 implementation which
behaves somewhat like md5sum, but with SHA1.

%prep
%setup -q

%build
sed -i -e 's|/usr/lib|%{_libdir}|' Makefile
make COPT="$RPM_OPT_FLAGS" "PACKAGER=RPM" gnu-openssl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}/
install -d $RPM_BUILD_ROOT/%{_mandir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install -d $RPM_BUILD_ROOT/%{_docdir}/
install -d $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

install -m 755 hashcash $RPM_BUILD_ROOT/%{_bindir}/
install -m 755 sha1 $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 hashcash.1 $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 sha1-hashcash.1 $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 README LICENSE CHANGELOG $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%{_bindir}/*
%{_mandir}/*/*
%{_docdir}/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.22-6mdv2011.0
+ Revision: 619355
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.22-5mdv2010.0
+ Revision: 429387
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.22-4mdv2009.0
+ Revision: 246794
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.22-2mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-2mdv2008.0
+ Revision: 89686
- rebuild

* Tue May 29 2007 Funda Wang <fwang@mandriva.org> 1.22-1mdv2008.0
+ Revision: 32375
- New upstream version

* Tue May 29 2007 Funda Wang <fwang@mandriva.org> 1.21-3mdv2008.0
+ Revision: 32327
- fix build on x86_64
- BuildRequires openssl-static-devel
- Really rebuild against openssl 0.98


* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.21-2mdk
- Fix BuildRequires

* Tue Mar 28 2006 Jerome Soyer <saispo@mandriva.org> 1.21-1mdk
- New release 1.21

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.17-2mdk
- BuildRequires fix

* Fri Jun 24 2005 Guillaume Cottenceau <gc@mandrakesoft.com> 1.17-1mdk
- mandrivaized

* Tue Sep 07 2004 Adam Back <adam@cypherspace.org>
- add cpu/platform specific tests to compile best code for platform

* Sun Mar 07 2004 Adam Back <adam@cypherspace.org>
- used general targets {_bin|_man|_doc}dir etc

* Sun Mar 07 2004 Jochen Schönfelder <arisel@arisel.de>
- tried to merge Mandrake & redhat rpms

* Sat Mar 06 2004 Jochen Schönfelder <arisel@arisel.de>
- Mandrake-build fixes
- sha1-manpage moved to sha1-hashcash

* Thu Jun 26 2003 Adam Back <adam@cypherspace.org> 
- First spec file

