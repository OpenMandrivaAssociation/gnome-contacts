%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-contacts
Version:	3.34
Release:	1
Summary:	Contacts manager for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv2+
Url:		https://live.gnome.org/ThreePointOne/Features/Contacts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	vala-devel
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(folks-eds)
BuildRequires:	pkgconfig(folks-telepathy)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(cheese) >= 3.6.0
BuildRequires:	pkgconfig(cheese-gtk) >= 3.6.0
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(geocode-glib-1.0)
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:  meson
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtd-xml


Requires:	telepathy-mission-control

%description
Standalone contacts manager for GNOME desktop.

%prep
%setup -q
%apply_patches

%build
%meson -Dwith-cheese=yes
%meson_build

%install
%meson_install

#fix .desktop file
desktop-file-edit %{buildroot}%{_datadir}/applications/org.gnome.Contacts.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
#{_datadir}/glib-2.0/schemas/org.gnome.Contacts.enums.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Contacts.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Contacts*.svg
%{_mandir}/man1/%{name}.1.*
%{_includedir}/libhandy-0.0/*
%{_libdir}/girepository-1.0/Handy-0.0.typelib
%{_libdir}/libhandy-*
%{_libdir}/pkgconfig/libhandy*
%{_datadir}/gir-1.0/Handy-0.0.gir
%{_datadir}/vala/vapi/libhandy-0.0.deps
%{_datadir}/vala/vapi/libhandy-0.0.vapi
