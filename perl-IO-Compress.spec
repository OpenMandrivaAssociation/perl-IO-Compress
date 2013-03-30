%define	modname	IO-Compress
%define	modver	2.060

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	IO Interface to compressed data files/buffers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{modver}.tar.gz

# perl provides this one unversionned
BuildRequires:	perl(Compress::Raw::Bzip2) >= %{version}
BuildRequires:	perl(Compress::Raw::Zlib) >= %{version}
BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{modname}-%{modver}

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

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.59.0-1
- cleanups
- new version

* Tue Mar 13 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.49.0-1
+ Revision: 784860
- new version
- change build dependency to use perl-Compress-Bzip2 package
- clean out spec

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-4
+ Revision: 765369
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-3
+ Revision: 763871
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.37.0-2
+ Revision: 763249
- force it
- rebuild

* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.37.0-1
+ Revision: 687108
- new version

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.35.0-1
+ Revision: 672851
- update to new version 2.035

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.33.0-2
+ Revision: 657343
- should be noarch package
- rebuild

* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.33.0-1
+ Revision: 634856
- new version

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-4mdv2011.0
+ Revision: 562529
- rebuild
- rebuild

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-2mdv2011.0
+ Revision: 561026
- rebuild
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 2.27.0-1mdv2011.0
+ Revision: 551221
- update to 2.027

* Fri Apr 09 2010 Jérôme Quelin <jquelin@mandriva.org> 2.26.0-1mdv2010.1
+ Revision: 533385
- update to 2.026

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 2.25.0-1mdv2010.1
+ Revision: 529773
- update to 2.025

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 2.24.0-1mdv2010.1
+ Revision: 488841
- update to 2.024

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 2.23.0-1mdv2010.1
+ Revision: 464053
- update to 2.023

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.22.0-1mdv2010.1
+ Revision: 461772
- update to 2.022

* Tue Sep 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.21.0-1mdv2010.0
+ Revision: 433069
- hardcode perl-Compress-Raw-Bzip2 dependency, as perl provides the virtual package unversioned

  + Jérôme Quelin <jquelin@mandriva.org>
    - bumping buildrequires: version requirement
    - update to 2.021

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.020-1mdv2010.0
+ Revision: 383486
- update to new version 2.020

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.019-2mdv2010.0
+ Revision: 371952
- obsoletes merged packages

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.019-1mdv2010.0
+ Revision: 371928
- import perl-IO-Compress


* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> v0.99.4-1mdv2009.0
- first mdv release
