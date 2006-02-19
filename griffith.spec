# TODO:
# - fix desktop file ??
#
Summary:	griffith - film collection manager
Summary(pl):	griffith - program kataloguj±cy filmy
Name:		griffith
Version:	0.5.1
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Multimedia
# wrrr. http://download.berlios.de/download.php?file=/griffith/griffith-0.5.1.tar.gz&key=2fd8408ad86e20cd41b1861f3f5cb1cd
Source0:	http://download.berlios.de/griffith/%{name}-%{version}.tar.gz
# Source0-md5:	0c7e745b2a2483fc8578f1d286555ea3
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://griffith.vasconunes.net/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
%pyrequires_eq	python-modules
Requires:	gtk+2 >= 2:2.6.0
Requires:	python-gnome-gconf
Requires:	python-gstreamer >= 0.8.2
Requires:	python-pygtk-gtk >= 2:2.6.0
Requires:	python-sqlite1
Requires:	python-Imaging
Requires:	python-ReportLab
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Griffith is a movie collection manager application.

%description -l pl
Griffith to program s³u¿±cy do katalogowania i zarz±dzania kolekcj±
filmów.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

ln -fs %{_libdir}/%{name}/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}
# XXX: missing files in %{_libdir}/%{name}?
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.*
%{_mandir}/
