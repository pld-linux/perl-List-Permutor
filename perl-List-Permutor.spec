#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Permutor
Summary:	List::Permutor - process all of the possible permutations of a list of items
Summary(pl.UTF-8):   List::Permutor - przetwarzanie wszystkich możliwych permutacji listy elementów
Name:		perl-List-Permutor
Version:	0.022
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5c0f922730b9493c7c1e0583a5c8f78
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make the object by passing a list of the objects to be permuted. Each
time that next() is called, another permutation will be returned.

%description -l pl.UTF-8
Tworzy obiekt po przekazaniu listy obiektów do permutowania. Za każdym
wywołaniem next(), zwracana jest kolejna permutacja.

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
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
