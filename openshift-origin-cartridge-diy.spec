%global cartridgedir %{_libexecdir}/openshift/cartridges/diy

Summary:       GOE DIY cartridge
Name:          goe-openshift-origin-cartridge-diy
Version: 1.24.1
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           https://www.openshift.com
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-origin-cartridge-diy-0.1 = 2.0.0
Obsoletes:     openshift-origin-cartridge-diy-0.1 <= 1.99.9
BuildArch:     noarch

%description
GOE DIY cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec
%__rm hooks/.gitkeep

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}/configuration
%{cartridgedir}/metadata
%{cartridgedir}/usr
%{cartridgedir}/env
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog


