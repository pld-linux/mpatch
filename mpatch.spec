Summary:	patch-like utility which helps to resolve rejects
Summary(pl.UTF-8):	Narzędzie podobne do patcha, pomagające nakładać fragmenty odrzucone
Name:		mpatch
Version:	0.8
Release:	3
License:	GPL v2
Group:		Applications/Text
Source0:	http://oss.oracle.com/~mason/mpatch/%{name}-%{version}.tar.bz2
# Source0-md5:	24f2027ae9d7b59e2c635ee2e485a887
URL:		http://oss.oracle.com/~mason/mpatch/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
%pyrequires_eq	python = %py_ver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpatch applies diffs and is generally similar to patch, but it can
also help resolve a number of common causes of patch rejects.

%description -l pl.UTF-8
mpatch nakłada różnice ("diffy") w sposób podobny do programu patch,
ale potrafi także rozwiązać wiele częstych przyczyn odrzucenia łaty.

%prep
%setup -q
%{__sed} -i -e 's,#! /usr/bin/env python,#!/usr/bin/python,' cmd/mpatch

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/mpatch/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/mpatch
%attr(755,root,root) %{py_sitedir}/mpatch/*.so
%{py_sitedir}/mpatch/*.py[co]
%{py_sitedir}/*.egg-info
