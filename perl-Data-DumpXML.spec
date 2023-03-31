%define	modname	 Data-DumpXML
%define	modver 1.06

Summary:	Dump arbitrary perl data structures as XML
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	17
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/authors/id/GAAS/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
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

