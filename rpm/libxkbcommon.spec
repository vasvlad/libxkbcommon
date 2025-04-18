%define keepstatic 1
Name:       libxkbcommon
Version:    1.3.1
Release:    1
Summary:    X.Org XKB parsing library
License:    MIT
URL:        http://www.x.org/
Source0:    libxkbcommon-%{version}.tar.bz2
Patch0:     0001-Add-enable-utils-meson-option.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  meson
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  pkgconfig(xkeyboard-config)
Requires:       xkeyboard-config

%description
%{name} is the X.Org library for compiling XKB maps into formats usable by
the X Server or other display servers.

%package devel
Summary:  X.Org XKB parsing development package
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package devel-static
Summary:  X.Org XKB parsing development package

%description devel-static
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Denable-docs=false \
       -Denable-x11=false \
       -Denable-wayland=false \
       -Denable-xkbregistry=false \
       -Denable-utils=false \
       -Ddefault_library=static
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
#%{_libdir}/libxkbcommon.so.0
#%{_libdir}/libxkbcommon.so.0.0.0
#%{_libdir}/*.a

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/xkbcommon/
%{_includedir}/xkbcommon/xkbcommon.h
%{_includedir}/xkbcommon/xkbcommon-names.h
%{_includedir}/xkbcommon/xkbcommon-keysyms.h
%{_includedir}/xkbcommon/xkbcommon-compat.h
%{_includedir}/xkbcommon/xkbcommon-compose.h
#%{_libdir}/libxkbcommon.so
%{_libdir}/pkgconfig/xkbcommon.pc

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/*.a
