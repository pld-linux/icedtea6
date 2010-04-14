#
Summary:	OpenJDK and GNU Classpath code
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath
Name:		icedtea6
Version:	1.8
Release:	0.1
License:	GPL
Group:		Development/Languages/Java
Source0:	http://icedtea.classpath.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	e08dd0762749fb50ec6c273c366ee8ae
# following sources should match those in Makefile.am
Source1:	http://download.java.net/openjdk/jdk6/promoted/b18/openjdk-6-src-b18-16_feb_2010.tar.gz
# Source1-md5:	94db01691ab38f98b7d42b2ebf4d5c0b
Source2:	http://kenai.com/projects/jdk6-drops/downloads/download/jdk6-jaxws-2009_10_27.zip
# Source2-md5:	3ea5728706169498b722b898a1008acf
Source3:	http://kenai.com/projects/jdk6-drops/downloads/download/jdk6-jaf-2009_10_27.zip
# Source3-md5:	7a50bb540a27cdd0001885630088b758
Source4:	https://jaxp.dev.java.net/files/documents/913/147329/jdk6-jaxp-2009_10_13.zip
# Source4-md5:	a2f7b972124cd776ff71e7754eb9a429
URL:		http://icedtea.classpath.org/wiki/Main_Page
BuildRequires:	alsa-lib-devel
BuildRequires:	bash
BuildRequires:	cups-devel
# BuildRequires:	eclipse-ecj
BuildRequires:	freetype-devel >= 2.3
BuildRequires:	gcc-java >= 6:4.3
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
#BuildRequires:	gdk-pixbuf-devel
BuildRequires:	java-gcj-compat-devel-base
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mercurial
BuildRequires:	motif-devel
BuildRequires:	rhino
BuildRequires:	unzip
BuildRequires:	java-xalan
BuildRequires:	java-xerces
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-xproto-devel
#BuildRequires:	xulrunner-devel
BuildRequires:	zlib-devel
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _gcj_home /usr/lib/java/java-1.5.0-gcj-1.5.0.0

%description
The IcedTea project provides a harness to build the source code from
http://openjdk.java.net/ using Free Software build tools and provides
replacements libraries for the binary plugs with code from the GNU
Classpath project.

%description -l pl.UTF-8
Projekt IcedTea daje możliwość kompilacji kodu źródłowego z
http://openjdk.java.net/ przy użyciu wolnodostępnych narzędzi oraz
dostarcza zamienniki biblioteczne binarnych wtyczek pochodzące z
projektu GNU Classpath.

%prep
%setup -q
mkdir drops
ln -s %{SOURCE1} .
ln -s %{SOURCE2} drops
ln -s %{SOURCE3} drops
ln -s %{SOURCE4} drops

%build
unset JAVA_HOME || :
%configure \
	--with-gcj-home=%{_gcj_home} \
	--with-ecj=%{_bindir}/ecj \
	--with-ecj-jar=%{_javadir}/ecj.jar \
	--with-libgcj-jar=%{_javadir}/libgcj.jar \
	--with-xalan2-jar=%{_javadir}/xalan.jar \
	--with-xalan2-serializer-jar=%{_javadir}/serializer.jar \
	--with-rhino=%{_javadir}/js.jar \
	--disable-plugin

%{__make} -j1 \
	SHELL=/bin/bash

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
