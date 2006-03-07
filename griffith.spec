# TODO:
# - fix desktop file ??
# - Requires: /usr/bin/env -> /usr/bin/python for autodeps
# - py_compile?
#
Summary:	griffith - film collection manager
Summary(pl):	griffith - program kataloguj±cy filmy
Name:		griffith
Version:	0.6
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://download.berlios.de/griffith/%{name}-%{version}.tar.gz
# Source0-md5:	a61e267d64197472a6068d7b5310ef55
Source1:	http://download.berlios.de/griffith/griffith-extra-artwork-%{version}.tar.gz
# Source1-md5:	83609337d721f35277c2970866dbfe7e
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://griffith.vasconunes.net/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
%pyrequires_eq	python-modules
Requires:	gtk+2 >= 2:2.6.0
Requires:	python-Imaging
Requires:	python-ReportLab
Requires:	python-gnome-gconf
Requires:	python-pygtk-gtk >= 2:2.6.0
Requires:	python-sqlite1 >= 1.1.7
#Suggests:	python-gnome-extras
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	%{_prefix}/lib

%description
Griffith is a movie collection manager application.

%description -l pl
Griffith to program s³u¿±cy do katalogowania i zarz±dzania kolekcj±
filmów.

%prep
%setup -q -a1
%patch0 -p1

mv griffith-extra-artwork-0.6/images/* images/

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

ln -fs %{_datadir}/%{name}/lib/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%attr(755,root,root) %{_datadir}/%{name}/lib/%{name}
%{_datadir}/%{name}/lib/*.py
%{_datadir}/%{name}/export_templates
%{_datadir}/%{name}/glade
%{_datadir}/%{name}/images
%{_datadir}/%{name}/plugins
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.*
%{_mandir}/*/man?/*
%{_mandir}/man?/*
