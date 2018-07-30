#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-defaults
Version  : 0.2.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/8c/e7/34f217ea8c75c53e59164242ea480defd7548466815acf9d903b3e6f2bc7/colcon-defaults-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8c/e7/34f217ea8c75c53e59164242ea480defd7548466815acf9d903b3e6f2bc7/colcon-defaults-0.2.0.tar.gz
Summary  : Extension for colcon to read defaults from a config file.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-defaults-python3
Requires: colcon-defaults-python
Requires: PyYAML
BuildRequires : buildreq-distutils3

%description
===============

%package python
Summary: python components for the colcon-defaults package.
Group: Default
Requires: colcon-defaults-python3

%description python
python components for the colcon-defaults package.


%package python3
Summary: python3 components for the colcon-defaults package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-defaults package.


%prep
%setup -q -n colcon-defaults-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532980505
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
