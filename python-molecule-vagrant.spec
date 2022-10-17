# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-molecule-vagrant
Epoch: 100
Version: 2.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Molecule Vangrant Driver
License: MIT
URL: https://github.com/ansible-community/molecule-vagrant/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Molecule Vagrant is designed to allow use of Vagrant for provisioning of
test resources.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-molecule-vagrant
Summary: Molecule Vangrant Driver
Requires: python3
Requires: python3-Jinja2 >= 2.11.3
Requires: python3-molecule >= 3.4.1
Requires: python3-PyYAML >= 5.1
Requires: python3-selinux
Requires: python3-vagrant >= 1.0.0
Provides: python3-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-vagrant) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-vagrant) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-vagrant) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-molecule-vagrant
Molecule Vagrant is designed to allow use of Vagrant for provisioning of
test resources.

%files -n python%{python3_version_nodots}-molecule-vagrant
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-molecule-vagrant
Summary: Molecule Vangrant Driver
Requires: python3
Requires: python3-Jinja2 >= 2.11.3
Requires: python3-molecule >= 3.4.1
Requires: python3-PyYAML >= 5.1
Requires: python3-selinux
Requires: python3-vagrant >= 1.0.0
Provides: python3-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-vagrant) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-vagrant) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-vagrant) = %{epoch}:%{version}-%{release}

%description -n python3-molecule-vagrant
Molecule Vagrant is designed to allow use of Vagrant for provisioning of
test resources.

%files -n python3-molecule-vagrant
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-molecule-vagrant
Summary: Molecule Vangrant Driver
Requires: python3
Requires: python3-jinja2 >= 2.11.3
Requires: python3-libselinux
Requires: python3-molecule >= 3.4.1
Requires: python3-pyyaml >= 5.1
Requires: python3-vagrant >= 1.0.0
Provides: python3-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-vagrant) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-vagrant) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-vagrant = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-vagrant) = %{epoch}:%{version}-%{release}

%description -n python3-molecule-vagrant
Molecule Vagrant is designed to allow use of Vagrant for provisioning of
test resources.

%files -n python3-molecule-vagrant
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
