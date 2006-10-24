#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	Log-BlueCoat
Summary:	Regexp::Log::BlueCoat - a regexp builder to parse BlueCoat log files
Summary(pl):	Regexp::Log::BlueCoat - tworzenie wyra�e� regularnych do analizy log�w BlueCoat
Name:		perl-Regexp-Log-BlueCoat
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c8da7082238dc926c545a9cdd130fc9a
%if %{with tests}
BuildRequires:	perl-Regexp-Log >= 0.01
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Log::BlueCoat is a module that computes custom regular
expressions to parse log files generated by the BlueCoat Systems
Port 80 Security Appliance.

%description -l pl
Regexp::Log::BlueCoat to modu� tworz�cy wyra�enia regularne do analizy
plik�w log�w wygenerowanych przez oprogramowanie Port 80 Security
Appliance firmy BlueCoat Systems.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Regexp/Log
%{perl_vendorlib}/Regexp/Log/BlueCoat.pm
%{_mandir}/man3/*
