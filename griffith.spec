#
# TODO: include /usr/share/griffith/lib/db/*.py[co] files?
#
# Conditional build:
%bcond_without gtkspell    # don't build with spell checker

%define	artworkver	0.9.4
Summary:	griffith - film collection manager
Summary(pl.UTF-8):	griffith - program katalogujący filmy
Name:		griffith
Version:	0.13
Release:	3
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://launchpad.net/griffith/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	cf130806516fb476a268d950ac8aec91
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
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	gtk+2 >= 2:2.6.0
Requires:	python-PIL
Requires:	python-PyXML
Requires:	python-ReportLab >= 1.19
Requires:	python-SQLAlchemy >= 0.5
%{?with_gtkspell:Requires: python-gnome-extras-gtkspell}
Requires:	python-gnome-gconf
Requires:	python-modules
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk >= 2:2.6.1
Requires:	python-sqlite >= 2.0.0
# Python interface for MySQL connectivity
Suggests:	python-MySQLdb >= 1.2.1-p2
# CSV file encoding detections
Suggests:	python-chardet
# Python interface for PostgreSQL connectivity
Suggests:	python-psycopg2 >= 1.1.21-6
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

%package -n bash-completion-griffith
Summary:	bash-completion for griffith
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla grifith
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}

%description -n bash-completion-griffith
bash-completion for griffith.

%description -n bash-completion-griffith -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla griffith.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv griffith-extra-artwork-%{artworkver}/images/*.png images/

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -fs %{_datadir}/%{name}/lib/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -p data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean %{_datadir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/griffith
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%attr(755,root,root) %{_datadir}/%{name}/lib/%{name}
%{_datadir}/%{name}/lib/*.py[co]
%dir %{_datadir}/%{name}/export_templates
%dir %{_datadir}/%{name}/export_templates/csv
%{_datadir}/%{name}/export_templates/csv/*
%dir %{_datadir}/%{name}/export_templates/html_tables
%{_datadir}/%{name}/export_templates/html_tables/*
%dir %{_datadir}/%{name}/export_templates/html_table
%{_datadir}/%{name}/export_templates/html_table/*
%dir %{_datadir}/%{name}/export_templates/latex
%{_datadir}/%{name}/export_templates/latex/*
%dir %{_datadir}/%{name}/export_templates/xml
%{_datadir}/%{name}/export_templates/xml/*
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/*.glade
%{_datadir}/%{name}/glade/*.png
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*.png
%dir %{_datadir}/%{name}/lib/db
%dir %{_datadir}/%{name}/lib/plugins
%dir %{_datadir}/%{name}/lib/plugins/movie
%dir %{_datadir}/%{name}/lib/plugins/export
%dir %{_datadir}/%{name}/lib/plugins/extensions
%dir %{_datadir}/%{name}/lib/plugins/imp
%{_datadir}/%{name}/lib/db/*.py[co]
%{_datadir}/%{name}/lib/plugins/*.py[co]
%{_datadir}/%{name}/lib/plugins/movie/*.py[co]
%{_datadir}/%{name}/lib/plugins/export/*.py[co]
%{_datadir}/%{name}/lib/plugins/extensions/*.py[co]
%{_datadir}/%{name}/lib/plugins/imp/*.py[co]
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}.xpm
%{_mandir}/man1/griffith.1*
%lang(pl) %{_mandir}/pl/man1/griffith.1*
%lang(pt) %{_mandir}/pt/man1/griffith.1*

%files extra-artwork
%defattr(644,root,root,755)
%{_datadir}/%{name}/images/PluginMovie*.png

%files -n bash-completion-griffith
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*
