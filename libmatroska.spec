Summary:	Extensible Binary Meta Language access library
Summary(pl):	Biblioteka dostêpu rozszerzalnego metajêzyka binarnego
Name:		libmatroska
Version:	0.7.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.matroska.org/downloads/libmatroska/%{name}-%{version}.tar.bz2
# Source0-md5:	8f034dc9253dbb1f8a214dafa12785ae
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-version_define.patch
URL:		http://www.matroska.org/
BuildRequires:	libebml-devel >= 0.7.3
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Requires:	libebml >= 0.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska is an extensible open standard Audio/Video container format,
aiming to become the standard of Multimedia Container Formats one day.
It is based on EBML (Extensible Binary Meta Language), a kind of
binary version of XML. This way the significant advantages in terms of
future format extensibility are gained without breaking file support
in old parsers.

%description -l pl
Matroska to rozszerzalny otwarty format kodowania d¼wiêku i obrazu,
d±¿±cy do stania siê pewnego dnia standardem formatów zawieraj±cych
multimedia. Jest on oparty na EBML (rozszerzalnym metajêzyku
binarnym), binarnym odpowiedniku XML-a. W ten sposób ma on przewagê
nad innymi formatami pod wzglêdem przysz³ej rozszerzalno¶ci przy
jednoczesnym zachowaniu kompatybilno¶ci wstecz.

%package devel
Summary:	Header files for matroska library
Summary(pl):	Nag³ówki dla biblioteki matroska
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libebml-devel >= 0.7.3
Requires:	libstdc++-devel

%description devel
Header files for matroska library.

%description devel -l pl
Nag³ówki dla biblioteki matroska.

%package static
Summary:	Static version of matroska library
Summary(pl):	Statyczna wersja biblioteki matroska
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of matroska library.

%description static -l pl
Statyczna wersja biblioteki matroska.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -C make/linux \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	DEBUGFLAGS="%{rpmcflags} %{?debug:-DDEBUG}" \
	LDFLAGS="%{rpmldflags}" \
	LIBEBML_INCLUDE_DIR="%{_includedir}/ebml"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C make/linux install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

# prepare docs (with working hyperlinks)
#install -d doc
#cp --parents src/api/index.html src/api/c/index.html doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libmatroska.so.*.*.*

%files devel
%defattr(644,root,root,755)
##%doc doc/src/api/*
%attr(755,root,root) %{_libdir}/libmatroska.so
%{_libdir}/libmatroska.la
%{_includedir}/matroska

%files static
%defattr(644,root,root,755)
%{_libdir}/libmatroska.a
