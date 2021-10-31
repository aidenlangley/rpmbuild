# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate const_format

Name:           rust-%{crate}
Version:        0.2.22
Release:        1%{?dist}
Summary:        Compile-time string formatting

# Upstream license specification: Zlib
License:        zlib
URL:            https://crates.io/crates/const_format
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Compile-time string formatting.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-ZLIB.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages
which use "all" feature of "%{crate}" crate.

%files       -n %{name}+all-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+assert-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+assert-devel %{_description}

This package contains library source intended for building other packages
which use "assert" feature of "%{crate}" crate.

%files       -n %{name}+assert-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+assertc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+assertc-devel %{_description}

This package contains library source intended for building other packages
which use "assertc" feature of "%{crate}" crate.

%files       -n %{name}+assertc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+assertcp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+assertcp-devel %{_description}

This package contains library source intended for building other packages
which use "assertcp" feature of "%{crate}" crate.

%files       -n %{name}+assertcp-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+const_generics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+const_generics-devel %{_description}

This package contains library source intended for building other packages
which use "const_generics" feature of "%{crate}" crate.

%files       -n %{name}+const_generics-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+constant_time_as_str-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+constant_time_as_str-devel %{_description}

This package contains library source intended for building other packages
which use "constant_time_as_str" feature of "%{crate}" crate.

%files       -n %{name}+constant_time_as_str-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+docsrs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+docsrs-devel %{_description}

This package contains library source intended for building other packages
which use "docsrs" feature of "%{crate}" crate.

%files       -n %{name}+docsrs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fmt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fmt-devel %{_description}

This package contains library source intended for building other packages
which use "fmt" feature of "%{crate}" crate.

%files       -n %{name}+fmt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly_const_generics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly_const_generics-devel %{_description}

This package contains library source intended for building other packages
which use "nightly_const_generics" feature of "%{crate}" crate.

%files       -n %{name}+nightly_const_generics-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+only_new_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+only_new_tests-devel %{_description}

This package contains library source intended for building other packages
which use "only_new_tests" feature of "%{crate}" crate.

%files       -n %{name}+only_new_tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+testing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing-devel %{_description}

This package contains library source intended for building other packages
which use "testing" feature of "%{crate}" crate.

%files       -n %{name}+testing-devel
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
* Sun Oct 31 2021 nedia <me@aidenlangley.com> - 0.2.22-1
- Initial package