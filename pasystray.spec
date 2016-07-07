Name:           pasystray
Version:        0.5.2
Release:        1%{?dist}
Summary:        PulseAudio system tray

License:        LGPLv2.1
URL:            https://github.com/christophgysin/pasystray
Source0:        https://github.com/christophgysin/pasystray/archive/pasystray-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(libnotify)

%description
pasystray allows setting the default PulseAudio source/sink and moving streams
on the fly between sources/sinks without restarting the client applications.


%prep
%setup -q -n pasystray-pasystray-%{version}
autoreconf -fvi


%build
%configure --with-gtk=3
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null ||:
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :


%files
%license LICENSE
%doc AUTHORS README.md TODO
/etc/xdg/autostart/pasystray.desktop
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/*.1*
%{_datadir}/pasystray/
%{_datadir}/pixmaps/*


%changelog
* Thu Jul 07 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.5.2-1
- Public release
