%define	upstream_name		IO-Compress
%define	upstream_version	2.049

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	IO Interface to compressed data files/buffers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

# perl provides this one unversionned
BuildRequires:	perl(Compress::Raw::Bzip2) >= %{version}
BuildRequires:	perl(Compress::Raw::Zlib) >= %{version}
BuildRequires:	perl-devel
BuildArch:	noarch

Obsoletes:	perl-Compress-Zlib
Obsoletes:	perl-IO-Compress-Base
Obsoletes:	perl-IO-Compress-Bzip2
Obsoletes:	perl-IO-Compress-Zlib
Obsoletes:	%{name} < 2.33.0-2

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

IO-Compress supports reading and writing of bzip2, RFC 1950, RFC
1951, RFC 1952 (i.e. gzip) and zip files/buffers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/man1/zipdetails.1*
%{_mandir}/man3/*
%{perl_vendorlib}/Compress
%{perl_vendorlib}/File
%{perl_vendorlib}/IO
