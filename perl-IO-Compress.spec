%define module   IO-Compress
%define version  2.019
%define release  %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    IO Interface to compressed data files/buffers
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/IO/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Compress::Raw::Bzip2)
BuildRequires: perl(Compress::Raw::Zlib)
Obsoletes:     perl-IO-Compress-Base
Obsoletes:     perl-IO-Compress-Bzip2
Obsoletes:     perl-IO-Compress-Zlib
Obsoletes:     perl-Compress-Zlib
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

IO-Compress supports reading and writing of bzip2, RFC 1950, RFC
1951, RFC 1952 (i.e. gzip) and zip files/buffers.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/IO
%{perl_vendorarch}/Compress
%{perl_vendorarch}/File
%{perl_vendorarch}/auto/IO
%{perl_vendorarch}/auto/Compress

