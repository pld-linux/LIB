Summary:	LIB - yet another (Polish) roguelike game
Summary(pl):	LIB - jeszcze jeden polski rogalik
Name:		LIB
Version:	0.1.67
Release:	1
Group:		Applications/Games
License:	GPL
Source0:	http://download.sourceforge.net/lib/%{name}.%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
URL:		http://LIB.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LIB is yet another (Polish) roguelike game.

%description -l pl
LIB to jeszcze jeden polski rogalik.

%prep
%setup  -q -n %{name}
%patch0 -p0

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__aclocal}
%{__autoconf}
%{__automake}
%configure2_13
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/games,%{_libdir}/games/LIB,%{_datadir}/locale/en/LC_MESSAGES} 

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install po/en.gmo $RPM_BUILD_ROOT%{_datadir}/locale/en/LC_MESSAGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_prefix}/games/LIB
%dir %{_libdir}/games/LIB
%{_libdir}/games/LIB/*
%{_datadir}/locale/en/LC_MESSAGES/*
