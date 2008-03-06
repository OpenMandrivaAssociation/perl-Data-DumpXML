%define	module	Data-DumpXML
%define	name	perl-%{module}
%define	version	1.06
%define	release	%mkrel 4

Summary:	Dump arbitrary perl data structures as XML
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0: 	http://www.cpan.org/authors/id/GAAS/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel perl-Array-RefElem perl-MIME-Base64 perl-XML-Parser
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://search.cpan.org/dist/%{module}/
Requires: 	perl-Array-RefElem >= 0.02
BuildArch:	noarch

%description
Dump arbitrary perl data structures as XML.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Data

