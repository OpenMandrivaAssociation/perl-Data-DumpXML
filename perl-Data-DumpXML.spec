%define	upstream_name	 Data-DumpXML
%define	upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Dump arbitrary perl data structures as XML
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0: 	http://www.cpan.org/authors/id/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Array-RefElem
BuildRequires:  perl-MIME-Base64
BuildRequires:  perl-XML-Parser
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
Requires: 	perl-Array-RefElem >= 0.02

%description
Dump arbitrary perl data structures as XML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Data
