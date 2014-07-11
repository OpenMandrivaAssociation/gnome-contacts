%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-contacts
Version:	3.6.2
Release:	7
Summary:	Contacts manager for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv2+
Url:		https://live.gnome.org/ThreePointOne/Features/Contacts
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(folks-eds)
BuildRequires:	pkgconfig(folks-telepathy)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(cheese) >= 3.6.0
BuildRequires:	pkgconfig(cheese-gtk) >= 3.6.0
BuildRequires:	pkgconfig(clutter-1.0)

Requires:	telepathy-mission-control

%description
Standalone contacts manager for GNOME desktop.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README NEWS TODO ChangeLog
%{_bindir}/%{name}
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/gnome-shell/search-providers/gnome-contacts-search-provider.ini
