Summary:	VA driver for Intel G45 and HD Graphics family
Summary(pl.UTF-8):	Sterownik VA do kart Intela z rodziny G45 i HD Graphics
Name:		libva-driver-intel
Version:	1.0.17
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: http://cgit.freedesktop.org/vaapi/intel-driver/
Source0:	http://cgit.freedesktop.org/vaapi/intel-driver/snapshot/intel-driver-%{version}.tar.bz2
# Source0-md5:	3421dcaed1df346b9070b85ec8b238cd
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.23
BuildRequires:	libva-devel >= 1.0.14
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libdrm >= 2.4.23
Requires:	libva >= 1.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libva-driver-intel is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.

%description -l pl.UTF-8
libva-driver-intel to implementacja VA-API dla układów Intel G45 oraz
Intel HD Graphics przeznaczonych dla rodziny procesorów Intel Core.

%prep
%setup -q -n intel-driver-%{version}

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
