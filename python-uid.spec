
%define 	module uid

Summary:	Implementation of a "unique" ID (UID) generator in Python
Summary(pl.UTF-8):	Implementacja generatora unikalnych identyfikatorów (UID) w Pythonie
Name:		python-%{module}
Version:	1.0.2
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.alcyone.com/software/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	79868221e3baa21ae189ebcecd1ad9e6
Patch0:		python-uid-first-line-path.patch
URL:		http://www.alcyone.com/software/uid/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of a "unique" ID (UID) generator in Python. The
implementation does not follow UUID or GUID standards, but rather uses
available system, host, user, shell environment, process, and other
ephemeral information fed into a hasher (by default MD5) to generate
the UID.

The system is designed to be used both as a standalone application and
as a module. The data used to be fed into the hash, as well as the
hashing mechanism itself, can be overridden both through the command
line and programmatically by importing the module.

%description -l pl.UTF-8
Implementacja generatora unikalnych identyfikatorów w Pythonie.
Implementacja nie spełnia standardów UUID lub GUID, lecz stara się
użyć dostępnych informacji systemowych, komputera, użytkownika,
środowiska powłoki, procesu oraz innych do wygenerowania
identyfikatora (domyślnie w postaci MD5).

%package doc
Summary:	Documentation for uid module
Summary(pl.UTF-8):	Dokumentacja do modułu uid
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This module contains documentation files for uid Python module.

%description doc -l pl.UTF-8
Moduł zawierający dokumentację dla modułu Pythona uid.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_bindir}}

cp uid.py $RPM_BUILD_ROOT%{py_sitescriptdir}
cp uid.py $RPM_BUILD_ROOT%{_bindir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/uid.py[oc]
%attr(755,root,root) %{_bindir}/uid.py

%files doc
%defattr(644,root,root,755)
%doc doc/*
