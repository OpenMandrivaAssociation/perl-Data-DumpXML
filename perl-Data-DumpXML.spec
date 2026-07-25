%define	modname	 Data-DumpXML
%define	modver 1.06

Summary:	Dump arbitrary perl data structures as XML
Name:		perl-%{modname}
Version:	%{modver}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Data-DumpXML
Source0:	https://cpan.metacpan.org/authors/id/G/GA/GAAS/Data-DumpXML-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-Array-RefElem
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel
Requires:	perl-Array-RefElem >= 0.02

%description
Dump arbitrary perl data structures as XML.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Data
%{_mandir}/man3/*

