%define	libva_req	1.7.3
Summary:	VA driver for Intel G45 and HD Graphics family
Summary(pl.UTF-8):	Sterownik VA do kart Intela z rodziny G45 i HD Graphics
Name:		libva-driver-intel
Version:	1.8.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/intel-vaapi-driver-%{version}.tar.bz2
# Source0-md5:	fd70a5f739b5d8a8dbf612843ebedf39
URL:		https://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libdrm-devel >= 2.4.52
BuildRequires:	libva-devel >= %{libva_req}
BuildRequires:	libva-drm-devel >= %{libva_req}
BuildRequires:	libva-wayland-devel >= %{libva_req}
BuildRequires:	libva-x11-devel >= %{libva_req}
BuildRequires:	libtool
BuildRequires:	pkgconfig
# API version, not just package version
BuildRequires:	pkgconfig(libva) >= 0.39.4
# wayland-client
BuildRequires:	wayland-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libdrm >= 2.4.52
Requires:	libva >= %{libva_req}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libva-driver-intel is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.

%description -l pl.UTF-8
libva-driver-intel to implementacja VA-API dla układów Intel G45 oraz
Intel HD Graphics przeznaczonych dla rodziny procesorów Intel Core.

%prep
%setup -q -n intel-vaapi-driver-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-hybrid-codec \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libva/dri/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/libva/dri/i965_drv_video.so
