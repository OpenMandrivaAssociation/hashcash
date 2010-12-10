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

