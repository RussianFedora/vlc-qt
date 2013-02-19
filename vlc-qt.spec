Summary:	Free library used to connect Qt and libvlc libraries
Name:		vlc-qt
Version:	0.8.0
Release:	1%{?dist}

URL:		http://projects.tano.si
Group:		Applications/Multimedia
License:	GPLv3
Source:		http://downloads.sourceforge.net/project/%{name}/VLC-Qt/%{version}/lib%{name}_%{version}_src.tar.gz

BuildRequires:	qt-devel
BuildRequires:	vlc-devel
BuildRequires:	cmake
Requires:	vlc

%description
VLC-Qt is a free library used to connect Qt and libvlc libraries. It contains
core classes for main media playback and also some GUI classes for faster media
player developement.

VLC-Qt is free (libre) software. This means that the library source code is
available to public, anyone is welcome to research how the library works,
participate in its development, freely distribute the library and spread the
word!

VLC-Qt runs on Linux and Windows, other operating systems are currently not
supported.


%package devel
Summary:	Devel libraries for %{name}
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}


%description devel
Files needed to build applications based on %{name}


%prep
%setup -q -n lib%{name}-%{version}


%build
mkdir build && cd build
%cmake ..
make


%install
make DESTDIR=%{buildroot} install -C build


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvlc-qt.pc
%{_includedir}/%{name}/*


%changelog
* Tue Feb 19 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 0.8.0-1.R
- initial build
