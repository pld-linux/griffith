#
# Conditional build:
%bcond_without gtkspell    # don't build with spell checker
#
Summary:	griffith - film collection manager
Summary(pl):	griffith - program kataloguj±cy filmy
Name:		griffith
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://download.berlios.de/griffith/%{name}-%{version}.tar.gz
# Source0-md5:	e1366baf254c587937389f5fef728c96
Source1:	http://download.berlios.de/griffith/%{name}-extra-artwork-0.6.tar.gz
# Source1-md5:	83609337d721f35277c2970866dbfe7e
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-env_python.patch
Patch2:		%{name}-plugin.patch
URL:		http://griffith.vasconunes.net/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(macros) >= 1.234
%pyrequires_eq	python-modules
Requires:	gtk+2 >= 2:2.6.0
Requires:	python-PIL
Requires:	python-ReportLab
%{?with_gtkspell:Requires: python-gnome-extras-gtkspell}
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

%package extra-artwork
Summary:	Extra graphic files
Summary(pl):	Dodatkowe plik graficzne
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-extra-artwork = %{version}-%{release}

%description extra-artwork
More graphic files.

%description extra-artwork -l pl
Dodatkowe pliki graficzne.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv griffith-extra-artwork-0.6/images/*.png images/

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

ln -fs %{_datadir}/%{name}/lib/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean %{_datadir}/%{name}

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
%{_datadir}/%{name}/lib/*.py[co]
%{_datadir}/%{name}/export_templates
%{_datadir}/%{name}/glade
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/00.png
%{_datadir}/%{name}/images/01.png
%{_datadir}/%{name}/images/010.png
%{_datadir}/%{name}/images/02.png
%{_datadir}/%{name}/images/03.png
%{_datadir}/%{name}/images/04.png
%{_datadir}/%{name}/images/05.png
%{_datadir}/%{name}/images/06.png
%{_datadir}/%{name}/images/07.png
%{_datadir}/%{name}/images/08.png
%{_datadir}/%{name}/images/09.png
%{_datadir}/%{name}/images/default.png
%{_datadir}/%{name}/images/default_thumbnail.png
%{_datadir}/%{name}/images/griffith.png
%{_datadir}/%{name}/images/meter00.png
%{_datadir}/%{name}/images/meter01.png
%{_datadir}/%{name}/images/meter010.png
%{_datadir}/%{name}/images/meter02.png
%{_datadir}/%{name}/images/meter03.png
%{_datadir}/%{name}/images/meter04.png
%{_datadir}/%{name}/images/meter05.png
%{_datadir}/%{name}/images/meter06.png
%{_datadir}/%{name}/images/meter07.png
%{_datadir}/%{name}/images/meter08.png
%{_datadir}/%{name}/images/meter09.png
%{_datadir}/%{name}/images/nill.png
%dir %{_datadir}/%{name}/plugins
%dir %{_datadir}/%{name}/plugins/movie
%dir %{_datadir}/%{name}/plugins/export
%{_datadir}/%{name}/plugins/movie/*.py[co]
%{_datadir}/%{name}/plugins/export/*.py[co]
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.*
%{_mandir}/*/man?/*
%{_mandir}/man?/*

%files extra-artwork
%defattr(644,root,root,755)
%{_datadir}/%{name}/images/PluginMovie*.png
