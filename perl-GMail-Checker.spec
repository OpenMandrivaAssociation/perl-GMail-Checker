%define upstream_name	 GMail-Checker
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Wrapper for Gmail accounts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~fays/GMail-Checker-1.04/Checker.pm
Source0:	http://search.cpan.org/CPAN/authors/id/F/FA/FAYS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(IO::Socket::SSL)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a wrapper that allows you to perform major operations on your gmail account. You may create a notifier to know about new incoming messages, get information about a specific e-mail, retrieve your mails using the POP3 via SSL interface.

%prep
%setup -q -n %{upstream_name}-104

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc MANIFEST README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*

