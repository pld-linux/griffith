# TODO:
# - fix desktop file ??
# - Requires: /usr/bin/env -> /usr/bin/python for autodeps
# - py_compile?
#
Summary:	griffith - film collection manager
Summary(pl):	griffith - program kataloguj±cy filmy
Name:		griffith
Version:	0.5.1
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Multimedia
# download from http://download.berlios.de/griffith/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
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
Requires:	python-Imaging
Requires:	python-ReportLab
Requires:	python-gnome-gconf
Requires:	python-gstreamer >= 0.8.2
Requires:	python-pygtk-gtk >= 2:2.6.0
Requires:	python-sqlite1
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
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

ln -fs %{_libdir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/__init__.py
%{_libdir}/%{name}/about.py
%{_libdir}/%{name}/add.py
%{_libdir}/%{name}/amazon.py
%{_libdir}/%{name}/backup.py
%{_libdir}/%{name}/config.py
%{_libdir}/%{name}/cover.py
%{_libdir}/%{name}/delete.py
%{_libdir}/%{name}/edit.py
%{_libdir}/%{name}/gdebug.py
%{_libdir}/%{name}/gemail.py
%{_libdir}/%{name}/gglobals.py
%{_libdir}/%{name}/gutils.py
%{_libdir}/%{name}/initialize.py
%{_libdir}/%{name}/loan.py
%{_libdir}/%{name}/main_treeview.py
%{_libdir}/%{name}/movie.py
%{_libdir}/%{name}/people.py
%{_libdir}/%{name}/preferences.py
%{_libdir}/%{name}/quick_filter.py
%{_libdir}/%{name}/sql.py
%{_libdir}/%{name}/update.py
%{_libdir}/%{name}/version.py
%{_libdir}/%{name}/view.py
%{_libdir}/%{name}/widgets.py
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/export
%{_libdir}/%{name}/plugins/export/PluginExportCSV.py
%{_libdir}/%{name}/plugins/export/PluginExportHTML.py
%{_libdir}/%{name}/plugins/export/PluginExportPDF.py
%{_libdir}/%{name}/plugins/export/PluginExportXML.py
%dir %{_libdir}/%{name}/plugins/movie
%{_libdir}/%{name}/plugins/movie/PluginMovie7arte.py
%{_libdir}/%{name}/plugins/movie/PluginMovieAniDB.py
%{_libdir}/%{name}/plugins/movie/PluginMovieCSFD.py
%{_libdir}/%{name}/plugins/movie/PluginMovieCineMovies.py
%{_libdir}/%{name}/plugins/movie/PluginMovieCinematografo.py
%{_libdir}/%{name}/plugins/movie/PluginMovieClubeMyDVD.py
%{_libdir}/%{name}/plugins/movie/PluginMovieE-Pipoca.py
%{_libdir}/%{name}/plugins/movie/PluginMovieFilmweb.py
%{_libdir}/%{name}/plugins/movie/PluginMovieIMDB.py
%{_libdir}/%{name}/plugins/movie/PluginMovieMediadis.py
%{_libdir}/%{name}/plugins/movie/PluginMovieMoviefone.py
%{_libdir}/%{name}/plugins/movie/PluginMovieOFDb.py
%{_libdir}/%{name}/plugins/movie/PluginMovieOnet.py
%{_libdir}/%{name}/plugins/movie/PluginMoviePTGate.py
%{_libdir}/%{name}/plugins/movie/PluginMovieStopklatka.py
%{_libdir}/%{name}/plugins/movie/PluginMovieTanukiAnime.py
%{_libdir}/%{name}/plugins/movie/PluginMovieWP.py
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.*
%{_mandir}/man?/*
