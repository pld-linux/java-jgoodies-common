#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc


%define		srcname		jgoodies-common
%define		ver	%(echo %{version} | tr . _)
Summary:	Common library shared by JGoodies libraries and applications
Summary(pl.UTF-8):	Wspólna biblioteka używana przez biblioteki i aplikacje JGoodies
Name:		java-%{srcname}
Version:	1.3.0
Release:	1
License:	BSD
Group:		Libraries/Java
Source0:	http://www.jgoodies.com/download/libraries/common/%{srcname}-%{ver}.zip
# Source0-md5:	538e04b89e855a47103ed510210de27b
URL:		http://www.jgoodies.com/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jgoodies-common is a common library shared by JGoodies libraries and
applications.

%description -l pl.UTF-8
jgoodies-common jest wspólną biblioteką używaną przez biblioteki i
aplikacje JGoodies.

%package javadoc
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%description javadoc -l fr.UTF-8
Javadoc pour %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}

# delete prebuild JAR
%{__rm} *.jar

%build
%ant jar %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a build/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.html RELEASE-NOTES.txt
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
