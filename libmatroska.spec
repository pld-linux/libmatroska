Summary:	Extensible Binary Meta Language access library
Summary(pl):	Biblioteka dostêpu rozszerzalnego metajêzyka binarnego
Name:		libmatroska
Version:	0.4.4
Release:	1
License:	GPL/QPL
Group:		Libraries
Source0:	http://matroska.free.fr/downloads/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	1d855dc5d7a16d562efcac53f9cbdf7b
Patch0:		%{name}-makefile.patch
URL:		http://www.matroska.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska is an extensible open standard Audio/Video container format, 
aiming to become the standard of Multimedia
Container Formats one day. It is based on EBML (Extensible Binary
Meta Language), a kind of binary version of XML. This way the
significant advantages in terms of future format extensability
are gained without breaking file support in old parsers.
     
   
%description -l pl
Matroska to rozszerzalny otwarty format kodowania d¼wiêku i obrazu,
d±¿±cy do stania sie. Jest on oparty na EBML (rozszerzalny metajêzyk 
binarny), binarnym odpowiedniku XML. W ten sposób ma on przewagê nad 
innymi formatami pod wzglêdem przysz³ej rozszerzalno¶ci przy jendoczesnym
zachowaniu kompatybilno¶ci wstecz.


%package devel
Summary:	Developmment files and headers for matroska.
Summary(pl):	Nag³ówki dla matroski.
Group:		Development/Libraries
Requires:       %{name} >= %{version}

%description devel
Developmment files and headers for matroska.

%description devel -l pl
Nag³ówki dla matroski.

%package static
Summary:        Static libraries for Extensible Binary Meta Language.
Summary(pl):   	Biblioteki statyczne dla rozszerzalnego metajêzyka binarnego.
Group:          Libraries

%description static
Static libraries for matroska.

%description static -l pl
Biblioteki statyczne dla matroski.

%prep
%setup -q 
%patch0 -p1 -b .dakh

%build
cd make/linux
%{__make} clean
%{__make}  prefix=%{_prefix} \
	CXX=%{__cxx} \
	LD=%{__cxx} \
	AR="%{__ar} rcvu"  \
	RANLIB=%{__ranlib} \
	INSTALL=%{__install} \
	CXXFLAGS="%{rpmcflags}" \
	%{?debug:DEBUG=yes} \
	INSTALL_OPTS="" \
	INSTALL_OPTS_LIB="" \
	INSTALL_DIR_OPTS="" \
	LDFLAGS="-shared -lebml -L. -L%{_libdir}"\
	LIBEBML_INCLUDE_DIR="%{_includedir}/ebml/" \
	SRC_DIR=%{_builddir}/%{name}-%{version}/src/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} -f make/linux/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} install \
	CXX=%{__cxx} \
	LD=%{__cxx} \
	AR="%{__ar} rcvu"  \
	RANLIB=%{__ranlib} \
	INSTALL=%{__install} \
	%{?debug:DEBUG=yes} \
	INSTALL_OPTS="" \
	INSTALL_OPTS_LIB="" \
	INSTALL_DIR_OPTS="" \
	SRC_DIR=%{_builddir}/%{name}-%{version}/src/\
	LDFLAGS="-shared -lebml -L. -L%{_libdir}" \
	LIBEBML_INCLUDE_DIR="%{_includedir}/ebml/" \
	CXXFLAGS="%{rpmcflags}"
	


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%{_libdir}/libmatroska.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/matroska/

%files static
%defattr(644,root,root,755)
%{_libdir}/libmatroska.a
