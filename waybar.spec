%global meson_wrap CFLAGS="${CFLAGS:--O2 -flto=false -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64  -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer }" ; export CFLAGS ; CXXFLAGS="${CXXFLAGS:--O2 -flto=false -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64  -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer }" ; export CXXFLAGS ; FFLAGS="${FFLAGS:--O2 -flto=false -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64  -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -I/usr/lib64/gfortran/modules }" ; export FFLAGS ; FCFLAGS="${FCFLAGS:--O2 -flto=disabled -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64  -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -I/usr/lib64/gfortran/modules }" ; export FCFLAGS ; VALAFLAGS="${VALAFLAGS:--g}" ; export VALAFLAGS ; LDFLAGS="${LDFLAGS:--Wl,-z,relro -Wl,--as-needed  -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -Wl,--build-id=sha1  }" ; export LDFLAGS ; LT_SYS_LIBRARY_PATH="${LT_SYS_LIBRARY_PATH:-/usr/lib64:}" ; export LT_SYS_LIBRARY_PATH ; CC="${CC:-gcc}" ; export CC ; CXX="${CXX:-g++}" ; export CXX; /usr/bin/meson setup --buildtype=plain --prefix=/usr --libdir=/usr/lib64 --libexecdir=/usr/libexec --bindir=/usr/bin --sbindir=/usr/sbin --includedir=/usr/include --datadir=/usr/share --mandir=/usr/share/man --infodir=/usr/share/info --localedir=/usr/share/locale --sysconfdir=/etc --localstatedir=/var --sharedstatedir=/var/lib --wrap-mode=default --auto-features=enabled . redhat-linux-build

%define _lto_cflags %{nil}
%define _unpackaged_files_terminate_build 0

Name:           waybar
Version:        0.9.24
Release:        1%{?dist}
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors
# Source files/overall project licensed as MIT, but
# - BSL-1.0
#   * include/util/clara.hpp
# - HPND-sell-variant
#   * protocol/ext-workspace-unstable-v1.xml
#   * protocol/wlr-foreign-toplevel-management-unstable-v1.xml
#   * protocol/wlr-layer-shell-unstable-v1.xml
# - ISC
#   * protocol/river-control-unstable-v1.xml
#   * protocol/river-status-unstable-v1.xml
#   * src/util/rfkill.cpp
License:        MIT AND BSL-1.0 AND ISC
URL:            https://github.com/Alexays/Waybar
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.50.0
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros
BuildRequires:  iniparser-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  portaudio-devel
BuildRequires:  portaudio

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(catch2)
BuildRequires:  pkgconfig(date)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fmt) >= 8.1.1
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(playerctl)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.10.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wireplumber-0.4)
BuildRequires:  pkgconfig(xkbregistry)

Conflicts:      waybar
Provides:       waybar

Enhances:       sway
Enhances:       hyprland
Recommends:     (font(fontawesome6free) or font(fontawesome5free))
Recommends:     cava

%description
%{summary}.

%prep
%autosetup -p1 -n Waybar-%{version}

%build
%meson_wrap \
    --force-fallback-for=cava,sndio \
    --wrap-mode=default \
    -Dcava=enabled  \
    -Dsndio=disabled \
    -Dcava:input_sndio=disabled
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_libdir}/libcava.so
%{_libdir}/pkgconfig/cava.pc
%{_bindir}/%{name}
%{_mandir}/man5/%{name}*
%{_userunitdir}/%{name}.service

%changelog
* Wed Aug 16 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.22-1
- Update to 0.9.22

* Mon Aug 14 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.21-1
- Update to 0.9.21

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.20-1
- Update to 0.9.20 (#2223828)

* Tue Jul 11 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.19-3
- Add patches for some known issues

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.19-2
- Rebuilt due to spdlog 1.12 update.

* Tue Jul 04 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.19-1
- Update to 0.9.19

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.18-2
- Rebuilt due to fmt 10 update.

* Mon May 29 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.18-1
- Update to 0.9.18
- Recommend Font Awesome 6 for F39

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.17-1
- Update to 0.9.17
- Convert License tag to SPDX

* Thu Nov 24 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.16-1
- Update to 0.9.16 (#2139998)

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.13-4
- Rebuilt due to spdlog update.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.13-2
- Rebuild for fmt 9.0.0

* Mon May 23 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.13-1
- Update to 0.9.13 (#2089525)

* Thu Mar 10 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12 (#2062615)

* Sun Mar 06 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10 (#2061176)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9
- Install systemd user service

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 0.9.8-3
- Rebuild (jsoncpp)

* Tue Nov 02 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.8-2
- Add patch for 'river/tags' protocol error on River

* Mon Aug 16 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.8-1
- Update to 0.9.8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 0.9.7-3
- Rebuild for new fmt version.

* Tue Jun 15 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.7-2
- Add patch for waybar crash on disabling outputs

* Thu Apr 15 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.7-1
- Update to 0.9.7

* Thu Apr 15 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.6-1
- Update to 0.9.6

* Wed Feb 10 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.9.5-4
- Add patch for rfkill exception with kernel 5.11
- Fixes rhbz#1927821

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.5-2
- Fix build with spdlog 1.5 (f32)
- Add patch for possible crashes in 'wlr/taskbar'

* Wed Dec 23 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Fri Nov 13 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.4-3
- Add patch for 'wlr/taskbar' protocol error with wlroots 0.12.0

* Tue Nov 03 2020 Jeff Law <law@redhat.com> - 0.9.4-2
- Fix mising #includes for gcc-11

* Mon Sep 21 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.4-1
- Update to 0.9.4

* Sun Sep 20 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.3-2
- Add patch for custom module signal handling regression
- Add patch for network module crash with fmt 7.0
- Add patch for broken updates in mpd and network modules

* Wed Aug 05 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.3-1
- Update to 0.9.3 (closes rhbz#1866571)
- Add patch for wlr/taskbar config strings

* Mon Aug 03 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.2-4
- Rebuild (date)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.9.2-2
- Rebuild (jsoncpp)

* Sat Apr 11 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Mon Feb 10 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.1-1
- Update to 0.9.1
- Remove upstreamed patch
- Add BuildRequires: pkgconfig(date)

* Sat Feb 08 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.9.0-1
- Initial import (#1798811)
