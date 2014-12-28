Summary:	LIB - yet another (Polish) roguelike game
Summary(pl.UTF-8):	LIB - jeszcze jeden polski rogalik
Name:		LIB
Version:	0.1.67
Release:	1
Group:		Applications/Games
License:	GPL
Source0:	http://dl.sourceforge.net/lib/%{name}.%{version}.tar.bz2
# Source0-md5:	c8e17aaf9c16ccc73f4336a0d170b3ba
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-configure.patch
URL:		http://lib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LIB is yet another (Polish) roguelike game.

%description -l pl.UTF-8
LIB to jeszcze jeden polski rogalik.

%prep
%setup  -q -n %{name}
%patch0 -p0
%patch1 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses" 
%configure \
	--disable-nls

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/games,%{_libdir}/games/LIB,%{_datadir}/locale/en/LC_MESSAGES}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install po/en.gmo $RPM_BUILD_ROOT%{_datadir}/locale/en/LC_MESSAGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%lang(pl) %doc COPYING
%attr(755,root,root) %{_prefix}/games/LIB
%dir %{_libdir}/games/LIB
%{_libdir}/games/LIB/*
# ???
%{_datadir}/locale/en/LC_MESSAGES/*
