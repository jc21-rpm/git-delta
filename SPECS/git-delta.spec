%global debug_package %{nil}

Name:           git-delta
Version:        0.16.5
Release:        1
Summary:        Syntax-highlighting pager for git
Group:          Applications/System
License:        MIT
URL:            https://github.com/dandavison/delta
Source:         https://github.com/dandavison/delta/archive/%{version}.tar.gz
BuildRequires:  cmake
%{?el7:BuildRequires: cargo, rust}

%description
Code evolves, and we all spend time studying diffs. Delta aims to make
this both efficient and enjoyable: it allows you to make extensive
changes to the layout and styling of diffs, as well as allowing you to
stay arbitrarily close to the default git/diff output.

%prep
%setup -q -n delta-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
install -D -m 755 target/release/delta %{buildroot}/usr/bin/delta

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE *.md
/usr/bin/delta

%changelog
* Tue Jun 6 2023 Jamie Curnow <jc@jc21.com> - 0.16.5-1
- v0.16.5

* Wed Dec 7 2022 Jamie Curnow <jc@jc21.com> - 0.15.1-1
- v0.15.1

* Thu Sep 1 2022 Jamie Curnow <jc@jc21.com> - 0.14.0-1
- v0.14.0

* Sun May 15 2022 Jamie Curnow <jc@jc21.com> - 0.13.0-1
- v0.13.0

* Mon Mar 7 2022 Jamie Curnow <jc@jc21.com> - 0.12.1-1
- v0.12.1

* Tue Feb 15 2022 Jamie Curnow <jc@jc21.com> - 0.12.0-1
- v0.12.0

* Fri Dec 10 2021 Jamie Curnow <jc@jc21.com> - 0.11.2-1
- v0.11.2

* Tue Nov 30 2021 Jamie Curnow <jc@jc21.com> - 0.10.2-1
- v0.10.2

* Sun Jun 20 2021 Jamie Curnow <jc@jc21.com> - 0.8.0-1
- v0.8.0

