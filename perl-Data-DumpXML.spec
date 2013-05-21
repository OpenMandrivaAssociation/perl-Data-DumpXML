%define	upstream_name	 Data-DumpXML
%define	upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Dump arbitrary perl data structures as XML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Array-RefElem
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel
BuildArch:	noarch
Requires: 	perl-Array-RefElem >= 0.02

%description
Dump arbitrary perl data structures as XML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Data


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-4mdv2012.0
+ Revision: 765144
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-2
+ Revision: 667072
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.1
+ Revision: 406969
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.06-5mdv2009.0
+ Revision: 223592
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.06-4mdv2008.1
+ Revision: 180381
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 15:14:59 (58463)
- mkrel

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 15:09:58 (58457)
Import perl-Data-DumpXML

* Wed Jun 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.06-2mdk
- Rebuild, add tests, spec fixes

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.06-1mdk
- 1.06

