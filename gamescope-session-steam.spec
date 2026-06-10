Name:           gamescope-session-steam
Version:        1.0
Release:        1%{?dist}
Summary:        Steam Big Picture session

License:        MIT
URL:            https://github.com/MNarath1/gamescope-session-steam

Source:         https://github.com/MNarath1/gamescope-session-steam/archive/refs/tags/1.0.tar.gz
BuildArch:      noarch

Requires:       gamescope-session

BuildRequires:  systemd-rpm-macros

%description
Steam Big Picture session

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/
cp -rv usr/bin/* %{buildroot}%{_bindir}
cp -rv usr/share/* %{buildroot}%{_datadir}
# rm -rf %{buildroot}%{_bindir}/steamos-polkit-helpers
# rm %{buildroot}%{_bindir}/jupiter-biosupdate
# rm %{buildroot}%{_bindir}/steamos-session-select
# rm %{buildroot}%{_bindir}/steamos-update

# Do post-installation
%post

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%{_bindir}/steam-http-loader
%{_bindir}/steamos-select-branch
%{_bindir}/steamos-polkit-helpers
%{_bindir}/jupiter-biosupdate
%{_bindir}/steamos-session-select
%{_bindir}/steamos-update
%{_datadir}/applications/gamescope-mimeapps.list
%{_datadir}/applications/steam_http_loader.desktop
%{_datadir}/gamescope-session-plus/sessions.d/steam
%{_datadir}/polkit-1/actions/org.chimeraos.update.policy
%{_datadir}/wayland-sessions/gamescope-session-steam.desktop
