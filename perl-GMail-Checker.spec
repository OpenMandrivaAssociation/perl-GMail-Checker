%define upstream_name	 GMail-Checker
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Wrapper for Gmail accounts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~fays/GMail-Checker-1.04/Checker.pm
Source0:	http://search.cpan.org/CPAN/authors/id/F/FA/FAYS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Socket::SSL)
BuildArch:	noarch

%description
This module provides a wrapper that allows you to perform major
operations on your gmail account. You may create a notifier to
know about new incoming messages, get information about a specific
e-mail, retrieve your mails using the POP3 via SSL interface.

%prep
%setup -q -n %{upstream_name}-104

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc MANIFEST README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 657440
- rebuild for updated spec-helper

* Wed Mar 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.40.0-1
+ Revision: 648165
- import perl-GMail-Checker

