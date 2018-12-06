# Run tests in check section
%bcond_without check

%global goipath         github.com/microcosm-cc/bluemonday
Version:                1.0.1

%global common_description %{expand:
bluemonday is a HTML sanitizer implemented in Go. It is fast and highly 
configurable.

bluemonday takes untrusted user generated content as an input, and will 
return HTML that has been sanitised against a whitelist of approved HTML 
elements and attributes so that you can safely include the content in your 
web page.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast golang HTML sanitizer
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/html)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE.md
%doc README.md CREDITS.md CONTRIBUTING.md


%changelog
* Tue Sep 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf0761eb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628gitf0761eb
- Bump to commit f0761eb8ed07c1cc892ef631b00c33463b9b6868

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git995366f
- First package for Fedora

