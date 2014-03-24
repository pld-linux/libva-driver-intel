Summary:	VA driver for Intel G45 and HD Graphics family
Summary(pl.UTF-8):	Sterownik VA do kart Intela z rodziny G45 i HD Graphics
Name:		libva-driver-intel
Version:	1.3.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-%{version}.tar.bz2
# Source0-md5:	26d5cb188b93e415e70ee662aad924f1
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libdrm-devel >= 2.4.45
BuildRequires:	libva-devel >= 1.3.0
BuildRequires:	libva-drm-devel >= 1.3.0
BuildRequires:	libva-wayland-devel >= 1.3.0
BuildRequires:	libva-x11-devel >= 1.3.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
# API version, not just package version
BuildRequires:	pkgconfig(libva) >= 0.32.0
# wayland-client
BuildRequires:	wayland-devel
Requires:	libdrm >= 2.4.45
Requires:	libva >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libva-driver-intel is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.

%description -l pl.UTF-8
libva-driver-intel to implementacja VA-API dla układów Intel G45 oraz
Intel HD Graphics przeznaczonych dla rodziny procesorów Intel Core.

%prep
%setup -q -n libva-intel-driver-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
