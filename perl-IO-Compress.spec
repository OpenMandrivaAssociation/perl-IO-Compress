%define upstream_name    IO-Compress
%define upstream_version 2.037

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    IO Interface to compressed data files/buffers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

# perl provides this one unversionned
#BuildRequires: perl(Compress::Raw::Bzip2) >= 2.21.0
BuildRequires: perl-Compress-Raw-Bzip2    >= 2.37.0
BuildRequires: perl(Compress::Raw::Zlib)  >= 2.37.0
BuildRequires: perl-devel
BuildArch: noarch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Obsoletes:     perl-Compress-Zlib
Obsoletes:     perl-IO-Compress-Base
Obsoletes:     perl-IO-Compress-Bzip2
Obsoletes:     perl-IO-Compress-Zlib
Obsoletes:     %{name} < 2.33.0-2

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

IO-Compress supports reading and writing of bzip2, RFC 1950, RFC
1951, RFC 1952 (i.e. gzip) and zip files/buffers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Compress
%{perl_vendorlib}/File
%{perl_vendorlib}/IO
