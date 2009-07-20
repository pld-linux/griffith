#
# TODO: include /usr/share/griffith/lib/db/*.py[co] files?
#
# Conditional build:
%bcond_without gtkspell    # don't build with spell checker
#
%define	artworkver	0.9.4
%define	_rc		rc1
#
Summary:	griffith - film collection manager
Summary(pl.UTF-8):	griffith - program katalogujący filmy
Name:		griffith
Version:	0.10
Release:	0.%{_rc}.1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://download.berlios.de/griffith/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	84467a45fcc7ae547ed96104efec4bf0
Source1:	http://download.berlios.de/griffith/%{name}-extra-artwork-%{artworkver}.tar.gz
# Source1-md5:	a18f9f900dc467f8ee801bb70776072f
Source2:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-env_python.patch
Patch2:		%{name}-plugin.patch
URL:		http://www.griffith.cc/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(macros) >= 1.234
%pyrequires_eq	python-modules
Requires:	gtk+2 >= 2:2.6.0
Requires:	python-PIL
Requires:	python-PyXML
Requires:	python-ReportLab
Requires:	python-SQLAlchemy
%{?with_gtkspell:Requires: python-gnome-extras-gtkspell}
Requires:	python-gnome-gconf
Requires:	python-pygtk-gtk >= 2:2.6.0
Requires:	python-sqlite >= 2.0.0
#Suggests:	python-gnome-extras
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	%{_prefix}/lib

%description
Griffith is a movie collection manager application.

%description -l pl.UTF-8
Griffith to program służący do katalogowania i zarządzania kolekcją
filmów.

%package extra-artwork
Summary:	Extra graphic files
Summary(pl.UTF-8):	Dodatkowe plik graficzne
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-extra-artwork = %{artworkver}-%{release}

%description extra-artwork
More graphic files.

%description extra-artwork -l pl.UTF-8
Dodatkowe pliki graficzne.

%prep
%setup -q -a1 -n %{name}-%{version}-%{_rc}
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv griffith-extra-artwork-%{artworkver}/images/*.png images/

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
%doc NEWS README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
#%%dir %{_datadir}/%{name}/lib
#%%dir %{_datadir}/%{name}/lib/sqlalchemy
#%%{_datadir}/%{name}/lib/sqlalchemy/*.py[co]
#%%dir %{_datadir}/%{name}/lib/sqlalchemy/databases
#%%{_datadir}/%{name}/lib/sqlalchemy/databases/*.py[co]
#%%dir %{_datadir}/%{name}/lib/sqlalchemy/engine
#%%{_datadir}/%{name}/lib/sqlalchemy/engine/*.py[co]
#%%dir %{_datadir}/%{name}/lib/sqlalchemy/ext
#%%{_datadir}/%{name}/lib/sqlalchemy/ext/*.py[co]
#%%dir %{_datadir}/%{name}/lib/sqlalchemy/mods
#%%{_datadir}/%{name}/lib/sqlalchemy/mods/*.py[co]
#%%dir %{_datadir}/%{name}/lib/sqlalchemy/orm
#%%{_datadir}/%{name}/lib/sqlalchemy/orm/*.py[co]
%attr(755,root,root) %{_datadir}/%{name}/lib/%{name}
%{_datadir}/%{name}/lib/*.py[co]
%dir %{_datadir}/%{name}/export_templates
%dir %{_datadir}/%{name}/export_templates/csv/
%{_datadir}/%{name}/export_templates/csv/*
%dir %{_datadir}/%{name}/export_templates/html_tables/
%{_datadir}/%{name}/export_templates/html_tables/*
%dir %{_datadir}/%{name}/export_templates/html_table/
%{_datadir}/%{name}/export_templates/html_table/*
%dir %{_datadir}/%{name}/export_templates/latex/
%{_datadir}/%{name}/export_templates/latex/*
%dir %{_datadir}/%{name}/export_templates/xml/
%{_datadir}/%{name}/export_templates/xml/*
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/*.glade
%{_datadir}/%{name}/glade/*.png
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
%{_datadir}/%{name}/images/seen.png
%{_datadir}/%{name}/images/unseen.png
%dir %{_datadir}/%{name}/lib/plugins
%dir %{_datadir}/%{name}/lib/plugins/movie
%dir %{_datadir}/%{name}/lib/plugins/export
%dir %{_datadir}/%{name}/lib/plugins/imp
%{_datadir}/%{name}/lib/plugins/*.py[co]
%{_datadir}/%{name}/lib/plugins/movie/*.py[co]
%{_datadir}/%{name}/lib/plugins/export/*.py[co]
%{_datadir}/%{name}/lib/plugins/imp/*.py[co]
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}.xpm
%{_mandir}/*/man?/*
%{_mandir}/man1/*

%files extra-artwork
%defattr(644,root,root,755)
%{_datadir}/%{name}/images/PluginMovie*.png
