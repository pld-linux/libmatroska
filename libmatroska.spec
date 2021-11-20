#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Extensible Binary Meta Language access library
Summary(pl.UTF-8):	Biblioteka dostępu rozszerzalnego metajęzyka binarnego
Name:		libmatroska
Version:	1.6.3
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://dl.matroska.org/downloads/libmatroska/%{name}-%{version}.tar.xz
# Source0-md5:	d3ac01c6b27d99e820351d07d29a089d
URL:		https://www.matroska.org/
BuildRequires:	cmake >= 3.1.2
BuildRequires:	libebml-devel >= 1.4.2
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libebml >= 1.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska is an extensible open standard Audio/Video container format,
aiming to become the standard of Multimedia Container Formats one day.
It is based on EBML (Extensible Binary Meta Language), a kind of
binary version of XML. This way the significant advantages in terms of
future format extensibility are gained without breaking file support
in old parsers.

%description -l pl.UTF-8
Matroska to rozszerzalny otwarty format kodowania dźwięku i obrazu,
dążący do stania się pewnego dnia standardem formatów zawierających
multimedia. Jest on oparty na EBML (rozszerzalnym metajęzyku
binarnym), binarnym odpowiedniku XML-a. W ten sposób ma on przewagę
nad innymi formatami pod względem przyszłej rozszerzalności przy
jednoczesnym zachowaniu kompatybilności wstecz.

%package devel
Summary:	Header files for matroska library
Summary(pl.UTF-8):	Nagłówki dla biblioteki matroska
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libebml-devel >= 1.4.0
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for matroska library.

%description devel -l pl.UTF-8
Nagłówki dla biblioteki matroska.

%package static
Summary:	Static version of matroska library
Summary(pl.UTF-8):	Statyczna wersja biblioteki matroska
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of matroska library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki matroska.

%prep
%setup -q

%build
# .pc file generation expects relative CMAKE_INSTALL_{INCLUDE,LIB}DIR
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}
cd ..
%endif

install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_libdir}/libmatroska.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmatroska.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatroska.so
%{_includedir}/matroska
%{_pkgconfigdir}/libmatroska.pc
%{_libdir}/cmake/Matroska

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmatroska.a
%endif
