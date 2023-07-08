%define	modname	IO-Compress

Summary:	IO Interface to compressed data files/buffers
Name:		perl-%{modname}
Version:	2.204
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{version}.tar.gz
BuildArch:	noarch
# perl provides this one unversionned
BuildRequires:	perl(Compress::Raw::Bzip2) >= %{version}
BuildRequires:	perl(Compress::Raw::Zlib) >= %{version}
BuildRequires:	perl-devel
Obsoletes:	perl-Compress-Zlib
Obsoletes:	perl-IO-Compress-Base
Obsoletes:	perl-IO-Compress-Bzip2
Obsoletes:	perl-IO-Compress-Zlib

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

IO-Compress supports reading and writing of bzip2, RFC 1950, RFC
1951, RFC 1952 (i.e. gzip) and zip files/buffers.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README
%{_bindir}/streamzip
%{_bindir}/zipdetails
%{perl_vendorlib}/Compress
%{perl_vendorlib}/File
%{perl_vendorlib}/IO
%{_mandir}/man1/streamzip.1*
%{_mandir}/man1/zipdetails.1*
%{_mandir}/man3/*
