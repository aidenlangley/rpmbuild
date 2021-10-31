# Generated by rust2rpm 18
%bcond_without check
%global __cargo_skip_build 0

%global crate pop-launcher-bin

Name:           rust-%{crate}
Version:        1.0.0
Release:        %autorelease
Summary:        Binary for pop-launcher

License:        GPLv3

%global     gituser     pop-os
%global     gitrepo     launcher
%global     commit      04d6653b0b42fa3e4c113cd9fb37ff084f9d9588

URL:        https://github.com/%{gituser}/%{gitrepo}
Source:     %{gitrepo}-%{commit}-bin.tar.xz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/pop-launcher-bin

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
