%define	modname	IO-Compress
%define modver 2.066

Summary:	IO Interface to compressed data files/buffers
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/zipdetails
%{perl_vendorlib}/Compress
%{perl_vendorlib}/File
%{perl_vendorlib}/IO
%{_mandir}/man1/zipdetails.1*
%{_mandir}/man3/*
