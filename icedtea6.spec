#
%bcond_without bootstrap	# don't use gcj, use an installed icedtea6
				# instead
#
# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 50.0
# JDK/JRE version, as returned with `java -version`, '_' replaced with '.'
%define		_jdkversion 1.6.0.18
#
Summary:	OpenJDK and GNU Classpath code
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath
Name:		icedtea6
Version:	1.8
Release:	0.2
License:	GPL v2
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
%{!?with_bootstrap:BuildRequires:	ant}
BuildRequires:	bash
BuildRequires:	cups-devel
BuildRequires:	freetype-devel >= 2.3
%{?with_bootstrap:BuildRequires:	gcc-java >= 6:4.3}
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
%{!?with_bootstrap:BuildRequires:	icedtea6-jdk-base}
%{?with_bootstrap:BuildRequires:	java-gcj-compat-devel-base}
BuildRequires:	libffi-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	motif-devel
BuildRequires:	nss-devel
BuildRequires:	unzip
BuildRequires:	java-rhino
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
Requires:	%{name}-jdk = %{version}-%{release}
Requires:	%{name}-jar = %{version}-%{release}
Requires:	%{name}-appletviewer = %{version}-%{release}
Obsoletes:	java-gcj-compat
Obsoletes:	java-gcj-compat-devel
Obsoletes:	java-sun
Obsoletes:	java-sun-demos
Obsoletes:	java-sun-jre-X11
Obsoletes:	java-sun-jre-alsa
Obsoletes:	java-sun-jre-jdbc
Obsoletes:	java-sun-sources
Obsoletes:	java-sun-tools
# redudant with the same in %{name}-jre, but seems needed for clean java-sun replacement
Obsoletes:	java-sun-jre 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _gcj_home /usr/%{_lib}/java/java-1.5.0-gcj-1.5.0.0

%define		dstreldir	%{name}-%{version}
%define		dstdir		%{_jvmdir}/%{dstreldir}
%define		jrereldir	%{dstreldir}/jre
%define		jredir		%{_jvmdir}/%{jrereldir}
%define		jvmjardir	%{_jvmjardir}/%{name}-%{version}

%description
The IcedTea project provides a harness to build the source code from
http://openjdk.java.net/ using Free Software build tools and provides
replacements libraries for the binary plugs with code from the GNU
Classpath project.

This is a meta-package which provides, by its dependencies, all the IcedTea6
components including the OpenJDK, Java 6 developement kit and runtime
environment.

%description -l pl.UTF-8
Projekt IcedTea daje możliwość kompilacji kodu źródłowego z
http://openjdk.java.net/ przy użyciu wolnodostępnych narzędzi oraz
dostarcza zamienniki biblioteczne binarnych wtyczek pochodzące z
projektu GNU Classpath.

To jest meta-pakiet, który, za pośrednictwem zależności, dostarcza
wszystkie komponenty IcedTea6, w tym środowisko programistyczne 
(OpenJDK) i uruchomieniowe (JRE).

%package jdk
Summary:	OpenJDK and GNU Classpath code - software developement kit
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko programistyczne
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jdk-base = %{version}-%{release}
Provides:	j2sdk = %{_jdkversion}
Provides:	jdk = %{_jdkversion}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe

%description jdk
OpenJDK compiled using IcedTea6 tool-set.

%package jdk-base
Summary:	OpenJDK and GNU Classpath code - software developement kit
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko programistyczne
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.6.6-14

%description jdk-base
OpenJDK runtime environment compiled using IcedTea6 tool-set.

%package jre
Summary:	OpenJDK and GNU Classpath code - runtime environment
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko uruchomieniowe
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Suggests:	%{name}-jre-X11 = %{version}-%{release}
Suggests:	%{name}-jre-freetype = %{version}-%{release}
Suggests:	%{name}-jre-freetype = %{version}-%{release}
Provides:	j2re = %{_jdkversion}
Provides:	java
Provides:	java1.4
Provides:	jre = %{_jdkversion}
Obsoletes:	jre

%description jre
OpenJDK runtime environment compiled using IcedTea6 tool-set.

