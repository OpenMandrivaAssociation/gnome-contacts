%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-contacts
Version:	3.4.1
Release:	%mkrel 1
Summary:	Contacts manager for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		https://live.gnome.org/ThreePointOne/Features/Contacts
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	vala >= 0.13.0
BuildRequires:	pkgconfig(folks) >= 0.6.1.1
BuildRequires:	pkgconfig(folks-eds)
BuildRequires:	pkgconfig(folks-telepathy)
BuildRequires:	pkgconfig(glib-2.0) >= 2.31.10
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(libebook-1.2) >= 3.2
BuildRequires:	pkgconfig(libedataserver-1.2) >= 3.2
BuildRequires:	pkgconfig(libnotify)
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
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop

