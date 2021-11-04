# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate darling_core

Name:           rust-%{crate}
Version:        0.13.0
Release:        %autorelease
Summary:        Helper crate for proc-macro library for reading attributes into structs when implementing custom derives

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/darling_core
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Helper crate for proc-macro library for reading attributes into structs when
implementing custom derives. Use https://crates.io/crates/darling in your code.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+diagnostics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+diagnostics-devel %{_description}

This package contains library source intended for building other packages
which use "diagnostics" feature of "%{crate}" crate.

%files       -n %{name}+diagnostics-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+strsim-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strsim-devel %{_description}

This package contains library source intended for building other packages
which use "strsim" feature of "%{crate}" crate.

%files       -n %{name}+strsim-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+suggestions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+suggestions-devel %{_description}

This package contains library source intended for building other packages
which use "suggestions" feature of "%{crate}" crate.

%files       -n %{name}+suggestions-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

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