%package jre-base
Summary:	OpenJDK and GNU Classpath code - runtime environment
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko uruchomieniowe
Group:		Development/Languages/Java
Provides:	java(ClassDataVersion) = %{_classdataversion}
Requires:	jpackage-utils >= 0:1.6.6-14

%description jre-base
OpenJDK runtime environment compiled using IcedTea6 tool-set.

%package jre-X11
Summary:	IcedTea6 OpenJDK - runtime environment - X11 support
Summary(pl.UTF-8):	IcedTea6 OpenJDK - środowisko uruchomieniowe - obsługa X11
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-jre-freetype = %{version}-%{release}

%description jre-X11
X11 support for OpenJDK runtime environment compiled using IcedTea6 tool-set.

%package jre-alsa
Summary:	IcedTea6 OpenJDK - runtime environment - ALSA support
Summary(pl.UTF-8):	IcedTea6 OpenJDK - środowisko uruchomieniowe - obsługa ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-alsa
ALSA sound support for OpenJDK runtime environment compiled using IcedTea6 tool-set.

%package jre-freetype
Summary:	IcedTea6 OpenJDK - runtime environment - font support
Summary(pl.UTF-8):	IcedTea6 OpenJDK - środowisko uruchomieniowe - obsługa fontów
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-freetype
Font handling library for OpenJDK runtime environment compiled using IcedTea6 tool-set.

%package jar
Summary:	OpenJDK and GNU Classpath code - JAR tool
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - narzędzie JAR
Requires:	%{name}-jdk-base = %{version}-%{release}
Provides:	jar
Obsoletes:	jar
Obsoletes:	fastjar
Group:		Development/Languages/Java

%description jar
JAR tool from OpenJDK compiled using IcedTea6 tool-set.

JAR is an archiver used to merge Java classes into a single library.

%package appletviewer
Summary:	OpenJDK and GNU Classpath code - appletviewer tool
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - narzędzie appletviewer
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	%{name}-jre-X11 = %{version}-%{release}
Obsoletes:	java-sun-appletviewer
Group:		Development/Languages/Java

%description appletviewer 
Appletviewer from OpenJDK compiled using IcedTea6 tool-set.

%package jdk-sources
Summary:	OpenJDK and GNU Classpath code - sources
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - kod źródłowy
Group:		Development/Languages/Java

%description jdk-sources
Source code for the OpenJDK runtime environment standard library.

%package examples
Summary:	OpenJDK and GNU Classpath code - examples
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - przykłady
Group:		Development/Languages/Java

%description examples
Code examples OpenJDK runtime environment compiled using IcedTea6 tool-set.

%prep
%setup -q

# let the build system extract the sources where it wants them
mkdir drops
ln -s %{SOURCE1} .
ln -s %{SOURCE2} drops
ln -s %{SOURCE3} drops
ln -s %{SOURCE4} drops

%build
JAVA_HOME=%{_jvmdir}/icedtea6
%configure \
%if %{with bootstrap}
	--with-gcj-home=%{_gcj_home} \
	--with-libgcj-jar=%{_javadir}/libgcj.jar \
	--with-ecj-jar=%{_javadir}/ecj.jar \
%else
	--with-openjdk=%{_jvmdir}/icedtea6 \
%endif
	--with-xalan2-jar=%{_javadir}/xalan.jar \
	--with-xalan2-serializer-jar=%{_javadir}/serializer.jar \
	--with-rhino=%{_javadir}/js.jar \
	--disable-plugin

%{__make} extract extract-ecj

%if %{with bootstrap}
# Cannot do that as patch, as the sources are prepared by make
%{__sed} -i -e's/CORBA_BUILD_ARGUMENTS = \\/CORBA_BUILD_ARGUMENTS = JVMLIB="" \\/' openjdk-ecj/make/corba-rules.gmk
%endif

%{__make} -j1 \
	PRINTF=/bin/printf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{dstdir},%{_mandir}/ja} \
	$RPM_BUILD_ROOT{%{jvmjardir},%{_prefix}/src/%{name}-{jdk-sources,examples}}

