#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose-cov
Version  : 1.6
Release  : 25
URL      : https://pypi.python.org/packages/source/n/nose-cov/nose-cov-1.6.tar.gz
Source0  : https://pypi.python.org/packages/source/n/nose-cov/nose-cov-1.6.tar.gz
Summary  : nose plugin for coverage reporting, including subprocesses and multiprocessing
Group    : Development/Tools
License  : MIT
Requires: nose-cov-license = %{version}-%{release}
Requires: nose-cov-python = %{version}-%{release}
Requires: nose-cov-python3 = %{version}-%{release}
Requires: cov-core
Requires: nose
BuildRequires : buildreq-distutils3
BuildRequires : cov-core
BuildRequires : nose

%description
========
        
        This plugin produces coverage reports.  It also supports coverage of subprocesses.
        
        All features offered by the coverage package should be available, either through nose-cov or
        through coverage's config file.
        
        
        Installation
        ------------

%package license
Summary: license components for the nose-cov package.
Group: Default

%description license
license components for the nose-cov package.


%package python
Summary: python components for the nose-cov package.
Group: Default
Requires: nose-cov-python3 = %{version}-%{release}

%description python
python components for the nose-cov package.


%package python3
Summary: python3 components for the nose-cov package.
Group: Default
Requires: python3-core
Provides: pypi(nose_cov)
Requires: pypi(cov_core)
Requires: pypi(nose)

%description python3
python3 components for the nose-cov package.


%prep
%setup -q -n nose-cov-1.6
cd %{_builddir}/nose-cov-1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583537771
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nose-cov
cp %{_builddir}/nose-cov-1.6/LICENSE.txt %{buildroot}/usr/share/package-licenses/nose-cov/07800edab5f4e77a7371e226f11ba91f963a11cf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nose-cov/07800edab5f4e77a7371e226f11ba91f963a11cf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
