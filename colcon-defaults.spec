#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-defaults
Version  : 0.2.3
Release  : 11
URL      : https://files.pythonhosted.org/packages/f1/c6/71e7ac3e16dae4c79cbbe3ef75fd948da62a1a77971b617b2dd054778317/colcon-defaults-0.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/f1/c6/71e7ac3e16dae4c79cbbe3ef75fd948da62a1a77971b617b2dd054778317/colcon-defaults-0.2.3.tar.gz
Summary  : Extension for colcon to read defaults from a config file.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-defaults-python = %{version}-%{release}
Requires: colcon-defaults-python3 = %{version}-%{release}
Requires: PyYAML
Requires: colcon-core
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
colcon-defaults
===============

An extension for `colcon-core <https://github.com/colcon/colcon-core>`_ to provide custom default values for the command line arguments from a configuration file.

For more information about the format of the configuration file see `colcon.readthedocs.io <http://colcon.readthedocs.io/en/released/user/configuration.html#defaults-yaml>`_.

%package python
Summary: python components for the colcon-defaults package.
Group: Default
Requires: colcon-defaults-python3 = %{version}-%{release}

%description python
python components for the colcon-defaults package.


%package python3
Summary: python3 components for the colcon-defaults package.
Group: Default
Requires: python3-core
Provides: pypi(colcon-defaults)

%description python3
python3 components for the colcon-defaults package.


%prep
%setup -q -n colcon-defaults-0.2.3
cd %{_builddir}/colcon-defaults-0.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582909202
# -Werror is for werrorists
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
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