# install the 'JDK image', it contains the JRE too
cp -R openjdk/build/linux-*/j2sdk-image/* $RPM_BUILD_ROOT%{dstdir}

# convenience symlinks without version number
ln -s %{dstreldir} $RPM_BUILD_ROOT%{_jvmdir}/%{name}
ln -s %{jrereldir} $RPM_BUILD_ROOT%{_jvmdir}/%{name}-jre

# move JDK sources and demo to /usr/src
mv $RPM_BUILD_ROOT%{dstdir}/demo $RPM_BUILD_ROOT%{_prefix}/src/%{name}-examples/
mv $RPM_BUILD_ROOT%{dstdir}/sample $RPM_BUILD_ROOT%{_prefix}/src/%{name}-examples/
mv $RPM_BUILD_ROOT%{dstdir}/src.zip $RPM_BUILD_ROOT%{_prefix}/src/%{name}-jdk-sources/

# move manual pages to its place
mv $RPM_BUILD_ROOT%{dstdir}/man/ja_JP.eucJP/man1 $RPM_BUILD_ROOT%{_mandir}/ja/man1
rmdir $RPM_BUILD_ROOT%{dstdir}/man/ja_JP.eucJP
rm $RPM_BUILD_ROOT%{dstdir}/man/ja
mv $RPM_BUILD_ROOT%{dstdir}/man/man1 $RPM_BUILD_ROOT%{_mandir}/man1
rmdir $RPM_BUILD_ROOT%{dstdir}/man

# replace duplicates with symlinks, link to %{_bindir}
for path in $RPM_BUILD_ROOT%{dstdir}/bin/* ; do
	filename=`basename $path`
	ln -sf "%{dstdir}/bin/$filename" $RPM_BUILD_ROOT%{_bindir}
	diff -q "$path" "$RPM_BUILD_ROOT%{jredir}/bin/$filename" > /dev/null || continue
	ln -sf "../jre/bin/$filename" "$path"
done
ln -sf ../jre/lib/jexec $RPM_BUILD_ROOT%{dstdir}/lib/jexec

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{jvmjardir}/jce.jar
for f in jndi jndi-ldap jndi-cos jndi-rmi jaas jdbc-stdext jdbc-stdext-3.0 \
	sasl jaxp_parser_impl jaxp_transform_impl jaxp jmx activation xml-commons-apis \
	jndi-dns jndi-rmi; do
	ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{jvmjardir}/$f.jar
done

rm -f $RPM_BUILD_ROOT%{dstdir}/{,jre/}{ASSEMBLY_EXCEPTION,LICENSE,THIRD_PARTY_README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKYOU

%files jdk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apt
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jconsole
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jhat
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jrunscript
%attr(755,root,root) %{_bindir}/jsadebugd
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/schemagen
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/wsgen
%attr(755,root,root) %{_bindir}/wsimport
%attr(755,root,root) %{_bindir}/xjc
%{_mandir}/man1/apt.*
%{_mandir}/man1/extcheck.*
%{_mandir}/man1/idlj.*
%{_mandir}/man1/jarsigner.*
%{_mandir}/man1/javac.*
%{_mandir}/man1/javadoc.*
%{_mandir}/man1/javah.*
%{_mandir}/man1/javap.*
%{_mandir}/man1/jconsole.*
%{_mandir}/man1/jdb.*
%{_mandir}/man1/jhat.*
%{_mandir}/man1/jinfo.*
%{_mandir}/man1/jmap.*
%{_mandir}/man1/jps.*
%{_mandir}/man1/jrunscript.*
%{_mandir}/man1/jsadebugd.*
%{_mandir}/man1/jstack.*
%{_mandir}/man1/jstat.*
%{_mandir}/man1/jstatd.*
%{_mandir}/man1/native2ascii.*
%{_mandir}/man1/schemagen.*
%{_mandir}/man1/serialver.*
%{_mandir}/man1/rmic.*
%{_mandir}/man1/wsgen.*
%{_mandir}/man1/wsimport.*
%{_mandir}/man1/xjc.*
%lang(ja) %{_mandir}/ja/man1/apt.*
%lang(ja) %{_mandir}/ja/man1/extcheck.*
%lang(ja) %{_mandir}/ja/man1/idlj.*
%lang(ja) %{_mandir}/ja/man1/jarsigner.*
%lang(ja) %{_mandir}/ja/man1/javac.*
%lang(ja) %{_mandir}/ja/man1/javadoc.*
%lang(ja) %{_mandir}/ja/man1/javah.*
%lang(ja) %{_mandir}/ja/man1/javap.*
%lang(ja) %{_mandir}/ja/man1/jconsole.*
%lang(ja) %{_mandir}/ja/man1/jdb.*
%lang(ja) %{_mandir}/ja/man1/jhat.*
%lang(ja) %{_mandir}/ja/man1/jinfo.*
%lang(ja) %{_mandir}/ja/man1/jmap.*
%lang(ja) %{_mandir}/ja/man1/jps.*
%lang(ja) %{_mandir}/ja/man1/jrunscript.*
%lang(ja) %{_mandir}/ja/man1/jsadebugd.*
%lang(ja) %{_mandir}/ja/man1/jstack.*
%lang(ja) %{_mandir}/ja/man1/jstat.*
%lang(ja) %{_mandir}/ja/man1/jstatd.*
%lang(ja) %{_mandir}/ja/man1/native2ascii.*
%lang(ja) %{_mandir}/ja/man1/schemagen.*
%lang(ja) %{_mandir}/ja/man1/serialver.*
%lang(ja) %{_mandir}/ja/man1/rmic.*
%lang(ja) %{_mandir}/ja/man1/wsgen.*
%lang(ja) %{_mandir}/ja/man1/wsimport.*
%lang(ja) %{_mandir}/ja/man1/xjc.*

%files jdk-base
%defattr(644,root,root,755)
%doc openjdk/build/linux-*/j2sdk-image/THIRD_PARTY_README
%doc openjdk/build/linux-*/j2sdk-image/ASSEMBLY_EXCEPTION
%dir %{dstdir}
%{_jvmdir}/%{name}
%dir %{dstdir}/bin
%attr(755,root,root) %{dstdir}/bin/appletviewer
%attr(755,root,root) %{dstdir}/bin/apt
%attr(755,root,root) %{dstdir}/bin/extcheck
%attr(755,root,root) %{dstdir}/bin/idlj
%attr(755,root,root) %{dstdir}/bin/jar
%attr(755,root,root) %{dstdir}/bin/jarsigner
%attr(755,root,root) %{dstdir}/bin/java
%attr(755,root,root) %{dstdir}/bin/java-rmi.cgi
%attr(755,root,root) %{dstdir}/bin/javac
%attr(755,root,root) %{dstdir}/bin/javadoc
%attr(755,root,root) %{dstdir}/bin/javah
%attr(755,root,root) %{dstdir}/bin/javap
%attr(755,root,root) %{dstdir}/bin/javaws
%attr(755,root,root) %{dstdir}/bin/jconsole
%attr(755,root,root) %{dstdir}/bin/jdb
%attr(755,root,root) %{dstdir}/bin/jhat
%attr(755,root,root) %{dstdir}/bin/jinfo
%attr(755,root,root) %{dstdir}/bin/jmap
%attr(755,root,root) %{dstdir}/bin/jps
%attr(755,root,root) %{dstdir}/bin/jrunscript
%attr(755,root,root) %{dstdir}/bin/jsadebugd
%attr(755,root,root) %{dstdir}/bin/jstack
%attr(755,root,root) %{dstdir}/bin/jstat
%attr(755,root,root) %{dstdir}/bin/jstatd
%attr(755,root,root) %{dstdir}/bin/keytool
%attr(755,root,root) %{dstdir}/bin/native2ascii
%attr(755,root,root) %{dstdir}/bin/orbd
%attr(755,root,root) %{dstdir}/bin/pack200
%attr(755,root,root) %{dstdir}/bin/policytool
%attr(755,root,root) %{dstdir}/bin/rmic
%attr(755,root,root) %{dstdir}/bin/rmid
%attr(755,root,root) %{dstdir}/bin/rmiregistry
%attr(755,root,root) %{dstdir}/bin/schemagen
%attr(755,root,root) %{dstdir}/bin/serialver
%attr(755,root,root) %{dstdir}/bin/servertool
%attr(755,root,root) %{dstdir}/bin/tnameserv
%attr(755,root,root) %{dstdir}/bin/unpack200
%attr(755,root,root) %{dstdir}/bin/wsgen
%attr(755,root,root) %{dstdir}/bin/wsimport
%attr(755,root,root) %{dstdir}/bin/xjc
%{dstdir}/include
%dir %{dstdir}/lib
%{dstdir}/lib/ct.sym
%{dstdir}/lib/dt.jar
%{dstdir}/lib/ir.idl
%{dstdir}/lib/jconsole.jar
%attr(755,root,root) %{dstdir}/lib/jexec
%{dstdir}/lib/orb.idl
%{dstdir}/lib/sa-jdi.jar
%{dstdir}/lib/tools.jar

