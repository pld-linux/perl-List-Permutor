%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Permutor
Summary:	List::Permutor - process all of the possible permutations of a list of items
Summary(pl):	List::Permutor - przetwarzanie wszystkich mo¿liwych permutacji listy elementów
Name:		perl-List-Permutor
Version:	0.022
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make the object by passing a list of the objects to be permuted. Each
time that next() is called, another permutation will be returned.

%description -l pl
Tworzy obiekt po przekazaniu listy obiektów do permutowania. Za ka¿dym
wywo³aniem next(), zwracana jest kolejna permutacja.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
