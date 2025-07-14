
# TODO:
#	- rgw support

Summary:	Deploy Ceph with minimal infrastructure
Summary(pl.UTF-8):	Wdrażanie Cepha z minimalną infrastrukturą
Name:		ceph-deploy
Version:	1.5.23
Release:	2
License:	MIT
Group:		Applications/System
Source0:	https://github.com/ceph/ceph-deploy/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9b92bb38adfbab41d3feff24291428ca
#Source0:	https://pypi.python.org/packages/source/c/ceph-deploy/%{name}-%{version}.tar.gz
# https://github.com/jajcus/ceph-deploy/tree/pld
Patch0:		%{name}-pld.patch
URL:		https://github.com/ceph/ceph-deploy
BuildRequires:	python-setuptools >= 1:7.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-remoto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ceph-deploy is a way to deploy Ceph relying on just SSH access to the
servers, sudo, and some Python. It runs fully on your workstation,
requiring no servers, databases, or anything like that.

If you set up and tear down Ceph clusters a lot, and want minimal
extra bureaucracy, this is for you.

%description -l pl.UTF-8
ceph-deploy to sposób wdrażania Cepha polegający jedynie na dostępie
SSH do serwerów, sudo i odrobinie Pythona. Uruchamia w pełni stację
roboczą bez wymagania serwerów, baz danych itp.

Jest to rozwiązanie dla tych, którzy często stawiają i wyłączają
klastry Cepha i chcą mieć przy tym jak najmniej biurokracji.

%prep
%setup -q
%patch -P0 -p1

%build
export CEPH_DEPLOY_NO_VENDOR=1
%py_build

%install
rm -rf $RPM_BUILD_ROOT

export CEPH_DEPLOY_NO_VENDOR=1
%py_install

# no %%py_postclean !
# ceph-deploy uses remoto/execnet to run its source code remotely

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/ceph-deploy
%{py_sitescriptdir}/ceph_deploy
%{py_sitescriptdir}/ceph_deploy-%{version}-py*.egg-info
