%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-contacts
Version:	48.0
Release:	1
Summary:	Contacts manager for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv2+
Url:		https://live.gnome.org/ThreePointOne/Features/Contacts
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	vala-devel
BuildRequires:	vala-tools
BuildRequires:  valadoc-devel
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(folks-eds)
BuildRequires:	pkgconfig(folks-telepathy)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libgdata)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:	pkgconfig(cheese) >= 3.6.0
BuildRequires:	pkgconfig(cheese-gtk) >= 3.6.0
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(geocode-glib-1.0)
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  meson
BuildRequires:  docbook-xsl
BuildRequires:  docbook-dtd-xml
BuildRequires:  xsltproc

Requires:  folks


Requires:	telepathy-mission-control

%description
Standalone contacts manager for GNOME desktop.

%prep
%autosetup -n %{name}-%{version} -p1

%build
# Needed because build fail with Clang 15: 
# error: non-void function 'contacts_nickname_chunk_constructor' should return a value [-Wreturn-type] 
# g_return_if_fail (G_TYPE_CHECK_INSTANCE_TYPE (_tmp3_, FOLKS_TYPE_NAME_DETAILS));
export CC=gcc
export CXX=g++
%meson
%meson_build

%install
%meson_install

#fix .desktop file
desktop-file-edit %{buildroot}%{_datadir}/applications/org.gnome.Contacts.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/gnome-contacts-search-provider
%{_libexecdir}/gnome-contacts/gnome-contacts-parser
%{_datadir}/metainfo/org.gnome.Contacts.metainfo.xml
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
#{_datadir}/glib-2.0/schemas/org.gnome.Contacts.enums.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Contacts.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Contacts*.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Contacts.Devel.svg
%{_mandir}/man1/%{name}.*
