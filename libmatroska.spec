Summary:	Extensible Binary Meta Language access library
Summary(pl):	Biblioteka dost�pu rozszerzalnego metaj�zyka binarnego
Name:		libmatroska
Version:	0.4.4
Release:	1
License:	GPL v2 or QPL
Group:		Libraries
Source0:	http://matroska.free.fr/downloads/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	1d855dc5d7a16d562efcac53f9cbdf7b
Patch0:		%{name}-makefile.patch
URL:		http://www.matroska.org/
BuildRequires:	libebml-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska is an extensible open standard Audio/Video container format,
aiming to become the standard of Multimedia Container Formats one day.
It is based on EBML (Extensible Binary Meta Language), a kind of
binary version of XML. This way the significant advantages in terms of
future format extensibility are gained without breaking file support
in old parsers.

%description -l pl
Matroska to rozszerzalny otwarty format kodowania d�wi�ku i obrazu,
d���cy do stania si� pewnego dnia standardem format�w zawieraj�cych
multimedia. Jest on oparty na EBML (rozszerzalnym metaj�zyku
binarnym), binarnym odpowiedniku XML. W ten spos�b ma on przewag� nad
innymi formatami pod wzgl�dem przysz�ej rozszerzalno�ci przy
jednoczesnym zachowaniu kompatybilno�ci wstecz.

%package devel
Summary:	Header files for matroska library
Summary(pl):	Nag��wki dla biblioteki matroska
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
Header files for matroska library.

%description devel -l pl
Nag��wki dla biblioteki matroska.

%package static
Summary:	Static version of matroska library
Summary(pl):	Statyczna wersja biblioteki matroska
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of matroska library.

%description static -l pl
Statyczna wersja biblioteki matroska.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C make/linux \
	prefix=%{_prefix} \
	CXX="%{__cxx}" \
	LD="%{__cxx}" \
	DEBUGFLAGS="%{rpmcflags} %{?debug:-DDEBUG}" \
	LDFLAGS="%{rpmldflags}" \
	LIBEBML_INCLUDE_DIR="%{_includedir}/ebml"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C make/linux install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

# prepare docs (with working hyperlinks)
install -d doc
cp --parents src/api/index.html src/api/c/index.html doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatroska.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/src/api/*
%attr(755,root,root) %{_libdir}/libmatroska.so
%{_libdir}/libmatroska.la
%{_includedir}/matroska

%files static
%defattr(644,root,root,755)
%{_libdir}/libmatroska.a