%files jre
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/javaws
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/pack200
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{_bindir}/unpack200
%{_mandir}/man1/java.*
%{_mandir}/man1/javaws.*
%{_mandir}/man1/keytool.*
%{_mandir}/man1/orbd.*
%{_mandir}/man1/pack200.*
%{_mandir}/man1/policytool.*
%{_mandir}/man1/rmid.*
%{_mandir}/man1/rmiregistry.*
%{_mandir}/man1/servertool.*
%{_mandir}/man1/tnameserv.*
%{_mandir}/man1/unpack200.*
%lang(ja) %{_mandir}/ja/man1/java.*
%lang(ja) %{_mandir}/ja/man1/javaws.*
%lang(ja) %{_mandir}/ja/man1/keytool.*
%lang(ja) %{_mandir}/ja/man1/orbd.*
%lang(ja) %{_mandir}/ja/man1/pack200.*
%lang(ja) %{_mandir}/ja/man1/policytool.*
%lang(ja) %{_mandir}/ja/man1/rmid.*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.*
%lang(ja) %{_mandir}/ja/man1/servertool.*
%lang(ja) %{_mandir}/ja/man1/tnameserv.*
%lang(ja) %{_mandir}/ja/man1/unpack200.*

%files jre-base
%defattr(644,root,root,755)
%doc openjdk/build/linux-*/j2sdk-image/THIRD_PARTY_README
%doc openjdk/build/linux-*/j2sdk-image/ASSEMBLY_EXCEPTION
%dir %{dstdir}
%dir %{jredir}
%{_jvmdir}/%{name}-jre
%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/javaws
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/pack200
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%attr(755,root,root) %{jredir}/bin/unpack200
%dir %{jredir}/lib
%dir %{jredir}/lib/applet
%{jredir}/lib/cmm
%{jredir}/lib/ext
%dir %{jredir}/lib/i386
%dir %{jredir}/lib/i386/client
%{jredir}/lib/i386/client/Xusage.txt
%attr(755,root,root) %{jredir}/lib/i386/client/*.so
%dir %{jredir}/lib/i386/headless
%attr(755,root,root) %{jredir}/lib/i386/headless/*.so
%dir %{jredir}/lib/i386/jli
%attr(755,root,root) %{jredir}/lib/i386/jli/*.so
%dir %{jredir}/lib/i386/native_threads
%attr(755,root,root) %{jredir}/lib/i386/native_threads/*.so
%dir %{jredir}/lib/i386/server
%{jredir}/lib/i386/server/Xusage.txt
%attr(755,root,root) %{jredir}/lib/i386/server/*.so
%{jredir}/lib/i386/jvm.cfg
%attr(755,root,root) %{jredir}/lib/i386/libattach.so
%attr(755,root,root) %{jredir}/lib/i386/libawt.so
%attr(755,root,root) %{jredir}/lib/i386/libdt_socket.so
%attr(755,root,root) %{jredir}/lib/i386/libhprof.so
%attr(755,root,root) %{jredir}/lib/i386/libinstrument.so
%attr(755,root,root) %{jredir}/lib/i386/libj2gss.so
%attr(755,root,root) %{jredir}/lib/i386/libj2pcsc.so
%attr(755,root,root) %{jredir}/lib/i386/libj2pkcs11.so
%attr(755,root,root) %{jredir}/lib/i386/libjaas_unix.so
%attr(755,root,root) %{jredir}/lib/i386/libjava.so
%attr(755,root,root) %{jredir}/lib/i386/libjava_crw_demo.so
%attr(755,root,root) %{jredir}/lib/i386/libjawt.so
%attr(755,root,root) %{jredir}/lib/i386/libjdwp.so
%attr(755,root,root) %{jredir}/lib/i386/libjpeg.so
%attr(755,root,root) %{jredir}/lib/i386/libjsig.so
%attr(755,root,root) %{jredir}/lib/i386/libjsound.so
%attr(755,root,root) %{jredir}/lib/i386/libjsoundalsa.so
%attr(755,root,root) %{jredir}/lib/i386/liblcms.so
%attr(755,root,root) %{jredir}/lib/i386/libmanagement.so
%attr(755,root,root) %{jredir}/lib/i386/libmlib_image.so
%attr(755,root,root) %{jredir}/lib/i386/libnet.so
%attr(755,root,root) %{jredir}/lib/i386/libnio.so
%attr(755,root,root) %{jredir}/lib/i386/libnpt.so
%attr(755,root,root) %{jredir}/lib/i386/librmi.so
%attr(755,root,root) %{jredir}/lib/i386/libsaproc.so
%attr(755,root,root) %{jredir}/lib/i386/libunpack.so
%attr(755,root,root) %{jredir}/lib/i386/libverify.so
%attr(755,root,root) %{jredir}/lib/i386/libzip.so
%{jredir}/lib/im
%{jredir}/lib/images
%{jredir}/lib/management
%{jredir}/lib/security
%{jredir}/lib/zi
#
%{jredir}/lib/about.jar
%{jredir}/lib/about.jnlp
%{jredir}/lib/calendars.properties
%{jredir}/lib/charsets.jar
%{jredir}/lib/classlist
%{jredir}/lib/content-types.properties
%{jredir}/lib/currency.data
%{jredir}/lib/flavormap.properties
%{jredir}/lib/fontconfig.*
%{jredir}/lib/jce.jar
%attr(755, root, root) %{jredir}/lib/jexec
%{jredir}/lib/jsse.jar
%{jredir}/lib/jvm.hprof.txt
%{jredir}/lib/logging.properties
%{jredir}/lib/management-agent.jar
%{jredir}/lib/meta-index
%{jredir}/lib/net.properties
%{jredir}/lib/psfont.properties.ja
%{jredir}/lib/psfontj2d.properties
%{jredir}/lib/resources.jar
%{jredir}/lib/rhino.jar
%{jredir}/lib/rt.jar
%{jredir}/lib/sound.properties
%{jredir}/lib/tz.properties
%{jvmjardir}

%files jre-X11
%defattr(644,root,root,755)
%dir %{jredir}/lib/i386/xawt
%attr(755,root,root) %{jredir}/lib/i386/xawt/*.so
%attr(755,root,root) %{jredir}/lib/i386/libsplashscreen.so

%files jre-alsa
%defattr(644,root,root,755)
%dir %{jredir}/lib/i386/xawt
%attr(755,root,root) %{jredir}/lib/i386/xawt/*.so

%files jre-freetype
%defattr(644,root,root,755)
%dir %{jredir}/lib/i386/xawt
%attr(755,root,root) %{jredir}/lib/i386/libfontmanager.so

%files jar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%{_mandir}/man1/jar.*
%lang(ja) %{_mandir}/ja/man1/jar.*

%files appletviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletviewer
%{_mandir}/man1/appletviewer.*
%lang(ja) %{_mandir}/ja/man1/appletviewer.*


%files jdk-sources
%defattr(644,root,root,755)
%dir %{_prefix}/src/%{name}-jdk-sources
%{_prefix}/src/%{name}-jdk-sources/src.zip

%files examples
%defattr(644,root,root,755)
%dir %{_prefix}/src/%{name}-examples
%{_prefix}/src/%{name}-examples
