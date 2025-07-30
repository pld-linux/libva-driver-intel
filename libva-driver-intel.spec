#
# Conditional build:
%bcond_without	nonfree_shaders		# Don't use closed source pre-built binary shaders (kernels)
%bcond_without	cmrtlib			# Build and Install cmrtlib together with media driver
#
%define		libva_ver	2.22.0
Summary:	VA driver for Intel GEN Graphics hardware
Summary(pl.UTF-8):	Sterownik VA do kart Intela opartych na GEN
Name:		libva-driver-intel
Version:	25.2.6
Release:	1
License:	MIT, BSD (see LICENSE.md)
Group:		Libraries
Source0:	https://github.com/intel/media-driver/archive/intel-media-%{version}/intel-vaapi-driver-%{version}.tar.gz
# Source0-md5:	86d04d3795985859ad5e59e1d2d8ac22
URL:		https://01.org/linuxmedia
BuildRequires:	cmake >= 3.12
BuildRequires:	intel-gmmlib-devel >= 22.8.0
BuildRequires:	libdrm-devel >= 2.4.52
BuildRequires:	libva-devel >= %{libva_ver}
BuildRequires:	libva-drm-devel >= %{libva_ver}
BuildRequires:	libva-wayland-devel >= %{libva_ver}
BuildRequires:	libva-x11-devel >= %{libva_ver}
BuildRequires:	pkgconfig
# VA-API version, not just package version
BuildRequires:	pkgconfig(libva) >= 1.1.0
# wayland-client
BuildRequires:	wayland-devel >= 1.11.0
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
Requires:	libdrm >= 2.4.52
Requires:	libva >= %{libva_ver}
Requires:	wayland >= 1.11.0
Suggests:	igfxcmrt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Intel(R) Media Driver for VAAPI is a new VA-API (Video
Acceleration API) user mode driver supporting hardware accelerated
decoding, encoding, and video post processing for GEN based graphics
hardware.

Supported Platforms:

- BDW (Broadwell)
- SKL (Skylake)
- BXTx (BXT: Broxton, APL: Apollo Lake, GLK: Gemini Lake)
- KBLx (KBL: Kaby Lake, CFL: Coffee Lake, WHL: Whiskey Lake,
        CML: Comet Lake, AML: Amber Lake)
- ICL (Ice Lake)
- JSL (Jasper Lake) / EHL (Elkhart Lake)
- TGLx (TGL: Tiger Lake, RKL: Rocket Lake, ADL-S/P/N: Alder Lake,
        RPL-S/P: Raptor Lake)
- DG1/SG1
- Alchemist(DG2)/ATSM
- MTLx (MTL: Meteor Lake, ARL-S/H: Arrow Lake)
- LNL (Lunar Lake)
- BMG (Battlemage)
- PTL (Pather Lake)

%description -l pl.UTF-8
Intel(R) Media Driver dla VAAPI to nowy sterownik VA-API (Video
Acceleration API) w przestrzeni użytkownika, wspierający sprzętowe
dekodowanie, enkodowanie i post processing video dla sprzetu opartego
na GEN.

Wspierane platformy:

- BDW (Broadwell)
- SKL (Skylake)
- BXTx (BXT: Broxton, APL: Apollo Lake, GLK: Gemini Lake)
- KBLx (KBL: Kaby Lake, CFL: Coffee Lake, WHL: Whiskey Lake,
        CML: Comet Lake, AML: Amber Lake)
- ICL (Ice Lake)
- JSL (Jasper Lake) / EHL (Elkhart Lake)
- TGLx (TGL: Tiger Lake, RKL: Rocket Lake, ADL-S/P/N: Alder Lake,
        RPL-S/P: Raptor Lake)
- DG1/SG1
- Alchemist(DG2)/ATSM
- MTLx (MTL: Meteor Lake, ARL-S/H: Arrow Lake)
- LNL (Lunar Lake)
- BMG (Battlemage)
- PTL (Pather Lake)

%package -n igfxcmrt
Summary:	Library for executing user-owned GPU kernels on Intel VA-API render engine
License:	MIT
Group:		Libraries

%description -n igfxcmrt
Runtime library needed when user wants to execute their own GPU
kernels on render engine. It calls iHD media driver to load the
kernels and allocate the resources. It provides a set of APIs for user
to call directly from application.

This cmrtlib library is a separate effort from a similar library
(https://github.com/intel/cmrt). They may provide the same
functionalities but this is not intended to replace the other.

%package -n igfxcmrt-devel
Summary:	Header files for cmrtlib library
License:	MIT
Group:		Development/Libraries
Requires:	igfxcmrt = %{version}-%{release}

%description -n igfxcmrt-devel
Header files for cmrtlib library.

%prep
%setup -q -n media-driver-intel-media-%{version}

%build
mkdir -p build
cd build
%cmake ../ \
	%{cmake_on_off nonfree_shaders ENABLE_NONFREE_KERNELS} \
	%{cmake_on_off cmrtlib BUILD_CMRTLIB}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -n igfxcmrt -p /sbin/ldconfig
%postun -n igfxcmrt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md security.md
%attr(755,root,root) %{_libdir}/libva/dri/iHD_drv_video.so

%files -n igfxcmrt
%defattr(644,root,root,755)
%doc cmrtlib/README.md
%ghost %{_libdir}/libigfxcmrt.so.7
%{_libdir}/libigfxcmrt.so.*.*.*

%files -n igfxcmrt-devel
%defattr(644,root,root,755)
%{_libdir}/libigfxcmrt.so
%{_includedir}/igfxcmrt
%{_pkgconfigdir}/igfxcmrt.pc
