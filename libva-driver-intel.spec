%define	libva_ver	2.4.0
Summary:	VA driver for Intel G45 and HD Graphics family
Summary(pl.UTF-8):	Sterownik VA do kart Intela z rodziny G45 i HD Graphics
Name:		libva-driver-intel
Version:	2.4.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/intel/intel-vaapi-driver/releases
Source0:	https://github.com/intel/intel-vaapi-driver/releases/download/%{version}/intel-vaapi-driver-%{version}.tar.bz2
# Source0-md5:	073fce0f409559109ad2dd0a6531055d
URL:		https://01.org/linuxmedia
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libdrm-devel >= 2.4.52
BuildRequires:	libva-devel >= %{libva_ver}
BuildRequires:	libva-drm-devel >= %{libva_ver}
BuildRequires:	libva-wayland-devel >= %{libva_ver}
BuildRequires:	libva-x11-devel >= %{libva_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
# VA-API version, not just package version
BuildRequires:	pkgconfig(libva) >= 1.1.0
# wayland-client
BuildRequires:	wayland-devel >= 1.11.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libdrm >= 2.4.52
Requires:	libva >= %{libva_ver}
Requires:	wayland >= 1.11.0
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
